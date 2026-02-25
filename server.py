from flask import Flask
from flask import request
import sqlite3

app = Flask(__name__)
def init_db():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   city TEXT
                   )
""")
    conn.commit()
    conn.close()
init_db()
#HOME PAGE
@app.route("/")
def home():
    return "THIS IS A HOME PAGE"

#ABOUT PAGE 
@app.route("/about")
def about():
    return "THIS IS ABOUT PAGE"

#CONTACT PAGE
@app.route("/contact")
def contact():
    return "CONTACT US AT email.test@gmail.com"

#STUDENT INFO
@app.route("/student")
def student():

    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()

    result = "" 
    for row in rows:
        result += f"ID: {row[0]}, Name: {row[1]}, City: {row[2]}<br>"

        conn.close()
        return result

#DYNAMIC ROUTE
@app.route("/square/<number>")
def square(number):
    result = int(number) * int(number)
    return f"Square is {result}"

#SERVER THAT RECIEVE DATA 

@app.route("/register",methods=["POST"])
def register():
    data = request.get_json()

    name = data["name"]
    city = data["city"]

    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO student (name,city) VALUES(?,?)",
        (name,city)
    )

    conn.commit()
    conn.close()

    return f"student {name} saved succesfully"

app.run()