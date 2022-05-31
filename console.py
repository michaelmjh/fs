import pdb
from models.booking import Booking
from models.fitness_class import FitnessClass
from models.member import Member

import repositories.booking_repository as booking_repository
import repositories.fitness_class_repository as fitness_class_repository
import repositories.member_repository as member_repository

# --------------------------------------------------------------------------
# UNCOMMENT CODE BELOW TO INSERT TEST DATA INTO DATABASE

# booking_repository.delete_all()
# fitness_class_repository.delete_all()
# member_repository.delete_all()

# member_1 = Member("Colonel John", "Matrix", False)
# member_repository.save(member_1)

# member_2 = Member("The", "Terminator", False)
# member_repository.save(member_2)

# member_3 = Member('Major Alan "Dutch"', 'Schaefer', True)
# member_repository.save(member_3)

# member_4 = Member("Conan T.", "Barbarian", True)
# member_repository.save(member_4)

# member_5 = Member("Detective John", "Kimble", False)
# member_repository.save(member_5)

# class_1 = FitnessClass("Flex Zone", "19", 5)
# fitness_class_repository.save(class_1)

# class_2 = FitnessClass("Protein 101", "21", 2)
# fitness_class_repository.save(class_2)

# class_3 = FitnessClass("Gains O'Clock", "12", 5)
# fitness_class_repository.save(class_3)

# booking_1 = Booking(class_1, member_1)
# booking_repository.save(booking_1)

# booking_2 = Booking(class_2, member_1)
# booking_repository.save(booking_2)

# booking_3 = Booking(class_3, member_1)
# booking_repository.save(booking_3)

# booking_4 = Booking(class_3, member_2)
# booking_repository.save(booking_4)

# booking_5 = Booking(class_2, member_3)
# booking_repository.save(booking_5)

# UNCOMMENT TO INSERT TEST DATA INTO DATABASE
# --------------------------------------------------------------------------

members = member_repository.select_active()
for member in members:
    print(member.__dict__)

members = member_repository.select_deactive()
for member in members:
    print(member.__dict__)

classes = fitness_class_repository.select_active()
for fc in classes:
    print(fc.__dict__)

classes = fitness_class_repository.select_deactive()
for fc in classes:
    print(fc.__dict__)

bookings = booking_repository.select_all()
for booking in bookings:
    print(booking.__dict__)

pdb.set_trace()
