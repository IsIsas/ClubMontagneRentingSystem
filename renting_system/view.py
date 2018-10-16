from flask import render_template, flash, redirect, url_for, jsonify
import logging
import os
from renting_system import app, db
from renting_system.forms import NewPersonForm, get_list_people, NewMaterialForm, NewRentalForm
from renting_system.model import Person, Material, Rental, get_person_code_by_email, \
    get_rentals, get_materials
from renting_system.utils import compute_code
from datetime import datetime

__author__ = "Isabella d'Annibale"
__email__ = "isabella.dannibale@gmail.com"

LOG = logging.getLogger(os.path.basename(__file__))
sh = logging.StreamHandler()
formatter = logging.Formatter('[%(name)s] %(levelname)s: %(message)s')
sh.setFormatter(formatter)
LOG.addHandler(sh)


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
        return redirect(url_for('people'))
    return render_template('people.html', form=form)


@app.route('/material', methods=['GET', 'POST'])
def material():
    form = NewMaterialForm()
    if form.validate_on_submit():
        new_material = Material(name=form.name.data,
                                brand=form.brand.data,
                                purchase_date=form.purchase_date.data,
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
        return redirect(url_for('material'))
    return render_template('material.html', form=form)


@app.route('/rentals', methods=['GET', 'POST'])
def rentals():
    form = NewRentalForm()
    if form.validate_on_submit():
        person_code = get_person_code_by_email(form.person_email.data)
        new_rental = Rental(person_code=str(person_code),
                            material_name=form.material_name.data,
                            date_rental=datetime.now(),
                            date_return=None,
                            price=form.price.data,
                            deposit=form.deposit.data,
                            notes=form.notes.data
                            )
        db.session.add(new_rental)
        db.session.commit()
        flash('New entry successfully added')
        return redirect(url_for('rentals'))
    return render_template('rentals.html', form=form)


'''@app.route('/people/<email:email>', methods=['GET', 'POST'])
def delete(email):
    code = get_person_code("", email)
    if delete_person(code):
        return render_template('people.html', )
'''


@app.route('/people_table', methods=['GET'])
def people_table():
    people_list = get_list_people()
    nl = []
    for e in people_list:
        nl.append(e.serialize)
    return jsonify(nl)


@app.route('/material_table', methods=['GET'])
def material_table():
    material_list = get_materials()
    nl = []
    for e in material_list:
        nl.append(e.serialize)
    return jsonify(nl)


@app.route('/rental_table', methods=['GET'])
def rental_table():
    rental_list = get_rentals()
    nl = []
    for e in rental_list:
        nl.append(e.serialize)
    return jsonify(nl)


if __name__ == '__main__':
    LOG.info('Hi! Welcome to the club montagne renting system')
    db.init_app(app)
    app.run()



