from renting_system.model import insert_new_person, show_people
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired, Email
from renting_system.model import Person


class NewPersonForm(FlaskForm):
    """
    Form to create a new person
    """
    name = StringField('Last Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    code = StringField('Code', validators=[DataRequired()])
    phone = StringField('Phone number', validators=[DataRequired()])
    type = IntegerField('Type', validators=[DataRequired()])
    bday = DateField('Birthday', validators=[DataRequired()], format='%d/%m/%Y')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if Person.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_code(self, field):
        if Person.query.filter_by(code=field.data).first():
            raise ValidationError('Code is already in use.')


def get_list_people():
    types, people = show_people()
    t = {}
    for row in types:
        t[row[0]] = row[1]
    people_table = []
    for row in people:
        people_table.append([elem for elem in row])

    return people_table


class NewMaterialForm(FlaskForm):
    """
    Form to create a new material
    """
    name = StringField('Name')
    brand = StringField('Brand')
    purchase_date = DateField('Purchase date')
    notes = StringField('Notes')
    size = IntegerField('Size')
    skin = IntegerField('Type')
    price = DateField('Birthday')
    # TODO: get the choices from a table on the db
    myChoices = ['ski']
    type = SelectField(u'Type', choices=myChoices)
    submit = SubmitField('Register')


class NewRentalForm(FlaskForm):

    person_code = StringField('Name')
    material_name = StringField('Brand')
    date_rental = DateField('Purchase date')
    date_return = StringField('Notes')
    price = IntegerField('Size')
    deposit = IntegerField('Type')
    returned = DateField('Birthday')
    notes = SelectField(u'Notes')
    submit = SubmitField('Register')
