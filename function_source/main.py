from flask import render_template, Flask, url_for, redirect
from flask import request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index(requests = None):
    print(request.args.get('test'))
    return render_template("index.html",text = "test")

@app.route("/page1", methods=["GET", "POST"])
def page1(requests = None):
    return render_template("page1.html")

def entrypoint(requests):
    func_name = request.args.get('func')
    if not(func_name):
        return index(requests)
    return page1(requests)
