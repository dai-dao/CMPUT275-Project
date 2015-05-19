"""
Common Names Used Throughout the Program's Files
"""

import pygame

pygame.init()
pygame.font.init()

# --- COLORS (Using RGB Codes)
WHITE = (255,255,255)
BLACK =  (0,0,0)
BROWN = (100,50,0)
GREEN1 = (0,200,0)
GREEN2 = (0,127,0)
TEAL = (0,100,100)
GREY1 = (200,200,200)
GREY2 = (100,100,100)
GREY3 = (50,50,50)
RED = (127,0,0)
RED2 = (200,0,0)
BLUE = (0,0,127)
PINK = (127,0,127)

#Fonts
Font = pygame.font.SysFont("DejaVu Sans",20)
BigFont = pygame.font.SysFont("DejaVu Sans",100)

# --- Sprites list

# List of every sprites
all_sprite = pygame.sprite.Group()

# List of unit blocks
block_list = pygame.sprite.Group()

# List of bullets
bullet_list = pygame.sprite.Group()

# Background image
bg = pygame.image.load('cave.gif')
