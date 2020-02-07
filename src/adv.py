from adventure.models import Player, Room

# people = {
# 'Jahmir' : Passenger("Jahmir", "811_SouthSt"),
# 'Zakariya' : Passenger("Zakariya", "414_LakeSt"),
# 'Amaria' : Passenger("Amaria", "414_LakeSt"),
# 'Melvin' : Passenger("Melvin", "414_LakeSt"),
# 'Naraly' : Passenger("Naraly", "414_LakeSt"),

# 'Shiro' : Passenger("Shiro","612_GrapeSt"),
# 'Zelma' : Passenger("Zelma", "012_AirportSt"),
# 'Roxen' : Passenger("Roxen", "014_AirportSt"),
# 'Allaina' : Passenger("Allaina", "514_ParkSt"),
# 'Urban' : Passenger("Urban", "514_ParkSt"),

# 'Ayliana' : Passenger("Ayliana", ""),
# 'Wallis' : Passenger("Wallis", "312_MagnoliaSt"),
# 'Usman': Passenger("Usman", "312_MagnoliaSt"),
# 'Meral': Passenger("Meral", "414_LakeSt"),
# 'Angeliz' : Passenger("Angeliz", "014_AirportSt"),

# 'Milagrace' : Passenger("Milagrace", "012_AirportSt"),
# 'Alyssia' : Passenger("Alyssia", "514_ParkSt"),
# 'Manelyk': Passenger("Manelyk", "811_SouthSt"),
# 'Aariyah': Passenger("Aariyah", ""),
# 'Torryn' : Passenger("Torryn", ""),

# 'Hanny' : Passenger("Hanny", "014_AirportSt"),
# 'Breslin' : Passenger("Breslin", "012_AirportSt"),
# 'Sofiya': Passenger("Sofiya", "014_AirportSt"),
# 'Kalayla': Passenger("Kalayla", "612_GrapeSt"),
# 'Khylei' : Passenger("Khylei", ""),

# }

# for p in people:
#     p.save()

