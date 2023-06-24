from source.setting import *
from source.display.support import *
import pygame

class Frame():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.create_frame()

    def create_frame(self):
        self.bg = pygame.image.load("texture/Shurima_Arena.jpeg").convert_alpha()
        self.bg = pygame.transform.scale(self.bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.shop = import_image_sheet("texture/hud.png", SIZE_SHOP_FRAME, NO_COLOR_KEY, POS_CUT_SHOP_FRAME)
        self.exp_bar = import_image_sheet("texture/hud.png", SIZE_EXP_BAR, NO_COLOR_KEY, POS_CUT_EXP_BAR)
        self.unlock = import_image_sheet("texture/hud.png", SIZE_UNLOCK, NO_COLOR_KEY, POS_CUT_UNLOCK)
        self.lock = import_image_sheet("texture/hud.png", SIZE_LOCK, NO_COLOR_KEY, POS_CUT_LOCK)
        self.money_bar = import_image_sheet("texture/hud.png", SIZE_MONEY_BAR, NO_COLOR_KEY, POS_CUT_MONEY_BAR)

    def update(self):
        self.display_surface.blit(self.shop, ((SCREEN_WIDTH-1371)//2,SCREEN_HEIGHT-184))
        self.display_surface.blit(self.money_bar, ((SCREEN_WIDTH - 190)//2,SCREEN_HEIGHT-184-47))
        self.display_surface.blit(self.exp_bar, ((SCREEN_WIDTH-1371)//2 +1,SCREEN_HEIGHT-184 -45))
        self.display_surface.blit(self.unlock, ((SCREEN_WIDTH+1371)//2 -88,SCREEN_HEIGHT-184 -38))
    
    def draw_background(self):
        self.display_surface.blit(self.bg, (0,0))
    
    