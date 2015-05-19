import pygame
from pygame.sprite import Sprite 
from math import *
from names import *

class Bullet(Sprite):
    """
    This class represents the bullet from a ranged attack.
    """
    def __init__(self,shooter):
        super().__init__()
        self.image = shooter.bullet
        self.rect = self.image.get_rect()
    
    def erase(self,screen):
        """
        Removes the bullet from the screen
        """
        screen.blit(bg,(self.rect.x,self.rect.y), (self.rect.x,self.rect.y,20,20))
        

    def update(self, target):
        """
        Moves the bullet towards the target
        """
        
        # Distance between self and target
        dx = (target.rect.x + target.rect.width//2-self.rect.x)
        dy = (target.rect.y + target.rect.height//2-self.rect.y)
        distance = sqrt(dx*dx+dy*dy)
        
        t = 5/distance
        self.rect.x = self.rect.x + t*dx
        self.rect.y = self.rect.y + t*dy
