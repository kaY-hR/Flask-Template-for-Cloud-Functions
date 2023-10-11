from flask import render_template, Flask
from .tools import entrypoint

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index(requests = None):
    return render_template("index.html",text = "test")

@app.route("/page1", methods=["GET", "POST"])
def page1(requests = None):
    return render_template("page1.html")

app_wrap = lambda request: entrypoint(app, request)