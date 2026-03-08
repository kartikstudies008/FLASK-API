from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/employee", methods=["POST"])
def employee():

    name = request.form["name"]
    email = request.form["email"]
    city = request.form["city"]
    state = request.form["state"]

    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="16.13@Ka",
        database="employee_db"
    )

    cursor = con.cursor()

    # Insert employee
    cursor.execute(
        "INSERT INTO employee(name,email) VALUES(%s,%s)",
        (name,email)
    )

    emp_id = cursor.lastrowid

    # Insert address
    cursor.execute(
        "INSERT INTO address(city,state,emp_id) VALUES(%s,%s,%s)",
        (city,state,emp_id)
    )

    con.commit()
    con.close()

    return "Employee Saved Successfully!"


if __name__ == "__main__":
    app.run(debug=True)