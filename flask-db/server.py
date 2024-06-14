from flask import Flask, render_template, request, redirect , url_for
from mysql.connector import connect

connection = connect(
    host= 'localhost',
    user= 'root',   
    password = '',
    database = 'flask_db'
    )





app = Flask(__name__)

app.secret_key = 'fsfdksjfhjsflshfjkshkfskjf'



@app.route('/')
def index():
    db =  connection.cursor()
    db.execute('SELECT * FROM users ORDER BY id DESC')
    users = db.fetchall()
    db.close()
    
    return render_template('users.html', users = users)


@app.route('/create', methods=['GET','POST'])
def create():

    if request.method == 'GET':
        return render_template('create-form.html')
    
    else:
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        phone = request.form['phone']
        city = request.form['city']
        country = request.form['country']
        education = request.form['education']

        db = connection.cursor()
        db.execute('INSERT INTO users (first_name, last_name, email, phone, city, country, education) VALUES (%s,%s,%s,%s,%s,%s,%s)',(first_name, last_name, email, phone, city, country, education) )

        connection.commit()
        db.close()

        return redirect( url_for('index') )
        # return request.form

@app.route('/edit/<id>', methods = ['GET', 'POST'])
def edit(id):

    if request.method == 'GET':

        db= connection.cursor()
        db.execute( f'SELECT * FROM users WHERE id ={id}' )
        user = db.fetchone()
        return render_template('edit-form.html', user=user)
    
    else:
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        phone = request.form['phone']
        city = request.form['city']
        country = request.form['country']
        education = request.form['education']

        db = connection.cursor()

        db.execute('UPDATE users SET first_name = %s, last_name = %s , email = %s , phone = %s , city = %s , country = %s, education = %s WHERE id = %s',(first_name, last_name,email,phone,city,country,education, id))

        result = connection.commit()
        # return result
        db.close()

        return redirect( url_for('index') )

    return f'edit {id}'

@app.route('/delete/<id>')
def delete(id):
    db= connection.cursor()
    db.execute(f'DELETE FROM users WHERE id = {id}')
    connection.commit()
    db.close()
    return redirect( url_for('index') )


    # return f'id {id}'





app.run(debug=True)