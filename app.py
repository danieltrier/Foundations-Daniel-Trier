from flask import Flask, redirect, url_for, render_template
from random import randint
app = Flask(__name__)
app.config.from_object('config')
cookies_data = {
  'chocolate-chip' : {'name': 'Chocolate Chip', 'price': '$1.50'},
  'oatmeal-raisin' : {'name': 'Oatmeal Raisin', 'price': '$1.00'},
  'sugar' : {'name': 'Sugar', 'price': '$0.75'},
  'peanut-butter' : {'name': 'Peanut Butter', 'price': '$0.50'},
  'oatmeal' : {'name': 'Oatmeal', 'price': '$0.25'},
  'salted-caramel' : {'name': 'Salted Caramel', 'price': '$1.00'},
}
@app.route('/')
def index():
    name = 'Daniel'
    number = 32

    return render_template('index.html', u_name = name, age = number)

@app.route('/about')
def about():
   return 'I like cookies'
@app.route('/cookies')
def keks():
   return render_template('/cookies.html', cookies = cookies_data)
@app.route('/about-me')
def about_me():
   return redirect(url_for('about'))
 
@app.route('/random')
def rand():
   number_random = randint(1,22)
   return '<p>A random number between 1 and 100 is <b>' + str(number_random) + '</b></p>'
@app.route('/cookies/<slug>')
def cookie(slug):
   return '<h1>' + cookies_data[slug]['name'] + '</h1><p>' + cookies_data[slug]['price'] + '</p>'

if __name__ == '__main__':
  app.run()