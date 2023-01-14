API endpoints:

GET: localhost:5000/api/meds/

POST: localhost:5000/api/meds/add requests JSON data for name, notes, and frequency. {"name": "medication", "notes": "take twice a day", "frequency: 1}

DELETE: localhost:5000/api/meds/delete requests JSON data for name string.

The flask app runs on port 5000.

views.py points the app to index.html in the templates folder.
