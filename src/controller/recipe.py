import src.repository.recipe as recipe_repository
import json 

def index():
    # Récuperer toutes les recette en BDD
    recipes = recipe_repository.get_all_recipes()
    # Afficher les recettes à l'utilisateur
    print(json.dumps(recipes))

def show():
    pass

def new():
    pass

def edit():
    pass

def delete():
    pass