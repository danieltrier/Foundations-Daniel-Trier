from .models import User
from flask import Blueprint, render_template

blueprint = Blueprint('simple_pages', __name__)

@blueprint.route('/')
def index():
    return render_template('simple_pages/index.html')

@blueprint.route('/login')
def login():
    return render_template('simple_pages/login.html')

@blueprint.route('/register')
def register():
    return render_template('simple_pages/register.html')