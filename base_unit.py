import pygame
from pygame.sprite import Sprite
from rolldice import rollDie
from bullet import Bullet
from names import *

# Class Definitions
class BaseUnit(Sprite):
    """
    The basic representation of a unit from which all other unit types
    extend. 
    """
    active_units = pygame.sprite.LayeredUpdates()
    
    def __init__(self,
                 team = None,
                 node = None,
                 activate = False,
                 **keywords):

        Sprite.__init__(self)
        
        self.team = team
        self.node = node
        self._moving = False
        self._active = False
        self._path = []
        
        #Default unit stats
        self.health = 10
        self.ranged = False
        self.max_health = self.health
        self.attack_cap = 1
        self.base_damage = 1
        self.damagedice = (1,1)
        self.base_defense = 1
        self.defensedice = (1,1)
        self.boost = [2,0]
        self.cost = 1
        self.type = "Base Unit"

        # Set unit block attributes
        self.image = pygame.Surface([80,80])
        self.rect = self.image.get_rect()
    
        
        if activate:
            self.activate()
    
    @property
    def active(self):
        """
        Returns whether this is active.
        """
        return self._active
    

    def update(self, screen, target):
        """
        Update the unit's image after movements
        """
        # Move the block to the target for melee attack"

        # Re-fill the block
        screen.blit(bg,(self.rect.x,self.rect.y), (self.rect.x,self.rect.y,80,80))

        # For x coordinate
        if self.rect.x > target.rect.x:
            self.rect.x = target.rect.x + 90
        elif self.rect.x < target.rect.x:
            self.rect.x = target.rect.x - 90

        # For y coordinate
        self.rect.y = target.rect.y 


    def activate(self):
        """
        Adds this unit to the active roster.
        """
        if not self._active:
            self._active = True
    
    def deactivate(self):
        """
        Removes this unit from the active roster.
        """
        if self._active:
            self._active = False

    def hurt(self, damage):
        """
        Causes damage to the unit, and destroys it when it's out of health.
        """
        self.health -= damage
        
        # Dead!
        if self.health <= 0:
            self.deactivate()
            self.team.remove(self)
        
    def get_damage(self, target):
        """
        Returns the potential attack damage against a given enemy.
        """

        # Get the unit's current defense.
        defense = target.get_defense()

        damage = self.base_damage +rollDie(self.boost[0], self.boost[1]) + rollDie(self.damagedice[0], self.damagedice[1])- defense
        
        # Don't do negative damage
        if damage <= 0:
            return 0
        
        return damage
        
    def get_defense(self):
        """
        Returns this unit's defense.
        """
        return self.base_defense + rollDie(self.defensedice[0],self.defensedice[1])
        
        
    def attack(self, target):
        damage = self.get_damage(target)
        if damage:
            target.hurt(damage)
 
        return damage
        
