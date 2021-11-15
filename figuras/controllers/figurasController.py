from flask import Blueprint, render_template, request
from ..services.figureServices import circleService, triangleService, rectangleService

figuras_controller = Blueprint('figuras',__name__,template_folder='templates')

@figuras_controller.route("/circleStart")
def startCircle():
    return render_template("circle.html")

@figuras_controller.route("/circleSet", methods=['POST','GET'])
def solveCircle():
    try:
        circleDict = circleService(request.form["radius"])
        return render_template("circleInfo.html", cd = circleDict)
    except Exception as e:
        return render_template("circle.html", error=True, errorMsg=str(e))

@figuras_controller.route("/triangleStart", methods=['POST','GET'])
def startTriangle():
    return render_template("triangle.html")

@figuras_controller.route("/triangleSet", methods=['POST','GET'])
def solvetriangle():
    try:
        triangleDict = triangleService(request.form["l1"], request.form["l2"], request.form["l3"])
        return render_template("triangleInfo.html", td = triangleDict)
    except Exception as e:
        return render_template("triangle.html", error=True, errorMsg=str(e))


@figuras_controller.route("/rectangleStart", methods=['POST','GET'])
def startRectangle():
    return render_template("rectangle.html")

@figuras_controller.route("/rectangleSet", methods=['POST','GET'])
def solveRectangle():
    try:
        rectangleDict = rectangleService(request.form["l1"], request.form["l2"])
        return render_template("rectangleInfo.html", rd = rectangleDict)
    except Exception as e:
        return render_template("rectangle.html", error=True, errorMsg=str(e))


