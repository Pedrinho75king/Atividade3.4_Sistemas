from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, Flask !!</h1>", 200

@app.route("/versao")
def versao():
    versao = "1.1.0"
    return f"App v{versao}", 200

@app.route("/saudar/<nome>")
def saudar(nome):
    nome_formatado = nome.capitalize()
    return f"Olá, {nome_formatado}!", 200

@app.route("/quadrado/<int:n>")
def quadrado(n):
    resultado = n ** 2
    return f"{n}² = {resultado}", 200

@app.route("/home")
def home():
    return redirect("/", code=302)

