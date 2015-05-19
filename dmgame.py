import pygame
from gui import Interface
from party import Hero, Party
from minions import Minion, Team
from names import *

pygame.init()
pygame.font.init()

nodes = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
nodepos = [(300,650),(300,575),(130,525),(350,480),(450,520),(220,440),(50,400),(550,430),(400,400),(300,370),(170,330),(500,310),(100,250),(280,260),(380,230),(140,150),(250,150),(430,140),(300,70),(300,0)]

edges = [(0,1),(1,2),(1,3),(1,4),(1,5),(2,5),(2,6),(2,10),(3,5),(3,8),(3,9),(4,7),(4,8),(4,11),(5,6),(5,9),(5,10),(6,10),(6,12),(7,8),(7,11),(8,9),(8,11),(8,13),(8,14),(9,10),(9,13),(9,14),(10,12),(10,16),(11,14),(11,17),(12,15),(12,16),(13,16),(13,14),(13,15),(14,16),(14,17),(14,18),(15,16),(15,18),(16,18),(17,18),(18,19)]

Heroes = Party()
#Generates a Party
Heroes.MakeParty()

Minions = Team()

GUI = Interface(800,600,"Dungeon Master",nodes,nodepos,edges,Heroes,Minions)
done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if (event.type == pygame.MOUSEBUTTONUP and event.button == 1 and pygame.mouse.get_focused()):
            GUI.on_click(event)
        if (event.type == pygame.MOUSEMOTION and pygame.mouse.get_focused()):
            GUI.on_hover(event)

    #Updates the screen
    GUI.screen_update()

    clock.tick(60)
