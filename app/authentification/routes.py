from flask import Blueprint, render_template, redirect, url_for, request
from app.simple_pages.models import User
from app.simple_pages.models import Task
from app.extensions.database import db
from datetime import datetime

blueprint = Blueprint('authentification', __name__)


@blueprint.route('/login')
def login():
    return render_template('authentification/login.html')


@blueprint.route('/register')
def register():
    return render_template('authentification/register.html')


@blueprint.get('/todo')
def dashboard():
    todos = Task.query.all()
    return render_template('authentification/todo.html', todos=todos)


@blueprint.post('/todo')
def savedtodo():
    name = request.form.get('name')
    date = request.form.get('date')
    time = request.form.get('time')
    date_format = datetime.strptime(date + ' ' + time, '%Y-%m-%d %H:%M')
    date = date_format.date()
    time = date_format.time()
    todo = Task(
        name=name,
        date=date,
        time=time,
        user_id=1
    )
    todo.save()
    # db.session.add(todo)
    # db.session.commit()
    return redirect(url_for('authentification.dashboard'))
