from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
from models.fitness_class import FitnessClass
from models.member import Member
import repositories.booking_repository as booking_repository
import repositories.fitness_class_repository as fitness_class_repository
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_active()
    return render_template("members/show.html", members = members)

@members_blueprint.route("/members/deactived")
def deactive_members():
    members = member_repository.select_deactived()
    return render_template("members/deactive.html", members = members)

@members_blueprint.route("/members/add", methods=['GET'])
def add_member():
    return render_template("members/add.html")

@members_blueprint.route("/members", methods=['POST'])
def create_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    member = Member(first_name, last_name)
    member_repository.save(member)

    return redirect('/members')

@members_blueprint.route("/members/<id>/edit", methods=['GET'])
def edit_member(id):
    member = member_repository.select(id)
    return render_template('members/edit.html', member=member)

@members_blueprint.route("/members/<id>", methods=['POST'])
def update_member(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    active_val = request.form['active']
    if active_val == 1:
        active = True
    else:
        active = False
    member = Member(first_name, last_name, active, id)
    member_repository.update(member)
    return redirect('/members')

@members_blueprint.route("/members/<id>/details", methods=['GET'])
def details(id):
    member = member_repository.select(id)
    booked_classes = member_repository.select_booked_classes(id)
    return render_template('/members/details.html', member = member, booked_classes = booked_classes)

@members_blueprint.route("/members/<id>/book", methods=['GET'])
def book(id):
    unbooked_classes = []
    member = member_repository.select(id)
    all_classes = fitness_class_repository.select_all()
    booked_classes = member_repository.select_booked_classes(id)
    for aclass in all_classes:
        booked = False
        for bclass in booked_classes:
            if aclass.class_id == bclass.class_id:
                booked = True
        if booked == False:
            unbooked_classes.append(aclass)

    return render_template('members/book.html', member = member, unbooked_classes = unbooked_classes)

@members_blueprint.route("/members/<id>/book", methods=['POST'])
def create_booking(id):
    member = member_repository.select(id)
    class_id = request.form['class_id']
    fitness_class = fitness_class_repository.select(class_id)
    booking = Booking(fitness_class, member)
    booking_repository.save(booking)
    return redirect(f'/members/{id}/details')
    