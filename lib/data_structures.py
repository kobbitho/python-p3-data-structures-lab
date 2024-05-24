spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return[food["name"] for food in spicy_foods]
food_names = get_names(spicy_foods)
#print(food_names)
    

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

spiciest_foods = get_spiciest_foods(spicy_foods)
#print(spiciest_foods)

    
def print_spicy_foods(spicy_foods):
   for food in spicy_foods:
        heat_level = ""
        for _ in range(food["heat_level"]):
            heat_level += "🌶"
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

#print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return next((food for food in spicy_foods if food["cuisine"]==cuisine), None)
#print(get_spicy_food_by_cuisine(spicy_foods, "American"))



def print_spiciest_foods(spicy_foods):
     for food in get_spiciest_foods(spicy_foods):
        heat_level = ""
        for _ in range(food["heat_level"]):
            heat_level += "🌶"
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

#print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    return total_heat_level / len(spicy_foods)

#print(get_average_heat_level(spicy_foods))


def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_food = {
        "name": spicy_food["name"],
        "cuisine": spicy_food["cuisine"],
        "heat_level": spicy_food["heat_level"]
    }
    spicy_foods.append(new_spicy_food)
    return spicy_foods

spicy_foods = create_spicy_food(spicy_foods, {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
})
#print(spicy_foods)
