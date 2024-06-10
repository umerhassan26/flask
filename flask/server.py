# import builtin functions and classes from flask module
from flask import Flask, redirect, url_for, render_template

# iniliaze flask app
app = Flask(__name__)

# routes
# @app.route('/about')
@app.route('/')
def index():
    return 'Hello world!.'

@app.route('/home')
def home():
    return "Home page."

@app.route('/about')
def about():
    return "About page."

# redirect
@app.route('/google')
def google():

    # return redirect('https://www.google.com')
    # return redirect('http://127.0.0.1:8000/home')

    # get url of any local fuction
    # return redirect(url_for('about'))
    return url_for('display',id=12.12)

# @app.route('/display/<name>')
# def display(name):
#     return f"Name is : {name} "

# @app.route('/display/<int:id>')
# def display(id):
#     return f"Id is : {id} "

# pass variable as parameter in route
@app.route('/display/<float:id>')
def display(id):
    return f"Id is : {id} "

# get form
# by default all routes are of get type
@app.route('/form')
def form():
    return render_template('form.html')


# use methods parameter to use any specific method ( GET or POST)
# @app.route('/submit', methods=['POST'])
# def submit():
#     return 'Form is submitted'

# we can allow multiple methods as paramerter
@app.route('/submit', methods=['POST','GET'])
def submit():
    return 'Form is submitted'


# app.run(host,port,debug,options)

# activate the debugging
# app.run(debug=True)

# change the port
# app.run(port=8000)
app.run(port=8000,debug=True)
