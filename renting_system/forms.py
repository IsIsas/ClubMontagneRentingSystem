from renting_system.model import show_people, get_person_code_by_email
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, IntegerField, \
    SelectField, FloatField, BooleanField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email
from renting_system.model import Person, get_people_datas, get_material_names, get_material_types, \
    is_item_rented
from wtforms.widgets import TextArea
from renting_system.utils import PeopleTypes


class NewPersonForm(FlaskForm):
    """
    Form to create a new person
    """
    name = StringField('Last Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone number', validators=[DataRequired()])
    people_types = [('%s'%p.value, p.name) for p in PeopleTypes]
    type = SelectField('Type', choices=people_types)
    bday = DateField('Birthday', validators=[DataRequired()], format='%d/%m/%Y')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if Person.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')


def get_list_people():
    people = show_people()

    return people


class NewMaterialForm(FlaskForm):
    """
    Form to create a new material
    """
    name = StringField('Name', validators=[DataRequired()])
    brand = StringField('Brand')
    purchase_date = DateField('Purchase date', format='%Y-%m-%d')
    notes = StringField('Notes', widget=TextArea())
    size = IntegerField('Size')
    skin = BooleanField('Skin')
    price = FloatField('Price')
    material_types = get_material_types()
    type = SelectField(u'Type', choices=[(elem[0], elem[0]) for elem in material_types])
    submit = SubmitField('Register')


def validate_person_email(code):
    def _validate(form, field):
        code_from_email = get_person_code_by_email(field.data)
        if code != code_from_email:
            raise ValidationError('Email or code wrong: they belong to two ' /
                                  'different people')
        return _validate


class EmailCodeValidator(object):
    def __init__(self, message=None):
        if not message:
            message = u'The person code and the email do not match!'
        self.message = message

    def __call__(self, form, field):
        # Pass field data to hash function
        person_code = get_person_code_by_email(form.person_email.data)
        if person_code != form.person_code.data:
            raise ValidationError(self.message)


class RentalMaterialValidator(object):
    def __init__(self, message=None):
        if not message:
            message = u'Thie object is currently rented!'
        self.message = message

    def __call__(self, form, field):
        if is_item_rented(form.material_name.data):
            raise ValidationError(self.message)


class NewRentalForm(FlaskForm):
    """
    Form to create a new rental
    """
    people_emails = []
    people_codes = []
    for data in get_people_datas():
        people_emails.append(data[0])
        people_codes.append(data[1])
    person_code = SelectField('Person code', choices=[(elem, elem) for elem in people_codes])
    person_email = SelectField('Person email', choices=[(elem, elem) for elem in people_emails],
                               validators=[Email(), EmailCodeValidator()])
    material_names = get_material_names()
    material_name = SelectField('Material names', choices=[(elem[0], elem[0]) for elem in material_names],
                                validators=[RentalMaterialValidator()])
    price = IntegerField('Rental price')
    deposit = FloatField('Deposit')
    notes = StringField(u'Notes', widget=TextArea())
    submit = SubmitField('Register')






