from pygame import*
window = display.set_mode((700, 500))
display.set_caption("Hola mundoxD")
background = transform.scale(image.load("D:/Alejandra Serrano/PythonPro/Backgrounds/background.png"), (700, 500))
# parámetros del primer objeto (cuadrado)
height = 60
width = 40
x = 5
y = 500 - height - 5
speed = 5
#parámetros del objeto de imagen
x2 = 100
y2 = 395
#imagen de personaje
img1 = transform.scale(image.load('D:/Alejandra Serrano/PythonPro/Heroes/balls/basketball.png'), (100, 100))
#ciclo de juego
run = True
while run:
  #el ciclo es ejecutado cada 0.05 seg
  time.delay(50)
  #en cada iteración, se pinta la pantalla del color inicial y se vuelve a dibujar el objeto en un nuevo lugar
  #window.fill((0,0,0)) #fondo negro
  window.blit(background,(0, 0))
   #Búsqueda de todos los eventos que podrían ocurrir
  for e in event.get():
      #evento de pulsación de botón “x” en ventana
      if e.type == QUIT:
          run = False
        
   #----------------------------------------------------------------------------
   #gestionando y actualizando la imagen del objeto cuadrado
   #un simple método de gestión – no funciona si se mantiene presionada una tecla
      if e.type == KEYDOWN: #se comprueba si hay un evento de pulsación de tecla
          if e.key == K_LEFT: #comprueba qué botón es presionado
              x -= speed
          elif e.key == K_RIGHT:
              x += speed
          elif e.key == K_UP:
              y -= speed
          elif e.key == K_DOWN:
              y += speed
  draw.rect(window, (0, 0, 255), (x, y, width, height))
 
  #----------------------------------------------------------------------------
  #gestionando y actualizando la imagen del objeto cuadrado
  #una solución más compleja – se detiene cuando una tecla se suelta, el personaje se mantiene dentro de los bordes de la pantalla.
  window.blit(img1, (x2, y2))
  keys = key.get_pressed()
  if keys[K_LEFT] and x2 > 5:
      x2 -= speed
  if keys[K_RIGHT] and x2 < 595:
      x2 += speed
  if keys[K_UP] and y2 > 5:
      y2 -= speed
  if keys[K_DOWN] and y2 < 395:
      y2 += speed
  display.update()