room = {

'911_MainSt' : Room(title="Starting Location", description="You are now ready to start driving. Please drive forward"),
'912_MainSt' : Room(title='912_MainSt', description="You are currently at 912 Main Street there are no bustops or intersections. Please drive forward"),
'913_MainSt' : Room(title='913_MainSt', description="There is a bustop to your right with 2 people waiting. Pick up the passengers and drop them off according to their instructions"),
'914_MainSt' : Room(title='914_MainSt', description="You are currently at 914 Main Street there are no bustops or intersections. Please drive forward"),
'915_MainSt' : Room(title='915_MainSt', description="You are at an intersection, please go left or right"),



'811_SouthSt' : Room(title='811_SouthSt', description="There is an empty bustop to your right."),
'812_SouthSt' : Room(title='812_SouthSt', description="You are currently at 812 South Street there are no bustops or intersections. Please drive forward"),
'813_SouthSt' : Room(title='813_SouthSt', description="You are currently at 813 South Street there are no bustops or intersections. Please drive forward"),
'814_SouthSt' : Room(title='814_SouthSt', description="You are currently at 814 South Street there are no bustops or intersections. Please drive forward"),
'815_SouthSt' : Room(title='815_SouthSt', description="You are at an intersection, please go left or right"),



'711_FrontSt':   Room(title='711_FrontSt', description="You are currently at 711 Front Street there are no bustops or intersections. Please drive forward"),
'712_FrontSt' : Room(
    title='712_FrontSt', 
    description="There is a bustop to your right with 4 people waiting"),
'713_FrontSt' : Room(title='713_FrontSt', description="You are currently at 713 Front Street there are no bustops or intersections. Please drive forward"),
'714_FrontSt' : Room(title='714_FrontSt', description="You are currently at 714 Front Street there are no bustops or intersections. Please drive forward"),
'715_FrontSt' : Room(title='715_FrontSt', description="You are at an intersection, please go left or right"),



'611_GrapeSt' : Room(title='611_GrapeSt', description="You are currently at 611 Grape Street there are no bustops or intersections. Please drive forward"),
'612_GrapeSt' : Room(title='612_GrapeSt', description="There is an empty bus stop to your right."),
'613_GrapeSt' : Room(title='613_GrapeSt', description="You are currently at 613 Grape Street there are no bustops or intersections. Please drive forward"),
'614_GrapeSt' : Room(
    title = '614_GrapeSt', 
    description = "There is a bustop to your right with 6 people waiting"),
'615_GrapeSt' : Room(title='615_GrapeSt', description="You are at an intersection, please go left or right"),



'511_ParkSt' : Room(title='511_ParkSt', description="You are currently at 511 Park Street there are no bustops or intersections. Please drive forward"),
'512_ParkSt' : Room(title='512_ParkSt', description="You are currently at 512 Park Street there are no bustops or intersections. Please drive forward"),
'513_ParkSt' : Room(title='513_ParkSt', description="You are currently at 513 Park Street there are no bustops or intersections. Please drive forward"),
'514_ParkSt' : Room(title='514_ParkSt', description="There is an empty bus stop to your right."),
'515_ParkSt' : Room(title='515_ParkSt', description="You are at an intersection, please go left or right"),


'411_LakeSt' : Room(title='411_LakeSt', description="You are currently at 411 Lake Street there are no bustops or intersections. Please drive forward"),
'412_LakeSt' : Room(title='412_LakeSt', description="You are currently at 412 Lake Street there are no bustops or intersections. Please drive forward"),
'413_LakeSt' : Room(title='413_LakeSt', description="You are currently at 413 Lake Street there are no bustops or intersections. Please drive forward"),
'414_LakeSt' : Room(title='414_LakeSt', description="There is an empty bus stop to your right."),
'415_LakeSt' : Room(title='415_LakeSt', description="You are at an intersection, please go left or right"),


'311_MagnoliaSt' : Room(title='311_MagnoliaSt', description="You are currently at 311 Magnolia Street there are no bustops or intersections. Please drive forward"),
'312_MagnoliaSt' : Room(title='312_MagnoliaSt', description="You are currently at 312 Magnolia Street there is an intersection to your right with an empty bus stop"),
'313_MagnoliaSt' : Room(title='313_MagnoliaSt', description="You are currently at 313 Magnolia Street there are no bustops or intersections. Please drive forward"),
'314_MagnoliaSt' : Room(title='314_MagnoliaSt', description="You are currently at 314 Magnolia Street there are no bustops or intersections. Please drive forward"),
'315_MagnoliaSt' : Room(title='315_MagnoliaSt', description="You are at an intersection, please go left or right"),


'211_SunsetSt' : Room(title='211_SunsetSt', description="You are currently at 211 Sunset Street there are no bustops or intersections. Please drive forward"),
'212_SunsetSt' : Room(title='212_SunsetSt', description="You are currently at 212 Sunset Street there are no bustops or intersections. Please drive forward"),
'213_SunsetSt' : Room(title='213_SunsetSt', description="You are currently at 213 Sunset Street there are no bustops or intersections. Please drive forward"),
'214_SunsetSt' : Room(title='214_SunsetSt', description="There is a bustop to your right with 6 people waiting"),
'215_SunsetSt' : Room(title='215_SunsetSt', description="You are at an intersection, please go left or right"),


'111_ApacheSt' : Room(title='111_ApacheSt', description="You are currently at 111 Apache Street there are no bustops or intersections. Please drive forward"),
'112_ApacheSt' : Room(title='112_ApacheSt', description="You are currently at 112 Apache Street there is an intersection to your right with an empty bus stop"),
'113_ApacheSt' : Room(title='113_ApacheSt', description="You are currently at 113 Apache Street there are no bustops or intersections. Please drive forward"),
'114_ApacheSt' : Room(title='114_ApacheSt', description="There is a bustop to your right with 5 people waiting"),
'115_ApacheSt' : Room(title='115_ApacheSt', description="You are at an intersection, please go left or right" ),


'011_AirportSt' : Room(title='011_AirportSt', description="You are currently at 011 Airport Street there are no bustops or intersections. Please drive forward"),
'012_AirportSt' : Room(title='012_AirportSt', description="You are currently at 012 Airport Street there is an intersection to your right with an empty bus stop"),
'013_AirportSt' : Room(title='013_AirportSt', description="You are currently at 013 Airport Street there are no bustops or intersections. Please drive forward"),
'014_AirportSt' : Room(title='014_AirportSt', description="We are at the airport."),
'015_AirportSt' : Room(title='015_AirportSt', description="There is a bus stop to your left with 2 people waiting"),

'1001_DrewSt' : Room(title="1001_DrewSt", description="You are now ready to start driving. Please drive forward"),
'1002_DrewSt' : Room(title="1002_DrewSt", description="You are currently at 1002 Drew Street there are no bustops or intersections. Please drive forward"),
'1003_DrewSt' : Room(title="1003_DrewSt", description="There is a bustop to your right with 2 people waiting. Pick up the passengers and drop them off according to their instructions"), 
'1004_DrewSt' : Room(title="1004_DrewSt", description="You are currently at 1004 Drew Street there are no bustops or intersections. Please drive forward"),
'1005_DrewSt' : Room(title="1005_DrewSt", description="You are at an intersection, please go left or right"),


'1101_MangoSt' : Room(title="1101_MangoSt", description="There is an empty bustop to your right."),
'1102_MangoSt' : Room(title="1102_MangoSt", description="You are currently at 1102 Mango Street there are no bustops or intersections. Please drive forward"),
'1103_MangoSt' : Room(title="1103_MangoSt", description="You are currently at 1103 Mango Street there are no bustops or intersections. Please drive forward"),
'1104_MangoSt' : Room(title="1104_MangoSt", description="You are currently at 1104 Mango Street there are no bustops or intersections. Please drive forward"),
'1105_MangoSt' :  Room(title="1105_MangoSt", description="You are at an intersection, please go left or right"),


'1201_WashingtonSt' : Room(title="1201_WashingtonSt", description="You are currently at 1201 Washington Street there are no bustops or intersections. Please drive forward"),
'1202_WashingtonSt' : Room(title="1202_WashingtonSt", description="There is a bustop to your right with 4 people waiting"),
'1203_WashingtonSt' : Room(title="1203_WashingtonSt", description="You are currently at 1203 Washington Street there are no bustops or intersections. Please drive forward"),
'1204_WashingtonSt' : Room(title="1204_WashingtonSt", description="You are currently at 1204 Washington Street there are no bustops or intersections. Please drive forward"),
'1205_WashingtonSt' : Room(title="1205_WashingtonSt", description="You are at an intersection, please go left or right"),


'1301_LincolnSt' : Room(title="1301_LincolnSt", description="You are currently at 1301 Lincoln Street there are no bustops or intersections. Please drive forward"),
'1302_LincolnSt' : Room(title="1302_LincolnSt", description="There is an empty bus stop to your right."),
'1303_LincolnSt' : Room(title="1303_LincolnSt", description="You are currently at 1303 Lincoln Street there are no bustops or intersections. Please drive forward"),
'1304_LincolnSt' : Room(title="1304_LincolnSt", description = "There is a bustop to your right with 6 people waiting"),
'1305_LincolnSt' : Room(title="1305 LincolnSt", description="You are at an intersection, please go left or right"),


'1401_HamiltonSt' : Room(title="1401_HamiltonSt", description="You are currently at 1401 Hamilton Street there are no bustops or intersections. Please drive forward"),
'1402_HamiltonSt' : Room(title="1402_HamiltonSt", description="You are currently at 1402 Hamilton Street there are no bustops or intersections. Please drive forward"),
'1403_HamiltonSt' : Room(title="1403_HamiltonSt", description="You are currently at 1403 Hamilton Street there are no bustops or intersections. Please drive forward"),
'1404_HamiltonSt' : Room(title="1404_HamiltonSt", description="There is an empty bus stop to your right."),
'1405_HamiltonSt' : Room(title="1405_HamiltonSt", description="You are at an intersection, please go left or right"),


'1501_GrahamSt' : Room(title="1501_GrahamSt", description="You are currently at 1501 Graham Street there are no bustops or intersections. Please drive forward"),
'1502_GrahamSt' : Room(title="1502_GrahamSt", description="You are currently at 1502 Graham Street there are no bustops or intersections. Please drive forward"),
'1503_GrahamSt' : Room(title="1503_GrahamSt", description="You are currently at 1503 Graham Street there are no bustops or intersections. Please drive forward"),
'1504_GrahamSt' : Room(title="1504_GrahamSt", description="There is an empty bus stop to your right."),
'1505_GrahamSt' : Room(title="1505_GrahamSt", description="You are at an intersection, please go left or right"),


'1601_OrchidSt' : Room(title="1601_OrchidSt", description="You are currently at 1601 Orchid Street there are no bustops or intersections. Please drive forward"),
'1602_OrchidSt' : Room(title="1602_OrchidSt", description="You are currently at 1602 Orchid Street there is an intersection to your right with an empty bus stop"),
'1603_OrchidSt' : Room(title="1603_OrchidSt", description="You are currently at 1603 Orchid Street there are no bustops or intersections. Please drive forward"),
'1604_OrchidSt' : Room(title="1604_OrchidSt", description="You are currently at 1604 Orchid Street there are no bustops or intersections. Please drive forward"),
'1605_OrchidSt' : Room(title="1605_OrchidSt", description="You are at an intersection, please go left or right"),


'1701_SunriseSt' : Room(title="1701_SunriseSt", description="You are currently at 1701 Sunrise Street there are no bustops or intersections. Please drive forward"),
'1702_SunriseSt' : Room(title="1702_SunriseSt", description="You are currently at 1702 Sunrise Street there are no bustops or intersections. Please drive forward"),
'1703_SunriseSt' : Room(title="1703_SunriseSt", description="You are currently at 1703 Sunrise Street there are no bustops or intersections. Please drive forward"),
'1704_SunriseSt' : Room(title="1704_SunriseSt", description="There is a bustop to your right with 6 people waiting"),
'1705_SunriseSt' : Room(title="1705_SunriseSt", description="You are at an intersection, please go left or right"),


'1801_PoppySt' : Room(title="1801_PoppySt", description="You are currently at 1801 Poppy Street there are no bustops or intersections. Please drive forward"),
'1802_PoppySt' : Room(title="1802_PoppySt", description="You are currently at 1802 Poppy Street there is an intersection to your right with an empty bus stop"),
'1803_PoppySt' : Room(title="1803_PoppySt", description="You are currently at 1803 Poppy Street there are no bustops or intersections. Please drive forward"),
'1804_PoppySt' : Room(title="1804_PoppySt", description="There is a bustop to your right with 5 people waiting"),
'1805_PoppySt' : Room(title="1805_PoppySt", description="You are at an intersection, please go left or right"),


'1901_JacksonSt' : Room(title="1901_JacksonSt", description="You are currently at 1901 Jackson Street there are no bustops or intersections. Please drive forward"),
'1902_JacksonSt' : Room(title="1902_JacksonSt", description="You are currently at 1902 Jackson Street there is an intersection to your right with an empty bus stop"),
'1903_JacksonSt' : Room(title="1903_JacksonSt", description="You are currently at 1903 Jackson Street there are no bustops or intersections. Please drive forward"),
'1904_JacksonSt' : Room(title="1904_JacksonSt", description="We are at the airport."),
'1905_JacksonSt' : Room(title="1905_JacksonSt", description="There is a bus stop to your left with 2 people waiting"),

}

