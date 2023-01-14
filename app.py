"""Flask app and SQLite setup."""

from flask import Flask
import sqlite3


app = Flask(__name__)


def connect_db():
    """Connects to sqlite database."""
    con = sqlite3.connect('medication.db')
    return con


def create_table():
    """Creates a medications table in the database."""
    try:
        con = connect_db()
        con.execute('''CREATE TABLE medications (
            name TEXT NOT NULL,
            notes TEXT NOT NULL,
            frequency INTEGER PRIMARY KEY NOT NULL
            );
        ''')

        con.commit()
        print("User table created.")
    except:
        print("Table creation failed")
    finally:
        con.close()


def insert_medication(medication):
    """Add a new medication entry to the table."""
    new_med = medication
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute("INSERT or IGNORE into medications (name, notes, frequency) VALUES (?, ?, ?)", 
        (medication['name'], medication['notes'], medication['frequency']))
        con.commit()
        con.rollback()
    except:
        print("Unable to add medication to database.")
    finally:
        con.close()


def get_meds():
    """Get all medications from the table."""
    meds = []
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute("SELECT * FROM medications")
        meds = cur.fetchall()
    except:
        print("Error: unable to fetch medications")
    finally:
        con.close()
    return meds


def get_med_by_name(name):
    """TEST AND FIX THIS FUNCTION"""
    """Get medication data by name."""
    medication = {}
    try:
        con = connect_db()
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM medication WHERE name = ?",
        (name,))
        row = cur.fetchone()

    except:
        medication = {}
    
    return medication


def update_med(medication):
    """TEST AND FIX THIS FUNCTION"""
    """Update a medication in the database."""
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute("UPDATE users SET name = ?, notes = ?, frequency = ?", 
        (medication['name'], medication['notes'], medication['frequency']))
        con.commit()
    except:
        con.rollback()
        updated_med = {}
    finally:
        con.close()


def delete_med(name):
    """Delete a medication from the database."""
    try:
        con = connect_db()
        con.execute("DELETE FROM medications WHERE name = ?",
        (name,))
        con.commit()
    except:
        con.rollback()
        print("Unable to delete medication.")
    finally:
        con.close()


"""example entry and function call

med1 = {"name": "Tylenol", "notes": "Take with food", "frequency": 1}
med2 = {"name": "Advil", "notes": "Take with foods", "frequency": 12}

insert_medication(med1)
insert_medication(med2)
#print(get_med_by_name("Tylenol"))
delete_med("Advil")
print(get_meds())
"""