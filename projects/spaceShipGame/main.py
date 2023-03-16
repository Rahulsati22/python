import time

import pygame
pygame.font.init()
pygame.mixer.init()
width = 900
height = 500
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rahul Sati's spaceship game")
FPS = 60
yellow_space_ship_image = pygame.transform.scale(pygame.image.load('./Assets/spaceship_yellow.png'), (55, 40))
red_space_ship_image = pygame.transform.scale(pygame.image.load('./Assets/spaceship_red.png'), (55, 40))
red_space_ship_image = pygame.transform.rotate(red_space_ship_image, 90)
yellow_space_ship_image = pygame.transform.rotate(yellow_space_ship_image, -90)
scree_left = pygame.transform.scale(pygame.image.load('./Assets/space.png'), (440, 500))
scree_right = pygame.transform.scale(pygame.image.load('./Assets/space.png'), (500, 500))
speed_spaceShip = 5
bullet_speed = 8
sound = pygame.mixer.Sound('./Assets/Gun+Silencer.mp3')
sound2 = pygame.mixer.Sound('./Assets/Grenade+1.mp3')
red_bullets = []
yellow_bullets = []
max_bullets = 5
red_health = 10
yellow_health = 10
health_font = pygame.font.SysFont('comicsans', 40)


def handleRedMovement(keys_pressed, red):
    if keys_pressed[pygame.K_a] and red.x > 10:
        red.x -= speed_spaceShip
    if keys_pressed[pygame.K_d] and red.x < 390:
        red.x += speed_spaceShip
    if keys_pressed[pygame.K_w] and red.y > 10:
        red.y -= speed_spaceShip
    if keys_pressed[pygame.K_s] and red.y < 440:
        red.y += speed_spaceShip


def handleYellowMovement(keys_pressed, yellow):
    if keys_pressed[pygame.K_DOWN] and yellow.y < 440:
        yellow.y += speed_spaceShip
    if keys_pressed[pygame.K_UP] and yellow.y > 10:
        yellow.y -= speed_spaceShip
    if keys_pressed[pygame.K_LEFT] and yellow.x > 460:
        yellow.x -= speed_spaceShip
    if keys_pressed[pygame.K_RIGHT] and yellow.x < 800:
        yellow.x += speed_spaceShip


def handleBulletsYellow(yellow_bullet, red_bullet, yellow, red):
    global red_health
    global yellow_health
    for bullets in yellow_bullet:
        bullets.x -= bullet_speed
        if red.colliderect(bullets):
            red_health -= 1
            sound.play()

            yellow_bullet.remove(bullets)

        elif bullets.x <= 0:
            yellow_bullet.remove(bullets)
        # yellow_bullet.remove(bullets)


def handleBulletsRed(yellow_bullet, red_bullet, yellow, red):
    global red_health
    global yellow_health
    for bullets in red_bullet:
        bullets.x += bullet_speed
        if yellow.colliderect(bullets):
            yellow_health -= 1
            sound.play()
            red_bullet.remove(bullets)

        elif bullets.x >= WIN.get_width():
            red_bullet.remove(bullets)
        # red_bullet.remove(bullets)


def drawWinner(winner_text):
    winner_name = health_font.render(winner_text, True, (255, 255, 255))
    WIN.blit(winner_name, (350, 250))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    global red_health
    global yellow_health
    clock = pygame.time.Clock()
    run = True
    red = pygame.Rect(100, 300, red_space_ship_image.get_width(), red_space_ship_image.get_height())
    yellow = pygame.Rect(700, 300, yellow_space_ship_image.get_width(), yellow_space_ship_image.get_height())
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and (len(red_bullets) < max_bullets):
                    bullet = pygame.Rect(red.x + red_space_ship_image.get_width(), red.y + red.height//2, 10, 5)
                    red_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and (len(yellow_bullets) < max_bullets):
                    bullet = pygame.Rect(yellow.x - yellow_space_ship_image.get_width(), yellow.y + yellow.height//2, 10, 5)
                    yellow_bullets.append(bullet)


        winner_text = ""
        if red_health == 0:
            winner_text = "yellow wins"
        if yellow_health == 0:
            winner_text = "red wins"
        if winner_text != "":
            sound2.play()
            drawWinner(winner_text)
            break
        keys_pressed = pygame.key.get_pressed()
        handleBulletsRed(yellow_bullets, red_bullets, yellow, red)
        handleBulletsYellow(yellow_bullets, red_bullets, yellow, red)
        handleRedMovement(keys_pressed, red)
        handleYellowMovement(keys_pressed, yellow)
        drawWindow(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    pygame.quit()


def drawWindow(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.fill((0, 0, 0))
    # WIN.blit(yellow_space_ship_image, ())
    WIN.blit(scree_left, (0, 0))
    WIN.blit(scree_right, (450, 0))
    red_health = health_font.render("Health : " + str(red_health), True, (225, 225, 225))
    yellow_health = health_font.render("Health : " + str(yellow_health), True, (255, 255, 255))
    WIN.blit(red_health, (10, 10))
    WIN.blit(yellow_health, (650, 10))
    WIN.blit(red_space_ship_image, (red.x, red.y))
    WIN.blit(yellow_space_ship_image, (yellow.x, yellow.y))
    for bullet in red_bullets:
        pygame.draw.rect(WIN, (255, 0, 0), bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, (255, 255, 0), bullet)
    pygame.display.update()


if __name__ == "__main__":
    main()
