# import builtin functions and classes from flask module
from flask import Flask, redirect, url_for, render_template, request

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
    # get form method (get,post)
    # return request.method
    
    # GET FORM
    # get all arguments
    # return request.args

    # get any argument
    # return request.args.get('fname')


    # POST form
    #get post form values
    # return request.form 

    # get any post form value
    # return request.form['fname']


    if request.method == 'POST':
        # return 'if POST'
        # return   request.form
        data = request.form
        return render_template('form-data.html',form_data = data)
    else:
        # return 'else GET'
        # return request.args
        data1 = request.args
        return render_template('form-data.html',form_data = data1)

    # return 'Form is submitted'


@app.route('/jinja')
def jinja():

    data = [
            {
                'name':'ali',
                'age': 20,
                'education': 'inter',
                'phone' : '030120217'
            },
            {
                'name':'ahmad',
                'age': 22,
                'education': 'matric',
                'phone' : '030120214657'
            },
            {
                'name':'adeel',
                'age': 19,
                'education': 'inter',
                'phone' : '03012240217'
            },
            {
                'name':'umer',
                'age': 25,
                'education': 'Phd',
                'phone' : '03012021700014'
            },
        ]
    
    # return data
    len(data) 
    # return f' {len(data)} ' 
    return render_template('jinja.html',data=data)

# app.run(host,port,debug,options)

# activate the debugging
# app.run(debug=True)

# change the port
# app.run(port=8000)
app.run(port=8000,debug=True)
