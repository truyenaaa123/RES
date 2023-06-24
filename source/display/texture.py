from setting import *
from support import *
import pygame;


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

is_running = True
while (is_running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running= False
    bg = sheet = pygame.image.load("texture/Shurima_Arena.jpeg").convert_alpha()
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    cost_1 = import_image_sheet("texture/hud.png", SIZE_CHAM_FRAME, NO_COLOR_KEY, POS_CUT_1COST)
    cost_2 = import_image_sheet("texture/hud.png", SIZE_CHAM_FRAME, NO_COLOR_KEY, POS_CUT_2COST)
    cost_3 = import_image_sheet("texture/hud.png", SIZE_CHAM_FRAME, NO_COLOR_KEY, POS_CUT_3COST)
    cost_4 = import_image_sheet("texture/hud.png", SIZE_CHAM_FRAME, NO_COLOR_KEY, POS_CUT_4COST)
    cost_5 = import_image_sheet("texture/hud.png", SIZE_CHAM_FRAME, NO_COLOR_KEY, POS_CUT_5COST)
    shop = import_image_sheet("texture/hud.png", SIZE_SHOP_FRAME, NO_COLOR_KEY, POS_CUT_SHOP_FRAME)
    roll = import_image_sheet("texture/hud.png", SIZE_ROLL_FRAME, NO_COLOR_KEY, POS_CUT_ROLL_FRAME)
    buy = import_image_sheet("texture/hud.png", SIZE_BUY_EXP_FRAME, NO_COLOR_KEY, POS_CUT_BUY_EXP_FRAME)
    exp_bar = import_image_sheet("texture/hud.png", SIZE_EXP_BAR, NO_COLOR_KEY, POS_CUT_EXP_BAR)
    unlock = import_image_sheet("texture/hud.png", SIZE_UNLOCK, NO_COLOR_KEY, POS_CUT_UNLOCK)
    lock = import_image_sheet("texture/hud.png", SIZE_LOCK, NO_COLOR_KEY, POS_CUT_LOCK)
    money_bar = import_image_sheet("texture/hud.png", SIZE_MONEY_BAR, NO_COLOR_KEY, POS_CUT_MONEY_BAR)
    ahri = import_image_sheet("texture/Ahri.png", (207, 120), NO_COLOR_KEY, (0,0), size_cut=(256,128))
    image_surf = pygame.Surface((215, 161)).convert_alpha() 
    rect_ahri = cost_5.get_rect(topleft= (4,4))
    image_surf.blit(ahri, rect_ahri)
    image_surf.blit(cost_5, (0,0))
    screen.blit(bg, (0,0))
    screen.blit(shop, ((SCREEN_WIDTH-1371)//2,SCREEN_HEIGHT-184))
    screen.blit(money_bar, ((SCREEN_WIDTH - 190)//2,SCREEN_HEIGHT-184-47))
    screen.blit(exp_bar, ((SCREEN_WIDTH-1371)//2 +1,SCREEN_HEIGHT-184 -45))
    screen.blit(unlock, ((SCREEN_WIDTH+1371)//2 -88,SCREEN_HEIGHT-184 -38))
    # screen.blit(ahri, rect_ahri)
    screen.blit(cost_1, ((SCREEN_WIDTH-1371)//2 +465-225+7,SCREEN_HEIGHT-184 + 15))
    screen.blit(cost_2, ((SCREEN_WIDTH-1371)//2 +465-225+7*2+215,SCREEN_HEIGHT-184 + 15))
    screen.blit(cost_3, ((SCREEN_WIDTH-1371)//2 +465-225+7*3+215*2,SCREEN_HEIGHT-184 + 15))
    screen.blit(cost_4, ((SCREEN_WIDTH-1371)//2 +465-225+7*4+215*3,SCREEN_HEIGHT-184 + 15))
    screen.blit(image_surf, ((SCREEN_WIDTH-1371)//2 +465-225+7*5+215*4,SCREEN_HEIGHT-184 + 15))
    # screen.blit(ahri, ((SCREEN_WIDTH-1371)//2 +465-225+7*5+215*4+4,SCREEN_HEIGHT-184 + 15+4))
    screen.blit(roll, ((SCREEN_WIDTH-1371)//2 +5+12,SCREEN_HEIGHT-184 + 15))
    screen.blit(buy, ((SCREEN_WIDTH-1371)//2 +5+12,SCREEN_HEIGHT-184 + 15 + 77+8))
    pygame.display.update()

pygame.quit()