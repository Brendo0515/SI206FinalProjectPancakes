# Import statements
import unittest
import sqlite3
import requests
import json
import re
import matplotlib
import matplotlib.pyplot as plt

def add_recipe_info(db_filename, recipe_name, recipe_id):
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()
    cur.execute('INSERT INTO Spoonacular(recipes_name, recipes_id) VALUES (?,?)', (recipe_name, recipe_id))
    conn.commit()
    cur.close()

offset = 0
# repeat search for 20 recipes 5 times to get 100 recipes
for i in range(5):
    #get 20 pancake recipes
    response = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search?number=20&offset="
    +str(offset)+"&query=pancakes",
      headers={
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "53727a77bemsh0a934f995b2ee59p1b05e5jsn6ff88a83a15e"
      }
    )
    list_of_pancake_recipes = json.loads(response.text)["results"]
    for recipe in list_of_pancake_recipes:
        #add recipe name to database
        recipe_name = recipe["title"]
        recipe_id = recipe["id"]
        add_recipe_info("pancakes.sqlite", recipe_name, recipe_id)

    #change offset to get the next 20 pancake recipes
    offset += 20

# #to clear database
# conn = sqlite3.connect("pancakes.sqlite")
# cur = conn.cursor()
# cur.execute("DELETE FROM Spoonacular")
# conn.commit()
# cur.close()