#for i in room:
 #   i.save()
move_map = {
    "n": "n_to",
    "s": "s_to",
    "e": "e_to",
    "w": "w_to" 
}

room['912_MainSt'].connectRooms(room['913_MainSt'], 'n_to')
room['911_MainSt'].connectRooms(room['912_MainSt'], 'n_to')
room['913_MainSt'].connectRooms(room['914_MainSt'], 'n_to')
room['914_MainSt'].connectRooms(room['915_MainSt'], 'n_to')

room['915_MainSt'].connectRooms(room['914_MainSt'], 's_to')
room['914_MainSt'].connectRooms(room['913_MainSt'], 's_to')
room['913_MainSt'].connectRooms(room['912_MainSt'], 's_to')
room['912_MainSt'].connectRooms(room['911_MainSt'], 's_to')

room['915_MainSt'].connectRooms(room['811_SouthSt'], 'e_to')
room['811_SouthSt'].connectRooms(room['915_MainSt'], 'w_to')

room['811_SouthSt'].connectRooms(room['812_SouthSt'], 'n_to')
room['812_SouthSt'].connectRooms(room['813_SouthSt'], 'n_to')
room['813_SouthSt'].connectRooms(room['814_SouthSt'], 'n_to')
room['814_SouthSt'].connectRooms(room['815_SouthSt'], 'n_to')

