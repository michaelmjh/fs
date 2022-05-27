from db.run_sql import run_sql
from models.booking import Booking
from models.fitness_class import FitnessClass
from models.member import Member

import repositories.fitness_class_repository as fitness_repository
import repositories.member_repository as member_repository

def save(booking):
    sql = "INSERT INTO bookings (class_id, member_id) VALUES (?, ?) RETURNING booking_id"
    values = [booking.fitness_class.class_id, booking.member.member_id]
    results = run_sql(sql, values)
    booking.booking_id = results[0]['booking_id']
    return booking

def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for row in results:
        fitness_class = fitness_repository.select(row['class_id'])
        member = member_repository.select(row['member_id'])
        booking = Booking(fitness_class, member, row['booking_id'])
        bookings.append(booking)
    return bookings

def select(id):
    booking = None
    sql = "SELECT * FROM bookings WHERE booking_id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        fitness_class = fitness_repository.select(result['class_id'])
        member = member_repository.select(result['member_id'])
        booking = Booking(fitness_class, member, result['booking_id'])
    return booking

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bookings WHERE booking_id = ?"
    values = [id]
    run_sql(sql, values)

def update(booking):
    sql = "UPDATE bookings SET (class_id, member_id) = (?, ?) WHERE booking_id = ?"
    values = [booking.fitness_class.class_id, booking.member.member_id, booking.booking_id]
    run_sql(sql, values)