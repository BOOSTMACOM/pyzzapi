import src.controller.recipe as recipe_controller
import src.fixtures.app as fixtures
import sys

args = sys.argv
call = args[1] if len(args) > 1 else None

commands = {
    "load:fixtures": fixtures.load_recipes
}

if call and call in commands:
    commands.get(call)()
    exit()

routes = {
    "/api/recipes/": recipe_controller.index,
    "/api/ingredients/": None
}

if call and call in routes:
    routes.get(call)()
    exit()

print("Not found - 404")
