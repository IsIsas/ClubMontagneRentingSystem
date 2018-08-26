#!/bin/env python
from flask import render_template, flash
import logging
import os
from renting_system import create_app, db
from renting_system.forms import NewPersonForm, get_list_people, NewMaterialForm, NewRentalForm
from renting_system.model import Person, Material, Rental
from renting_system.utils import compute_code


__author__ = "Isabella d'Annibale"
__email__ = "isabella.dannibale@gmail.com"

LOG = logging.getLogger(os.path.basename(__file__))
sh = logging.StreamHandler()
formatter = logging.Formatter('[%(name)s] %(levelname)s: %(message)s')
sh.setFormatter(formatter)
LOG.addHandler(sh)

app = create_app()


@app.route('/')
def welcome():
    return render_template('base.html')


@app.route('/people', methods=['GET', 'POST'])
def people():
    form = NewPersonForm()
    if form.validate_on_submit():
        new_person = Person(name=form.name.data,
                            surname=form.surname.data,
                            email=form.email.data,
                            code=compute_code(form.name.data,form.surname.data,form.bday.data),
                            phone=form.phone.data,
                            type=form.type.data,
                            bday=form.bday.data
                            )

        # add Person to the database
        db.session.add(new_person)
        db.session.commit()
        flash('You have successfully registered one person')
    people_list = get_list_people()
    return render_template('people.html', form=form, people=people_list)


@app.route('/renting')
def renting():
    return render_template('renting.html')


@app.route('/material')
def material():
    form = NewMaterialForm()
    if form.validate_on_submit():
        new_material = Material(name=form.name.data,
                                brand=form.brand.data,
                                purchase_date=form.Purchase_date.data,
                                notes=form.notes.data,
                                size=form.size.data,
                                skin=form.skin.data,
                                price=form.price.data,
                                type=form.type.data
                                )

        # add Person to the database
        db.session.add(new_material)
        db.session.commit()
        flash('New entry successfully added')
    return render_template('material.html', form=form)


@app.route('/rentals')
def rentals():
    form = NewRentalForm()
    if form.validate_on_submit():
        new_rental = Rental()

        db.session.add(new_rental)
        db.session.commit()
        flash('New entry successfully added')
    return render_template('rental.html', form=form)


if __name__ == '__main__':
    LOG.info('Hi! Welcome to the club montagne renting system')
    app.run()

