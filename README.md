# 🎮 Adivina el Número

Un divertido y clásico juego de consola escrito en Python donde tu objetivo es adivinar un número secreto generado al azar en la menor cantidad de intentos posible. 

## 📖 ¿Qué es?
"Adivina el número" es un juego interactivo de terminal/consola. El sistema piensa un número y el jugador debe descubrir cuál es mediante ensayo y error. Para hacerlo más interesante, el juego incluye un sistema de puntuación, diferentes niveles de dificultad y una tabla de posiciones (leaderboard) que registra los mejores resultados de la sesión actual.

## ⚙️ ¿Cómo funciona?
El juego fluye a través de las siguientes etapas en cada partida:
1. **Registro:** El juego te pide tu nombre. (Si lo dejas en blanco, jugarás como "Jugador").
2. **Dificultad:** Puedes elegir entre tres niveles que cambian el rango de los números y la cantidad de intentos:
   - **Fácil:** Rango de 1 a 20 con 8 intentos.
   - **Medio:** Rango de 1 a 50 con 7 intentos.
   - **Difícil:** Rango de 1 a 100 con 6 intentos.
3. **El Juego:** Ingresas tus números. Si fallas, el juego te dará pistas indicando si el número secreto es "Muy alto" o "Muy bajo" respecto a tu intento.
4. **Puntuación y Leaderboard:** Si ganas, recibes una puntuación basada en los intentos que te sobraron (cada intento sobrante suma 10 puntos). Al final de la ronda, se muestra el "Top 3" de los mejores jugadores de la sesión.
5. **Rejugabilidad:** Puedes decidir si quieres jugar otra ronda o salir del juego.

## 🚀 Cómo ejecutarlo

### Requisitos previos
Para poder jugar, necesitas tener **Python 3.x** instalado en tu computadora. Este código utiliza únicamente bibliotecas estándar de Python (`random` y `datetime`), por lo que no necesitas instalar ninguna dependencia externa.

### Instrucciones paso a paso
1. Clona este repositorio o descarga el archivo del código fuente (por ejemplo, guardalo como `juego.py`).
2. Abre una terminal o símbolo del sistema (Command Prompt / PowerShell / Bash).
3. Navega hasta la carpeta donde guardaste el archivo usando el comando `cd`. Ejemplo:
   ```bash
   cd ruta/a/tu/carpeta
   ```
4. Ejecuta el script con el siguiente comando:
   ```bash
   python juego.py
   ```
   *(Nota: En algunos sistemas, como macOS o Linux, es posible que debas usar `python3 juego.py`)*

## 🛠️ Tecnologías utilizadas
* **Python 3:** Lenguaje principal de desarrollo.
* **Módulo `random`:** Para la generación del número secreto.
* **Módulo `datetime`:** Para registrar el momento exacto en el que se guarda un puntaje (preparado para futuras expansiones, como guardar el historial en un archivo).

---
*¡Gracias por jugar y divertirte programando!*