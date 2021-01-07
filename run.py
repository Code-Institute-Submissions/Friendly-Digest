import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/meat", methods=["GET"])
def meat():
    recipes = mongo.db.recipes.find()
    return render_template(
        "meat.html", recipes=recipes, page_title="Meat Recipes")


@app.route("/fish", methods=["GET"])
def fish():
    recipes = mongo.db.recipes.find()
    return render_template(
        "fish.html", recipes=recipes, page_title="Fish Recipes")


@app.route("/veg", methods=["GET"])
def veg():
    recipes = mongo.db.recipes.find()
    return render_template(
        "veg.html", recipes=recipes, page_title="Veg Recipes")


@app.route("/dessert", methods=["GET"])
def dessert():
    recipes = mongo.db.recipes.find()
    return render_template(
        "dessert.html", recipes=recipes, page_title="Dessert Recipes")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username exists in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get(
                    "password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                    "myRecipes", username=session["user"]))

            else:
                # Invalid password match
                flash("Incorrect Username and/or Password. Please try again.")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password. Please try again.")
            return redirect(url_for("login"))

    return render_template("login.html", page_title="Log In")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if username already exists in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # Redirect back if username exists
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # Store username and password into DB as items in disctionary
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        # Calls and inserts 'users' collection in Mongo DB
        mongo.db.users.insert_one(register)

        # Put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("myRecipes", username=session["user"]))

    return render_template("register.html", page_title="Register")


@app.route("/myRecipes/<username>", methods=["GET", "POST"])
def myRecipes(username):
    # Grab the session user's username from DB
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template(
            "myRecipes.html", username=username, page_title="My Recipes")

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/addRecipe", methods=["GET", "POST"])
def addRecipe():
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_prep_mins": request.form.get("recipe_prep_mins"),
            "recipe_cook_mins": request.form.get("recipe_cook_mins"),
            "recipe_calories": request.form.get("recipe_calories"),
            "recipe_servings": request.form.get("recipe_servings"),
            "recipe_level": request.form.get("recipe_level"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_instructions": request.form.get("recipe_instructions"),
            "recipe_image": request.form.get("recipe_image"),
            "author_name": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added!")
        return redirect(url_for("index"))

    # Get data from categories collection on Mongo DB
    categories = mongo.db.categories.find().sort("category_name")
    return render_template(
        "addRecipe.html", categories=categories, page_title="Add Recipe")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
