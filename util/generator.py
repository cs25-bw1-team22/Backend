from django.contrib.auth.models import User
from adventure.models import Player, Room, Passenger
import random

descriptions = ["rand desc 1", "rand desc 2", "rand desc 2"]
random(descriptoions)


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

class WorldMap:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.width = 0
    
    def generate_rooms(self, width, height, num_rooms):
        self.grid = [None] * height
        self.width = width
        self.height = height

        # Initializes the grid
        for i in range( len(self.grid) ):
            self.grid[i] = [None] * width
        
        # Sets starting point
        x = -1
        y = 0
        # keeps track of rooms built
        room_count = 0 

        # What direction do we want to generate rooms?


        # Loop that creates all the rooms
        previous_room = None
        while room_count < num_rooms:

            # rooms need to some how find their neighbors
            # and fall into place on the grid here


            # When the place on the grid is found create the room
            room = Room()


