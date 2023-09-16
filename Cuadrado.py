from pygame import *
#                          x,   y
window = display.set_mode((700, 500))
display.set_caption("Elipse")
background = (255, 255, 255)
window.fill(background)

#Colores RGB (Red, Green, Blue)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

#draw.aaline(window, (a,b,c), [x1, y1], [x2, y2])
x1 = 150
y1 = 55
x2 = 500
y2= 100
#draw.rect(window, (a,b,c), (x, y, width, height))
xRect = 200
yRect = 300
widthRect = 200
heightRect = 200
#draw.ellipse(window, (a,b,c), (x, y, width, height)) 
xElipse = 300
yElipse = 100
widthElipse = 200
heightElipse = 200

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        window.fill(background)
        draw.aaline(window, (blue), [x1, y1], [x2, y2])
        draw.rect(window, (red), (xRect, yRect, widthRect, heightRect))
        draw.ellipse(window, (green), (xElipse, yElipse, widthElipse, heightElipse))
    display.update()
