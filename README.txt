Code Written by Ben Schreiber and Dai Dao, CMPUT 275 B1

The Graph class in Gamegraph.py was copied from provided code on eClass
Matrix class in matrix.py copied from earlier work done for CMPUT 275 Assignment
2
Images found on www.spriter-resource.com, credit to submitters Dazz, SmithyGCN,
Felix Flywheel, daemoth

Dungeon Master is a game that pits the player against a Party of Fantasy 
Role-Playing Game (RPG) Heros. The player must send teams of minions, such as
Goblins, Orks or Trolls, in attempt to eliminate the party before they reach the
end of the map.

HOW TO RUN:
Install Pygame for Python3 (See http://www.pygame.org/wiki/ for installation 
instructions)
Ensure that all provided .py and .gif files are in the current folder
Run the game by calling "dmgame.py" in a python interpreter

HOW TO PLAY:
At the start of the Game, the player is shown a map of connected nodes. The Node
at the bottom of the screen has a blue square inside the regular node, 
indicating the current location of the party. The Party composition is shown on
the sidebar.

Once the player presses the "Create Team" Button on the sidebar, the screen 
changes to the battlefield setting, with the current party shown on the left 
side of the playing screen. On the sidebar is shown the player's current team
capacity, as well as an automatic team button and 4 buttons for the player's 
unit types. Hovering over the unit type buttons brings their picture and 
information up on the sidebar, and clicking on them will add them to the 
player's team, and they will appear on the battlefield. Pressing the "Generate 
Team" Button will cause the program to generate the strongest possible team,
based on the capacity and the unit type's value as per the "Value(enemies)" 
function in the units class. 

Once the Player has chosen a team, they press the "Fight" Button on the sidebar.
The party and the player's team will then engage in simulated combat. To skip 
the simulation, the player can press the "Skip Fight" button on the sidebar, 
and the visual display of combat will end, and the simulated fight quickly 
resolves itself. Regardless of skipping, after the fight, the display returns to
the map mode. If the party won the combat, they move to a randomly selected node
along their possible paths. If the player's team defeated all of the party, the
Player wins, and the game is over.

The Game continues until either the party is defeated, or they reach the node at
the very top of the screen, at which point the player loses.

