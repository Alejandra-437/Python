from pygame import*
window = display.set_mode((700, 500))
display.set_caption("Primera aplicación")
background = (255, 255, 255)
#color azul
color = (0, 0, 255)
colorElipse = (255, 0, 0)
#cordenas de los puntos de la línea
x1 = 10
y1 = 5
x2 = 20
y2 = 10

# Define las coordenadas, ancho y alto de la elipse
x, y, width, height = 300, 300, 100, 150

# Dibuja la elipse

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        window.fill(background)
        draw.ellipse(window, colorElipse, (x, y, width, height))

        draw.aaline(window, (color), [x1, y1], [x2, y2])
        
    display.update()
# Cierra Pygame