room['815_SouthSt'].connectRooms(room['814_SouthSt'], 's_to')
room['814_SouthSt'].connectRooms(room['813_SouthSt'], 's_to')
room['813_SouthSt'].connectRooms(room['812_SouthSt'], 's_to')
room['812_SouthSt'].connectRooms(room['811_SouthSt'], 's_to')

room['815_SouthSt'].connectRooms(room['711_FrontSt'], 'w_to')
room['711_FrontSt'].connectRooms(room['815_SouthSt'], 'e_to')

room['711_FrontSt'].connectRooms(room['712_FrontSt'], 'n_to')
room['712_FrontSt'].connectRooms(room['713_FrontSt'], 'n_to')
room['713_FrontSt'].connectRooms(room['714_FrontSt'], 'n_to')
room['714_FrontSt'].connectRooms(room['715_FrontSt'], 'n_to')

room['715_FrontSt'].connectRooms(room['714_FrontSt'], 's_to')
room['714_FrontSt'].connectRooms(room['713_FrontSt'], 's_to')
room['713_FrontSt'].connectRooms(room['712_FrontSt'], 's_to')
room['712_FrontSt'].connectRooms(room['711_FrontSt'], 's_to')

room['715_FrontSt'].connectRooms(room['611_GrapeSt'], 'e_to')
room['611_GrapeSt'].connectRooms(room['715_FrontSt'], 'w_to')

