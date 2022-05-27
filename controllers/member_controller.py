from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.booking_repository as booking_repository
import repositories.fitness_class_repository as fitness_class_repository
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/show.html", members = members)

@members_blueprint.route("/members/add", methods=['GET'])
def add_member():
    return render_template("members/add.html")

@members_blueprint.route("/members", methods=['POST'])
def create_member():
    member_name = request.form['member_name']
    member = Member(member_name)
    member_repository.save(member)

    return redirect('/members')

@members_blueprint.route("/members/<id>/edit", methods=['GET'])
def edit_member(id):
    member = member_repository.select(id)
    return render_template('members/edit.html', member=member)


@members_blueprint.route("/members/<id>", methods=['POST'])
def update_member(id):
    member_name = request.form['member_name']
    member = Member(member_name, id)
    member_repository.update(member)

    return redirect('/members')

@members_blueprint.route("/members/<id>/book", methods=['GET'])
def book(id):
    member = member_repository.select(id)
    fitness_classes = fitness_class_repository.select_all()
    return render_template('members/book.html', member = member, fitness_classes = fitness_classes)

