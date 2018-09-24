#!/usr/bin/python

import pymysql
from renting_system import db


class Person(db.Model):

    __tablename__ = 'PEOPLE'

    name = db.Column(db.String(30))
    surname = db.Column(db.String(30))
    email = db.Column(db.String(30), unique=True, primary_key=True)
    type = db.Column(db.Integer)
    phone = db.Column(db.String(20), unique=True)
    code = db.Column(db.String(30), unique=True)
    bday = db.Column(db.Date)

    def __init__(self, name, surname, email, type, phone, code, bday):
        self.name = name
        self.surname = surname
        self.email = email
        self.type = type
        self.phone = phone
        self.code = code
        self.bday = bday

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'type': self.type,
            'phone': self.phone,
            'code': self.code,
            'bday': self.bday
        }


class Material(db.Model):

    __tablename__ = 'MATERIAL'

    # name == code
    name = db.Column(db.String(10), primary_key=True)
    brand = db.Column(db.String(30))
    purchase_date = db.Column(db.Date)
    notes = db.Column(db.String(200))
    size = db.Column(db.Integer)
    skin = db.Column(db.Integer)
    price = db.Column(db.Float)
    type = db.Column(db.String(20))

    def __init__(self, name, brand, purchase_date, notes, size, skin, price, type):
        self.name = name
        self.brand = brand
        self.purchase_date = purchase_date
        self.notes = notes
        self.size = size
        self.skin = skin
        self.price = price
        self.type = type

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'brand': self.brand,
            'purchase_date': self.purchase_date,
            'notes': self.notes,
            'size': self.size,
            'skin': self.skin,
            'price': self.price,
            'type': self.type
        }


class Rental(db.Model):

    __tablename__ = 'RENTALS'

    person_code = db.Column(db.String(16))
    material_name = db.Column(db.String(10))
    date_rental = db.Column(db.Date)
    date_return = db.Column(db.Date)
    price = db.Column(db.Float)
    deposit = db.Column(db.Float)
    notes = db.Column(db.String(200))
    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, person_code, material_name, date_rental, date_return, price, deposit, notes):
        self.person_code = person_code
        self.material_name = material_name
        self.date_rental = date_rental
        self.date_return = date_return
        self.price = price
        self.deposit = deposit
        self.notes = notes


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'person_code': self.person_code,
            'material_name': self.material_name,
            'date_rental': self.date_rental,
            'date_return': self.date_return,
            'price': self.price,
            'deposit': self.deposit,
            'notes': self.notes,
            'id': self.id
        }


class MaterialTypes(db.Model):

    __tablename__ = 'MATERIAL_TYPES'

    name = db.Column(db.String(20), primary_key=True)
    rental_price = db.Column(db.Float)
    deposit_price = db.Column(db.Float)


class Types(db.Model):

    __tablename__ = 'TYPES'

    type_name = db.Column(db.String(30), primary_key=True)
    price_factor = db.Column(db.Float)


def show_people():
    people = Person.query.all()
    return people


def get_people_datas():
    people_datas = Person.query.with_entities(Person.email, Person.code)
    return people_datas


def get_person_code(code, email):
    if code is not None:
        return code
    person_code = Person.query().with_entities(Person.code).filter_by(email=email)
    return person_code


def get_material_names():
    material_names = Material.query.with_entities(Material.name)
    return material_names


def get_material_types():
    material_types = MaterialTypes.query.with_entities(MaterialTypes.name)
    return material_types


def get_rentals():
    rentals = Rental.query.all()
    return rentals


def get_materials():
    materials = Material.query.all()
    return materials
