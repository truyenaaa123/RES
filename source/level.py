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
list_name_cham = lambda list: [o.name if o != None else None for o in list]
list_star_cham = lambda list: [o.star if o != None else None for o in list]
    

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

        # Tạo button
        self.create_button()
        self.refresh_shop()
        self.press_D = False
        self.press_E = False
        self.bench_button = {}
        # self.ui = UI()
        #Quay trờ lại màn hình chờ

    # Khởi tạo button
    def create_button(self):
        roll = import_image_sheet("texture/hud.png", SIZE_ROLL_FRAME, NO_COLOR_KEY, POS_CUT_ROLL_FRAME)
        buy_exp = import_image_sheet("texture/hud.png", SIZE_BUY_EXP_FRAME, NO_COLOR_KEY, POS_CUT_BUY_EXP_FRAME)
        self.roll_button = Button((SCREEN_WIDTH-1371)//2 +5+12,SCREEN_HEIGHT-184 + 15,roll)
        self.buy_exp_button = Button((SCREEN_WIDTH-1371)//2 +5+12,SCREEN_HEIGHT-184 + 15 + 77+8, buy_exp)

    # Trả về surface của khung cost tương ứng trên shop và refresh shop
    def refresh_shop(self):
        self.shop.shop_refresh(self.player.level, self.player.list_3stars)
        self.shop_button = {}
        for idx, cham in enumerate(self.shop.shop_list):
            if cham != None:
                cham_frame_surf = ChampionShopFrame(cham.name, cham.cost,self.cost_frame, self.list_cham_surf).cham_frame_surf
                self.shop_button[idx] = Button((SCREEN_WIDTH-1371)//2 +465-225+7*(idx+1)+215*idx,SCREEN_HEIGHT-184 + 15,cham_frame_surf)
    
    # 
    def create_all_bench_button(self, idx_shop):
        self.bench_button = {}
        for idx, cham in enumerate(self.player.list_cham):
            if cham != None:
                cham = self.player.list_cham[idx]
                cham_bench_surf = ChampionBenchFrame(cham.name, cham.star, self.list_cham_surf).cham_bench_surf
                self.bench_button[idx] = Button(318 + 100*(idx%9),623 - 100*(idx//9),cham_bench_surf, pygame.K_e)
            else: self.bench_button[idx] = None

    # Vẽ và kiểm tra button đã click chưa
    def button_update(self):
        # Refresh và vẽ shop khi ấn vào button Roll hoặc ấn nút D
        keys = pygame.key.get_pressed()
        if self.roll_button.update() or (keys[pygame.K_d] and self.press_D == False):
            self.press_D = True
            self.refresh_shop()
        if keys[pygame.K_d] == 0:
            self.press_D = False
            
        #  Mua EXP khi ấn nút Mua exp hoặc ấn nút F
        if self.buy_exp_button.update():
            print("Buy EXP")
        for idx in range(5):
            if self.shop.shop_list[idx] == None and idx in self.shop_button:
                self.shop_button[idx] = None
            elif idx in self.shop_button and self.shop_button[idx].update():
                num_none_shop = self.shop.shop_list.count(None)
                self.player.pick_champion(self.shop, idx)
                if num_none_shop != self.shop.shop_list.count(None):
                    self.create_all_bench_button(idx)

        
        for idx in range(len(self.player.list_cham)):
            if self.player.list_cham[idx] == None and idx in self.bench_button:
                self.bench_button[idx] = None
            elif idx in self.bench_button and self.bench_button[idx].update(keys):
                # print("Sell")
                # if (keys[pygame.K_e] and self.press_E == False):
                    print("Sell")
                    self.press_E = True
                    self.player.sell_champion(self.shop, idx)
            if keys[pygame.K_e] == 0:
                self.press_E = False

    def run(self):
        # process the game
        # update funtion

        self.frame.draw_background()
        self.frame.update()
        self.button_update()

        



        