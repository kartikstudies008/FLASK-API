from flask import Flask, session
from datetime import datetime
import uuid

app = Flask(__name__)

# Secret key required for sessions
app.secret_key = "kartik_secret_key"

@app.route("/")
def session_info():

    # If session does not exist → create new
    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())
        session["creation_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Update last accessed time
    session["last_accessed"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"""
    <h2>Session Information (Flask)</h2>
    <p><b>Session ID:</b> {session['session_id']}</p>
    <p><b>Creation Time:</b> {session['creation_time']}</p>
    <p><b>Last Accessed Time:</b> {session['last_accessed']}</p>
    <p>Refresh the page to see Last Accessed Time change.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)