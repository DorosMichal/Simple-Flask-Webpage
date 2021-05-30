from page import app, db
from itertools import groupby
from flask import render_template, request, jsonify

@app.route('/')
@app.route('/home')
def home():
    cur = db.connection.cursor()
    cur.execute('''
    SELECT state, city, COUNT(ID) AS NB
    FROM addresses
    GROUP BY state, city
    HAVING NB >= 2
    ORDER BY state, NB DESC
    ''')
    resp = cur.fetchall()
    resp = {state : [el[1:] for el in data] for state, data in groupby(resp, lambda x : x[0])}
    return render_template('home.html', data=resp)

@app.route('/details', methods = ['POST'])
def details():
    state = request.form["state"]
    city = request.form["city"]
    cur = db.connection.cursor()
    cur.execute('''
    SELECT first_name, last_name, email
    FROM 
    (SELECT first_name, last_name, email, state, city
    FROM addresses
    WHERE state=%s AND city=%s) AS T
    ORDER BY first_name
    ''', args=(state, city))
    resp = cur.fetchall()
    return jsonify(resp)
