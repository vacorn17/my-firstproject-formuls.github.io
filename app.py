from flask import Flask
from flask import render_template
#from flask_sqlalchemy import SQLAlchemy
#import sqlalchemy as sa
#import sqlalchemy.orm as so
import random

app = Flask(__name__)

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/subjects')
def subjects():
  return render_template('subjects.html')

@app.route('/math')
def math():
  return render_template('math.html')
@app.route('/algebra')
def algebra():
  return render_template('algebra.html')
@app.route('/geometry')
def geometry():
  return render_template('geometry.html')
@app.route('/probability and statistics')
def probability():
  return render_template('probability and statistics.html')

@app.route('/physics')
def physics():
  return render_template('physics.html')

@app.route('/abc')
def abc():
  return render_template('abc.html')


app.run(debug=True)