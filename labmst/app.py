# Import Flask session to store data per user, redirect to forward requests,
# url_for to build URLs by function name, and datetime/timedelta for time calculations
from flask import Flask, session, redirect, url_for
from datetime import datetime, timedelta

# Create the Flask application instance
app = Flask(__name__)

# Secret key required to sign the session cookie securely
app.secret_key = "kartik_secret"

# Session timeout – session data will expire after 30 seconds of inactivity
app.permanent_session_lifetime = timedelta(seconds=30)


# START SESSION ROUTE – creates a new session and records the start time
@app.route("/")
def start_session():

    # Mark the session as permanent so the timeout setting above applies
    session.permanent = True
    # Record the time when the session was started
    session["start_time"] = datetime.now().strftime("%H:%M:%S")

    # Display the start time and a link to check the session status
    return f"""
    <h2>Session Started</h2>
    Start Time: {session['start_time']}<br>
    Refresh within 30 seconds or session will expire.
    <br><br>
    <a href='/check'>Check Session</a>
    """


# CHECK SESSION ROUTE – verifies whether the session is still active or has expired
@app.route("/check")
def check_session():

    # If the session data is still present, show the start time
    if "start_time" in session:
        return f"""
        <h2>Session Active</h2>
        Start Time: {session['start_time']}
        """

    # If the session has expired or was never started, show an expiry message
    else:
        return "<h2>Session Expired</h2>"


# Only start the server when this file is run directly (not when imported)
if __name__ == "__main__":
    app.run(debug=True)