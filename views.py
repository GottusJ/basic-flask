from flask import Blueprint, render_template, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

name = "Joshua"


@views.route("/")
def home():
    return render_template("index.html", name=name)


@views.route("/profile")
def prfile():
    return render_template("index.html", name=name)


@views.route("/json")
def get_json():
    return jsonify({"name": "Joshua"})


@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))
