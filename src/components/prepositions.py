prepositions = {
    "Si las rosas son rojas y las violetas son azules": "and",
    "Van al cine si hay promoción o les pagan la quincena" : "or",
}


list_of_prepositions = list(prepositions.keys())


def get_answer(random_preposition):
    return prepositions.get(random_preposition)

