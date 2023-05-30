from flask import jsonify, request

from . import create_app, db
from .models import Reminder

app = create_app()


@app.route("/")
def index():
    breakpoint()
    
    reminders = Reminder.query.all() # Queries the database using a SQLAlchemy model
    # TODO: currently reminder_data is is empty, 
    # use the Reminder model to query for data and replace None with such 
    # a database call.
    reminder_data = Reminder(title = request.json['title'],
    description=request.json['description']
    )


    # Do not touch the code below (Fix code up there 👆👆)
    reminder_data = [item.to_json() for item in reminder_data]
    return jsonify({"reminders": reminder_data})


@app.route("/add-reminder", methods=["POST"])
def add_reminder():
    try:
        # TODO: Create an instance of Reminder and using the SQLAlchemy documentation
        # we update it the way it is usually prescribed in the docs.
        # Use the to_json() method we defined in the class earlier
        
        reminder_data = None # replace None with some code 
        
        reminder_data = Reminder(title = request.json['title'],
    description=request.json['description']
    )




        # DO not touch code below
        return jsonify(reminder_data.to_json())
    except Exception as e:
        print(e)
        return jsonify({"message": "Something bad happened"}), 500


@app.route("/reminders/<int:reminder_id>")
def reminder(reminder_id):
    # TODO: Replace the value of None with a SQLalchemy database call
    reminder_data = None

    # DO NOT TOUCH the code below this line
    if not reminder_data:
        return jsonify({"message": "Reminder not found"}), 404
    return jsonify(reminder_data.to_json())


@app.route("/reminders/<int:reminder_id>", methods=["DELETE"])
def delete_reminder(reminder_id):
    # TODO: Add code to delete a reminder
    reminder_data = None
    
    # Do not touch code below
    return jsonify({"message": "Successfully deleted!"})


@app.route("/reminders/<int:reminder_id>/update", methods=["PUT"])
def update_reminder(reminder_id):
    try:
        reminder_data = Reminder.query.get(reminder_id)
        reminder_data.title = request.json.get("title", reminder_data.title)
        reminder_data.description = request.json.get(
            "description", reminder_data.description
        )
        db.session.commit()
        return jsonify(reminder_data.to_json()), 201
    except TypeError:
        return jsonify({"message": "Reminder not found"}), 404
