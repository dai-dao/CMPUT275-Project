from base_unit import BaseUnit
from names import *
import pygame
from rolldice import rollDie
from base_group import BaseGroup

class Minion(BaseUnit):
    """
    The Minion class
    """
    def __init__(self, **keywords):
        #load the base class
        super().__init__(**keywords)
        
        self.type = "Minion"
        self.cost = 1
        self.color = WHITE
        
    def set_type(self,number):
        """
        Sets the type of hero based on an inputted number
        """
        if number == 0:
            self.Goblin()
        
        if number == 1:
            self.Ork()

        if number == 2:
            self.Skeleton()

        if number == 3:
            self.Troll()

    def Goblin(self):
        """
        Turns the minion into a Goblin 
        """
        self.type = "Goblin"
        self.image = pygame.image.load("Goblin.gif")
        self.cost = 1
        self.health = 20
        self.max_health = self.health
        self.base_damage = 1 
        self.damagedice = (3,2)
        self.base_defense = 1
        self.defensedice = (2,1)
        self.color = BROWN
        self.activate()

    def Ork(self):
        """
        Turns the minion into an Ork
        """
        self.type = "Ork"
        self.image = pygame.image.load("Ork.gif")
        self.cost = 2
        self.health = 40
        self.max_health = self.health
        self.base_damage = 3
        self.damagedice = (4,2)
        self.base_defense = 1
        self.defensedice = (3,1)
        self.color = GREEN1
        self.activate()

    def Troll(self):
        """
        Turns the minion into a Troll
        """
        self.type = "Troll"
        self.image = pygame.image.load("Troll.gif")
        self.cost = 4
        self.health = 60
        self.max_health = self.health
        self.base_damage = 6 
        self.damagedice = (3,2)
        self.base_defense = 2
        self.defensedice = (3,1)
        self.color = TEAL
        self.activate()

    def Skeleton(self):
        """
        Turns the minion into a Skeleton
        """
        self.type = "Skeleton"
        self.image = pygame.image.load("Skeleton.gif")
        self.bullet = pygame.image.load("ArrowLeft.gif")
        self.cost = 3
        self.health = 30
        self.max_health = self.health
        self.base_damage = 2 
        self.damagedice = (3,2)
        self.base_defense = 1
        self.defensedice = (3,1)
        self.attack_cap = 2
        self.ranged = True
        self.color = GREY1
        self.activate()

    def Value(self,enemies):
        """
        Returns the Value of the unit based on the composition of the enemy 
        party
        """
        if self.type == "Goblin":
            if "Bard" in enemies.inteam and not "Fighter" in enemies.inteam:
                return 2
            else:
                return 1

        if self.type == "Ork":
            if "Archer" in enemies.inteam or "Fighter" in enemies.inteam:
                return 3
            else:
                return 2
        if self.type == "Skeleton":
            if "Mage" in enemies.inteam or "Archer" in enemies.inteam:
                return 5
            else:
                return 3
            
        if self.type == "Troll":
            if "Fighter" in enemies.inteam and not "Mage" in enemies.inteam:
                return 7
            else:
                return 4

class Team(BaseGroup):
    """
    Class for a Team of Minions
    """
    def __init__(self):
        super().__init__()   
        self.maxsize = 2+rollDie(6)   
        self.side = 1 

    def reset(self):
        """
        Resets the Team to be empty and randomizes the maximum size
        """
        self.members = []
        self.membertypes = []
        self.size = 0
        self.maxsize = 2+rollDie(6)
        self.alive = True
