import src.repository.ingredient as ingredient_repository
import json 

def index():
    # Récuperer toutes les recette en BDD
    ingredients = ingredient_repository.get_all()
    # Afficher les recettes à l'utilisateur
    print(ingredients)
    #print(json.dumps(ingredients))

def show(id: int):
    print(ingredient_repository.get(id))

def new():
    pass

def edit():
    pass

def delete():
    pass