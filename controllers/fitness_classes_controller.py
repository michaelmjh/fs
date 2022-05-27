from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.fitness_class import FitnessClass
from models.member import Member
import repositories.fitness_class_repository as fitness_class_repository
import repositories.member_repository as member_repository

fitness_class_blueprint = Blueprint("fitness_class", __name__)

@fitness_class_blueprint.route("/classes")
def classes():
    classes = fitness_class_repository.select_all()
    return render_template("classes/show.html", classes = classes)

@fitness_class_blueprint.route("/classes/add", methods=['GET'])
def add_class():
    return render_template("classes/add.html")

@fitness_class_blueprint.route("/classes", methods=['POST'])
def create_class():
    class_name = request.form['class_name']
    class_time = request.form['class_time']
    fitness_class = FitnessClass(class_name, class_time)
    fitness_class_repository.save(fitness_class)

    return redirect('/classes')

@fitness_class_blueprint.route("/classes/<id>/edit", methods=['GET'])
def edit_class(id):
    fitness_class = fitness_class_repository.select(id)
    return render_template('classes/edit.html', fitness_class=fitness_class)


@fitness_class_blueprint.route("/classes/<id>", methods=['POST'])
def update_member(id):
    class_name = request.form['class_name']
    class_time = request.form['class_time']
    fitness_class = FitnessClass(class_name, class_time, id)
    fitness_class_repository.update(fitness_class)

    return redirect('/classes')