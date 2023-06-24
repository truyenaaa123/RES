import pygame

class Button():
    def __init__(self, x, y, surface:pygame.surface.Surface):
        width = surface.get_width()
        height = surface.get_height()
        self.display_surface = pygame.display.get_surface()
        self.surface = surface
        self.rect = self.surface.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def click(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        self.display_surface.blit(self.surface, (self.rect.x, self.rect.y))

        return action

    def update(self):
        return self.click()
    
class ChampionButton(Button):
    def __init__(self, x, y, surface: pygame.surface.Surface):
        super().__init__(x, y, surface)

