#!/usr/bin/python

import pymysql
from renting_system import db


class Person(db.Model):

    __tablename__ = 'PEOPLE'

    name = db.Column(db.String(30), unique=True, primary_key=True)
    surname = db.Column(db.String(30), unique=True, primary_key=True)
    email = db.Column(db.String(30), unique=True, primary_key=True)
    type = db.Column(db.Integer)
    phone = db.Column(db.String(20), unique=True)
    code = db.Column(db.String(30), unique=True)
    bday = db.Column(db.Date)


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
