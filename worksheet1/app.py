hfrom flask import Flask, request, render_templateu

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


# GET METHOD
@app.route("/get", methods=["GET"])
def get_method():

    fname = request.args.get("fname")
    lname = request.args.get("lname")

    return f"""
    <h2>GET Method Response</h2>
    First Name: {fname}<br>
    Last Name: {lname}
    """


# POST METHOD
@app.route("/post", methods=["POST"])
def post_method():

    fname = request.form.get("fname")
    lname = request.form.get("lname")

    return f"""
    <h2>POST Method Response</h2>
    First Name: {fname}<br>
    Last Name: {lname}
    """


if __name__ == "__main__":
    app.run(debug=True)
