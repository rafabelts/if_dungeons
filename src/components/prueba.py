import random
prepositions = {
    "Si las rosas son rojas": "and",

}

prepositions_keys = list(prepositions.keys())

print(prepositions.get("Si las peras y manzanas"))
print(random.choice(prepositions_keys))
