import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Boy Playing Football Animation")

green = (0, 128, 0)
white = (255, 255, 255)

boy_color = (0, 0, 255)
football_color = (255, 255, 0)

boy_width, boy_height = 50, 100
football_radius = 15
boy_x, boy_y = 100, screen_height - 150
football_x, football_y = boy_x + 50, boy_y + 60

boy_speed = 5
football_speed = 10
is_kicking = False

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:  
        boy_x += boy_speed
        if not is_kicking:
            football_x += boy_speed
    if keys[pygame.K_SPACE]:  
        is_kicking = True

    if is_kicking:
        football_x += football_speed
        if football_x > screen_width:  
            football_x = boy_x + 50
            is_kicking = False

    screen.fill(green)  

    pygame.draw.rect(screen, boy_color, (boy_x, boy_y, boy_width, boy_height))

    pygame.draw.circle(screen, football_color, (football_x, football_y), football_radius)

    pygame.display.update()

    clock.tick(30)

pygame.quit()
sys.exit()
