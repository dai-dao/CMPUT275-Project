from base_unit import BaseUnit
from names import *
import pygame
from rolldice import rollDie
from base_group import BaseGroup

class Hero(BaseUnit):
    """
    The Hero class
    """
    def __init__(self, **keywords):
        #load the base class
        super().__init__(**keywords)

        self.type = "Hero"
        self.color = GREY1
 
    def set_type(self,number):
        """
        Sets the type of hero based on an inputted number
        """
        if number == 0:
            self.Fighter()
        
        if number == 1:
            self.Archer()

        if number == 2:
            self.Mage()
            
        if number == 3:
            self.Bard()
        
    def Fighter(self):
        """
        Turns the Hero into a Fighter
        """
        self.type = "Fighter"
        self.image = pygame.image.load("Fighter.gif")
        self.health = 100
        self.max_health = self.health
        self.base_damage = 4 
        self.damagedice = (4,2)
        self.base_defense = 2
        self.defensedice = (3,1)
        self.color = RED
        self.activate()

    def Archer(self):
        """
        Turns the Hero into an Archer
        """
        self.type = "Archer"
        self.image = pygame.image.load("Archer.gif")
        self.bullet = pygame.image.load("ArrowRight.gif")
        self.health = 70
        self.max_health = self.health
        self.base_damage = 2
        self.damagedice = (3,2)
        self.attack_cap = 2
        self.ranged = True
        self.base_defense = 2
        self.defensedice = (2,1)
        self.color = GREEN2
        self.activate()

    def Mage(self):
        """
        Turns the Hero into a Mage
        """
        self.type = "Mage"
        self.image = pygame.image.load("Mage.gif")
        self.bullet = pygame.image.load("Fireball.gif")
        self.health = 50
        self.max_health = self.health
        self.base_damage = 3
        self.damagedice = (2,2)
        self.attack_cap = 4
        self.ranged = True
        self.base_defense = 1
        self.defensedice = (2,1)
        self.color= BLUE
        self.activate()

    def Bard(self):
        """
        Turns the Hero into a Bard
        """
        self.type = "Bard"
        self.image = pygame.image.load("Bard.gif")
        self.health = 60
        self.max_health = self.health
        self.base_damage = 3
        self.damagedice = (3,2)
        self.base_defense = 1
        self.defensedice = (3,1)
        self.color = PINK
        self.activate()


class Party(BaseGroup):
    """
    The Class for the Party of Heroes
    """
    def __init__(self):
        super().__init__()
        
        #There are 4 members in the Party
        self.maxsize = 4

        #Tracks the number of Bards in the party that give damage boosts
        self.bards = 0
        self.side = 0

    def MakeParty(self):
        """
        Creates a random Four Team Membered Party
        """
        for i in range(self.maxsize):
            hero = Hero()
            hero.set_type(rollDie(4,1)-1)
            if hero.type == "Bard":
                self.bards += 1
            self.add(hero)

        #For each Bard in the party, every member gains a boost in damage
        for i in self.members:
            for j in range(self.bards):
                i.boost[1] += 1

        #Sets the Party to be at Node 1
        self.node = 1

    def party_node(self):
        """
        Returns the node the party is at
        """
        return self.node

    def move_party(self, newnode):
        """
        Moves the party to a new node
        """
        self.node = newnode
