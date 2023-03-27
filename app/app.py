from flask import Flask, redirect, url_for, render_template, send_file
from random import randint
from . import simple_pages

def create_app():
  app = Flask(__name__)
  app.config.from_object('app.config')
  register_blueprints(app)

  return app


def register_blueprints(app: Flask):
  app.register_blueprint(simple_pages.routes.blueprint)





