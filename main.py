def game():
    import pygame
    import sys
    import random
    #import self

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
            self.bullets = []
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
            if keys[pygame.K_x]:
                self.bullets.append(Bullet(5,
                                           50, 55,
                                           self.hitbox.x, self.hitbox.y,
                                           "png-klev-club-ab03-p-solo-shd-png-9.png"))

            for bullet in self.bullets:
                bullet.move()

        def draw(self, window):
            window.blit(self.texture, self.hitbox)
            for bullet in self.bullets:
                bullet.draw(window)
    class UFO:
        def __init__(self, speed, width, height, x, y, filename):
            self.texture = pygame.image.load(filename)
            self.texture = pygame.transform.scale(self.texture, [width, height])
            self.hitbox = self.texture.get_rect()
            self.hitbox.x = x
            self.hitbox.y = y
            self.speed = speed

        def draw(self, window):
            window.blit(self.texture, self.hitbox)

        def move(self):
            self.hitbox.y += self.speed

    class Asteroid:
        def __init__(self, filename, width, height, x, y, speed):
            self.texture = pygame.image.load(filename)
            self.texture = pygame.transform.scale(self.texture, [width, height])
            self.hitbox = self.texture.get_rect()
            self.hitbox.x = x
            self.hitbox.y = y
            self.speed = speed
            window.blit(self.texture, self.hitbox)






    class Bullet:
        def __init__(self, speed,   width, height, x , y, skin):
            self.texture = pygame.image.load(skin)
            self.texture = pygame.transform.scale(self.texture, [width, height])
            self.hitbox = self.texture.get_rect()
            self.hitbox.x = x
            self.hitbox.y = y
            self.speed = speed

        def move(self):
                self.hitbox.y -= self.speed

        def draw(self, window):
            window.blit(self.texture, self.hitbox)













    UFOs = []
    y = 200
    for i in range(10):
        UFOs.append(UFO(5, 120, 150, random.randint(0, 650), y, "png-klev-club-8zaz-p-bravo-stars-bull-png-6.png"))
        y -= 100

    y = 200
    for i in range(10):
        UFOs.append(UFO(5, 120, 150, random.randint(0, 650), y, "png-klev-club-d05q-p-edgar-bravo-stars-png-14.png"))
        y -= 100

    score = 0
    score_lbl = pygame.font.Font(None, 23).render("Score: " + str(score), True, [0,0,0])

    fps = pygame.time.Clock()
    player = Rocket(9, 100, 200, 650, 450, "png-klev-club-a6lo-p-kolt-bravo-stars-png-28.png")


    background = pygame.image.load('png-klev-club-appf-p-solo-shd-png-20.png')
    background = pygame.transform.scale(background, window.get_size())


    window.blit(background, [0, 0])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
        player.move()
        for e in UFOs:
            e.move()
            if e.hitbox.y > 1080:
                e.hitbox.y = -100
                e.hitbox.x = random.randint(0, 1920)

        for e in UFOs:
            for b in player.bullets:
                if e.hitbox.colliderect(b.hitbox):
                    b.hitbox.x = 5000
                    player.bullets.remove(b)
                    e.hitbox.y = -100
                    e.hitbox.x = random.randint(0, 1920)
                    score += 1
                    break
        score_lbl = pygame.font.Font(None, 23).render("Score: " + str(score), True, [0, 0, 0])

        window.fill([255, 255, 255])
        window.blit(background, [0, 0])
        player.draw(window)
        for ufo in UFOs:
            ufo.draw(window)



        pygame.display.flip()
        fps.tick(60)
game()