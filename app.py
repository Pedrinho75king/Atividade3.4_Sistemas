from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, Flask !!</h1>", 200

@app.route("/versao")
def versao():
    versao = "1.1.0"
    return f"App v{versao}", 200

