import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


# -- Redirects users that aren't logged in to login page -- #
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "user" in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login to see this page.")
            return redirect(url_for("login"))
    return wrap


# ---- Home/Landing Page ---- #

@app.route("/")
def index():
    return render_template("index.html")


# ---- Search Recipes Page ---- #

@ app.route('/searchRecipes', methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    results = mongo.db.recipes.find({"$text": {"$search": query}}).limit(10)
    result_num = mongo.db.recipes.find({"$text": {"$search": query}}).count()
    if result_num > 0:
        return render_template(
            "searchRecipes.html", results=results, query=query,
            page_title="Search Results")
    else:
        return render_template(
            "searchRecipes.html", results=results,
            query=query, page_title="Search Results",
            message="No Search Results Found. Please Try Again.")


# ---- Individual Recipe Page ---- #

@ app.route('/recipe/<recipe_id>', methods=["GET"])
def recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "recipe.html", recipe=recipe)


# ---- Category Recipe Page ---- #

@app.route("/categoryRecipes/<category>", methods=["GET"])
def categoryRecipes(category):
    recipes = mongo.db.recipes.find({"$text": {"$search": category}})
    return render_template(
        "categoryRecipes.html", recipes=recipes, page_title=category)


# ---- Log In Page ---- #

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username exists in DB.
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Ensure hashed password matches user input.
            if check_password_hash(
                existing_user["password"], request.form.get(
                    "password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                    "myRecipes", username=session["user"]))

            else:
                # Invalid password match.
                flash("Incorrect Username and/or Password. Please try again.")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist.
            flash("Incorrect Username and/or Password. Please try again.")
            return redirect(url_for("login"))

    return render_template("login.html", page_title="Log In")


# ---- Register Page ---- #

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if username already exists in DB.
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # Redirect back if username exists.
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # Store username and password into DB as items in dictionary.
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        # Calls and inserts 'users' collection in Mongo DB.
        mongo.db.users.insert_one(register)

        # Put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("myRecipes", username=session["user"]))

    return render_template("register.html", page_title="Register")


# ---- My Recipes Page ---- #

@app.route("/myRecipes/<username>", methods=["GET", "POST"])
@login_required
def myRecipes(username):
    # Grab the session user's username from DB.
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # If user logged in, load myRecipes page.
    if session["user"]:
        recipes = mongo.db.recipes.find({"author_name": username})
        return render_template(
            "myRecipes.html", username=session["user"],
            recipes=recipes, page_title="My Recipes")

    return redirect(url_for("login"))


# ---- Add Recipe Page ---- #

@app.route("/addRecipe", methods=["GET", "POST"])
@login_required
def addRecipe():
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_prep_mins": int(request.form.get("recipe_prep_mins")),
            "recipe_cook_mins": int(request.form.get("recipe_cook_mins")),
            "recipe_calories": int(request.form.get("recipe_calories")),
            "recipe_servings": int(request.form.get("recipe_servings")),
            "recipe_level": request.form.get("recipe_level"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_instructions": request.form.get("recipe_instructions"),
            "recipe_image": request.form.get("recipe_image"),
            "author_name": session["user"]
        }
        # Display flash message when recipe is added.
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added!")
        return redirect(url_for("myRecipes", username=session["user"]))

    # Get data from categories & difficulties collections on Mongo DB.
    categories = mongo.db.categories.find()
    difficulties = mongo.db.difficulties.find()
    return render_template(
        "addRecipe.html", categories=categories,
        difficulties=difficulties, page_title="Add Recipe")


# ---- Edit Recipe Page ---- #

@app.route("/editRecipe/<recipe_id>", methods=["GET", "POST"])
@login_required
def editRecipe(recipe_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_prep_mins": int(request.form.get("recipe_prep_mins")),
            "recipe_cook_mins": int(request.form.get("recipe_cook_mins")),
            "recipe_calories": int(request.form.get("recipe_calories")),
            "recipe_servings": int(request.form.get("recipe_servings")),
            "recipe_level": request.form.get("recipe_level"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_instructions": request.form.get("recipe_instructions"),
            "recipe_image": request.form.get("recipe_image"),
            "author_name": session["user"]
        }
        # Display flash message when recipe is added.
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated!")
        return redirect(url_for("myRecipes", username=session["user"]))

    # Get data from recipes, categories & difficulties collections on Mongo DB.
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find()
    difficulties = mongo.db.difficulties.find()
    return render_template(
        "editRecipe.html", recipe=recipe,
        categories=categories, difficulties=difficulties,
        page_title="Edit Recipe")


# ---- Delete Recipe Function ---- #

@app.route("/deleteRecipe/<recipe_id>")
def deleteRecipe(recipe_id):
    # Premanently deletes recipe from database
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted!")
    return redirect(url_for("myRecipes", username=session["user"]))


# ---- Log Out Function ---- #

@app.route("/logout")
def logout():
    # Remove user from session cookie.
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# ---- Errors ----- #

@ app.errorhandler(404)
def page_not_found(error):
    # Renders error page when error 404 occurs
    return render_template('errors/404.html'), 404


@ app.errorhandler(500)
def internal_error(error):
    # Renders error page when error 500 occurs
    return render_template('errors/500.html'), 500


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=False)
