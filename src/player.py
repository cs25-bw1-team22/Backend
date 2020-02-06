from room import Room
class Player:
    def __init__(self, title, current_room, passengers=None):

        self.title = title
        self.current_room = current_room
        self.passengers = []

    def move_player(self, inp):
        possible_room = self.current_room.get_room_in_direction(inp)
            
        if possible_room is not None:
            self.current_room = possible_room
            self.current_room.where_am_i()
        
        else:
            print("\n"+"There is nothing in that direction"+"\n")


    def get_passenger(self, passenger):
        for obj in self.current_room.passengers:
            if obj.title == passenger:
                self.passengers.append(obj)
                obj.on_take()
                self.current_room.passengers.remove(obj)


    def drop_passenger(self,passenger):
        for obj in self.passengers:
            if obj.title == passenger:
                self.passengers.remove(obj)
                obj.on_drop()
                self.current_room.passengers.append(obj)
