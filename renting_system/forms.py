from renting_system.model import show_people
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, IntegerField, DateField,\
    SelectField, FloatField, BooleanField
from wtforms.validators import DataRequired, Email
from renting_system.model import Person, get_people_datas, get_material_names, get_material_types
from wtforms.widgets import TextArea
from enum import Enum


class PeopleTypes(Enum):
    COMMITTEE = 1
    EPFL_STUDENT = 2
    UNIL_STUDENT = 3
    EPFL_PHD = 4
    UNIL_PHD = 5


class NewPersonForm(FlaskForm):
    """
    Form to create a new person
    """
    name = StringField('Last Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone number', validators=[DataRequired()])
    people_types = [('%s'%p.value, p.name) for p in PeopleTypes]
    print(people_types)
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
    purchase_date = DateField('Purchase date', format='%d/%m/%Y',)
    notes = StringField('Notes', widget=TextArea())
    size = IntegerField('Size')
    skin = BooleanField('Skin')
    price = FloatField('Price')
    material_types = get_material_types()
    type = SelectField(u'Type', choices=[(elem[0], elem[0]) for elem in material_types])
    submit = SubmitField('Register')


class NewRentalForm(FlaskForm):
    people_emails = []
    people_codes = []
    for data in get_people_datas():
        people_emails.append(data[0])
        people_codes.append(data[1])
    person_email = SelectField('Person email', choices=[(elem, elem) for elem in people_emails])
    material_names = get_material_names()
    material_name = SelectField('Material names', choices=[(elem, elem) for elem in material_names])
    date_rental = DateField('Purchase date')
    price = IntegerField('Rental price')
    deposit = FloatField('Deposit')
    notes = StringField(u'Notes', widget=TextArea())
    submit = SubmitField('Register')

