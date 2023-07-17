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
    return jsonify(
        {
            "users": [
                {"name": "John Doe", "age": 30, "email": "john.doe@example.com"},
                {"name": "Jane Smith", "age": 25, "email": "jane.smith@example.com"},
                {
                    "name": "Michael Johnson",
                    "age": 35,
                    "email": "michael.johnson@example.com",
                },
            ],
            "products": [
                {"name": "Product 1", "price": 19.99, "quantity": 10},
                {"name": "Product 2", "price": 9.99, "quantity": 5},
                {"name": "Product 3", "price": 14.99, "quantity": 3},
            ],
            "countries": ["USA", "Canada", "UK", "Australia"],
        }
    )


@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))

