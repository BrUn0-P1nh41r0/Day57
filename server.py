import random
import requests
from datetime import datetime
from flask import Flask, render_template

AGIFY_URL = "https://api.agify.io?name="
GENDERIZE_URL = "https://api.genderize.io?name="

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    year = datetime.now().year
    return render_template("index.html", num=random_number, year=year)

@app.route("/guess/<name>")
def age_gender(name):
    agify_response = requests.get(url = f"{AGIFY_URL}{name}")
    genderize_response = requests.get(url = f"{GENDERIZE_URL}{name}")
    agify_data = agify_response.json()
    genderize_data = genderize_response.json()
    return render_template("guess.html",
                           name=name, age=agify_data["age"],
                           gender=genderize_data["gender"])


if __name__ == "__main__":
    app.run(debug=True)