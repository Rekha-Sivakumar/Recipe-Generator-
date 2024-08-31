import random

# Predefined set of simple recipes with ingredients and instructions
recipes_db = {
    "Pasta Salad": {
        "ingredients": ["pasta", "tomato", "olive oil", "basil"],
        "instructions": "Boil the pasta. Mix with chopped tomatoes, olive oil, and fresh basil."
    },
    "Banana Smoothie": {
        "ingredients": ["banana", "milk", "honey"],
        "instructions": "Blend banana with milk and honey until smooth."
    },
    "Masala Dosa": {
        "ingredients": ["rice", "urad dal", "potatoes", "spices"],
        "instructions": "Prepare dosa batter, cook the dosa and fill it with spicy mashed potatoes."
    }
}

def generate_recipe(input_ingredients):
    matched_recipes = []
    input_ingredients = [ingredient.strip().lower() for ingredient in input_ingredients]

    for recipe, details in recipes_db.items():
        if all(ingredient in input_ingredients for ingredient in details['ingredients']):
            matched_recipes.append(recipe)

    if matched_recipes:
        recipe = random.choice(matched_recipes)
        return f"Recipe: {recipe}\nIngredients: {', '.join(recipes_db[recipe]['ingredients'])}\nInstructions: {recipes_db[recipe]['instructions']}"
    else:
        return "No matching recipe found. Try different ingredients."

# Get input from the user
user_input = input("Enter the ingredients you have (comma-separated): ").split(",")
print(generate_recipe(user_input))
