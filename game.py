import pygame
from pygame.locals import *
import gameobject
import component
from vector import Vector2

# initilize window
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
component.SpriteRenderer.screen = screen

#loading assets
petr = pygame.image.load("Assets/Sprites/Petr/PetrBase.png")
obj = gameobject.Gameobject("Petr", component.Transform(Vector2(200, 200), Vector2(5, 5), 0))
obj.add_componenet(component.SpriteRenderer(obj, petr))
velocity = 0

#game loop
while True:
    #clear screen
    screen.fill(0)

    #update gameobjects
    gameobject.Gameobject.update_all()

    #show render
    pygame.display.flip()
    
    #check for game window close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit(0)

        obj.transform.position.translate(Vector2(velocity, 0))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocity = -1
            elif event.key == pygame.K_RIGHT:
                velocity = 1

