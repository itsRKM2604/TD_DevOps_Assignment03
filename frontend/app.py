from flask import Flask, render_template, request, redirect, url_for
import requests
from werkzeug.security import generate_password_hash

BACKEND_URL = "http://localhost:9090"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def handleFormSubmit():
    name = request.form.get('fname')
    email = request.form.get('email')
    password = request.form.get('password')

    hashed_password = generate_password_hash(password)

    form_data = {
        "name": name,
        "email": email,
        "password": hashed_password
    }

    try:
        response = requests.post(
            BACKEND_URL + "/submit",
            json=form_data,
            timeout=1
        )

        data = response.json()

        if response.status_code == 200 and data.get("success"):
            return render_template("success.html", success="Data inserted Successfully")
        else:
            return render_template(
                "index.html",
                error=data.get("error", "Something went wrong.")
            )

    except requests.exceptions.ConnectionError:
        return render_template(
            "index.html",
            error="No connection could be made because the target machine actively refused it"
        )

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=9001)