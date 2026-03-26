# Import Flask utilities and the MySQL connector library
from flask import Flask, render_template, request
import mysql.connector

# Create the Flask application instance
app = Flask(__name__)

# HOME ROUTE – renders the employee registration form
@app.route("/")
def home():
    return render_template("index.html")


# EMPLOYEE ROUTE – receives form data and saves an employee + address to MySQL
@app.route("/employee", methods=["POST"])
def employee():

    # Read form fields submitted by the user
    name = request.form["name"]
    email = request.form["email"]
    city = request.form["city"]
    state = request.form["state"]

    # Open a connection to the MySQL database
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="16.13@Ka",
        database="employee_db"
    )

    cursor = con.cursor()

    # Insert the employee's name and email into the employee table
    cursor.execute(
        "INSERT INTO employee(name,email) VALUES(%s,%s)",
        (name,email)
    )

    # Retrieve the auto-generated primary key of the newly inserted employee
    emp_id = cursor.lastrowid

    # Insert the employee's city and state into the address table,
    # linking it to the employee via emp_id (foreign key)
    cursor.execute(
        "INSERT INTO address(city,state,emp_id) VALUES(%s,%s,%s)",
        (city,state,emp_id)
    )

    # Commit the transaction to save both inserts atomically
    con.commit()
    # Close the database connection
    con.close()

    return "Employee Saved Successfully!"


# Only start the server when this file is run directly (not when imported)
if __name__ == "__main__":
    app.run(debug=True)