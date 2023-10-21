
from pygame import *


class Superior(sprite.Sprite):
    #consturctor de la clase
    def __init__(self, player_image, player_x, player_y, player_speed): 
        #manda a llamar el constuctor de la clase Sprite() = super().__init__(self)
        sprite.Sprite.__init__(self)

        #creando las propiedades
        #guardando la imagen del jugador
        self.image = transform.scale(image.load(player_image),(80, 80))
        self.speed = player_speed

        #cada objeto tiene que almacenar la propiedad rectangulo (rect) porque ahi es donde el ibjeto sera ingresado
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

        #metodo de dibujo del personaje en la ventana, sease, poner la imagen en la ventana
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#Clase hijo de la clase Superior
class Player(Superior):
    #metodo que implementa el control de los objetos(jugadores) utilizando los botones WASD del teclado
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

#Segunda clase hijo de la clase Superior
class Enemy(Superior):
    side = "left"
    #movimiento de nuestro enemigo
    def update(self):
        if self.rect.x <= 400:
            self.side = "right"
        if self.rect.x >= win_width - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

#clase del elemnto pared
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        sprite.Sprite.__init__(self)
        self.color_1 =color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        #imagen de nuestra pared -> rectangulo del tamaño y color que ustedes quieran
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))

        #cada objeto tiene que almacenar la propiedad rectangulo (rect) porque ahi es donde el ibjeto sera ingresado
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

        #dibujo del rectangulo
    def draw_wall(self):
        draw.rect(window, (self.color_1,self.color_2, self.color_3),(self.rect.x, self.rect.y, self.width, self.height))



win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption("Cualquiera Laberinto")
#creando paredes          x= 116.67 aprox        y=250
p1 = Wall(32,0,97,win_width/2-win_width/3,win_height/2,300,10)
p2 = Wall(21, 233, 219, 400, win_height/2 - win_height/4,10, 350)
#Creando objetos

volcancito = Player('hero.png',5, win_height-80, 10)
La_Jura = Enemy('cyborg.png',win_width-80, 200,15)
Trophy = Superior('pac-1.png', win_width-85,win_height-100,0)

#variable que ve como termina el juego
finish = False

#ciclo de juego
run = True
while run:
    #el ciclo se ira ejecutando cada 0.05 segundos
    time.delay(50)
    #validando tdodos los eventos que puedan suceder
    for e in event.get():
        if e.type == QUIT:
            run = False
    #comprobar que el juego no haya terminado todavia
    if not finish:
        window.fill((240,199,63))
        #dibujar paredes
        p1.draw_wall()
        p2.draw_wall()
        #movimientos de los objetos
        volcancito.update()
        La_Jura.update()
        #actualizacion en nueva ubicacion con cada iteracion del ciclo
        volcancito.reset()
        La_Jura.reset()
        Trophy.reset()

        #comprobar el choque entre el personaje y el enemigo o paredes
    if sprite.collide_rect(volcancito, La_Jura) or sprite.collide_rect(volcancito, p1) or sprite.collide_rect(volcancito, p2):
        finish = True
        #calcular la tasa

        img = image.load('game-over_1.png')
        d = img.get_width() // img.get_height()
            
        window.blit(transform.scale(img, (win_height *d , win_height)),(90,0))
    if sprite.collide_rect(volcancito,Trophy):
        finish =True
        img= image.load('thumb.jpg')
        window.fill((240,199,63))
        window.blit(transform.scale(img,(win_width, win_width)),(0,0))

    display.update()