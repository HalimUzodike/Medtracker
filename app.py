"""Flask app and SQLite setup."""

from flask import Flask
import sqlite3

app = Flask(__name__)


def connect_db():
    """Connects to sqlite database."""
    try:
        con = sqlite3.connect('medication.db')
    except:
        print("medicaiton.db connetion failed")
    finally:
        return con


def create_table():
    """Creates a medications table in the database."""
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute("CREATE TABLE medications ("
                    "name TEXT NOT NULL, "
                    "notes TEXT NOT NULL, "
                    "frequency INTEGER NOT NULL)")

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
    """Get medication data by name."""
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute(f"SELECT * FROM medications WHERE name= ?;",(name,))
        row = cur.fetchall()
        print(row)
    except:
        print("get med by name failed")
    finally:
        con.close()
        return row


def update_med(medication):
    """TEST AND FIX THIS FUNCTION"""
    """Update a medication in the database."""
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute("UPDATE or IGNORE medications SET name = ?, notes = ?, frequency = ? WHERE name = ?",
                    (medication['name'], medication['notes'], medication['frequency'], medication['name']))
        con.commit()
    except:
        # con.rollback()
        print("update med failed")
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


# example entry and function call

# create_table()

med1 = {"name": "Tylenol", "notes": "Take with food", "frequency": 1}
med2 = {"name": "Advil", "notes": "Take with foods", "frequency": 12}
med3 = {"name": "NotTylenol", "notes": "Take with foodsd", "frequency": 14}
med4 = {"name": "NotAdvil", "notes": "Take with foodsdd", "frequency": 13}

insert_medication(med1)
insert_medication(med2)
insert_medication(med3)
insert_medication(med4)

medication = {"name": "NotAdvil", "notes": "Take with foodsdd", "frequency": 30}
new_medication = {"name": "NotAdvil", "notes": "Take with foodsdd", "frequency": 77}


update_med(medication)
update_med(new_medication)



#print(get_med_by_name("Tylenol"))
# print(get_med_by_name())
# print(get_med_by_name())
#delete_med("Advil")
# print(get_meds())


