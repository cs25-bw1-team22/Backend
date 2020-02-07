from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid

class Room(models.Model):
    title = models.CharField(max_length=50, default="DEFAULT TITLE")
    description = models.CharField(max_length=500, default="DEFAULT DESCRIPTION")
    n_to = models.IntegerField(default=0)
    s_to = models.IntegerField(default=0)
    e_to = models.IntegerField(default=0)
    w_to = models.IntegerField(default=0)

    def connectRooms(self, destinationRoom, direction):
        destinationRoomID = destinationRoom.id
        try:
            destinationRoom = Room.objects.get(id=destinationRoomID)
        except Room.DoesNotExist:
            print("That room does not exist")
        else:
            if direction == "n":
                self.n_to = destinationRoomID
            elif direction == "s":
                self.s_to = destinationRoomID
            elif direction == "e":
                self.e_to = destinationRoomID
            elif direction == "w":
                self.w_to = destinationRoomID
            else:
                print("Invalid direction")
                return
            self.save()
    def playerNames(self, currentPlayerID):
        return [p.user.username for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]
    def playerUUIDs(self, currentPlayerID):
        return [p.uuid for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default="DEFAULT TITLE")
    currentRoom = models.CharField(max_length=500)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    #title = models.CharField(max_length=500)
    #passenger_inv = models.ArrayField(models.CharField(max_length=500))


    def initialize(self):
        if self.currentRoom == 0:
            self.currentRoom = Room.objects.first().id
            self.save()
    def room(self):
        try:
            return Room.objects.get(id=self.currentRoom)
        except Room.DoesNotExist:
            self.initialize()
            return self.room()
    '''
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
                self.passenger_inv.append(obj)
                self.save()
                obj.on_take()
                self.current_room.passengers.remove(obj)


    def drop_passenger(self,passenger):
        for obj in self.passenger_inv:
            if obj.title == passenger:
                if obj.description == self.current_room.title:
                    self.passenger_inv.remove(obj)
                    obj.on_drop()
                    self.current_room.passengers.append(obj)
                else:
                    print("\nNot the right drop-off location\n")            

class Passenger(models.Model):
    def __init__(self, title, description):
        self.title = title
        self.description = description
    def __str__(self):
        return f"{self.title} : {self.description}"


    def on_take(self):
        print(f"PICKED UP {self.title} {self.description}")

    def on_drop(self):
        print(f"DROPPED OFF {self.title}")

    '''

# class Passenger(models.Model):
#     def __init__(self, title, description):
#         self.title = title
#         self.description = description
#     def __str__(self):
#         return f"{self.title} : {self.description}"


#     def on_take(self):
#         print(f"PICKED UP {self.title} {self.description}")

#     def on_drop(self):
#         print(f"DROPPED OFF {self.title}")

#     def check(self):
#         self.drop_check()

@receiver(post_save, sender=User)
def create_user_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)
        Token.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_player(sender, instance, **kwargs):

    instance.player.save()


    instance.player.save()

