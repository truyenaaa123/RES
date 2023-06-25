import pygame

def import_image_sheet(path, size, colorkey,topleft =(0,0), scale = 1, rotation = 0, size_cut= 0):
    if size_cut == 0:
        size_cut = size
    sheet = pygame.image.load(path).convert_alpha()
    image_surf = pygame.Surface(size_cut, pygame.SRCALPHA).convert_alpha() 
    image_surf.blit(sheet, (0,0), (topleft[0], topleft[1], size_cut[0], size_cut[1]))
    image_surf = pygame.transform.scale(image_surf, (int(size[0]*scale), int(size[1]*scale)))
    image_surf = image_surf.subsurface(pygame.Rect(0, 0, int(size[0]*scale), int(size[1]*scale)))
    image_surf = pygame.transform.rotate(image_surf, rotation)
    image_surf.set_colorkey(colorkey)
    return image_surf

