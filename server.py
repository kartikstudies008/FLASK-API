# Import Flask framework and helper utilities
from flask import Flask
from flask import jsonify
import requests
from flask import render_template
import sqlite3

# Create the Flask application instance
app = Flask(__name__)

# Initialize the SQLite database and create the student table if it doesn't exist
def init_db():
    # Connect to (or create) the student.db database file
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    # Create the student table only if it has not been created yet
    cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   city TEXT
                   )
""")
    # Save changes and close the connection
    conn.commit()
    conn.close()

# Run database initialization when the server starts
init_db()

#HOME PAGE
@app.route("/")
def home():
    # Return a simple string response for the root URL
    return "THIS IS A HOME PAGE"

#ABOUT PAGE 
@app.route("/about")
def about():
    # Return information about the application
    return "THIS IS ABOUT PAGE"

#CONTACT PAGE
@app.route("/contact")
def contact():
    # Return contact information
    return "CONTACT US AT email.test@gmail.com"

#STUDENT INFO
@app.route("/student")
def student():
    # Connect to the database
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    # Fetch all student records
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()

    # Build an HTML string from all rows
    result = "" 
    for row in rows:
        result += f"ID: {row[0]}, Name: {row[1]}, City: {row[2]}<br>"

        conn.close()
        return result

#DYNAMIC ROUTE – computes the square of the number passed in the URL
@app.route("/square/<number>")
def square(number):
    # Convert the URL parameter to int and multiply it by itself
    result = int(number) * int(number)
    return f"Square is {result}"

#SERVER THAT RECEIVES DATA – accepts a POST request with JSON body and saves to DB


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

    # 3️⃣ Validate that both required fields are present
    if not name or not city:
        return jsonify({"error": "Missing name or city"}), 400

    # 4️⃣ Insert the new student record into the database
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO student (name, city) VALUES (?, ?)",
        (name, city)
    )

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

    # 5️⃣ Return a success response with HTTP 201 Created
    return jsonify({
        "success": True,
        "message": f"STUDENT {name} SAVED SUCCESSFULLY"
    }), 201


# JOKE ROUTE – fetches a random joke from an external public API
@app.route("/joke")
def joke():

    # Call external joke API
    response = requests.get("https://official-joke-api.appspot.com/random_joke")

    # Parse the response body as JSON
    data = response.json()

    # Return only the setup and punchline fields to the client
    return jsonify({
        "setup": data["setup"],
        "punchline": data["punchline"]
    })

# JOKE UI ROUTE – renders the HTML page that calls the /joke endpoint via JavaScript
@app.route("/joke-ui")
def joke_ui():
    return render_template("joke.html")

# Start the development server with debug mode enabled
app.run(debug=True)