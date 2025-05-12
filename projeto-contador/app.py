from flask import Flask, request, render_template
import unicodedata
import string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def contador():
    resultado_vogais = ""
    resultado_consoantes = ""
    resultado_outros = ""

    if request.method == "POST":
        entrada = request.form["frase"]
        frase = entrada.lower()
        frase = unicodedata.normalize("NFD", frase)
        frase = "".join([letra for letra in frase if unicodedata.category(letra) != "Mn"])

        vogais = sum(1 for c in frase if c in "aeiou")
        consoantes = sum(1 for c in frase if c in string.ascii_lowercase and c not in "aeiou")
        outros = sum(1 for c in frase if c not in string.ascii_lowercase and c not in "0123456789")

        resultado_vogais = f"Vogais: {vogais}"
        resultado_consoantes = f"Consoantes: {consoantes}"
        resultado_outros = f"Outros: {outros}"

    return render_template("index.html", resultado_vogais=resultado_vogais, resultado_consoantes=resultado_consoantes, resultado_outros=resultado_outros)

if __name__ == "__main__":
    app.run(debug=True)
