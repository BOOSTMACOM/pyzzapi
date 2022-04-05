import imp
from flask import Flask, jsonify
import src.repository.recipe as recipe_repository

app = Flask(__name__)

@app.route("/api/recipes")
def api_recipes_index():
    return jsonify(recipe_repository.get_all())