room['611_GrapeSt'].connectRooms(room['612_GrapeSt'], 'n_to')
room['612_GrapeSt'].connectRooms(room['613_GrapeSt'], 'n_to')
room['613_GrapeSt'].connectRooms(room['614_GrapeSt'], 'n_to')
room['614_GrapeSt'].connectRooms(room['615_GrapeSt'], 'n_to')

room['615_GrapeSt'].connectRooms(room['614_GrapeSt'], 's_to')
room['614_GrapeSt'].connectRooms(room['613_GrapeSt'], 's_to')
room['613_GrapeSt'].connectRooms(room['612_GrapeSt'], 's_to')
room['612_GrapeSt'].connectRooms(room['611_GrapeSt'], 's_to')

room['615_GrapeSt'].connectRooms(room['511_ParkSt'], 'e_to')
room['511_ParkSt'].connectRooms(room['615_GrapeSt'], 'w_to')

room['511_ParkSt'].connectRooms(room['512_ParkSt'], 'n_to')
room['512_ParkSt'].connectRooms(room['513_ParkSt'], 'n_to')
room['513_ParkSt'].connectRooms(room['514_ParkSt'], 'n_to')
room['514_ParkSt'].connectRooms(room['515_ParkSt'], 'n_to')

room['515_ParkSt'].connectRooms(room['514_ParkSt'], 's_to')
room['514_ParkSt'].connectRooms(room['513_ParkSt'], 's_to')
room['513_ParkSt'].connectRooms(room['512_ParkSt'], 's_to')
room['512_ParkSt'].connectRooms(room['511_ParkSt'], 's_to')

room['515_ParkSt'].connectRooms(room['411_LakeSt'], 'w_to')
room['411_LakeSt'].connectRooms(room['515_ParkSt'], 'e_to')

room['411_LakeSt'].connectRooms(room['412_LakeSt'], 'n_to')
room['412_LakeSt'].connectRooms(room['413_LakeSt'], 'n_to')
room['413_LakeSt'].connectRooms(room['414_LakeSt'], 'n_to')
room['414_LakeSt'].connectRooms(room['415_LakeSt'], 'n_to')

room['415_LakeSt'].connectRooms(room['414_LakeSt'], 's_to')
room['414_LakeSt'].connectRooms(room['413_LakeSt'], 's_to')
room['413_LakeSt'].connectRooms(room['412_LakeSt'], 's_to')
room['412_LakeSt'].connectRooms(room['411_LakeSt'], 's_to')

room['415_LakeSt'].connectRooms(room['311_MagnoliaSt'], 'e_to')
room['311_MagnoliaSt'].connectRooms(room['415_LakeSt'], 'w_to')

room['311_MagnoliaSt'].connectRooms(room['312_MagnoliaSt'], 'n_to')
room['312_MagnoliaSt'].connectRooms(room['313_MagnoliaSt'], 'n_to')
room['313_MagnoliaSt'].connectRooms(room['314_MagnoliaSt'], 'n_to')
room['314_MagnoliaSt'].connectRooms(room['315_MagnoliaSt'], 'n_to')

