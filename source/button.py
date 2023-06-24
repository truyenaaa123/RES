import pygame
from source.core.player import *
from source.core.shop import *
from source.display.cost_frame import *

class Button():
    def __init__(self, x, y, surface:pygame.surface.Surface, key_interact = pygame.K_HELP):
        width = surface.get_width()
        height = surface.get_height()
        self.display_surface = pygame.display.get_surface()
        self.surface = surface
        self.rect = self.surface.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.key_interact = key_interact

    def click(self, keys):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if (pygame.mouse.get_pressed()[0] == 1 or keys[self.key_interact] == 1) and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        self.display_surface.blit(self.surface, (self.rect.x, self.rect.y))

        return action

    def update(self, keys = {pygame.K_HELP: 0}):
        return self.click(keys)
    
class ChampionShopButton(Button):
    def __init__(self, x, y, surface: pygame.surface.Surface, pos_shop):
        super().__init__(x, y, surface)
        self.pos_shop = pos_shop

    def update(self, shop:Shop):
        action = self.click()
        if action:
            self.cham = shop.shop_list[self.pos_shop]
            # player.pick_champion(shop, self.pos_shop)
        return action

class ChampionBenchButton(Button):
    def __init__(self, x, y, surface: pygame.surface.Surface):
        super().__init__(x, y, surface)
        # self.pos_bench = pos_bench

    def update(self, shop:Shop, player:Player):
        action = self.click()
        if action:
            print("bench")
        return action


