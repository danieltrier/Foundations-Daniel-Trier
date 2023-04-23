from app.extensions.database import db, CRUDMixin
from datetime import datetime


class User(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(80), unique=True)
    first_name = db.Column(db.String(80), unique=True)
    e_mail = db.Column(db.String(150))
    password = db.Column(db.String(80))
    tasks = db.relationship('Task', backref='user', lazy=True)


class Task(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    time = db.Column(db.Time, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
