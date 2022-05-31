<img width="1080" alt="home_page" src="https://user-images.githubusercontent.com/74016689/171225711-449259e5-ca42-44d4-8f88-0191f0ad997d.png">

## Brief
    A local gym has asked for a piece of software to help them to manage memberships, and register members for classes.

    MVP
    The app allows staff to create and edit Members
    The app allows staff to create and edit Classes
    The app should allow the gym to book members on specific classes
    The app should show a list of all upcoming classes
    The app should show all members that are booked in for a particular class
    Classes could have a maximum capacity, and users can only be added while there is space remaining.
    The gym could be able to give its members Premium or Standard membership. Standard members can only be signed up for classes during off-peak hours.
    The Gym could mark members and classes as active/deactivated. Deactivated members/classes will not appear when creating bookings.

## Running Instructions
    Initialise the database:
    - sqlite3 db/gym_manager.db < db/gym_manager.sql
    Populate database with test data:
    - python3 console.py
    Run app:
    - flask run

## Technologies Used
    - Python
    - SQLite3
    - HTML
    - CSS
    - Flask

## Screenshots
<img width="1080" alt="show_classes" src="https://user-images.githubusercontent.com/74016689/171225728-370154e5-77b7-4ecc-b505-2f51d10ca9e0.png">
<img width="1080" alt="class_details" src="https://user-images.githubusercontent.com/74016689/171225706-a738a8ec-1806-4949-be60-b02b65947698.png">
<img width="1080" alt="add_member" src="https://user-images.githubusercontent.com/74016689/171225694-b3dc4461-014f-4156-b598-4397a9e63be1.png">
<img width="1080" alt="show_bookings" src="https://user-images.githubusercontent.com/74016689/171225723-86ca2d3f-492b-41af-8568-cafa4af1ded6.png">
