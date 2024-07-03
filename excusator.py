import random

excusas = [
        "mi perro meó en el router.",
        "me distraje investigando sobre el movimiento obrero en los 70.",
        "mi gato tiró mi notebook del escritorio.",
        "creo que me agarré Covid.",
        "me quedé hasta las 3 AM puteándome con gente en Twitter.",
        "todo es una construcción social, incluso hacer un commit.",
        "Fibertel es una porquería.",
        "el tarot me dijo que esta no es una buena semana para eso.",
        "colgué mirando videos de la Scaloneta."
    ]

def generar_excusa():
    return random.choice(excusas)

if __name__ == "__main__":
    excusa = generar_excusa()
    print(f"Perdón profe, no pude subir el código porque {excusa}")
