# ui_main.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

def start_ui():
    """Run the Flask server for UI."""
    app.run(host='0.0.0.0', port=8080, debug=True)

if __name__ == "__main__":
    start_ui()
