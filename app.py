from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    ano = request.args.get("ano", "")
    if ano:
        idade = idade_from(ano)
    else:
        idade = ""

    return (
        	"""<h2> Vamos calcular a sua idade? </h2>"""
            """<h3> Insira o ano de seu nascimento </h3>"""
		"""<form action="" method="get">
                <input type="text" name="ano">
                <input type="submit" value="Calcular">
            </form>"""
        + "idade: "
        + '<a id="idade">' +idade+ '</a>'

    )
 
@app.route("/<int:ano>")
def idade_from(ano):
    """Convert ano to idade."""
    idade = 2023 - int(ano)
    return str(idade)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
     #app.run(host="0.0.0.0", port=8080, debug=False)
