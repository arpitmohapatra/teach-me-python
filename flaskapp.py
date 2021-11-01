from flask import Flask, jsonify, request, session, redirect, url_for
from pymongo import MongoClient

app = Flask("FlaskApp")
app.secret_key = b'@$#$FVFVFDrgrg23'

db_client = MongoClient()
db = db_client['testdb']
col = db['users']

col.insert_many([{'username': 'test1', 'password': 'password1'},
                 {'username': 'test2', 'password': 'password2'},
                 {'username': 'test3', 'password': 'password3'}])


@app.route('/', methods=['GET'])
def home():
    if session.get('loggedin'):
        return "Logged in"
    else:
        return "Not logged in"


@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.get_json()['username']
    password = request.get_json()['password']

    dbvalues = col.find_one({"username": username})

    if dbvalues and dbvalues['password'] == password:
        session['loggedin'] = True
    else:
        session['loggedin'] = False
    return redirect(url_for('home'))


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['loggedin'] = False
    return redirect(url_for('home'))


@app.route('/users')
def users_list():
    dbvalues = col.find({}, {{'_id': False}})
    return jsonify(list(dbvalues))


@app.errorhandler(404)
def error_page(e):
    return jsonify({"message": "This page is not available"})


app.run(debug=True)
