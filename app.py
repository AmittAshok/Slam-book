from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL configurations
db = mysql.connector.connect(
    host="mysql",
    user="amittashok",
    password="aWelcome@123",
    database="user_info"
)

cursor = db.cursor()

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

    query = "INSERT INTO users (name, dob, blood_group, location, hobbies) VALUES (%s, %s, %s, %s, %s)"
    values = (name, dob, blood_group, location, hobbies)
    cursor.execute(query, values)
    db.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
    
