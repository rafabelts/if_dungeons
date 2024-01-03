prepositions = {
    "Si las rosas son rojas y las violetas son azules": "and",
    "Van al cine si hay promoción o les pagan la quincena": "or",
    "Vivir o morir": "exclusive disjunction",
    "Si te portas bien, te llevare de viaje": "implies",
    "p si y sólo si q": "biconditional",
    "Sacaras diez si estudias y haces tus tareas": "and",
    "Si limpias tu cuarto te sentiras más comodo": "implies",
    "El perro ladra y el gato maulla": "and",
    "Barreran si no esta lloviendo o si esta muy sucio": "or",
    "Hoy me levante temprano y desayune": "and",
    "Me duermo tarde o desayuno": "exclusive disjunction",
    "Si hoy me levanto temprano desayunare": "implies"
}

list_of_prepositions = list(prepositions.keys())


def get_answer(random_preposition):
    return prepositions.get(random_preposition)

