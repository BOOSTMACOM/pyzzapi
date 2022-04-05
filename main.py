import src.controller.recipe as recipe_controller
import src.controller.ingredient as ingredient_controller
import src.fixtures.app as fixtures
import sys
import re

args = sys.argv
call = args[1] if len(args) > 1 else None

commands = {
    "load:fixture:recipes": fixtures.load_recipes,
    "load:fixture:ingredients": fixtures.load_ingredients
}

if call and call in commands:
    commands.get(call)()
    exit()

routes = {
    "/api/recipes/": recipe_controller.index,
    "/api/recipes/{id}": recipe_controller.show,
    "/api/ingredients/": ingredient_controller.index,
    "/api/ingredients/{id}": ingredient_controller.show
}

regex = r"([a-z\/]+)([0-9]+)"
param = None
if call:
    matches = re.findall(regex, call, re.MULTILINE)
    if len(matches) > 0:
        route, param = matches[0]
        call = route + "{id}"

if call and call in routes:
    routes.get(call)(param) if param else routes.get(call)()
    exit()

print("Not found - 404")
