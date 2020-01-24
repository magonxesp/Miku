from pygame.sprite import Sprite, Group
from miku.animation import MikuIdleAnimation
import pygame


class MikuSprite(Sprite):

    def __init__(self):
        super().__init__()
        self.idle_animation = MikuIdleAnimation()
        self.idle_animation.speed = 1
        self.image = None
        self.rect = pygame.Rect(10, 10, 100, 100)

    def update(self, *args):
        _image = self.idle_animation.play()
        image_rect = _image.get_rect()
        self.rect.width = image_rect.width
        self.rect.height = image_rect.height
        self.image = _image


sprite_group = Group()
sprite_group.add(MikuSprite())
