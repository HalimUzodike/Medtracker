import sqlite3

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
        cur.execute("INSERT INTO medications (name, notes, frequency) VALUES (?, ?, ?)", 
        (medication['name'], medication['notes'], medication['frequency']))
        con.commit()
        new_med = get_user_by_id(cur.lastrowid)
    except:
        con.rollback()
    finally:
        con.close()
    return new_med


"""example entry and function call"""
medication = {
    'name': 'Tylenol',
    'notes': 'Take with food',
    'frequency': 4
}
print((insert_medication(medication)))