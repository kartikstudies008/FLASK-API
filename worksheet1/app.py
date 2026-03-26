# Import Flask, request (to read form/query data), and render_template (for HTML pages)
from flask import Flask, request, render_template

# Create the Flask application instance
app = Flask(__name__)

# HOME ROUTE – renders the main HTML page
@app.route("/")
def home():
    return render_template("index.html")


# GET METHOD – reads query parameters from the URL (e.g. /get?fname=John&lname=Doe)
@app.route("/get", methods=["GET"])
def get_method():

    # Extract first and last name from the query string
    fname = request.args.get("fname")
    lname = request.args.get("lname")

    # Return an HTML response showing the received values
    return f"""
    <h2>GET Method Response</h2>
    First Name: {fname}<br>
    Last Name: {lname}
    """


# POST METHOD – reads form data submitted via an HTML form (e.g. from index.html)
@app.route("/post", methods=["POST"])
def post_method():

    # Extract first and last name from the submitted form body
    fname = request.form.get("fname")
    lname = request.form.get("lname")

    # Return an HTML response showing the received values
    return f"""
    <h2>POST Method Response</h2>
    First Name: {fname}<br>
    Last Name: {lname}
    """


# Only start the server when this file is run directly (not when imported)
if __name__ == "__main__":
    app.run(debug=True)
