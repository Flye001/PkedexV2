import time
import pygame

#usrtext = raw_input("Do some shit: ")

pygame.init()
screen = pygame.display.set_mode((800,480))

screen.fill((0,255,0))

pygame.font.init()
myfont= pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render("Welcome to my Pokedex", False, (0, 0, 0))
screen.blit(textsurface,(20,20))
#screen.fill((0,255,0))
#pygame.Surface.fill((2555,0,0))

pygame.display.update()
time.sleep(15)
pygame.quit()
