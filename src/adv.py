from room import Room
from player import Player
from passenger import Passenger



people = {
'Jahmir' : Passenger("Jahmir", "811_SouthSt"),
'Zakariya' : Passenger("Zakariya", "414_LakeSt"),
'Amaria' : Passenger("Amaria", "414_LakeSt"),
'Melvin' : Passenger("Melvin", "414_LakeSt"),
'Naraly' : Passenger("Naraly", "414_LakeSt"),

'Shiro' : Passenger("Shiro","612_GrapeSt"),
'Zelma' : Passenger("Zelma", "012_AirportSt"),
'Roxen' : Passenger("Roxen", "014_AirportSt"),
'Allaina' : Passenger("Allaina", "514_ParkSt"),
'Urban' : Passenger("Urban", "514_ParkSt"),

}

room = {

'911_MainSt' : Room(title="Starting Location", description="You are now ready to start driving. Please drive forward", passengers=[]),
'912_MainSt' : Room(title='912_MainSt', description="You are currently at 912 Main Street there are no bustops or intersections. Please drive forward",passengers=[]),
'913_MainSt' : Room(
    title='913_MainSt', 
    description="There is a bustop to your right with 2 people waiting. Pick up the passengers and drop them off according to their instructions", 
    passengers = [people['Jahmir'], people['Zakariya']]),
'914_MainSt' : Room(title='914_MainSt', description="You are currently at 914 Main Street there are no bustops or intersections. Please drive forward",passengers=[]),
'915_MainSt' :Room(title='915_MainSt', description="You are at an intersection, please go left or right",passengers=[]),



'811_SouthSt' : Room(title='811_SouthSt', description="There is an empty bustop to your right.", passengers=[]),
'812_SouthSt' : Room(title='812_SouthSt', description="You are currently at 812 South Street there are no bustops or intersections. Please drive forward", passengers=[]),
'813_SouthSt' : Room(title='813_SouthSt', description="You are currently at 813 South Street there are no bustops or intersections. Please drive forward", passengers=[]),
'814_SouthSt' : Room(title='814_SouthSt', description="You are currently at 814 South Street there are no bustops or intersections. Please drive forward", passengers=[]),
'815_SouthSt' : Room(title='815_SouthSt', description="You are at an intersection, please go left or right", passengers=[]),



'711_FrontSt':   Room(title='711_FrontSt', description="You are currently at 711 Front Street there are no bustops or intersections. Please drive forward", passengers=[]),
'712_FrontSt' : Room(
    title='712_FrontSt', 
    description="There is a bustop to your right with 4 people waiting",
    passengers = [people['Amaria'], people['Melvin'], people['Naraly'], people['Shiro']]),
'713_FrontSt' : Room(title='713_FrontSt', description="You are currently at 713 Front Street there are no bustops or intersections. Please drive forward", passengers=[]),
'714_FrontSt' : Room(title='714_FrontSt', description="You are currently at 714 Front Street there are no bustops or intersections. Please drive forward", passengers=[]),
'715_FrontSt' : Room(title='715_FrontSt', description="You are at an intersection, please go left or right", passengers=[]),



'611_GrapeSt' : Room(title='611_GrapeSt', description="You are currently at 611 Grape Street there are no bustops or intersections. Please drive forward", passengers=[]),
'612_GrapeSt' : Room(title='612_GrapeSt', description="There is an empty bus stop to your right.", passengers=[]),
'613_GrapeSt' : Room(title='613_GrapeSt', description="You are currently at 613 Grape Street there are no bustops or intersections. Please drive forward", passengers=[]),
'614_GrapeSt' : Room(
    title = '614_GrapeSt', 
    description = "There is a bustop to your right with 6 people waiting",
    passengers = [people['Zelma'], people['Roxen'], people['Allaina'], people['Urban']]),
'615_GrapeSt' : Room(title='615_GrapeSt', description="You are at an intersection, please go left or right", passengers=[]),



'511_ParkSt' : Room(title='511_ParkSt', description="You are currently at 511 Park Street there are no bustops or intersections. Please drive forward", passengers=[]),
'512_ParkSt' : Room(title='512_ParkSt', description="You are currently at 512 Park Street there are no bustops or intersections. Please drive forward", passengers=[]),
'513_ParkSt' : Room(title='513_ParkSt', description="You are currently at 513 Park Street there are no bustops or intersections. Please drive forward", passengers=[]),
'514_ParkSt' : Room(title='514_ParkSt', description="There is an empty bus stop to your right.", passengers=[]),
'515_ParkSt' : Room(title='515_ParkSt', description="You are at an intersection, please go left or right", passengers=[]),


'411_LakeSt' : Room(title='411_LakeSt', description="You are currently at 411 Lake Street there are no bustops or intersections. Please drive forward", passengers=[]),
'412_LakeSt' : Room(title='412_LakeSt', description="You are currently at 412 Lake Street there are no bustops or intersections. Please drive forward", passengers=[]),
'413_LakeSt' : Room(title='413_LakeSt', description="You are currently at 413 Lake Street there are no bustops or intersections. Please drive forward", passengers=[]),
'414_LakeSt' : Room(title='414_LakeSt', description="There is an empty bus stop to your right.", passengers=[]),
'415_LakeSt' : Room(title='415_LakeSt', description="You are at an intersection, please go left or right", passengers=[]),


'311_MagnoliaSt' : Room(title='311_MagnoliaSt', description="You are currently at 311 Magnolia Street there are no bustops or intersections. Please drive forward", passengers=[]),
'312_MagnoliaSt' : Room(title='312_MagnoliaSt', description="You are currently at 312 Magnolia Street there is an intersection to your right with an empty bus stop", passengers=[]),
'313_MagnoliaSt' : Room(title='313_MagnoliaSt', description="You are currently at 313 Magnolia Street there are no bustops or intersections. Please drive forward", passengers=[]),
'314_MagnoliaSt' : Room(title='314_MagnoliaSt', description="You are currently at 314 Magnolia Street there are no bustops or intersections. Please drive forward", passengers=[]),
'315_MagnoliaSt' : Room(title='315_MagnoliaSt', description="You are at an intersection, please go left or right", passengers=[]),


'211_SunsetSt' : Room(title='211_SunsetSt', description="You are currently at 211 Sunset Street there are no bustops or intersections. Please drive forward", passengers=[]),
'212_SunsetSt' : Room(title='212_SunsetSt', description="You are currently at 212 Sunset Street there are no bustops or intersections. Please drive forward", passengers=[]),
'213_SunsetSt' : Room(title='213_SunsetSt', description="You are currently at 213 Sunset Street there are no bustops or intersections. Please drive forward", passengers=[]),
'214_SunsetSt' : Room(title='214_SunsetSt', description="There is a bustop to your right with 6 people waiting", passengers=[]),
'215_SunsetSt' : Room(title='215_SunsetSt', description="You are at an intersection, please go left or right", passengers=[]),


'111_ApacheSt' : Room(title='111_ApacheSt', description="You are currently at 111 Apache Street there are no bustops or intersections. Please drive forward", passengers=[]),
'112_ApacheSt' : Room(title='112_ApacheSt', description="You are currently at 112 Apache Street there is an intersection to your right with an empty bus stop", passengers=[]),
'113_ApacheSt' : Room(title='113_ApacheSt', description="You are currently at 113 Apache Street there are no bustops or intersections. Please drive forward", passengers=[]),
'114_ApacheSt' : Room(title='114_ApacheSt', description="There is a bustop to your right with 5 people waiting", passengers=[]),
'115_ApacheSt' : Room(title='115_ApacheSt', description="You are at an intersection, please go left or right", passengers=[]),


'011_AirportSt' : Room(title='011_AirportSt', description="You are currently at 011 Airport Street there are no bustops or intersections. Please drive forward", passengers=[]),
'012_AirportSt' : Room(title='012_AirportSt', description="You are currently at 012 Airport Street there is an intersection to your right with an empty bus stop", passengers=[]),
'013_AirportSt' : Room(title='013_AirportSt', description="You are currently at 013 Airport Street there are no bustops or intersections. Please drive forward", passengers=[]),
'014_AirportSt' : Room(title='014_AirportSt', description="We are at the airport.", passengers=[]),
'015_AirportSt' : Room(title='015_AirportSt', description="There is a bus stop to your left with 2 people waiting", passengers=[]),
}

