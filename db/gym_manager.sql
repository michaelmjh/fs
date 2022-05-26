PRAGMA FOREIGN_KEYS = ON;

DROP TABLE bookings;
DROP TABLE members;
DROP TABLE fitness_classes;

CREATE TABLE members (
    member_id INTEGER PRIMARY KEY AUTOINCREMENT,
    member_name VARCHAR
);

CREATE TABLE fitness_classes (
    class_id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_name VARCHAR,
    class_time VARCHAR
);

CREATE TABLE bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
        FOREIGN KEY (class_id)
            REFERENCES fitness_classes(class_id) ON DELETE CASCADE,
        FOREIGN KEY (member_id)
            REFERENCES members(member_id) ON DELETE CASCADE
);