room['315_MagnoliaSt'].connectRooms(room['314_MagnoliaSt'], 's_to')
room['314_MagnoliaSt'].connectRooms(room['313_MagnoliaSt'], 's_to')
room['313_MagnoliaSt'].connectRooms(room['312_MagnoliaSt'], 's_to')
room['312_MagnoliaSt'].connectRooms(room['311_MagnoliaSt'], 's_to')

room['315_MagnoliaSt'].connectRooms(room['211_SunsetSt'], 'w_to')
room['211_SunsetSt'].connectRooms(room['315_MagnoliaSt'], 'e_to')

room['211_SunsetSt'].connectRooms(room['212_SunsetSt'], 'n_to')
room['212_SunsetSt'].connectRooms(room['213_SunsetSt'], 'n_to')
room['213_SunsetSt'].connectRooms(room['214_SunsetSt'], 'n_to')
room['214_SunsetSt'].connectRooms(room['215_SunsetSt'], 'n_to')

room['215_SunsetSt'].connectRooms(room['214_SunsetSt'], 's_to')
room['214_SunsetSt'].connectRooms(room['213_SunsetSt'], 's_to')
room['213_SunsetSt'].connectRooms(room['212_SunsetSt'], 's_to')
room['212_SunsetSt'].connectRooms(room['211_SunsetSt'], 's_to')

room['215_SunsetSt'].connectRooms(room['111_ApacheSt'], 'w_to')
room['111_ApacheSt'].connectRooms(room['215_SunsetSt'], 'e_to')

room['111_ApacheSt'].connectRooms(room['112_ApacheSt'], 'n_to')
room['112_ApacheSt'].connectRooms(room['113_ApacheSt'], 'n_to')
room['113_ApacheSt'].connectRooms(room['114_ApacheSt'], 'n_to')
room['114_ApacheSt'].connectRooms(room['115_ApacheSt'], 'n_to')

room['115_ApacheSt'].connectRooms(room['114_ApacheSt'], 's_to')
room['114_ApacheSt'].connectRooms(room['113_ApacheSt'], 's_to')
room['113_ApacheSt'].connectRooms(room['112_ApacheSt'], 's_to')
room['112_ApacheSt'].connectRooms(room['111_ApacheSt'], 's_to')

room['115_ApacheSt'].connectRooms(room['011_AirportSt'], 'e_to')
room['011_AirportSt'].connectRooms(room['115_ApacheSt'], 'w_to')

room['011_AirportSt'].connectRooms(room['012_AirportSt'], 'n_to')
room['012_AirportSt'].connectRooms(room['013_AirportSt'], 'n_to')
room['013_AirportSt'].connectRooms(room['014_AirportSt'], 'n_to')
room['014_AirportSt'].connectRooms(room['015_AirportSt'], 'n_to')

room['015_AirportSt'].connectRooms(room['014_AirportSt'], 's_to')
room['014_AirportSt'].connectRooms(room['013_AirportSt'], 's_to')
room['013_AirportSt'].connectRooms(room['012_AirportSt'], 's_to')
room['012_AirportSt'].connectRooms(room['011_AirportSt'], 's_to')

room['015_AirportSt'].connectRooms(room['1001_DrewSt'], 'w_to')
room['1001_DrewSt'].connectRooms(room['015_AirportSt'], 'e_to')

room['1001_DrewSt'].connectRooms(room['1002_DrewSt'], 'n_to')
room['1002_DrewSt'].connectRooms(room['1003_DrewSt'], 'n_to')
room['1003_DrewSt'].connectRooms(room['1004_DrewSt'], 'n_to')
room['1004_DrewSt'].connectRooms(room['1005_DrewSt'], 'n_to')

room['1005_DrewSt'].connectRooms(room['1004_DrewSt'], 's_to')
room['1004_DrewSt'].connectRooms(room['1003_DrewSt'], 's_to')
room['1003_DrewSt'].connectRooms(room['1002_DrewSt'], 's_to')
room['1002_DrewSt'].connectRooms(room['1001_DrewSt'], 's_to')

room['1005_DrewSt'].connectRooms(room['1101_MangoSt'], 'e_to')
room['1101_MangoSt'].connectRooms(room['1005_DrewSt'], 'w_to')

