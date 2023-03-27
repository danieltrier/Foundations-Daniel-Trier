from flask import Flask, redirect, url_for, render_template, send_file
from random import randint
from . import simple_pages
app = Flask(__name__)
app.config.from_object('app.config')



app.register_blueprint(simple_pages.routes.blueprint)





