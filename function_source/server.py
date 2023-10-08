from flask import render_template, Flask

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html",text = "test!!")