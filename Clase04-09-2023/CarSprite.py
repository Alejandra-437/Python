from pygame import *

# Clase del jugador principal - coches
class Car(sprite.Sprite):
    def __init__(self, image_path, x, y):
        sprite.Sprite.__init__(self)

        # Carga y escala la imagen del carro
        self.image = transform.scale(image.load(image_path), (80, 80))

        # Crea un rectángulo para el carro
        self.rect = self.image.get_rect()

        # Establece la ubicación inicial del carro
        self.rect.x = x
        self.rect.y = y

    # Método para definir el movimiento del objeto
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= 5
        if keys[K_RIGHT]:
            self.rect.x += 5
        if keys[K_UP]:
            self.rect.y -= 5
        if keys[K_DOWN]:
            self.rect.y += 5

        # Dibuja un rectángulo de color negro como la imagen
        self.image = Surface([80, 80])
        self.image.fill((0, 0, 0))
    def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))

# Dimensiones de la ventana
win_width = 700
win_height = 500
display.set_caption("Carro")
window = display.set_mode((win_width, win_height))
finish = False

# Crea una instancia de la clase Car
car = Car('D:/Alejandra Serrano/PythonPro/car.jpg', 5, win_height - 80)

# Ciclo de juego
run = True
while run:
    # El ciclo se ejecuta cada 0.05 segundos
    time.delay(50)
    
    # Se revisan todos los eventos que pueden suceder
    for e in event.get():
        # Evento de clic en el botón “cerrar”
        if e.type == QUIT:
            run = False
    
    if not finish:
        # Actualiza el fondo con cada iteración
        window.fill((255, 255, 255))
        
        # Actualiza el estado del carro
        car.update()
        car.reset()
    
    display.update()

# Cierra la ventana al salir del ciclo
display.quit()