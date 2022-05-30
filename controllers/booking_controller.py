from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
from models.fitness_class import FitnessClass
from models.member import Member
import repositories.booking_repository as booking_repository
import repositories.fitness_class_repository as fitness_class_repository
import repositories.member_repository as member_repository

booking_blueprint = Blueprint("bookings", __name__)

@booking_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/show.html", bookings = bookings)

@booking_blueprint.route("/bookings/<id>/del", methods=['GET'])
def delete(id):
    booking_repository.delete(id)
    return redirect("/bookings")