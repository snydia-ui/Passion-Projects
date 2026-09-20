# CREDITSO CHLOE S IRENEO
# SHE SHOWED ME HER PROGRAM SO I GOT THE IDEA TO DO THIS
import pygame # nya uwu
import sys #meowww mmfghh

pygame.init()
pygame.font.init()
widthity = 800
heightity = 600
screen = pygame.display.set_mode((widthity, heightity))
pygame.display.set_caption("My First Pygame Window")

screen.fill((255,255,255))

my_font = pygame.font.Font(None, 36)
text_surface = my_font.render("MEOWWW", True, (0,0,0))
screen.blit(text_surface, (400,300))
title_rect = text_surface.get_rect()
title_rect.center = (400, 300)


dvd_rect = pygame.Rect(0,0,40,40)
dvd_color = (0, 0,255)
dvd_speed_y = 1
dvd_speed_x = 1

button_rect = pygame.Rect(0,0 , 200, 60)
button_color = (0,255,0)
button_text = my_font.render("BUTTON", True, (0,0,0))
button_text_rect = button_text.get_rect()

sensor_rect = pygame.Rect(0,0,400,120)
sensor_color = (255,0,0)
sensor_text = my_font.render("SENSOR", True, (0,0,0))
sensor_text_rect = sensor_text.get_rect()

button_rect.center = (400, 540)
sensor_rect.center = (400, 180)
dvd_rect.center = (100, 100)

clock = pygame.time.Clock()
bg_color = (255, 255, 255)

sensor_text_rect.center = sensor_rect.center
button_text_rect.center = button_rect.center


pygame.display.flip()




Nya = True
while Nya:
    mouse_pos = pygame.mouse.get_pos()
    pygame.draw.rect(screen, button_color, button_rect)
    pygame.draw.rect(screen, sensor_color, sensor_rect)
    pygame.draw.rect(screen, dvd_color, dvd_rect)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Nya = False
        if event.type == pygame.KEYDOWN:
            screen.fill((123,123,123))
            pygame.display.flip()
        if event.type == pygame.KEYUP:
            screen.fill((200, 150, 200))
            pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 1 means Left Click
                if button_rect.collidepoint(mouse_pos):
                    button_color = (150,255,150)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # 1 means Left Click
                button_color = (0,255,0)
    if sensor_rect.collidepoint(mouse_pos) or sensor_rect.colliderect(dvd_rect):
            sensor_color = (255,150,150)
    if not sensor_rect.collidepoint(mouse_pos) and not sensor_rect.colliderect(dvd_rect):
            sensor_color = (255,0,0)
    if dvd_rect.colliderect(sensor_rect):
        dvd_color = (150, 150, 255)
    else:
        dvd_color = (0, 0, 255)

    dvd_rect.y += dvd_speed_y
    dvd_rect.x += dvd_speed_x
    if dvd_rect.bottom >= heightity or dvd_rect.top <= 0:
        dvd_speed_y *= -1
    if dvd_rect.right >= widthity or dvd_rect.left <= 0:
        dvd_speed_x *= -1


    screen.fill(bg_color)
    screen.blit(text_surface, title_rect)
    pygame.draw.rect(screen, button_color, button_rect)
    pygame.draw.rect(screen, sensor_color, sensor_rect)
    pygame.draw.rect(screen, dvd_color, dvd_rect)
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(sensor_text, sensor_text_rect)
    screen.blit(button_text, button_text_rect)


    pygame.display.flip()

pygame.quit()
sys.exit()