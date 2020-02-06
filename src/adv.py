from room import Room
from player import Player
from item import Passenger


room = {

'911_MainSt' : Room(title="Starting Location", description="You are now ready to start driving. Please drive forward"),
'912_MainSt' : Room(title="912 Main Street", description="You are currently at 912 Main Street there are no bustops or intersections. Please drive forward"),
'913_MainSt' : Room(title="913 Main Street", description="There is a bustop to your right with 2 people waiting. Pick up the passengers and drop them off according to their instructions"),
'914_MainSt' : Room(title="914 Main Street", description="You are currently at 914 Main Street there are no bustops or intersections. Please drive forward"),
'915_MainSt' :Room(title="915 Main Street", description="You are at an intersection, please go left or right"),



'811_SouthSt' : Room(title="811 South Street", description="There is an empty bustop to your right."),
'812_SouthSt' : Room(title="812 South Street", description="You are currently at 812 South Street there are no bustops or intersections. Please drive forward"),
'813_SouthSt' : Room(title="813 South Street", description="You are currently at 813 South Street there are no bustops or intersections. Please drive forward"),
'814_SouthSt' : Room(title="814 South Street", description="You are currently at 814 South Street there are no bustops or intersections. Please drive forward"),
'815_SouthSt':   Room(title="815 South Street", description="You are at an intersection, please go left or right"),



'711_FrontSt':   Room(title="711 Front Street", description="You are currently at 711 Front Street there are no bustops or intersections. Please drive forward"),
'712_FrontSt' : Room(title="712 Front Street", description="There is a bustop to your right with 4 people waiting"),
'713_FrontSt' : Room(title="713 Front Street", description="You are currently at 713 Front Street there are no bustops or intersections. Please drive forward"),
'714_FrontSt' : Room(title="714 Front Street", description="You are currently at 714 Front Street there are no bustops or intersections. Please drive forward"),
'715_FrontSt' : Room(title="715 Front Street", description="You are at an intersection, please go left or right"),



'611_GrapeSt' : Room(title="611 Grape Street", description="You are currently at 611 Grape Street there are no bustops or intersections. Please drive forward"),
'612_GrapeSt' : Room(title="612 Grape Street", description="There is an empty bus stop to your right."),
'613_GrapeSt' : Room(title="613 Grape Street", description="You are currently at 613 Grape Street there are no bustops or intersections. Please drive forward"),
'614_GrapeSt' : Room(title="614 Grape Street", description="There is a bustop to your right with 6 people waiting"),
'615_GrapeSt' : Room(title="615 Grape Street", description="You are at an intersection, please go left or right"),



'511_ParkSt' : Room(title="511 Park Street", description="You are currently at 511 Park Street there are no bustops or intersections. Please drive forward"),
'512_ParkSt' : Room(title="512 Park Street", description="You are currently at 512 Park Street there are no bustops or intersections. Please drive forward"),
'513_ParkSt' : Room(title="513 Park Street", description="You are currently at 513 Park Street there are no bustops or intersections. Please drive forward"),
'514_ParkSt' : Room(title="514 Park Street", description="There is an empty bus stop to your right."),
'515_ParkSt' : Room(title="515 Park Street", description="You are at an intersection, please go left or right"),


'411_LakeSt' : Room(title="411 Lake Street", description="You are currently at 411 Lake Street there are no bustops or intersections. Please drive forward"),
'412_LakeSt' : Room(title="412 Lake Street", description="You are currently at 412 Lake Street there are no bustops or intersections. Please drive forward"),
'413_LakeSt' : Room(title="413 Lake Street", description="You are currently at 413 Lake Street there are no bustops or intersections. Please drive forward"),
'414_LakeSt' : Room(title="414 Lake Street", description="There is an empty bus stop to your right."),
'415_LakeSt' : Room(title="415 Lake Street", description="You are at an intersection, please go left or right"),


'311_MagnoliaSt' : Room(title="311 Magnolia Street", description="You are currently at 311 Magnolia Street there are no bustops or intersections. Please drive forward"),
'312_MagnoliaSt' : Room(title="312 Magnolia Street", description="You are currently at 312 Magnolia Street there is an intersection to your right with an empty bus stop"),
'313_MagnoliaSt' : Room(title="313 Magnolia Street", description="You are currently at 313 Magnolia Street there are no bustops or intersections. Please drive forward"),
'314_MagnoliaSt' : Room(title="314 Magnolia Street", description="You are currently at 314 Magnolia Street there are no bustops or intersections. Please drive forward"),
'315_MagnoliaSt' : Room(title="315 Magnolia Street", description="You are at an intersection, please go left or right"),


'211_SunsetSt' : Room(title="211 Sunset Street", description="You are currently at 211 Sunset Street there are no bustops or intersections. Please drive forward"),
'212_SunsetSt' : Room(title="212 Sunset Street", description="You are currently at 212 Sunset Street there are no bustops or intersections. Please drive forward"),
'213_SunsetSt' : Room(title="213 Sunset Street", description="You are currently at 213 Sunset Street there are no bustops or intersections. Please drive forward"),
'214_SunsetSt' : Room(title="214 Sunset Street", description="There is a bustop to your right with 6 people waiting"),
'215_SunsetSt' : Room(title="215 Sunset Street", description="You are at an intersection, please go left or right"),


'111_ApacheSt' : Room(title="111 Apache Street", description="You are currently at 111 Apache Street there are no bustops or intersections. Please drive forward"),
'112_ApacheSt' : Room(title="112 Apache Street", description="You are currently at 112 Apache Street there is an intersection to your right with an empty bus stop"),
'113_ApacheSt' : Room(title="113 Apache Street", description="You are currently at 113 Apache Street there are no bustops or intersections. Please drive forward"),
'114_ApacheSt' : Room(title="114 Apache Street", description="There is a bustop to your right with 5 people waiting"),
'115_ApacheSt' : Room(title="115 Apache Street", description="You are at an intersection, please go left or right"),


'011_AirportSt' : Room(title="011 Airport Street", description="You are currently at 011 Airport Street there are no bustops or intersections. Please drive forward"),
'012_AirportSt' : Room(title="012 Airport Street", description="You are currently at 012 Airport Street there is an intersection to your right with an empty bus stop"),
'013_AirportSt' : Room(title="013 Airport Street", description="You are currently at 013 Airport Street there are no bustops or intersections. Please drive forward"),
'014_AirportSt' : Room(title="014 Airport Street", description="We are at the airport."),
'015_AirportSt' : Room(title="015 Airport Street", description="There is a bus stop to your left with 2 people waiting"),

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

room['815_SouthSt']._w_to = room['711_FrontSt']
room['711_FrontSt']._w_to = room['815_SouthSt']

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

room['515_ParkSt']._w_to = room['411_LakeSt']
room['411_LakeSt']._e_to = room['515_ParkSt']

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

room['315_MagnoliaSt']._w_to = room['211_SunsetSt']
room['211_SunsetSt']._e_to = room['315_MagnoliaSt']

room['211_SunsetSt'].n_to = room['212_SunsetSt']
room['212_SunsetSt'].n_to = room['213_SunsetSt']
room['213_SunsetSt'].n_to = room['214_SunsetSt']
room['214_SunsetSt'].n_to = room['215_SunsetSt']

room['215_SunsetSt'].s_to = room['214_SunsetSt']
room['214_SunsetSt'].s_to = room['213_SunsetSt']
room['213_SunsetSt'].s_to = room['212_SunsetSt']
room['212_SunsetSt'].s_to = room['211_SunsetSt']

room['215_SunsetSt']._w_to = room['111_ApacheSt']
room['111_ApacheSt']._e_to = room['215_SunsetSt']

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

Jahmir = Passenger("Two Tickets", "STOP 811 SOUTHST")
Zakariya = Passenger("STOP 414 LAKEST","")
Amaria= Passenger("One Ticket", "STOP 414 LAKEST")
Melvin= Passenger("Two Tickets", "STOP 414 LAKEST")
Naraly = Passenger("STOP 414 LAKEST", "")

Shiro = Passenger("One Ticket","STOP 612 GRAPE ST")
Zelma = Passenger("Two Tickets", "STOP 012 AIRPORT")
Roxen= Passenger("STOP 014 AIRPORT", "")
Allaina= Passenger("Three Tickets", "STOP 514 PARK ST")
Urban = Passenger("STOP 514 PARK ST", "")

Ayliana = Passenger("STOP 514 PARK ST", "")
Wallis = Passenger("One Ticket", "312 MAGNOLIA ST")
Usman= Passenger("One Ticket", "312 MAGNOLIA ST")
Meral= Passenger("One Ticket", "414 LAKEST")
Angeliz = Passenger("One Ticket", "014 AIRPORT")

Milagrace = Passenger("One Ticket", "012 AIRPORT")
Alyssia = Passenger("One Ticket", "514 PARK ST")
Manelyk= Passenger("Three Tickets", "STOP 811 SOUTH ST")
Aariyah= Passenger("STOP 811 SOUTH ST", "")
Torryn = Passenger("STOP 811 SOUTH ST", "")

Hanny = Passenger("One Ticket", "STOP 014 AIRPORT")
Breslin = Passenger("One Ticket", "STOP 012 AIRPORT")
Sofiya= Passenger("One Ticket", " STOP 014 AIRPORT")
Kalayla= Passenger("Two Tickets", "STOP 612 GRAPE ST")
Khylei = Passenger("STOP 612 GRAPE ST", "")

room['913_MainSt'].passengers.append([Jahmir, Zakariya])
room['712_FrontSt'].passengers.append([Amaria, Melvin, Naraly, Shiro])
room['614_GrapeSt'].passengers.append([Zelma, Roxen, Allaina, Urban, Ayliana, Wallis])
room['214_SunsetSt'].passengers.append([Usman, Meral, Angeliz, Milagrace, Alyssia, Manelyk])
room['114_ApacheSt'].passengers.append([Aariyah, Torryn, Hanny, Breslin, Sofiya])
room['015_AirportSt'].passengers.append([Kalayla, Khylei])

player_1 = Player("Buzz", room["911_MainSt"])

while True:

    quit = player_1.input_instructions()

    if quit == True:
        break
