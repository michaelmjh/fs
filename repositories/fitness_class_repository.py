from db.run_sql import run_sql
from models.booking import Booking
from models.fitness_class import FitnessClass
from models.member import Member

def save(fitness_class):
    sql = "INSERT INTO fitness_classes (class_name, class_time) VALUES (?, ?) RETURNING class_id"
    values = [fitness_class.class_name, fitness_class.class_time]
    results = run_sql(sql, values)
    fitness_class.class_id = results[0]['class_id']
    return fitness_class

def select_all():
    fitness_classes = []

    sql = "SELECT * FROM fitness_classes"
    results = run_sql(sql)
    for row in results:
        fitness_class = FitnessClass(row['class_name'],row['class_time'], row['class_id'])
        fitness_classes.append(fitness_class)
    return fitness_classes

def select(id):
    fitness_class = None
    sql = "SELECT * FROM fitness_classes WHERE class_id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        fitness_class = FitnessClass(result['class_name'], result['class_time'], result['class_id'] )
    return fitness_class

def delete_all():
    sql = "DELETE FROM fitness_classes"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM fitness_classes WHERE class_id = ?"
    values = [id]
    run_sql(sql, values)

def update(fitness_class):
    sql = "UPDATE fitness_classes SET (class_name, class_time) = (?, ?) WHERE class_id = ?"
    values = [fitness_class.class_name, fitness_class.class_time, fitness_class.class_id]
    run_sql(sql, values)

def select_booked_members(id):
    booked_members = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON members.member_id = bookings.member_id WHERE class_id = ?"
    values = [id]
    results = run_sql(sql, values)

    for result in results:
        member_name = result['member_name']
        member_id = result['member_id']
        new_member = Member(member_name, member_id)
        booked_members.append(new_member)
    return booked_members
    