from controllers import fitness_classes_controller
from db.run_sql import run_sql
from models.booking import Booking
from models.fitness_class import FitnessClass
from models.member import Member

def save(fitness_class):
    sql = "INSERT INTO fitness_classes (name, time, capacity, active) VALUES (?, ?, ?, ?) RETURNING class_id"
    values = [fitness_class.name, fitness_class.time, fitness_class.capacity, fitness_class.active]
    results = run_sql(sql, values)
    fitness_class.class_id = results[0]['class_id']
    return fitness_class

def select_active():
    fitness_classes = []

    sql = "SELECT * FROM fitness_classes WHERE active = True"
    results = run_sql(sql)
    for row in results:
        fitness_class = FitnessClass(row['name'], row['time'], row['capacity'], row['active'], row['class_id'])
        fitness_classes.append(fitness_class)
    return fitness_classes

def select_standard(fitness_classes):
    standard_classes = []
    for fclass in fitness_classes:
        if int(fclass.time) < 17 or int(fclass.time) > 20:
            standard_classes.append(fclass)
    return standard_classes

def select_deactive():
    fitness_classes = []

    sql = "SELECT * FROM fitness_classes WHERE active = False"
    results = run_sql(sql)
    for row in results:
        fitness_class = FitnessClass(row['name'], row['time'], row['capacity'], row['active'], row['class_id'])
        fitness_classes.append(fitness_class)
    return fitness_classes

def select(id):
    fitness_class = None
    sql = "SELECT * FROM fitness_classes WHERE class_id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        fitness_class = FitnessClass(result['name'], result['time'], result['capacity'], result['active'], result['class_id'] )
    return fitness_class

def delete_all():
    sql = "DELETE FROM fitness_classes"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM fitness_classes WHERE class_id = ?"
    values = [id]
    run_sql(sql, values)

def update(fitness_class):
    sql = "UPDATE fitness_classes SET (name, time, capacity, active) = (?, ?, ?, ?) WHERE class_id = ?"
    values = [fitness_class.name, fitness_class.time, fitness_class.capacity, fitness_class.active, fitness_class.class_id]
    run_sql(sql, values)

def select_booked_members(id):
    booked_members = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON members.member_id = bookings.member_id WHERE class_id = ?"
    values = [id]
    results = run_sql(sql, values)

    for result in results:
        first_name = result['first_name']
        last_name = result['last_name']
        premium_member = result['premium_member']
        member_id = result['member_id']      
        active = result['active']      
        new_member = Member(first_name, last_name, premium_member, active, member_id)
        booked_members.append(new_member)
    return booked_members

def select_premium_members(members):
    available_members = []
    for member in members:
        if member.premium_member == True:
            available_members.append(member)
    return available_members