import pygame
import random
from source.setting import *
from source.core.shop import Shop
from source.core.player import Player
from source.core.statistical import Statistical
from source.button import *
from source.display.support import import_image_sheet
from source.display.frame import Frame
from source.display.cost_frame import *


class Level():
    def __init__(self) :
        # get display surface
        self.display_surface = pygame.display.get_surface()

        # Vẽ khung 
        self.frame = Frame()
        self.cost_frame = CostFrame()
        self.list_cham_surf = ChampionSurface()
        # System
        self.player = Player(LEVEL, STARTED_EXP, STARTED_GOLD)
        self.shop = Shop()
        self.shop.shop_refresh(LEVEL, self.player.list_3stars)
        # Tạo button
        self.create_button()
        self.refresh_shop()
        self.press_D = False
        # self.ui = UI()
        #Quay trờ lại màn hình chờ

    # Khởi tạo button
    def create_button(self):
        roll = import_image_sheet("texture/hud.png", SIZE_ROLL_FRAME, NO_COLOR_KEY, POS_CUT_ROLL_FRAME)
        buy_exp = import_image_sheet("texture/hud.png", SIZE_BUY_EXP_FRAME, NO_COLOR_KEY, POS_CUT_BUY_EXP_FRAME)
        self.roll_button = Button((SCREEN_WIDTH-1371)//2 +5+12,SCREEN_HEIGHT-184 + 15,roll)
        self.buy_exp_button = Button((SCREEN_WIDTH-1371)//2 +5+12,SCREEN_HEIGHT-184 + 15 + 77+8, buy_exp)

    # Trả về surface của khung cost tương ứng
    def refresh_shop(self):
        self.shop.shop_refresh(self.player.level, self.player.list_3stars)
        self.shop_button = {}
        for idx, cham in enumerate(self.shop.shop_list):
            cham_frame_surf = ChampionFrame(cham.name, cham.cost,self.cost_frame, self.list_cham_surf).cham_frame_surf
            self.shop_button[idx] = ChampionButton((SCREEN_WIDTH-1371)//2 +465-225+7*(idx+1)+215*idx,SCREEN_HEIGHT-184 + 15,cham_frame_surf)
        
    # Vẽ và kiểm tra button đã click chưa
    def button_update(self):
        # Refresh và vẽ shop khi ấn vào button Roll hoặc ấn nút D
        keys = pygame.key.get_pressed()
        if self.roll_button.update() or (keys[pygame.K_d] and self.press_D == False):
            self.press_D = True
            self.refresh_shop()
            print("Shop")
        if keys[pygame.K_d] == 0:
            self.press_D = False
            
        #  Mua EXP khi ấn nút Mua exp hoặc ấn nút F
        if self.buy_exp_button.update():
            print("Buy EXP")
        for button_shop in self.shop_button.values():
            if button_shop.update():
                print("Button Shop")

    def run(self):
        # process the game
        # update funtion
        self.frame.update()
        self.button_update()
        



        