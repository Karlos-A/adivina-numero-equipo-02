import random
from datetime import datetime

GAME_TITLE = "Adivina el número"
DIFFICULTIES = {
    "1": {"name": "Fácil", "minimum": 1, "maximum": 20, "attempts": 8},
    "2": {"name": "Medio", "minimum": 1, "maximum": 50, "attempts": 7},
    "3": {"name": "Difícil", "minimum": 1, "maximum": 100, "attempts": 6},
}


def get_player_name():
    name = input("¿Cómo te llamas? ").strip()
    if name == "":
        return "Jugador"
    return name


def choose_difficulty():
    print("\nSelecciona una dificultad:")
    print("1. Fácil (1–20, 8 intentos)")
    print("2. Medio (1–50, 7 intentos)")
    print("3. Difícil (1–100, 6 intentos)")

    choice = input("Opción: ").strip().lower()
    if choice in DIFFICULTIES:
        return DIFFICULTIES[choice]

    print("Opción inválida. Se usará la dificultad Fácil.")
    return DIFFICULTIES["1"]


def get_valid_guess(minimum: int, maximum: int) -> int:
    while True:
        raw_guess = input(f"Escribe un número entre {minimum} y {maximum}: ").strip()

        try:
            guess = int(raw_guess)
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")
            continue

        if guess < minimum or guess > maximum:
            print(f"El número debe estar entre {minimum} y {maximum}. Inténtalo de nuevo.")
            continue

        return guess


def calculate_score(attempts_used, maximum_attempts, won):
    if won is False:
        return 0

    points = (maximum_attempts - attempts_used) * 10
    if points < 0:
        points = 0
    return points


def play_round(settings):
    secret_number = random.randint(settings["minimum"], settings["maximum"])
    attempts_used = 0
    won = False

    print(
        f"\nAdivina el número entre {settings['minimum']} y "
        f"{settings['maximum']}. Tienes {settings['attempts']} intentos."
    )

    while attempts_used < settings["attempts"] and won is False:
        guess = get_valid_guess(settings["minimum"], settings["maximum"])
        attempts_used += 1

        if guess < secret_number:
            print("Muy bajo.")
        elif guess > secret_number:
            print("Muy alto.")
        else:
            print("¡Correcto!")
            won = True

    if won:
        print(f"Adivinaste en {attempts_used} intentos.")
    else:
        print(f"Se acabaron los intentos. El número era {secret_number}.")

    score = calculate_score(attempts_used, settings["attempts"], won)
    return {
        "won": won,
        "attempts_used": attempts_used,
        "score": score,
        "secret_number": secret_number,
    }


def save_score(scores: list, player_name: str, result: dict, difficulty_name: str) -> dict:
    record = {
        "player_name": player_name,
        "score": result["score"],
        "won": result["won"],
        "difficulty_name": difficulty_name,
        "played_at": datetime.now(),
    }
    scores.append(record)
    scores.sort(key=lambda item: item["score"], reverse=True)
    return record


def show_leaderboard(scores):
    print("\n--- Mejores resultados de esta sesión ---")
    if len(scores) == 0:
        print("Todavía no hay resultados.")
        return

    for position, result in enumerate(scores[:3], start=1):
        print(
            f"{position}. {result['player_name']} — {result['score']} puntos "
            f"({result['difficulty_name']})"
        )

# Mejora Adicional
def show_round_summary(result: dict):
    print("\n" + "=" * 30)
    print("      RESUMEN DE LA PARTIDA")
    print("=" * 30)

    if result["won"]:
        print("Resultado: ¡Victoria!")
    else:
        print("Resultado: Derrota")

    print(f"Número secreto: {result['secret_number']}")
    print(f"Intentos utilizados: {result['attempts_used']}")
    print(f"Puntuación obtenida: {result['score']} puntos")


def play_game(session_scores: list):
    player_name = get_player_name()
    settings = choose_difficulty()
    result = play_round(settings)

    show_round_summary(result)
    save_score(session_scores, player_name, result, settings["name"])
    show_leaderboard(session_scores)


def ask_to_play_again():
    answer = input("\n¿Quieres jugar otra vez? (s/n): ").strip().lower()
    if answer in ["s", "si", "sí"]:
        return True
    return False


def main():
    print(f"=== {GAME_TITLE} ===")
    print("Adivina el número secreto y consigue la mayor puntuación.")
    scores = []

    while True:
        play_game(scores)
        if ask_to_play_again() is False:
            break

    print("\nGracias por jugar.")


if __name__ == "__main__":
    main()