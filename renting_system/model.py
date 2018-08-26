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


def show_people():
    db = pymysql.connect(host="localhost", port=3306, user="root", password="miao", db="club_montagne")
    try:
        with db.cursor() as cursor:
            # Create a new record
            sql = """SELECT * from TYPES"""
            cursor.execute(sql)
            types = cursor.fetchall()
            sql = """SELECT * from PEOPLE"""
            cursor.execute(sql)
            people = cursor.fetchall()

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        db.commit()
    finally:
        db.close()
    return types, people


def insert_new_person(name, surname, email, type, phone, code, bday):
    db = pymysql.connect(host="localhost", port=3306, user="root", password="miao", db="club_montagne")
    try:
        with db.cursor() as cursor:
            # Create a new record
            sql = """INSERT INTO PEOPLE (name, surname, email, type, phone, code) """ \
                  """VALUES("%s", "%s", "%s", %d, "%s", "%s, "%s")""" % (name, surname, email, type, phone, code, bday)
            print(sql)
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        db.commit()
    finally:
        db.close()


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


def insert_new_matos(name, marque, date, type_matos):
    db = pymysql.connect(host="localhost", port=3306, user="root", password="miao", db="club_montagne")
    try:
        with db.cursor() as cursor:
            # Create a new record
            sql = """INSERT INTO PEOPLE (name, marque, dateachat, type) VALUES("%s", "%s", "%s", %s, "%s")""" % (name, marque, date, type_matos)
            print(sql)
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        db.commit()
    finally:
        db.close()


class Rental(db.Model):

    __tablename__ = 'RENTALS'

    person_code = db.Column(db.String(16))
    material_name = db.Column(db.String(10))
    date_rental = db.Column(db.Date)
    date_return = db.Column(db.Date)
    price = db.Column(db.Float)
    deposit = db.Column(db.Float)
    returned = db.Column(db.Integer)
    notes = db.Column(db.String(200))
    id = db.Column(db.Integer, primary_key=True)


