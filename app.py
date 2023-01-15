"""Flask app and SQLite setup."""

from flask import Flask
import sqlite3
from datetime import date

app = Flask(__name__)

meds = []


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
                    "dosage TEXT, "
                    "frequency TEXT, "
                    "notes TEXT)")


        con.commit()
        print("User table created.")
    except:
        print("Table creation failed")
    finally:
        con.close()


def insert_medication(medication):
    """Add a new medication entry to the table."""
    new_med = medication
    #try:
    con = connect_db()
    cur = con.cursor()
    cur.execute("INSERT or IGNORE into medications (name, notes, frequency, dosage) VALUES (?, ?, ?, ?)",
                (medication['name'], medication['notes'], medication['frequency'], medication['dosage']))
    con.commit()
    con.rollback()
#except:
 #   print("Unable to add medication to database.")
#finally:
    con.close()


def get_meds():
    """Get all medications from the table."""
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute("SELECT * FROM medications")
        medication_data = cur.fetchall()

        for data in medication_data:
            dict = {"name": data[0], "dosage": data[1], "frequency": data[2], "notes": data[3]}
            meds.append(dict)

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
    """Update a medication in the database."""
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute("UPDATE or IGNORE medications SET name = ?, notes = ?, frequency = ?, dose = ?, WHERE name = ?",
                    (medication['name'], medication['notes'], medication['frequency'], medication['dosage'], medication['name']))
        con.commit()
    except:
        con.rollback()
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

# TEST BLOCK
#example entry and function call

# create_table()

# today = str(date.today())

med1 = {"name": "Tylenol", "notes": "Take with food", "frequency": "every day", "dosage": "take 2 every 4 hours"}
med2 = {"name": "Ibuprofen", "notes": "", "frequency": "every day as needed", "dosage": "take 4 every 4 hours"}
# med3 = {"name": "NotTylenol", "notes": "Take with food", "frequency": 14, "dosage": 10}
# med4 = {"name": "NotAdvil", "notes": "Take with food", "frequency": 13, "dosage": 3}

insert_medication(med1)
insert_medication(med2)
# insert_medication(med3)
# insert_medication(med4)


#update_med(med1)
#update_med(new_medication)

#delete_med("Tylenol")

#print(get_med_by_name("Tylenol"))
print(get_meds())












