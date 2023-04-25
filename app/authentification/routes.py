from flask import Blueprint, render_template, redirect, url_for, request
from app.simple_pages.models import User
from app.simple_pages.models import Task
from app.extensions.database import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, logout_user, login_user, current_user


blueprint = Blueprint('authentification', __name__)


@blueprint.get('/login')
def get_login():
    return render_template('authentification/login.html')


@blueprint.post('/login')
def post_login():
    try:
        user = User.query.filter_by(e_mail=request.form.get('e_mail')).first()

        if not user:
            raise Exception('No user with the given email address was found.')
        elif not check_password_hash(user.password, request.form.get('password')):
            raise Exception('The password does not appear to be correct.')
        login_user(user)
        return redirect(url_for('authentification.dashboard'))

    except Exception as error_message:
        error = error_message or 'An error occurred while logging in. Please verify your email and password.'
        return render_template('authentification/login.html', error=error)


@blueprint.get('/register')
def get_register():
    return render_template('authentification/register.html')


@blueprint.post('/register')
def post_register():
    try:
        if request.form.get('password') != request.form.get('password_confirmation'):
            raise Exception(
                'The password confirmation must match the password.')
        elif User.query.filter_by(e_mail=request.form.get('e_mail')).first():
            raise Exception('The email address is already registered.')

        user = User(
            e_mail=request.form.get('e_mail'),
            password=generate_password_hash(request.form.get('password'))
        )
        user.save()
        login_user(user)
        return redirect(url_for('authentification.dashboard'))
    except Exception as error_message:
        error = error_message or 'An error occurred while creating a user. Please make sure to enter valid data.'
        return render_template('authentification/register.html', error=error)


@blueprint.get('/logout')
def logout():
    logout_user()
    return redirect(url_for('simple_pages.index'))


@blueprint.get('/todo')
@login_required
def dashboard():
    todos = Task.query.filter(Task.user_id == current_user.id).all()
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
        user_id=current_user.id
    )
    todo.save()
    # db.session.add(todo)
    # db.session.commit()
    return redirect(url_for('authentification.dashboard'))