room['1101_MangoSt'].connectRooms(room['1102_MangoSt'], 'n_to')
room['1102_MangoSt'].connectRooms(room['1103_MangoSt'], 'n_to')
room['1103_MangoSt'].connectRooms(room['1104_MangoSt'], 'n_to')
room['1104_MangoSt'].connectRooms(room['1105_MangoSt'], 'n_to')

room['1105_MangoSt'].connectRooms(room['1104_MangoSt'], 's_to')
room['1104_MangoSt'].connectRooms(room['1103_MangoSt'], 's_to')
room['1103_MangoSt'].connectRooms(room['1102_MangoSt'], 's_to')
room['1102_MangoSt'].connectRooms(room['1101_MangoSt'], 's_to')

room['1105_MangoSt'].connectRooms(room['1201_WashingtonSt'], 'w_to')
room['1201_WashingtonSt'].connectRooms(room['1105_MangoSt'], 'e_to')

room['1201_WashingtonSt'].connectRooms(room['1202_WashingtonSt'], 'n_to')
room['1202_WashingtonSt'].connectRooms(room['1203_WashingtonSt'], 'n_to')
room['1203_WashingtonSt'].connectRooms(room['1204_WashingtonSt'], 'n_to')
room['1204_WashingtonSt'].connectRooms(room['1205_WashingtonSt'], 'n_to')

room['1205_WashingtonSt'].connectRooms(room['1204_WashingtonSt'],'s_to')
room['1204_WashingtonSt'].connectRooms(room['1203_WashingtonSt'], 's_to')
room['1203_WashingtonSt'].connectRooms(room['1202_WashingtonSt'], 's_to')
room['1202_WashingtonSt'].connectRooms(room['1201_WashingtonSt'], 's_to')

room['1205_WashingtonSt'].connectRooms(room['1301_LincolnSt'], 'e_to')
room['1301_LincolnSt'].connectRooms(room['1205_WashingtonSt'], 'w_to')

room['1301_LincolnSt'].connectRooms(room['1302_LincolnSt'], 'n_to')
room['1302_LincolnSt'].connectRooms(room['1303_LincolnSt'], 'n_to')
room['1303_LincolnSt'].connectRooms(room['1304_LincolnSt'], 'n_to')
room['1304_LincolnSt'].connectRooms(room['1305_LincolnSt'], 'n_to')

room['1305_LincolnSt'].connectRooms(room['1304_LincolnSt'], 's_to')
room['1304_LincolnSt'].connectRooms(room['1303_LincolnSt'], 's_to')
room['1303_LincolnSt'].connectRooms(room['1302_LincolnSt'], 's_to')
room['1302_LincolnSt'].connectRooms(room['1301_LincolnSt'], 's_to')

room['1305_LincolnSt'].connectRooms(room['1401_HamiltonSt'], 'e_to')
room['1401_HamiltonSt'].connectRooms(room['1305_LincolnSt'], 'w_to')

room['1401_HamiltonSt'].connectRooms(room['1402_HamiltonSt'], 'n_to')
room['1402_HamiltonSt'].connectRooms(room['1403_HamiltonSt'], 'n_to')
room['1403_HamiltonSt'].connectRooms(room['1404_HamiltonSt'], 'n_to')
room['1404_HamiltonSt'].connectRooms(room['1405_HamiltonSt'], 'n_to')

room['1405_HamiltonSt'].connectRooms(room['1404_HamiltonSt'], 's_to')
room['1404_HamiltonSt'].connectRooms(room['1403_HamiltonSt'], 's_to')
room['1403_HamiltonSt'].connectRooms(room['1402_HamiltonSt'], 's_to')
room['1402_HamiltonSt'].connectRooms(room['1401_HamiltonSt'], 's_to')

