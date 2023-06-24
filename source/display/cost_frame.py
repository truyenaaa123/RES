from source.setting import *
from source.display.support import *
from source.core.database import*
import pygame

class CostFrame():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.cost = {}
        self.create_cos_frame()

    def create_cos_frame(self):
        self.cost[1] = import_image_sheet("texture/hud.png", SIZE_CHAM_FRAME, NO_COLOR_KEY, POS_CUT_1COST)
        self.cost[2] = import_image_sheet("texture/hud.png", SIZE_CHAM_FRAME, NO_COLOR_KEY, POS_CUT_2COST)
        self.cost[3] = import_image_sheet("texture/hud.png", SIZE_CHAM_FRAME, NO_COLOR_KEY, POS_CUT_3COST)
        self.cost[4] = import_image_sheet("texture/hud.png", SIZE_CHAM_FRAME, NO_COLOR_KEY, POS_CUT_4COST)
        self.cost[5] = import_image_sheet("texture/hud.png", SIZE_CHAM_FRAME, NO_COLOR_KEY, POS_CUT_5COST)

class ChampionSurface():
    def __init__(self):
        self.list_cham_surf = {}
        self.create_list_cham_surf()

    def create_list_cham_surf(self):
        database = Database()
        for idx in database.list_champion.keys():
            for cham in database.list_champion[idx]:
                self.list_cham_surf[cham.name] = import_image_sheet("texture/champion/"+cham.name+".png", (207, 120), NO_COLOR_KEY, (0,0), size_cut=(256,128))


class ChampionShopFrame():
    def __init__(self, name_cham, cost, cost_frame:CostFrame, list_cham_surf:ChampionSurface):
        self.name_cham = name_cham
        self.cost = cost
        self.cost_frame = cost_frame
        self.list_cham_surf = list_cham_surf.list_cham_surf
        self.create_cham_frame()
    
    def create_cham_frame(self):
        cham = self.list_cham_surf[self.name_cham]
        rect_cham = self.cost_frame.cost[self.cost].get_rect(topleft= (4,4))
        self.cham_frame_surf = pygame.Surface((215, 161)).convert_alpha() 
        self.cham_frame_surf.blit(cham, rect_cham)
        self.cham_frame_surf.blit(self.cost_frame.cost[self.cost], (0,0))

class ChampionBenchFrame():
    def __init__(self, name_cham, star, list_cham_surf:ChampionSurface):
        self.name_cham = name_cham
        self.star = star
        self.list_cham_surf = list_cham_surf.list_cham_surf
        self.create_cham_bench_frame()
    
    def create_cham_bench_frame(self):
        radius = 50
        width, height = radius * 2, radius * 2
        circle_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.circle(circle_surface, (255, 255, 255), (radius, radius), radius)
        self.cham_bench_surf = pygame.Surface((width, height), pygame.SRCALPHA)
        self.cham_bench_surf.blit(circle_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MAX)
        self.cham_bench_surf.blit(self.list_cham_surf[self.name_cham], (-90, 0), special_flags=pygame.BLEND_RGBA_MIN)
        self.cham_bench_surf = pygame.transform.scale(self.cham_bench_surf, (70,70))

    