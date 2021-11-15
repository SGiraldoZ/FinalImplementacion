from flask import Flask, request, redirect, render_template, session, redirect, url_for

import figuras.controllers.figurasController
from figuras.controllers.figurasController import figuras_controller
from mathModule.controllers.mathController import math_controller


app = Flask(__name__)
app.register_blueprint(figuras_controller, url_prefix='/figures')
app.register_blueprint(math_controller, url_prefix='/math')

@app.route('/', methods = ['GET'])
def index():
    return render_template("index.html")

@app.route('/indexMenu', methods = ['POST','GET'])
def menuRedirect():
    if request.args.get("option") == "triangle":
        return redirect("figures/triangleStart")
    if request.args.get("option") == "circle":
        return redirect("figures/circleStart")
    if request.args.get("option") == "factorial":
        return redirect("math/factorialStart")
    if request.args.get("option") == "rectangle":
        return redirect("figures/rectangleStart")
    if request.args.get("option") == "fibonacci":
        return redirect("math/fibonacciStart")
if __name__ == "__main__":
    app.secret_key = "clave muy secreta"
    app.run(debug=True)