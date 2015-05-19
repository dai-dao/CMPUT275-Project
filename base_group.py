from base_unit import BaseUnit
import pygame
from rolldice import rollDie
from names import *

class BaseGroup():
    """
    The Base Class for Groups of Units
    """
    def __init__(self):
        self.members = []
        self.membertypes = []
        self.node = 0
        self.alive = True
        self.size = 0
        self.maxsize = 0
        self.side = 0
        
    def add(self,unit):
        """
        Adds unit to the Group
        """
        if self.size + unit.cost <= self.maxsize:
            self.members.append(unit)
            self.membertypes.append(unit.type)
            unit.team = self
            self.size += unit.cost 
            if not self.alive:
                self.alive = True
                
            return True
        else:
            return False

    def remove(self,unit):
        """
	Removes unit from the Group
	"""
        self.members.remove(unit)
        self.membertypes.remove(unit.type)
        self.size -= unit.cost

	#If Removing a Bard from the Group, adjust the boost levels of all members
        if unit.type == "Bard":
            self.bards -= 1
            for i in self.members:
                i.boost[1] -= 1

        unit.team = None
    
    @property
    def inteam(self):
        """
        Returns the members of the current team
        """
        return self.membertypes

    def status(self):
        """
        Checks if the group is still alive
        """
        temp = 0
        for i in self.members:
            if i.active:
                temp = 1
            else:
                self.remove(i)
                
        if temp == 0:
            self.alive = False
        
        return self.alive

    def drawGroup(self,screen):
        """
        Draws the Group on their side of the screen
        """
        screen.blit(bg,((300*self.side),0),((300*self.side),0,300,600))
   
        for i, member in enumerate(self.members):

            # Set unit's block coordinates
            member.rect.x = 50+(250*self.side)+((i//4)*180)
            member.rect.y = 100+((i%4)*100)

            # Draw the unit blocks
            screen.blit(member.image, (member.rect.x,member.rect.y))

            # Add the sprites to the list
            block_list.add(member)
            all_sprite.add(member)

            # Draw the health text of each units blocks
            health_text = Font.render("{}".format(member.health), True, RED2)
            screen.blit(health_text, member.rect)
