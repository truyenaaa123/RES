from source.setting import *
from source.display.support import *
import pygame

class EffectSurface():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.create_effect()

    def create_effect(self):
        self.shine = import_image_sheet("texture/glow.png", (256, 256), NO_COLOR_KEY, (0,0))
        image_width, image_height = self.shine.get_size()
        for x in range(image_width):
            for y in range(image_height):
                self.shine.set_at((x, y), (255,255,255, max(self.shine.get_at((x,y))[0], 0)))
        self.shine.set_alpha(180)
        self.shine.set_colorkey((0,0,0))

        self.border_animation = import_image_sheet("texture/border1.png", (256,256), NO_COLOR_KEY, (0,0), scale=1.1)
        self.border_position = self.border_animation.get_rect(center= (219//2, 165//2))

