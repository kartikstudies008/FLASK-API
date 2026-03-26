# Import Flask session to persist data across requests, and datetime/uuid for unique IDs
from flask import Flask, session
from datetime import datetime
import uuid

# Create the Flask application instance
app = Flask(__name__)

# Secret key required for sessions – used to cryptographically sign the session cookie
app.secret_key = "kartik_secret_key"

# ROOT ROUTE – displays session details and creates a new session if one doesn't exist
@app.route("/")
def session_info():

    # If no session exists yet, generate a unique session ID and record the creation time
    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())
        session["creation_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Update last accessed time on every page visit
    session["last_accessed"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Render session details as an HTML response
    return f"""
    <h2>Session Information (Flask)</h2>
    <p><b>Session ID:</b> {session['session_id']}</p>
    <p><b>Creation Time:</b> {session['creation_time']}</p>
    <p><b>Last Accessed Time:</b> {session['last_accessed']}</p>
    <p>Refresh the page to see Last Accessed Time change.</p>
    """

# Only start the server when this file is run directly (not when imported)
if __name__ == "__main__":
    app.run(debug=True)