room['1405_HamiltonSt'].connectRooms(room['1501_GrahamSt'], 'w_to)
room['1501_GrahamSt'].connectRooms(room['1405_HamiltonSt'], 'e_to)

room['1501_GrahamSt'].connectRooms(room['1502_GrahamSt'], 'n_to')
room['1502_GrahamSt'].connectRooms(room['1503_GrahamSt'], 'n_to')
room['1503_GrahamSt'].connectRooms(room['1504_GrahamSt'], 'n_to')
room['1504_GrahamSt'].connectRooms(room['1505_GrahamSt'], 'n_to')

room['1505_GrahamSt'].connectRooms(room['1504_GrahamSt'], 's_to')
room['1504_GrahamSt'].connectRooms(room['1503_GrahamSt'], 's_to')
room['1503_GrahamSt'].connectRooms(room['1502_GrahamSt'], 's_to')
room['1502_GrahamSt'].connectRooms(room['1501_GrahamSt'], 's_to')

room['1505_GrahamSt'].connectRooms(room['1601_OrchidSt'], 'e_to')
room['1601_OrchidSt'].connectRooms(room['1505_GrahamSt'], 'w_to')

room['1601_OrchidSt'].connectRooms(room['1602_OrchidSt'], 'n_to')
room['1602_OrchidSt'].connectRooms(room['1603_OrchidSt'], 'n_to')
room['1603_OrchidSt'].connectRooms(room['1604_OrchidSt'], 'n_to')
room['1604_OrchidSt'].connectRooms(room['1605_OrchidSt'], 'n_to')

room['1605_OrchidSt'].connectRooms(room['1604_OrchidSt'], 's_to')
room['1604_OrchidSt'].connectRooms(room['1603_OrchidSt'], 's_to')
room['1603_OrchidSt'].connectRooms(room['1602_OrchidSt'], 's_to')
room['1602_OrchidSt'].connectRooms(room['1601_OrchidSt'], 's_to')

room['1605_OrchidSt'].connectRooms(room['1701_SunriseSt'], 'w_to')
room['1701_SunriseSt'].connectRooms(room['1605_OrchidSt'], 'e_to')

room['1701_SunriseSt'].connectRooms(room['1702_SunriseSt'], 'n_to')
room['1702_SunriseSt'].connectRooms(room['1703_SunriseSt'], 'n_to')
room['1703_SunriseSt'].connectRooms(room['1704_SunriseSt'], 'n_to')
room['1704_SunriseSt'].connectRooms(room['1705_SunriseSt'], 'n_to')

room['1705_SunriseSt'].connectRooms(room['1704_SunriseSt'], 's_to')
room['1704_SunriseSt'].connectRooms(room['1703_SunriseSt'], 's_to')
room['1703_SunriseSt'].connectRooms(room['1702_SunriseSt'], 's_to')
room['1702_SunriseSt'].connectRooms(room['1701_SunriseSt'], 's_to')

room['1705_SunriseSt'].connectRooms(room['1801_PoppySt'], 'w_to')
room['1801_PoppySt'].connectRooms(room['1705_SunriseSt'], 'e_to')

room['1801_PoppySt'].connectRooms(room['1802_PoppySt'], 'n_to')
room['1802_PoppySt'].connectRooms(room['1803_PoppySt'], 'n_to')
room['1803_PoppySt'].connectRooms(room['1804_PoppySt'], 'n_to')
room['1804_PoppySt'].connectRooms(room['1805_PoppySt'], 'n_to')

room['1805_PoppySt'].connectRooms(room['1804_PoppySt'], 's_to')
room['1804_PoppySt'].connectRooms(room['1803_PoppySt'], 's_to')
room['1803_PoppySt'].connectRooms(room['1802_PoppySt'], 's_to')
room['1802_PoppySt'].connectRooms(room['1801_PoppySt'], s_to)

room['1805_PoppySt'].connectRooms(room['1901_JacksonSt'], 'e_to')
room['1901_JacksonSt'].connectRooms(room['1805_PoppySt'], 'w_to')

room['1901_JacksonSt'].connectRooms(room['1902_JacksonSt'], 'n_to')
room['1902_JacksonSt'].connectRooms(room['1903_JacksonSt'], 'n_to')
room['1903_JacksonSt'].connectRooms(room['1904_JacksonSt'], 'n_to')
room['1904_JacksonSt'].connectRooms(room['1905_JacksonSt'], 'n_to')

room['1905_JacksonSt'].connectRooms(room['1904_JacksonSt'], 's_to')
room['1904_JacksonSt'].connectRooms(room['1903_JacksonSt'], 's_to')
room['1903_JacksonSt'].connectRooms(room['1902_JacksonSt'], 's_to')
room['1902_JacksonSt'].connectRooms(room['1901_JacksonSt'], 's_to')


move_list = ['n', 'e', 's', 'w']
action_list = ['pickup', 'dropoff']

'''
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
        '''