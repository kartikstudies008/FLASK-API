from flask import Flask
from flask import jsonify
import requests
from flask import render_template
import sqlite3

app = Flask(__name__)
def init_db():
    conn = sqlite3.connect("student.db")    #CONNECT TO DATABASE 1
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


@app.route("/register", methods=["POST"])
def register():

    # 1️⃣ Get JSON safely
    data = request.get_json()

    # If client didn't send JSON
    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    # 2️⃣ Get fields safely (no crash)
    name = data.get("name")
    city = data.get("city")

    # 3️⃣ VALIDATION  ← ADD IT HERE
    if not name or not city:
        return jsonify({"error": "Missing name or city"}), 400

    # 4️⃣ Database
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO student (name, city) VALUES (?, ?)",
        (name, city)
    )

    conn.commit()
    conn.close()

    # 5️⃣ Response
    return jsonify({
        "success": True,
        "message": f"STUDENT {name} SAVED SUCCESSFULLY"
    }), 201


@app.route("/joke")
def joke():

    # Call external API
    response = requests.get("https://official-joke-api.appspot.com/random_joke")

    # Convert to JSON
    data = response.json()

    # Send to browser
    return jsonify({
        "setup": data["setup"],
        "punchline": data["punchline"]
    })
@app.route("/joke-ui")
def joke_ui():
    return render_template("joke.html")

app.run(debug=True)
