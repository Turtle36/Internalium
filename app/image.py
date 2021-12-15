from app.main import app
from flask import url_for, redirect


@app.route("/image/icon.png")
def icon_png():
    return redirect(url_for("static", filename='img/png/icon.png'))


@app.route("/image/rocket.png")
def rocket_png():
    return redirect(url_for("static", filename='img/png/rocket.png'))


@app.route("/image/picture.png")
def picture_png():
    return redirect(url_for("static", filename='img/png/picture.png'))


@app.route("/image/paint.png")
def paint_png():
    return redirect(url_for("static", filename='img/png/paint.png'))


@app.route("/image/icon.ico")
def icon_ico():
    return redirect(url_for("static", filename='img/ico/icon.ico'))
