from app.extensions.database import db, migrate
from flask import Flask, redirect, url_for, render_template, send_file
from random import randint
from . import simple_pages, authentification
from app.extensions.database import db
from app.extensions.authentication import login_manager


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    register_extensions(app)
    register_blueprints(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(simple_pages.routes.blueprint)
    app.register_blueprint(authentification.routes.blueprint)


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    login_manager.init_app(app)