room['911_MainSt'].n_to = room['912_MainSt']
room['912_MainSt'].n_to = room['913_MainSt']
room['913_MainSt'].n_to = room['914_MainSt']
room['914_MainSt'].n_to = room['915_MainSt']

room['915_MainSt'].s_to = room['914_MainSt']
room['914_MainSt'].s_to = room['913_MainSt']
room['913_MainSt'].s_to = room['912_MainSt']
room['912_MainSt'].s_to = room['911_MainSt']

room['915_MainSt'].e_to = room['811_SouthSt']
room['811_SouthSt'].w_to = room['915_MainSt']

room['811_SouthSt'].n_to = room['812_SouthSt']
room['812_SouthSt'].n_to = room['813_SouthSt']
room['813_SouthSt'].n_to = room['814_SouthSt']
room['814_SouthSt'].n_to = room['815_SouthSt']

room['815_SouthSt'].s_to = room['814_SouthSt']
room['814_SouthSt'].s_to = room['813_SouthSt']
room['813_SouthSt'].s_to = room['812_SouthSt']
room['812_SouthSt'].s_to = room['811_SouthSt']

room['815_SouthSt'].w_to = room['711_FrontSt']
room['711_FrontSt'].e_to = room['815_SouthSt']

room['711_FrontSt'].n_to = room['712_FrontSt']
room['712_FrontSt'].n_to = room['713_FrontSt']
room['713_FrontSt'].n_to = room['714_FrontSt']
room['714_FrontSt'].n_to = room['715_FrontSt']

