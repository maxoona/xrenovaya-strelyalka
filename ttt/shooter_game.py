from pygame import *
from random import randint
from time import time as timer

mixer.init()
mixer.music.loud('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

font.init()
font1 = fontFont(None,80)
win = font1.render('you win', True, (255, 255, 255))
lose = font1.render('you lose', True, (180, 0, 0))
font2 = font.Font(None, 36)

img_back = "galaxy.jpg"
img_hero = "rocket.jpg"
img_enemy = "ufo.jpg"
img_ast = "asteroid.png"

score = 0
lost = 0
max_lost = 3
life = 3

class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
    
        sprite.Sprite.__init__(self)


        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed


        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y= player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):

    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost

        if self.rect.y > win_height
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


win_width = 700
win_height = 500
display.set_cartion("strelyalka")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back))

ship = player(img_hero, 5, win_height - 100, 80, 100, 10)


monsters = sprite.Group()
for i in range(6):
    monsters = Enemy(img_enemy, randint(80, win_width - 80), - 40, 80, 50, randin(1, 5))
    monsters.add(monsters)

asteroids = sprite.Group()
for i in range(6)
    asteroid = Enemy(img_ast, randint(30, win_width - 30), -40, 80, 50, randint(1, 5))

bullets = sprite.Group()

finish = False 

run = True

rel_time = False

num_fire = 0

while run:
    for e in event.get():
        if e.type == QUIT
            run = False

        elif e.type == KEYDOWN:
            if e.key == KEY_SPACE:
                
                if num_fire < 5 and rel_time == False: 
                    num_fire = num_fire + 1 
                    fire_sound.play()
                    ship.fire()

                if num_fire >= 5 and rel_time == False:
                    last_time = timer()
                    rel_time = True

                

    if not finish:
        window.blit(background,(0,0))
        text = font2.render("schet" + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        text.lose = font2.render("losed: " + str(lost), 1, (255, 255, 255))
        window.blit
        
        
        ship.update()
        monsters.update()
        asteroids.update()
        bullets.update()



        if rel_time == True:
            now_time = timer()

            if now_time - last_time < 3:
                reload = font2.render('Wait, reloading...', 1, (150, 0, 0))
                window.blit(reload, (260, 460))
            else: 
                num_fire = 0
                rel_time = False

    if sprite.spritecollide(ship, monsters, False) or sprite.spritecollide(ship, asteroids, False):
        sprite.collide(ship, mosters, True)
        sprite.spritecollide(ship, asteroids, True)







