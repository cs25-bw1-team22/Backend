from django.contrib.auth.models import User
from adventure.models import Player, Room, Passenger
import random

"""
Example of how Random Works:

descriptions = ["rand desc 1", "rand desc 2", "rand desc 2"]
random(descriptoions)
"""


Room.object.all().delete()

"""
This is where our generator logic will go
Remember to use .save() after generating 
each room to save to django database

Possible Methods Needed:
Generate Rooms Grid
   - With random descriptions
Link Bus Stops (rooms)
Place Bus at Start (Player)
Place Passengers

"""
#Create a class called "World"
class World:
    # instialize it with no parameters but a grid, width, and height attribute
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0
    
    # add the ability to print the world as a string

    # create a method that will connect the rooms:
    #
    # Generate Rooms:
    # Generate Descriptions of Rooms:
    # Generate the Map Grid (Not in Snake):

    


"""
Probably put this in Create_world.py
Now the world needs to intialized and
then the players need to be placed on the board.
"""

# set a new instance of the World to a variable
# call the generator and pass in 10 for width and 10 for height
# set up the grid by looping through the width and the height
# save the room to the database using .save()


# set up a new instance of the players
# for each player:
# place them in a current room on the map
# save the instances to the database using .save()