room['715_FrontSt'].s_to = room['714_FrontSt']
room['714_FrontSt'].s_to = room['713_FrontSt']
room['713_FrontSt'].s_to = room['712_FrontSt']
room['712_FrontSt'].s_to = room['711_FrontSt']

room['715_FrontSt'].e_to = room['611_GrapeSt']
room['611_GrapeSt'].w_to = room['715_FrontSt']

room['611_GrapeSt'].n_to = room['612_GrapeSt']
room['612_GrapeSt'].n_to = room['613_GrapeSt']
room['613_GrapeSt'].n_to = room['614_GrapeSt']
room['614_GrapeSt'].n_to = room['615_GrapeSt']

room['615_GrapeSt'].s_to = room['614_GrapeSt']
room['614_GrapeSt'].s_to = room['613_GrapeSt']
room['613_GrapeSt'].s_to = room['612_GrapeSt']
room['612_GrapeSt'].s_to = room['611_GrapeSt']

room['615_GrapeSt'].e_to = room['511_ParkSt']
room['511_ParkSt'].w_to = room['615_GrapeSt']

room['511_ParkSt'].n_to = room['512_ParkSt']
room['512_ParkSt'].n_to = room['513_ParkSt']
room['513_ParkSt'].n_to = room['514_ParkSt']
room['514_ParkSt'].n_to = room['515_ParkSt']

room['515_ParkSt'].s_to = room['514_ParkSt']
room['514_ParkSt'].s_to = room['513_ParkSt']
room['513_ParkSt'].s_to = room['512_ParkSt']
room['512_ParkSt'].s_to = room['511_ParkSt']

room['515_ParkSt'].w_to = room['411_LakeSt']
room['411_LakeSt'].e_to = room['515_ParkSt']

room['411_LakeSt'].n_to = room['412_LakeSt']
room['412_LakeSt'].n_to = room['413_LakeSt']
room['413_LakeSt'].n_to = room['414_LakeSt']
room['414_LakeSt'].n_to = room['415_LakeSt']

room['415_LakeSt'].s_to = room['414_LakeSt']
room['414_LakeSt'].s_to = room['413_LakeSt']
room['413_LakeSt'].s_to = room['412_LakeSt']
room['412_LakeSt'].s_to = room['411_LakeSt']

room['415_LakeSt'].e_to = room['311_MagnoliaSt']
room['311_MagnoliaSt'].w_to = room['415_LakeSt']

