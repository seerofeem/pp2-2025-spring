import pygame
import math
import time

pygame.init()

WIDTH, HEIGHT = 800, 800
CENTER = (WIDTH // 2, HEIGHT // 2)
FPS = 60

right_hand = pygame.image.load("C:\\Users\\Arsen\\Desktop\\pp2\\lab7\\arrow.png") 
clock_face = pygame.image.load("C:\\Users\\Arsen\\Desktop\\pp2\\lab7\\clocks.png")  
left_hand = pygame.image.load("C:\\Users\\Arsen\\Desktop\\pp2\\lab7\\arrow.png")  

clock_face = pygame.transform.scale(clock_face, (WIDTH, HEIGHT))
right_hand = pygame.transform.scale(right_hand, (50,300))  
left_hand = pygame.transform.scale(left_hand, (80, 150))  


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

def blit_rotate_center(surf, image, pos, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=pos)
    surf.blit(rotated_image, new_rect.topleft)

running = True
while running:
    screen.fill((255, 255, 255))  
    screen.blit(clock_face, (0, 0))  

    t = time.localtime()
    minutes = t.tm_min
    seconds = t.tm_sec


    minute_angle = - (minutes * 12)  
    second_angle = - (seconds * 12)  

    blit_rotate_center(screen, right_hand, CENTER, minute_angle)
    blit_rotate_center(screen, left_hand, CENTER, second_angle)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)

pygame.quit()
