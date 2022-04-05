import src.repository.recipe as recipe_repository
import src.repository.ingredient as ingredient_repository

def load_recipes():
    recipes = [
        {
            'title': 'Pizza 6 fromages'
        },
        {
            'title': 'Pizza bolo'
        },
        {
            'title': 'Pizz à poil'
        },
        {
            'title': 'Pizza kebab'
        },
        {
            'title': 'Pizza Margarita'
        },
        {
            'title': 'Pizza Reine'
        },
    ]

    for recipe in recipes:
        recipe_repository.insert(recipe)

def load_ingredients():
    ingredients = [
        {
            'label': 'Tomate'
        },
        {
            'label': 'Mozarella'
        },
        {
            'label': 'Olive noire'
        },
        {
            'label': 'Crème'
        },
        {
            'label': 'Emmental râpé'
        },
        {
            'label': 'Comté'
        },
        {
            'label': 'Blanc de poulet'
        },
        {
            'label': 'Lardons'
        },
    ]

    for ing in ingredients:
        ingredient_repository.insert(ing)
