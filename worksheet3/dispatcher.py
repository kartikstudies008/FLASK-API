# Import Flask utilities: render_template for HTML, request for form data,
# redirect to forward the browser to another URL, url_for to build URLs by function name
from flask import Flask, render_template, request, redirect, url_for

# Create the Flask application instance
app = Flask(__name__)

# Step 1: HOME ROUTE – serves the main index page
@app.route("/")
def home():
    return render_template("index.html")


# Step 2: SERVLET1 EQUIVALENT – shows a name entry form (GET) and processes it (POST)
@app.route("/servlet1", methods=["GET", "POST"])
def servlet1():

    # GET request: display an HTML form for the user to enter their name
    if request.method == "GET":
        return '''
        <h2>Enter Your Name</h2>
        <form method="post">
        Name: <input type="text" name="username">
        <input type="submit" value="Submit">
        </form>
        '''

    # POST request: read the submitted name and forward (dispatch) to servlet2
    if request.method == "POST":
        name = request.form.get("username")

        # Redirect to servlet2, passing the username as a query parameter
        return redirect(url_for("servlet2", uname=name))


# Step 3: SERVLET2 EQUIVALENT – receives the forwarded name and displays a welcome message
@app.route("/servlet2")
def servlet2():

    # Read the username query parameter passed from servlet1
    name = request.args.get("uname")

    return f"""
    <h2>Welcome {name}</h2>
    <h3>This is Servlet2</h3>
    """


# Only start the server when this file is run directly (not when imported)
if __name__ == "__main__":
    app.run(debug=True)
    