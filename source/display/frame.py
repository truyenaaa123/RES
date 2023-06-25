from source.setting import *
from source.display.support import *
from source.core.player import *
import pygame

class Frame():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font("texture/GillSansMTPro-Medium.otf", 20)
        self.create_frame()

    def create_frame(self):
        self.bg = pygame.image.load("texture/Shurima_Arena.jpeg").convert_alpha()
        self.bg = pygame.transform.scale(self.bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.shop = import_image_sheet("texture/hud.png", SIZE_SHOP_FRAME, NO_COLOR_KEY, POS_CUT_SHOP_FRAME)
        self.exp_bar = import_image_sheet("texture/hud.png", SIZE_EXP_BAR, NO_COLOR_KEY, POS_CUT_EXP_BAR)
        self.unlock = import_image_sheet("texture/hud.png", SIZE_UNLOCK, NO_COLOR_KEY, POS_CUT_UNLOCK)
        self.lock = import_image_sheet("texture/hud.png", SIZE_LOCK, NO_COLOR_KEY, POS_CUT_LOCK)
        self.money_bar = import_image_sheet("texture/hud.png", SIZE_MONEY_BAR, NO_COLOR_KEY, POS_CUT_MONEY_BAR)
        self.gold_icon = import_image_sheet("texture/hud.png", (15,14), NO_COLOR_KEY, (346,398))


    def update(self):
        self.display_surface.blit(self.shop, ((SCREEN_WIDTH-1371)//2,SCREEN_HEIGHT-184))
        self.display_surface.blit(self.unlock, ((SCREEN_WIDTH+1371)//2 -88,SCREEN_HEIGHT-184 -38))
    
    def draw_background(self):
        self.display_surface.blit(self.bg, (0,0))
    
    def draw_gold_lv_bar(self, player:Player):
        self.display_surface.blit(self.exp_bar, ((SCREEN_WIDTH-1371)//2 +1,SCREEN_HEIGHT-184 -45))
        text_surface = self.font.render("Lvl. "+ str(player.level), True, (255, 255, 255))
        self.display_surface.blit(text_surface,((SCREEN_WIDTH-1371)//2 +1 + 20,SCREEN_HEIGHT-184 -45 + 20))
        text_surface = self.font.render(str(player.exp) + "/" + str(player.database.exp_size[player.level]), True, (255, 255, 255))
        self.display_surface.blit(text_surface,((SCREEN_WIDTH-1371)//2 +1 + 150,SCREEN_HEIGHT-184 -45 + 20))

        self.display_surface.blit(self.money_bar, ((SCREEN_WIDTH - 190)//2,SCREEN_HEIGHT-184-47))
        text_surface = self.font.render(str(player.gold), True, (255, 255, 255))
        self.display_surface.blit(self.gold_icon, ((SCREEN_WIDTH - 190)//2 + 70,SCREEN_HEIGHT-184-47 + 22))
        self.display_surface.blit(text_surface, ((SCREEN_WIDTH - 190)//2 + 90,SCREEN_HEIGHT-184-47 + 22))




    
    