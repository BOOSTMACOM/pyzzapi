import src.repository.recipe as recipe_repository

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
        recipe_repository.create_new_recipe(recipe)
