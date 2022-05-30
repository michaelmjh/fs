from db.run_sql import run_sql
from models.booking import Booking
from models.fitness_class import FitnessClass
from models.member import Member

def save(member):
    sql = "INSERT INTO members (first_name, last_name, premium_member, active) VALUES (?, ?, ?, ?) RETURNING member_id"
    values = [member.first_name, member.last_name, member.premium_member, member.active]
    results = run_sql(sql, values)
    member.member_id = results[0]['member_id']
    return member

def select_active():
    members = []

    sql = "SELECT * FROM members WHERE active = True"
    results = run_sql(sql)
    for row in results:

        member = Member(row['first_name'], row['last_name'], row['premium_member'], row['active'], row['member_id'])
        members.append(member)
    return members

def select_deactive():
    members = []

    sql = "SELECT * FROM members WHERE active = False"
    results = run_sql(sql)
    for row in results:

        member = Member(row['first_name'], row['last_name'], row['premium_member'], row['active'], row['member_id'])
        members.append(member)
    return members

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE member_id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['premium_member'], result['active'], result['member_id'])
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE member_id = ?"
    values = [id]
    run_sql(sql, values)

def update(member):
    sql = "UPDATE members SET (first_name, last_name, premium_member, active) = (?, ?, ?, ?) WHERE member_id = ?"
    values = [member.first_name, member.last_name, member.premium_member, member.active, member.member_id]
    run_sql(sql, values)

def select_booked_classes(id):
    booked_classes = []
    sql = "SELECT fitness_classes.* FROM fitness_classes INNER JOIN bookings ON fitness_classes.class_id = bookings.class_id WHERE member_id = ?"
    values = [id]
    results = run_sql(sql, values)

    for result in results:
        name = result['name']
        time = result['time']
        capacity = result['capacity']
        active = True
        class_id = result['class_id']
        new_class= FitnessClass(name, time, capacity, active, class_id)
        booked_classes.append(new_class)
    return booked_classes