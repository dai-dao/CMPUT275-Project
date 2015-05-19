import pygame
import time
from gamegraph import GameGraph
from minions import Team, Minion
from party import Party, Hero
from rolldice import rollDie
from names import *
from matrix import Matrix, max_val_group
from bullet import Bullet

# Fight mode variables
FPS = 30
fpsTime = pygame.time.Clock()
sim_fight = True
win = False

class Modes:
    """
    Sets Values for each of the possible Screen Modes
    """
    Map, MakeTeam, Combat, GameOver = range(4)

class Interface():
    """
    Graphical User Interface for the Game
    """
    def __init__(self,width,height,name,nodes,nodepos,edges,party,team):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption(name)
        self.mode = Modes.Map
        self.nodes = nodes
        self.nodepos = nodepos
        self.edges = edges
        self.map = GameGraph(nodes,nodepos,edges,self.screen)
        self.party = party
        self.team = team
        self.show_min = None
        
    def change_mode(self, newmode):
        """
        Changes the Interface mode to newmode
        """
        self.mode = newmode
        pygame.draw.rect(self.screen,BLACK,pygame.Rect(0,0,self.width,self.height))

    def auto_team(self):
        """
        Creates the strongest possible team of minions based on the party
        composition and maximum team size
        """
        cap = self.team.maxsize - self.team.size
        poss_min = []
        num_guys = []
        num_types = 4
        type_costs = [1,2,3,4]
        
        for i in range(num_types):
            num_guys.append(cap//type_costs[i])
        
        costs = list()
        values = list()

        index = 0

        for i in range(num_types):
            for k in range(num_guys[i]):
                poss_min.append(None)
                poss_min[index] = Minion()
                poss_min[index].set_type(i)
                costs.append(poss_min[index].cost)
                values.append(poss_min[index].Value(self.party))
                index += 1

        best_team = max_val_group(cap,costs,values)

        for h, val in enumerate(best_team):
            if val == 1:
                self.team.add(poss_min[h])

    def draw_info(self,minion):
        pygame.Rect(625,200,150,150)
        if minion.type == "Goblin":
            NameText = Font.render(minion.type, True, WHITE)
            HealthText = Font.render("Health: {}".format(minion.health), True, WHITE)
            StrengthText = Font.render("Low Damage", True, WHITE)
            self.screen.blit(NameText, pygame.Rect(630,200,150,20))
            self.screen.blit(HealthText, pygame.Rect(630,220,150,20))
            self.screen.blit(StrengthText, pygame.Rect(630,240,150,20))

        if minion.type == "Ork":
            NameText = Font.render(minion.type, True, WHITE)
            HealthText = Font.render("Health: {}".format(minion.health), True, WHITE)
            StrengthText = Font.render("Med Damage", True, WHITE)
            self.screen.blit(NameText, pygame.Rect(630,200,150,20))
            self.screen.blit(HealthText, pygame.Rect(630,220,150,20))
            self.screen.blit(StrengthText, pygame.Rect(630,240,150,20))

        if minion.type == "Skeleton":
            NameText = Font.render(minion.type, True, WHITE)
            HealthText = Font.render("Health: {}".format(minion.health), True, WHITE)
            StrengthText = Font.render("Med Damage", True, WHITE)
            RangedText = Font.render("2 Attacks", True, WHITE)
            self.screen.blit(NameText, pygame.Rect(630,200,150,20))
            self.screen.blit(HealthText, pygame.Rect(630,220,150,20))
            self.screen.blit(StrengthText, pygame.Rect(630,240,150,20))
            self.screen.blit(RangedText, pygame.Rect(630,260,80,20))

        if minion.type == "Troll":
            NameText = Font.render(minion.type, True, WHITE)
            HealthText = Font.render("Health: {}".format(minion.health), True, WHITE)
            StrengthText = Font.render("High Damage", True, WHITE)
            self.screen.blit(NameText, pygame.Rect(630,200,150,20))
            self.screen.blit(HealthText, pygame.Rect(630,220,150,20))
            self.screen.blit(StrengthText, pygame.Rect(630,240,150,20))

    def on_hover(self,event):
        """
        Certain events to occur if the cursor is located over certain areas of
        the screen
        """
        if self.mode == Modes.MakeTeam:
            if(pygame.Rect(610,450,80,50).collidepoint(event.pos)):
                self.show_min = 1
                    
            elif(pygame.Rect(710,450,80,50).collidepoint(event.pos)):
                self.show_min = 2
    
            elif(pygame.Rect(610,525,80,50).collidepoint(event.pos)):
                self.show_min = 3

            elif(pygame.Rect(710,525,80,50).collidepoint(event.pos)):
                self.show_min = 4
            else:
              self.show_min = None  

    def on_click(self,event):
        """
        Certain events to occur if the cursor is clicked based on the location
        of the click
        """
        if self.mode == Modes.Map:
            if (pygame.Rect(625,25,150,50).collidepoint(event.pos)):
                self.change_mode(Modes.MakeTeam)
                return

        if self.mode == Modes.MakeTeam:
            if (pygame.Rect(625,25,150,50).collidepoint(event.pos)):
                self.change_mode(Modes.Combat)
                return

            if (pygame.Rect(625,125,150,50).collidepoint(event.pos)):
                self.auto_team()

            if(pygame.Rect(610,450,80,50).collidepoint(event.pos)):
                minion = Minion()
                minion.set_type(0)
                self.team.add(minion)
                return

            if(pygame.Rect(710,450,80,50).collidepoint(event.pos)):
                minion = Minion()
                minion.set_type(1)
                self.team.add(minion)
                return

            if(pygame.Rect(610,525,80,50).collidepoint(event.pos)):
                minion = Minion()
                minion.set_type(2)
                self.team.add(minion)
                return
            
            if(pygame.Rect(710,525,80,50).collidepoint(event.pos)):
                minion = Minion()
                minion.set_type(3)
                self.team.add(minion)
                return

            for i in self.team.members:
                if(i.rect.collidepoint(event.pos)):
                    self.team.remove(i)

        if self.mode == Modes.Combat:
           if (pygame.Rect(625,25,150,50).collidepoint(event.pos)):
                self.change_mode(Modes.Map)

        if self.mode == Modes.GameOver:
            pass

    def screen_update(self):
        """
        Updates what is shown on the display based on the mode
        """
        global sim_fight
        global win
        #draw sidebar
        pygame.draw.rect(self.screen,GREY2,pygame.Rect(600,0,200,600))

        #Drawn if in Map mode
        if self.mode == Modes.Map:
            #draw top button
            pygame.draw.rect(self.screen,GREY3,pygame.Rect(625,25,150,50))
            text = Font.render("Create Team", True, WHITE)
            self.screen.blit(text, (630, 40))

            for i, member in enumerate(self.party.members):
                rect = pygame.Rect(625,150+(i*100),150,80)
                pygame.draw.rect(self.screen,member.color,rect)
                # Draw the health text of each units blocks
                name_text = Font.render(member.type, True, WHITE)
                self.screen.blit(name_text, rect)
                #Draw the Unit's Picture on the Block
                self.screen.blit(member.image, (670, 150+(i*100)))
                health_text = Font.render("{}".format(member.health), True, WHITE)
                rect.x += 125 - ((member.health//100) * 10)
                self.screen.blit(health_text, rect)
                
            self.map.draw_graph()
            self.map.draw_group(self.party.node)

        #Drawn if in MakeTeam mode
        if self.mode == Modes.MakeTeam:
            #draw top button
            pygame.draw.rect(self.screen,GREY3,pygame.Rect(625,25,150,50))
            text = Font.render("Fight", True, WHITE)
            self.screen.blit(text, (630, 40))

            self.party.drawGroup(self.screen)
            self.team.drawGroup(self.screen)

            pygame.draw.rect(self.screen,GREY3,pygame.Rect(625,125,150,50))
            text = Font.render("Generate Team", True, WHITE)
            self.screen.blit(text, (625,130))

            pygame.draw.rect(self.screen,GREY3,pygame.Rect(625,200,150,150))
            pygame.draw.rect(self.screen,GREY3,pygame.Rect(625,375,150,50))

            text0 = Font.render("Capacity: {}".format(self.team.maxsize), True, WHITE)
            self.screen.blit(text0, (630, 375))
            texta = Font.render("Used: {}".format(self.team.size), True, WHITE)
            self.screen.blit(texta, (630, 400))

            testmin = Minion()
            testmin.Goblin()
            pygame.draw.rect(self.screen,(testmin.color),pygame.Rect(610,450,85,50))
            nametext = Font.render(testmin.type, True, WHITE)
            self.screen.blit(nametext, (610, 450))
            costtext = Font.render("Cost: {}".format(testmin.cost), True, WHITE)
            self.screen.blit(costtext, (610, 475))
            if self.show_min == 1:
                self.screen.blit(testmin.image, (695,270))
                self.draw_info(testmin)

            testmin.Ork()
            pygame.draw.rect(self.screen,(testmin.color),pygame.Rect(705,450,85,50))
            nametext = Font.render(testmin.type, True, WHITE)
            self.screen.blit(nametext, (710, 450))
            costtext = Font.render("Cost: {}".format(testmin.cost), True, WHITE)
            self.screen.blit(costtext, (710, 475))
            if self.show_min == 2:
                self.screen.blit(testmin.image, (695,270))
                self.draw_info(testmin)

            testmin.Skeleton()
            pygame.draw.rect(self.screen,(testmin.color),pygame.Rect(610,525,85,50))
            nametext = Font.render(testmin.type, True, WHITE)
            self.screen.blit(nametext, (610, 525))
            costtext = Font.render("Cost: {}".format(testmin.cost), True, WHITE)
            self.screen.blit(costtext, (610, 550))
            if self.show_min == 3:
                self.screen.blit(testmin.image, (695,270))
                self.draw_info(testmin)

            testmin.Troll()
            pygame.draw.rect(self.screen,testmin.color,pygame.Rect(705,525,85,50))
            nametext = Font.render(testmin.type, True, WHITE)
            self.screen.blit(nametext, (710, 525))
            costtext = Font.render("Cost: {}".format(testmin.cost), True, WHITE)
            self.screen.blit(costtext, (710, 550))
            if self.show_min == 4:
                self.screen.blit(testmin.image, (695,270))
                self.draw_info(testmin)

        #Drawn if in Combat mode
        if self.mode == Modes.Combat:
            self.party.drawGroup(self.screen)
            self.team.drawGroup(self.screen)
            #draw top button
            pygame.draw.rect(self.screen,GREY3,pygame.Rect(625,25,150,50))
            text = Font.render("Skip Fight", True, WHITE)
            self.screen.blit(text, (630, 40))

            sim_fight = True
            while self.team.status() and self.party.status():
                fight(self.team, self.party, self.screen)
                fight(self.party, self.team, self.screen)

            self.team.reset()

            if self.party.status():
                nex = self.map.neighbours(self.party.node)
                self.party.move_party(nex[rollDie(len(nex))-1])
                if self.party.node >= 19:
                    self.change_mode(Modes.GameOver)
                else:
                    self.change_mode(Modes.Map)
            else:
                win = True
                self.change_mode(Modes.GameOver)

        #Drawn if in GameOver mode
        if self.mode == Modes.GameOver:
            if win:
                pygame.draw.rect(self.screen,(50,50,200),pygame.Rect(0,0,self.width,self.height))
                wintext = BigFont.render("YOU WIN!", True, WHITE)
                self.screen.blit(wintext, (200, 200))

            else:
                pygame.draw.rect(self.screen,(200,50,50),pygame.Rect(0,0,self.width,self.height))
                losetext = BigFont.render("Sorry, You Lost", True, WHITE)
                self.screen.blit(losetext, (50, 200))
    
        #refresh screen
        pygame.display.update()
  
def fight(team,otherteam, screen):
    """
    Simulates a round of combat where team attacks otherteam, drawing it on the
    screen
    """
    global sim_fight
    for i in team.members:
        try:
            for b in range(i.attack_cap):
                l = len (otherteam.members)
                target = otherteam.members[rollDie(l,1)-1]

                for event in pygame.event.get():
                    if (event.type == pygame.MOUSEBUTTONUP and event.button == 1 and pygame.mouse.get_focused()):
                        if (pygame.Rect(625,25,150,50).collidepoint(event.pos)):
                            sim_fight = False
                            
                if sim_fight == True:
                    if i.ranged == True:
                        bullet = Bullet(i)
                        if i.rect.x > target.rect.x:
                            bullet.rect.x = i.rect.x - 25
                        elif i.rect.x < target.rect.x:
                            bullet.rect.x = i.rect.x + 85
                        bullet.rect.y = i.rect.y
                        bullet_list.add(bullet)

                        while True:
                            team.drawGroup(screen)
                            otherteam.drawGroup(screen)
                            bullet_list.update(target)
                            bullet_list.draw(screen)
                            pygame.display.update()
                            fpsTime.tick(FPS)

                            if bullet.rect.colliderect(target.rect):
                                bullet.erase(screen)
                                team.drawGroup(screen)
                                otherteam.drawGroup(screen)
                                damage = i.attack(target)
                                draw_damage(damage,target,screen)
                                pygame.display.update()
                                pygame.time.delay(500)
                                bullet_list.remove(bullet)
                                if not target.active:
                                    #Erase the Target If Dead
                                    pygame.draw.rect(screen,BLACK,target.rect)
                                team.drawGroup(screen)
                                otherteam.drawGroup(screen)
                                pygame.display.update()
                                break

                    elif i.ranged == False:
                        orgx = i.rect.x
                        orgy = i.rect.y

                        i.update(screen, target)
                        damage = i.attack(target)
                        draw_damage(damage,target,screen)

                        # Draw the unit
                        draw_unit(screen, i)
                        pygame.display.update()
                        pygame.time.delay(500)
                        if not target.active:
                            screen.blit(bg,(target.rect.x,target.rect.y), (target.rect.x,target.rect.y,80,80))
                        screen.blit(bg,(i.rect.x, i.rect.y), (i.rect.x, i.rect.y,80,80))
                        pygame.display.update()

                        i.rect.x = orgx
                        i.rect.y = orgy
                        team.drawGroup(screen)
                        otherteam.drawGroup(screen)
                        pygame.display.update()
                        pygame.time.delay(500)
                else:
                    damage = i.attack(target)
 

        except (IndexError):
            pass
                 

def draw_unit(screen, unit):
    """
    Draws the unit on the screen at it's current location
    """
    screen.blit(unit.image, (unit.rect.x,unit.rect.y))

def draw_damage(damage,target,screen):
    """
    Prints a damage value in the top-right corner of the unit's location when 
    damaged
    """
    # Printing deduct health on the attacked target
    deduct_health = Font.render(" - {}".format(damage), True, WHITE)
    # New block to print deduct health
    deduct_rect = target.rect.copy()
    deduct_rect.x += 50

    # Print out health deducted
    screen.blit(deduct_health, deduct_rect)
