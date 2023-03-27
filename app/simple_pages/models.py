from app.extensions.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    last_name = db.Column(db.String(80), unique = True)
    first_name = db.Column(db.String(80), unique=True)
    e_mail = db.Column(db.String((80)))
    password = db.Column(db.String(80))




    