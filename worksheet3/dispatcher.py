from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Step 1 : Open index page
@app.route("/")
def home():
    return render_template("index.html")


# Step 2 : Servlet1 equivalent
@app.route("/servlet1", methods=["GET", "POST"])
def servlet1():

    if request.method == "GET":
        return '''
        <h2>Enter Your Name</h2>
        <form method="post">
        Name: <input type="text" name="username">
        <input type="submit" value="Submit">
        </form>
        '''

    if request.method == "POST":
        name = request.form.get("username")

        # forward to servlet2
        return redirect(url_for("servlet2", uname=name))


# Step 3 : Servlet2 equivalent
@app.route("/servlet2")
def servlet2():

    name = request.args.get("uname")

    return f"""
    <h2>Welcome {name}</h2>
    <h3>This is Servlet2</h3>
    """


if __name__ == "__main__":
    app.run(debug=True)
    