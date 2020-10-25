from vector import Vector2
from pygame import *
import pygame

class Component:
    def __init__(self, gameobject):
        self.gameobject = gameobject

    def update(self):
        pass

class Transform(Component):
    def __init__(self, position, scale, rotation):
        self.position = position
        self.scale = scale
        self.rotation = rotation

class SpriteRenderer(Component):
    screen = None
     
    def __init__(self, gameobject, sprite):
        super().__init__(gameobject)
        self.sprite = sprite
        self.sprite_size = Vector2(self.sprite.get_size()[0], self.sprite.get_size()[1])

    def update(self):
        self.sprite = pygame.transform.scale(self.sprite, (int(self.sprite_size.x * self.gameobject.transform.scale.x), int(self.sprite_size.y * self.gameobject.transform.scale.y)))
        self.render()

    def render(self):
        SpriteRenderer.screen.blit(self.sprite, self.gameobject.transform.position.tuple())

