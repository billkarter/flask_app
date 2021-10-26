from flask import Flask

app = Flask(__name__)
@app.route("/<name>")
@app.route("/hello/<name>")
def hello_world(name):
    return "<p>пртвеь {}.!</p>".format(name)





