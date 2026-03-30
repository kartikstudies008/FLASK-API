from flask import Flask, session, redirect, url_for
from datetime import datetime, timedelta

app = Flask(__name__)

# secret key required for sessions
app.secret_key = "kartik_secret"

# session timeout = 30 seconds
app.permanent_session_lifetime = timedelta(seconds=30)    # set session lifetime to 30 seconds


@app.route("/")
def start_session():

    session.permanent = True
    session["start_time"] = datetime.now().strftime("%H:%M:%S")

    return f"""
    <h2>Session Started</h2>
    Start Time: {session['start_time']}<br>
    Refresh within 30 seconds or session will expire.
    <br><br>
    <a href='/check'>Check Session</a>
    """


@app.route("/check")
def check_session():

    if "start_time" in session:
        return f"""
        <h2>Session Active</h2>
        Start Time: {session['start_time']}
        """

    else:
        return "<h2>Session Expired</h2>"


if __name__ == "__main__":
    app.run(debug=True)