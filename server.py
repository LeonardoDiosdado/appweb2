from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template(
        "index.html",
        titulo="Inicio",
        mensaje="¡Bienvenido a la Biblioteca de la Universidad de León!",
    )


@app.route("/catalogo")
def catalogo():
    return render_template(
        "catalogo.html",
        titulo="Catálogo",
        mensaje="Explora los materiales académicos disponibles para apoyar tus estudios e investigaciones UDL.",
    )


@app.route("/servicios")
def servicios():
    return render_template(
        "servicios.html",
        titulo="Servicios",
        mensaje="Conoce los servicios que ponemos a tu disposición para facilitar tu aprendizaje UDL.",
    )


@app.route("/contacto")
def contacto():
    return render_template(
        "contacto.html",
        titulo="Contacto",
        mensaje="Comunícate con nuestro equipo para resolver tus dudas o solicitar información UDL.",
    )


if __name__ == "__main__":
    app.run(debug=True)