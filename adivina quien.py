import random

# Lista de equipos de fútbol mexicano
equipos = [
    "América",
    "Chivas",
    "Cruz Azul",
    "Pumas",
    "Tigres",
    "Monterrey",
    "Santos",
    "León",
    "Tijuana",
    "Pachuca"
]

# Función para jugar
def adivina_quien():
    equipo_seleccionado = random.choice(equipos)
    print("He seleccionado un equipo de fútbol mexicano.")
    
    preguntas = [
        "¿Es un equipo que ha ganado la liga más de 10 veces?",
        "¿Juega en la Ciudad de México?",
        "¿Es un equipo del norte de México?",
        "¿Es un equipo que tiene un gato como mascota?",
        "¿Es conocido por su afición muy apasionada?"
    ]

    respuestas = {
        "América": [True, True, False, False, True],
        "Chivas": [False, True, False, False, True],
        "Cruz Azul": [True, True, False, False, True],
        "Pumas": [False, True, False, True, True],
        "Tigres": [True, False, True, True, True],
        "Monterrey": [True, False, True, False, True],
        "Santos": [False, False, True, False, True],
        "León": [True, False, False, False, True],
        "Tijuana": [False, False, True, False, False],
        "Pachuca": [True, False, False, False, True]
    }

    max_preguntas = 5
    for i in range(max_preguntas):
        print(f"\nPregunta {i + 1}: {preguntas[i]}")
        respuesta = input("Respuesta (sí/no): ").strip().lower()
        
        if respuesta == 'sí':
            respuesta_real = True
        elif respuesta == 'no':
            respuesta_real = False
        else:
            print("Respuesta inválida. Debes responder 'sí' o 'no'.")
            continue

        if respuesta_real != respuestas[equipo_seleccionado][i]:
            print("Esa respuesta no coincide con el equipo seleccionado. Intenta de nuevo.")
            continue

    adivinanza = input("\n¿Adivinas cuál es el equipo? ")
    if adivinanza.lower() == equipo_seleccionado.lower():
        print("¡Correcto! ¡Has adivinado el equipo!")
    else:
        print(f"Incorrecto. El equipo era {equipo_seleccionado}.")

# Ejecutar el juego
if __name__ == "__main__":
    adivina_quien()
