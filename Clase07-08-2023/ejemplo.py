from pygame import *   
# Configuración de la ventana
window_size = (800, 500)
window = display.set_mode(window_size)
display.set_caption("Ejemplo de figuras en Pygame")

# Color de la línea (rojo en este caso)
color = (255, 0, 0)

# Puntos de inicio y fin para la línea
x1, y1 = 100, 100
x2, y2 = 400, 300

# Bucle principal del juego
run = True
while run:
    for e in event.get():
      #evento de pulsación de botón “x” en ventana
      if e.type == QUIT:
          run = False

    # Limpia la pantalla
    window.fill((255, 255, 255))

    # Dibuja la línea antialiased en la ventana
    draw.aaline(window, color, (x1, y1), (x2, y2))
    # Limpia la pantalla
    #window.fill((255, 255, 255))

    # Dibuja el rectángulo en la ventana
    draw.rect(window,(0, 255, 0), (100, 300, 200, 150))

    # Dibuja la elipse en la ventana
    draw.ellipse(window, (0, 0, 255), (400, 200, 200, 100))

    # Actualiza la ventana
    display.flip()