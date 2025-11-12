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

@app.route("/pagina")
def pagina():
    return render_template("pagina.html"), 200

@app.route("/buscar/<item>")
def buscar(item):
    itens = ["banana", "maçã", "uva", "laranja"]
    encontrado = False

    for i in itens:
        if i == item:
            encontrado = True
            break

    if encontrado:
        return f"Item '{item}' encontrado na lista!", 200
    else:
        return f"Item '{item}' não encontrado.", 200

if __name__ == "__main__":
    app.run(debug=True)