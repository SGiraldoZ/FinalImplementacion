from flask import Blueprint, render_template, request
from ..modelo.Number import invalidN
from ..services.mathService import fibonacciService, factorialService


math_controller = Blueprint('math',__name__,template_folder='templates')

@math_controller.route("/fibonacciStart")
def startFibonacci():
    return render_template("number.html", fibonacci = True)

@math_controller.route("/fibonacciSet", methods=['POST','GET'])
def solveFibonacci():
    try:
        results = fibonacciService(request.form["n"])
        return render_template("fibonacci.html", results=results)

    except invalidN as e:
        return render_template("number.html", fibonacci=True, error=True, errorMsg=str(e))
    except Exception as e:
        print(e)
        return render_template("number.html", fibonacci=True, error=True, errorMsg="Algo ha salido mal :/")

@math_controller.route("/factorialStart")
def startFactorial():
    return render_template("number.html", fibonacci = False)

@math_controller.route("/factorialSet", methods=['POST','GET'])
def solveFactorial():
    try:
        factorial = factorialService(request.form["n"])
        return render_template("factorial.html",n=request.form["n"], result = factorial)
    except invalidN as e:
        return render_template("number.html", fibonacci=False, error=True, errorMsg=str(e))
    except Exception as e:
        print(n)
        return render_template("number.html", fibonacci=False, error=True, errorMsg="Algo ha salido mal :/")


