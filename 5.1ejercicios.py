""" 
================
      DATES
================
""" 

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

aquarium_creatures = [
	{"name": "sammy", "species": "shark", "tank number": 11, "type": "fish"},
	{"name": "ashley", "species": "crab", "tank number": 25, "type": "shellfish"},
	{"name": "jo", "species": "guppy", "tank number": 18, "type": "fish"},
	{"name": "jackie", "species": "lobster", "tank number": 21, "type": "shellfish"},
	{"name": "charlie", "species": "clownfish", "tank number": 12, "type": "fish"},
	{"name": "olly", "species": "green turtle", "tank number": 34, "type": "turtle"}
]

# Uso de map
# elevar los numeros de una lista al cuadrado
mapped_numbers = list(map(lambda x: x ** 2, numbers))
print(mapped_numbers)

# obtener los valores de una lista de diccionarios
names_creatures = list(map(lambda creature: creature['name'],aquarium_creatures))
print(names_creatures)

# Agregar una nueva key a los dicionarios
meal = list(map(lambda add: {**add, **{'meal': 'Tacos' if add['type'] == 'fish' else 'Other'}}, aquarium_creatures))
print(meal)

# Obteniendo los datos del la nueva lista
the_meal_creatures = list(map(lambda meal_crature: meal_crature['meal'], meal))
print(the_meal_creatures)

# Uso de filter
# filtrar por keys
fishes = list(filter(lambda fish: fish['type'] == 'fish', aquarium_creatures))
print(fishes)

