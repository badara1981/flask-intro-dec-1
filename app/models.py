from . import db

# TODO: Add a User model with username and password.
# When the user is saved to the database, the password should not be stored as clear text
# Find out how to safely store passwords in databases in applications built with Flask
    

class Reminder(db.Model):
    __tablename__ = "reminders"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text())

    # TODO: Design a method in the Reminder class called to_json() instance method that returns a dictionary that looks like this:
    # { "id": 1, "title": "Some title", "description": "Some description" }
    
    def to_json(self):
       return{
         "id" : self.id,
         "title": self.title,
         "description": self.description }