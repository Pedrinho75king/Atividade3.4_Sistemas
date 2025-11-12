from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, Flask !!</h1>", 200