room['311_MagnoliaSt'].n_to = room['312_MagnoliaSt']
room['312_MagnoliaSt'].n_to = room['313_MagnoliaSt']
room['313_MagnoliaSt'].n_to = room['314_MagnoliaSt']
room['314_MagnoliaSt'].n_to = room['315_MagnoliaSt']

room['315_MagnoliaSt'].s_to = room['314_MagnoliaSt']
room['314_MagnoliaSt'].s_to = room['313_MagnoliaSt']
room['313_MagnoliaSt'].s_to = room['312_MagnoliaSt']
room['312_MagnoliaSt'].s_to = room['311_MagnoliaSt']

room['315_MagnoliaSt'].w_to = room['211_SunsetSt']
room['211_SunsetSt'].e_to = room['315_MagnoliaSt']

room['211_SunsetSt'].n_to = room['212_SunsetSt']
room['212_SunsetSt'].n_to = room['213_SunsetSt']
room['213_SunsetSt'].n_to = room['214_SunsetSt']
room['214_SunsetSt'].n_to = room['215_SunsetSt']

room['215_SunsetSt'].s_to = room['214_SunsetSt']
room['214_SunsetSt'].s_to = room['213_SunsetSt']
room['213_SunsetSt'].s_to = room['212_SunsetSt']
room['212_SunsetSt'].s_to = room['211_SunsetSt']

room['215_SunsetSt'].w_to = room['111_ApacheSt']
room['111_ApacheSt'].e_to = room['215_SunsetSt']

room['111_ApacheSt'].n_to = room['112_ApacheSt']
room['112_ApacheSt'].n_to = room['113_ApacheSt']
room['113_ApacheSt'].n_to = room['114_ApacheSt']
room['114_ApacheSt'].n_to = room['115_ApacheSt']

room['115_ApacheSt'].s_to = room['114_ApacheSt']
room['114_ApacheSt'].s_to = room['113_ApacheSt']
room['113_ApacheSt'].s_to = room['112_ApacheSt']
room['112_ApacheSt'].s_to = room['111_ApacheSt']

room['115_ApacheSt'].e_to = room['011_AirportSt']
room['011_AirportSt'].w_to = room['115_ApacheSt']

room['011_AirportSt'].n_to = room['012_AirportSt']
room['012_AirportSt'].n_to = room['013_AirportSt']
room['013_AirportSt'].n_to = room['014_AirportSt']
room['014_AirportSt'].n_to = room['015_AirportSt']

room['015_AirportSt'].s_to = room['014_AirportSt']
room['014_AirportSt'].s_to = room['013_AirportSt']
room['013_AirportSt'].s_to = room['012_AirportSt']
room['012_AirportSt'].s_to = room['011_AirportSt']

move_map = {
    "n": "n_to",
    "s": "s_to",
    "e": "e_to",
    "w": "w_to" 
}

move_list = ['n', 'e', 's', 'w']
action_list = ['pickup', 'dropoff']


player_1 = Player("Buzz", room["911_MainSt"])

while True:

    user_input = input(    "\n"
                           +"What would you like to do?\nTo move type: n,s,e,w\n"
                           +"to pick up a passenger 'pickup <passenger name>'\n"
                           +"to drop off a passenger 'dropoff <passenger name>'\n"
                           +"Type 'i' to view who is on the bus\n"
                           +"Type 'q' to quit\n"
                           +"\n")

    if len(user_input) == 1:

        if user_input in move_list:
            player_1.move_player(user_input)
        elif user_input == "i":
            print("\nPassengers:  "+"\n")
            if (len(player_1.passenger_inv) == 0):
                print('\nNo passengers on the bus\n')
            else:
                for i in range(len(player_1.passenger_inv)):
                    print(player_1.passenger_inv[i])
            

        elif user_input == "q":
            # Quit
            print("Goodbye!")
            exit()
        else:
            print("\nDid not recognize that command\n")
    
    else:
        
        if user_input.split(' ')[0] == 'pickup':
            player_1.get_passenger(user_input.split(' ')[1])

        elif user_input.split(' ')[0] == 'dropoff':
            player_1.drop_passenger(user_input.split(' ')[1])

        else:
            print("\nDid not recognize that command")

    