from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
from models.fitness_class import FitnessClass
from models.member import Member
import repositories.booking_repository as booking_repository
import repositories.fitness_class_repository as fitness_class_repository
import repositories.member_repository as member_repository

fitness_class_blueprint = Blueprint("fitness_class", __name__)

@fitness_class_blueprint.route("/classes")
def classes():
    classes = fitness_class_repository.select_active()
    return render_template("classes/show.html", classes = classes)

@fitness_class_blueprint.route("/classes/deactive")
def deactivated_classes():
    classes = fitness_class_repository.select_deactive()
    return render_template("classes/deactive.html", classes = classes)

@fitness_class_blueprint.route("/classes/add", methods=['GET'])
def add_class():
    return render_template("classes/add.html")

@fitness_class_blueprint.route("/classes", methods=['POST'])
def create_class():
    name = request.form['name']
    time = request.form['time']
    fitness_class = FitnessClass(name, time)
    fitness_class_repository.save(fitness_class)

    return redirect('/classes')

@fitness_class_blueprint.route("/classes/<id>/edit", methods=['GET'])
def edit_class(id):
    fitness_class = fitness_class_repository.select(id)
    return render_template('classes/edit.html', fitness_class=fitness_class)

@fitness_class_blueprint.route("/classes/<id>", methods=['POST'])
def update_class(id):
    name = request.form['name']
    time = request.form['time']
    active_val = request.form['active']
    if active_val == "1":
        active = True
    elif active_val == "0":
        active = False
    fitness_class = FitnessClass(name, time, active, id)
    fitness_class_repository.update(fitness_class)
    return redirect('/classes')

@fitness_class_blueprint.route("/classes/<id>/details", methods = ['GET'])
def details(id):
    fitness_class = fitness_class_repository.select(id)
    booked_members = fitness_class_repository.select_booked_members(id)
    return render_template('/classes/details.html', fitness_class = fitness_class, booked_members = booked_members)

@fitness_class_blueprint.route('/classes/<id>/book', methods = ['GET'])
def book_members(id):
    unbooked_members = []
    fitness_class = fitness_class_repository.select(id)
    all_members = member_repository.select_active()
    booked_members = fitness_class_repository.select_booked_members(id)
    for member in all_members:
        booked = False
        for bmember in booked_members:
            if member.member_id == bmember.member_id:
                booked = True
        if booked == False:
            unbooked_members.append(member)

    return render_template('classes/book_members.html', fitness_class = fitness_class, unbooked_members = unbooked_members)

@fitness_class_blueprint.route('/classes/<id>/book', methods=['POST'])
def result(id):
    members_list = request.form.getlist('member_selected')
    for member in members_list:
        member_to_book = member_repository.select(member)
        fitness_class = fitness_class_repository.select(id)
        new_booking = Booking(fitness_class, member_to_book)
        booking_repository.save(new_booking)
    return redirect(f"/classes/{id}/details")