
import pygame
import sys

pygame.init()
window = pygame.display.set_mode((0,0))

class Rocket:
    def __init__(self,speed, width , height, x, y, skin):
        self.texture = pygame.image.load(skin)
        self.texture = pygame.transform.scale(self.texture, [width, height])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
    def move(self):
        keys = pygame.key.get_pressed()
        if keys [pygame.K_RIGHT]:
            self.hitbox.x += self.speed
        if keys [pygame.K_DOWN]:
            self.hitbox.y += self.speed
        if keys [pygame.K_UP]:
            self.hitbox.y -= self.speed
        if keys [pygame.K_LEFT]:
            self.hitbox.x -= self.speed


    def draw(self, window):
        window.blit(self.texture, self.hitbox)
class UFO:
    def __init__(self,speed, width , height, x, y, skin):
        self.texture = pygame.image.load(skin)
        self.texture = pygame.transform.scale(self.texture, [width, height])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
    def draw(self, window):
        window.blit(self.texture, self.hitbox)

UFOs = [
     UFO(1, 100,100,100, 100,"ufo.png"),
     UFO(1, 100,100,200, 100,"ufo.png"),
     UFO(1, 100,100,300, 100,"ufo.png"),
     UFO(1, 100,100,400, 100,"ufo.png"),
     UFO(1, 100,100,500, 100,"ufo.png"),
     UFO(1, 100,100,600, 100,"ufo.png"),
     UFO(1, 100,100,700, 100,"ufo.png"),
     UFO(1, 100,100,800, 100,"ufo.png"),
     UFO(1, 100,100,900, 100,"ufo.png"),
     UFO(1, 100,100,1000, 200,"ufo.png"),
     UFO(1, 100,100,1100, 200,"ufo.png"),
     UFO(1, 100,100,1200, 200,"ufo.png"),
     UFO(1, 100,100,1300, 200,"ufo.png"),
     UFO(1, 100,100,1400, 200,"ufo.png"),
     UFO(1, 100,100,1500, 200,"ufo.png"),
     UFO(1, 100,100,1600, 200,"ufo.png"),








]







fps = pygame.time.Clock()
player = Rocket(3, 50, 125, 350, 250, "rocket.png")


background = pygame.image.load('galaxy.jpg')
background = pygame.transform.scale(background, window.get_size())


window.blit(background, [0, 0])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    player.move()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
        pygame.display.toggle_fullscreen()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            pygame.quit()


    window.fill([255, 255, 255])
    window.blit(background, [0, 0])
    player.draw(window)
    for ufo in UFOs:
        ufo.draw(window)



    pygame.display.flip()
    fps.tick(60)