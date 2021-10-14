from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def alive():
  return "alive !!"

@app.route("/test")
def test():
  myDict = {
    "name": "ego"
  }
  return myDict

@app.route("/hello/<name>")
def hello(name):
  
  return render_template("hello.html", name = name)

