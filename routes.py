from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/birthday')
def birthday():
    return 'September 15 1992'

@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello ' + name

@app.route('/add/<first>/<second>')
def add(first, second):
    return str(int(first) + int(second))

@app.route('/multiply/<num1>/<num2>')
def mutiply(num1, num2):
    return str(int(num1) * int(num2))

@app.route('/subtract/<integer1>/<integer2>')
def subtract(integer1, integer2):
    return str(int(integer1) - int(integer2))

@app.route('/favoriteFoods')
def favoriteFoods():
    myFavFoods = ['eggs', 'spaghetti', 'pancakes']
    return jsonify(myFavFoods)
