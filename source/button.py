import pygame
from source.core.player import *
from source.core.shop import *
from source.display.cost_frame import *
from source.display.cost_frame import pygame
from source.display.effect import *
list_name_cham = lambda list: [o.name if o != None else None for o in list]
list_star_cham = lambda list: [o.star if o != None else None for o in list]
  
class Button():
    def __init__(self, x, y, surface:pygame.surface.Surface, key_interact = pygame.K_HELP):
        width = surface.get_width()
        height = surface.get_height()
        self.display_surface = pygame.display.get_surface()
        self.surface = surface
        self.temp_surface = None
        self.rect = self.surface.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.key_interact = key_interact

    def update(self, keys = {pygame.K_HELP: 0}):
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


class ButtonShopChampion(Button):
    def __init__(self, x, y, cham_name, surface: pygame.surface.Surface, effect_button: EffectSurface, key_interact=pygame.K_HELP):
        super().__init__(x, y, surface, key_interact)
        width = surface.get_width()
        height = surface.get_height()
        self.font = pygame.font.Font("texture/GillSansMTPro-Medium.otf", 18)
        text_surface = self.font.render(str(cham_name), True, (255, 255, 255))
        self.surface.blit(text_surface, (10, 135))
        self.bg_surface = pygame.Surface((width + 4, height+ 4), pygame.SRCALPHA)
        # self.bg_surface.set_colorkey(NO_COLOR_KEY)
        self.temp_surface = None
        self.shine = effect_button.shine
        self.border_animation = effect_button.border_animation
        self.border_position = effect_button.border_position
        self.shine_frame_index = -90
        self.border_animation_frame_index = 0

    def update(self, player: Player, cham_name: str, keys = {pygame.K_HELP: 0}):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if (pygame.mouse.get_pressed()[0] == 1 or keys[self.key_interact] == 1) and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        list_same_cham_1_star = [cham for cham in player.list_cham if cham != None and cham.star == 1 and cham.name == cham_name]
        list_same_any_star = [cham for cham in player.list_cham if cham != None and cham.name == cham_name]
        
        if len(list_same_any_star) > 0:
            x = self.shine_frame_index
            y = self.shine_frame_index
            if (x>= 256) and (y>=256):
                self.shine_frame_index = -30

            width = self.bg_surface.get_width()
            height = self.bg_surface.get_height()

            if len(list_same_cham_1_star) > 1:
                if self.border_animation_frame_index == -360:
                    self.border_animation_frame_index = 0

                rotate_border_animation = pygame.transform.rotate(self.border_animation, self.border_animation_frame_index)
                rotate_border_animation.set_colorkey(NO_COLOR_KEY)
                rotate_border_position = rotate_border_animation.get_rect(center = self.border_position.center)
                self.bg_surface.blit(rotate_border_animation, rotate_border_position)

                rotate_border_animation2 = pygame.transform.rotate(self.border_animation, self.border_animation_frame_index+180)
                rotate_border_animation2.set_colorkey(NO_COLOR_KEY)
                rotate_border_position2 = rotate_border_animation2.get_rect(center = self.border_position.center)
                self.bg_surface.blit(rotate_border_animation2, rotate_border_position2)
                self.border_animation_frame_index -=1
            else:
                self.bg_surface = pygame.Surface((width, height), pygame.SRCALPHA)

            self.temp_surface = pygame.Surface((width, height), pygame.SRCALPHA)
            self.temp_surface.blit(self.shine, (x-100, y-100))
            self.shine_frame_index += 3


        
        final_surface = self.bg_surface.copy()
        final_surface.blit(self.surface, (2,2))
        if self.temp_surface == None:
            pass
            # final_surface.set_colorkey(NO_COLOR_KEY)
            # self.display_surface.blit(self.surface, (self.rect.x, self.rect.y))
        else:
            final_surface.blit(self.temp_surface, (0,0))
        self.display_surface.blit(final_surface, (self.rect.x, self.rect.y))
        self.temp_surface = None

        return action

