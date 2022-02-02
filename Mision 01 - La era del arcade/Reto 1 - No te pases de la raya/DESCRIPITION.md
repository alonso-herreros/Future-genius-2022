# **[¡No te pases de la raya!](https://immune.hackrocks.com/challenges/start/no-te-pases-de-la-raya)**

| 30 Points | EASY |
|-----------|------|

## Summary
Los miembros más veteranos de la plantilla de VR Electronics no pueden contener su indignación: ¡El Space Invaders, uno de los juegos más icónicos de toda la historia y al que todos tanto jugaron de jóvenes, ha sido mancillado! Si queremos devolver el juego a su estado original, ¡habrá que ponerse manos a la obra y arreglarlo!

## In this challenge:
- Desarrollo de videojuegos
- Python

---

Mientras nuestros ingenieros revisaban el estado del código del Space Invaders tras el ciberataque, se percataron de que algo no iba bien: ¡La nave abandona los límites de la pantalla de juego sin control! No podemos permitir semejante error en el funcionamiento.

Te encargan revisar el código, y tras una inspección inicial, llegas a las siguientes conclusiones:

1. Una vez ejecutado el script, la nave puede moverse horizontalmente, siendo controlada con las flechas izquierda y derecha del teclado. En el bloque de líneas de código que va de la línea 41 a la 47 se detecta si alguna de las flechas está pulsada, y si ese es el caso, se aumenta o disminuye la posición de la nave, para que ésta avance en la dirección apropiada.
2. También, antes de modificar la posición de la nave, ésta es comparada con dos variables que actúan como límites, para ver si la nave puede seguir avanzando o si debe detenerse porque ha llegado a uno de los bordes de la ventana de juego.
Tu misión es descubrir dónde está el error que hace que la nave se salga de los límites de la ventana de juego, y una vez descubierto, solucionarlo, de manera que la nave quede contenida en la ventana de juego y se aproveche al máximo el espacio de la misma.

---

### **Solución:**
La solución a este reto consiste en los dos valores numéricos que solucionan el problema que hace que la nave no esté contenida exactamente en los bordes de la ventana de juego. El token será introducirlos separados por una coma, de la forma “**A, B**”.