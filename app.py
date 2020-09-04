# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__) 

db = SQLAlchemy(app)



app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/login"



class Login(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    date_time = db.Column(db.String(12), nullable=False)

@app.route('/home')
def home():
    return "<h1>Hello ADMIN</h1>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form.get('username')
        password = request.form.get('password')
        entry = Login(email = email, password = password, date_time= datetime.now())
        db.session.add(entry)
        db.session.commit()
        
    return render_template('login.html', error=error)


app.run(debug=True)
