from flask import Flask , render_template

# package for sql connection
from mysql.connector import connect


# make connection using credentials
connection = connect(host='localhost', user='root' , password = '' , database= 'test_db')


app = Flask(__name__)

@app.route('/')
def users():

    # open connection with db 
    db = connection.cursor()

    # execute any command
    db.execute('SELECT * FROM users')

    users = db.fetchall()

    db.close()

    return render_template('users.html', users = users)

app.run(debug=True)