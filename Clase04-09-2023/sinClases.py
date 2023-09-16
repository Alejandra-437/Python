from pygame import *
#Crear una ventana
win_width = 700
win_height = 500
display.set_caption("Laberinto")
window = display.set_mode((win_width, win_height))
 
image_hero = transform.scale(image.load('D:/Alejandra Serrano/PythonPro/Laberinto/Copy of hero.png'), (80, 80))
speed_hero = 5
rect_hero = image_hero.get_rect()
rect.x_hero = 5 # type: ignore
rect.y_hero = win_height - 80 # type: ignore
 
side = "izquierda"
image_enemy = transform.scale(image.load('D:/Alejandra Serrano/PythonPro/Laberinto/Copy of cyborg.png'), (80, 80))
speed_enemy = 5
rect_enemy = image_enemy.get_rect()
rect.x_enemy = win_width - 80 # type: ignore
rect.y_enemy = 200 # type: ignore
 
wall_width = 300
wall_height = 10
wall_x = win_width / 2 - win_width / 3
wall_y = win_height / 2
 
image_final = transform.scale(image.load('D:/Alejandra Serrano/PythonPro/Laberinto/Copy of pac-1.png'), (80, 80))
rect_final = image_final.get_rect()
rect.x_final = win_width - 85 # type: ignore
rect.y_final = win_height - 100 # type: ignore
 
# imagen de la pared – un rectángulo del tamaño y color deseado:
image_wall = Surface([wall_width, wall_height])
image_wall.fill((0, 0, 0))
rect_wall = image_wall.get_rect()
rect_wall = Rect(wall_x, wall_y, wall_width, wall_height)
 
#variable responsable por cómo termina el juego
finish = False
#ciclo de juego
run = True
while run:
  #el ciclo se ejecuta cada 0.05 segundos
  time.delay(50)
   #se comprueban todos los eventos que pueden suceder
  for e in event.get():
      #evento del clic del botón “cerrar”
      if e.type == QUIT:
          run = False
 
#comprobar que el juego no está terminado todavía
  if not finish:
       #actualizar el fondo con cada iteración
       window.fill((255, 255, 255))
  
       #dibujar las paredes
       draw.rect(window, (0, 0, 0), (wall_x, wall_y, wall_width, wall_height))
       #ejecutar el movimiento del objeto
       keys = key.get_pressed()
       if keys[K_LEFT] and rect.x_hero > 5: # type: ignore
           rect.x_hero -= speed_hero # type: ignore
       if keys[K_RIGHT] and rect.x_hero < win_width - 80: # type: ignore
           rect.x_hero += speed_hero # type: ignore
       if keys[K_UP] and rect.y_hero > 5: # type: ignore
           rect.y_hero -= speed_hero # type: ignore
       if keys[K_DOWN] and rect.y_hero < win_height - 80: # type: ignore
           rect.y_hero += speed_hero # type: ignore
      
      
       if rect.x_enemy <= 410: # type: ignore
           side = "right"
       if rect.x_enemy >= win_width - 85: # type: ignore
           side = "left"
       if side == "left":
           rect.x_enemy -= speed_enemy # type: ignore
       else:
           rect.x_enemy += speed_enemy # type: ignore
      
       #actualizarlos en una nueva ubicación con cada iteración del ciclo
       window.blit(image_hero, (rect.x_hero, rect.y_hero)) # type: ignore
       window.blit(image_enemy, (rect.x_enemy, rect.y_enemy)) # type: ignore
       window.blit(image_final, (rect.x_final, rect.y_final)) # type: ignore
 
  display.update()

