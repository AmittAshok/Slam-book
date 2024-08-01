from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# MySQL configurations
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="mysql",
            user="amittashok",
            password="aWelcome@123",
            database="user_info"
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    dob = request.form['dob']
    blood_group = request.form['blood-group']
    location = request.form['location']
    hobbies = request.form['hobbies']

    connection = get_db_connection()
    if connection is None:
        return "Database connection failed", 500

    try:
        cursor = connection.cursor()
        query = "INSERT INTO users (name, dob, blood_group, location, hobbies) VALUES (%s, %s, %s, %s, %s)"
        values = (name, dob, blood_group, location, hobbies)
        cursor.execute(query, values)
        connection.commit()
    except Error as e:
        print(f"Error executing query: {e}")
        return "Error occurred while submitting data", 500
    finally:
        cursor.close()
        connection.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

    
