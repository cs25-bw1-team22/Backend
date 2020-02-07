from adventure.models import Player, Room

# people = {
# 'Jahmir = Passenger("Jahmir", "811_SouthSt"),
# 'Zakariya = Passenger("Zakariya", "414_LakeSt"),
# 'Amaria = Passenger("Amaria", "414_LakeSt"),
# 'Melvin = Passenger("Melvin", "414_LakeSt"),
# 'Naraly = Passenger("Naraly", "414_LakeSt"),

# 'Shiro = Passenger("Shiro","612_GrapeSt"),
# 'Zelma = Passenger("Zelma", "012_AirportSt"),
# 'Roxen = Passenger("Roxen", "014_AirportSt"),
# 'Allaina = Passenger("Allaina", "514_ParkSt"),
# 'Urban = Passenger("Urban", "514_ParkSt"),

# 'Ayliana = Passenger("Ayliana", ""),
# 'Wallis = Passenger("Wallis", "312_MagnoliaSt"),
# 'Usman': Passenger("Usman", "312_MagnoliaSt"),
# 'Meral': Passenger("Meral", "414_LakeSt"),
# 'Angeliz = Passenger("Angeliz", "014_AirportSt"),

# 'Milagrace = Passenger("Milagrace", "012_AirportSt"),
# 'Alyssia = Passenger("Alyssia", "514_ParkSt"),
# 'Manelyk': Passenger("Manelyk", "811_SouthSt"),
# 'Aariyah': Passenger("Aariyah", ""),
# 'Torryn = Passenger("Torryn", ""),

# 'Hanny = Passenger("Hanny", "014_AirportSt"),
# 'Breslin = Passenger("Breslin", "012_AirportSt"),
# 'Sofiya': Passenger("Sofiya", "014_AirportSt"),
# 'Kalayla': Passenger("Kalayla", "612_GrapeSt"),
# 'Khylei = Passenger("Khylei", ""),

# }

# for p in people:
#     p.save()



s911_MainSt = Room(title="Starting Location", description="You are now ready to start driving. Please drive forward")
s912_MainSt = Room(title='912_MainSt', description="You are currently at 912 Main Street there are no bustops or intersections. Please drive forward")
s913_MainSt = Room(title='913_MainSt', description="There is a bustop to your right with 2 people waiting. Pick up the passengers and drop them off according to their instructions")
s914_MainSt = Room(title='914_MainSt', description="You are currently at 914 Main Street there are no bustops or intersections. Please drive forward")
s915_MainSt = Room(title='915_MainSt', description="You are at an intersection, please go left or right")

s811_SouthSt = Room(title='811_SouthSt', description="There is an empty bustop to your right.")
s812_SouthSt = Room(title='812_SouthSt', description="You are currently at 812 South Street there are no bustops or intersections. Please drive forward")
s813_SouthSt = Room(title='813_SouthSt', description="You are currently at 813 South Street there are no bustops or intersections. Please drive forward")
s814_SouthSt = Room(title='814_SouthSt', description="You are currently at 814 South Street there are no bustops or intersections. Please drive forward")
s815_SouthSt = Room(title='815_SouthSt', description="You are at an intersection, please go left or right")

s711_FrontSt =  Room(title='711_FrontSt', description="You are currently at 711 Front Street there are no bustops or intersections. Please drive forward")
s712_FrontSt = Room(title='712_FrontSt', description="There is a bustop to your right with 4 people waiting")
s713_FrontSt = Room(title='713_FrontSt', description="You are currently at 713 Front Street there are no bustops or intersections. Please drive forward")
s714_FrontSt = Room(title='714_FrontSt', description="You are currently at 714 Front Street there are no bustops or intersections. Please drive forward")
s715_FrontSt = Room(title='715_FrontSt', description="You are at an intersection, please go left or right")

s611_GrapeSt = Room(title='611_GrapeSt', description="You are currently at 611 Grape Street there are no bustops or intersections. Please drive forward")
s612_GrapeSt = Room(title='612_GrapeSt', description="There is an empty bus stop to your right.")
s613_GrapeSt = Room(title='613_GrapeSt', description="You are currently at 613 Grape Street there are no bustops or intersections. Please drive forward")
s614_GrapeSt = Room(title = '614_GrapeSt', description = "There is a bustop to your right with 6 people waiting")
s615_GrapeSt = Room(title='615_GrapeSt', description="You are at an intersection, please go left or right")


s511_ParkSt = Room(title='511_ParkSt', description="You are currently at 511 Park Street there are no bustops or intersections. Please drive forward")
s512_ParkSt = Room(title='512_ParkSt', description="You are currently at 512 Park Street there are no bustops or intersections. Please drive forward")
s513_ParkSt = Room(title='513_ParkSt', description="You are currently at 513 Park Street there are no bustops or intersections. Please drive forward")
s514_ParkSt = Room(title='514_ParkSt', description="There is an empty bus stop to your right.")
s515_ParkSt = Room(title='515_ParkSt', description="You are at an intersection, please go left or right")

s411_LakeSt = Room(title='411_LakeSt', description="You are currently at 411 Lake Street there are no bustops or intersections. Please drive forward")
s412_LakeSt = Room(title='412_LakeSt', description="You are currently at 412 Lake Street there are no bustops or intersections. Please drive forward")
s413_LakeSt = Room(title='413_LakeSt', description="You are currently at 413 Lake Street there are no bustops or intersections. Please drive forward")
s414_LakeSt = Room(title='414_LakeSt', description="There is an empty bus stop to your right.")
s415_LakeSt = Room(title='415_LakeSt', description="You are at an intersection, please go left or right")

s311_MagnoliaSt = Room(title='311_MagnoliaSt', description="You are currently at 311 Magnolia Street there are no bustops or intersections. Please drive forward")
s312_MagnoliaSt = Room(title='312_MagnoliaSt', description="You are currently at 312 Magnolia Street there is an intersection to your right with an empty bus stop")
s313_MagnoliaSt = Room(title='313_MagnoliaSt', description="You are currently at 313 Magnolia Street there are no bustops or intersections. Please drive forward")
s314_MagnoliaSt = Room(title='314_MagnoliaSt', description="You are currently at 314 Magnolia Street there are no bustops or intersections. Please drive forward")
s315_MagnoliaSt = Room(title='315_MagnoliaSt', description="You are at an intersection, please go left or right")

s211_SunsetSt = Room(title='211_SunsetSt', description="You are currently at 211 Sunset Street there are no bustops or intersections. Please drive forward")
s212_SunsetSt = Room(title='212_SunsetSt', description="You are currently at 212 Sunset Street there are no bustops or intersections. Please drive forward")
s213_SunsetSt = Room(title='213_SunsetSt', description="You are currently at 213 Sunset Street there are no bustops or intersections. Please drive forward")
s214_SunsetSt = Room(title='214_SunsetSt', description="There is a bustop to your right with 6 people waiting")
s215_SunsetSt = Room(title='215_SunsetSt', description="You are at an intersection, please go left or right")

s111_ApacheSt = Room(title='111_ApacheSt', description="You are currently at 111 Apache Street there are no bustops or intersections. Please drive forward")
s112_ApacheSt = Room(title='112_ApacheSt', description="You are currently at 112 Apache Street there is an intersection to your right with an empty bus stop")
s113_ApacheSt = Room(title='113_ApacheSt', description="You are currently at 113 Apache Street there are no bustops or intersections. Please drive forward")
s114_ApacheSt = Room(title='114_ApacheSt', description="There is a bustop to your right with 5 people waiting")
s115_ApacheSt = Room(title='115_ApacheSt', description="You are at an intersection, please go left or right" )

s011_AirportSt = Room(title='011_AirportSt', description="You are currently at 011 Airport Street there are no bustops or intersections. Please drive forward")
s012_AirportSt = Room(title='012_AirportSt', description="You are currently at 012 Airport Street there is an intersection to your right with an empty bus stop")
s013_AirportSt = Room(title='013_AirportSt', description="You are currently at 013 Airport Street there are no bustops or intersections. Please drive forward")
s014_AirportSt = Room(title='014_AirportSt', description="We are at the airport.")
s015_AirportSt = Room(title='015_AirportSt', description="There is a bus stop to your left with 2 people waiting")

s1001_DrewSt = Room(title="1001_DrewSt", description="You are now ready to start driving. Please drive forward")
s1002_DrewSt = Room(title="1002_DrewSt", description="You are currently at 1002 Drew Street there are no bustops or intersections. Please drive forward")
s1003_DrewSt = Room(title="1003_DrewSt", description="There is a bustop to your right with 2 people waiting. Pick up the passengers and drop them off according to their instructions")
s1004_DrewSt = Room(title="1004_DrewSt", description="You are currently at 1004 Drew Street there are no bustops or intersections. Please drive forward")
s1005_DrewSt = Room(title="1005_DrewSt", description="You are at an intersection, please go left or right")

s1101_MangoSt = Room(title="1101_MangoSt", description="There is an empty bustop to your right.")
s1102_MangoSt = Room(title="1102_MangoSt", description="You are currently at 1102 Mango Street there are no bustops or intersections. Please drive forward")
s1103_MangoSt = Room(title="1103_MangoSt", description="You are currently at 1103 Mango Street there are no bustops or intersections. Please drive forward")
s1104_MangoSt = Room(title="1104_MangoSt", description="You are currently at 1104 Mango Street there are no bustops or intersections. Please drive forward")
s1105_MangoSt =  Room(title="1105_MangoSt", description="You are at an intersection, please go left or right")

s1201_WashingtonSt = Room(title="1201_WashingtonSt", description="You are currently at 1201 Washington Street there are no bustops or intersections. Please drive forward")
s1202_WashingtonSt = Room(title="1202_WashingtonSt", description="There is a bustop to your right with 4 people waiting")
s1203_WashingtonSt = Room(title="1203_WashingtonSt", description="You are currently at 1203 Washington Street there are no bustops or intersections. Please drive forward")
s1204_WashingtonSt = Room(title="1204_WashingtonSt", description="You are currently at 1204 Washington Street there are no bustops or intersections. Please drive forward")
s1205_WashingtonSt = Room(title="1205_WashingtonSt", description="You are at an intersection, please go left or right")

s1301_LincolnSt = Room(title="1301_LincolnSt", description="You are currently at 1301 Lincoln Street there are no bustops or intersections. Please drive forward")
s1302_LincolnSt = Room(title="1302_LincolnSt", description="There is an empty bus stop to your right.")
s1303_LincolnSt = Room(title="1303_LincolnSt", description="You are currently at 1303 Lincoln Street there are no bustops or intersections. Please drive forward")
s1304_LincolnSt = Room(title="1304_LincolnSt", description = "There is a bustop to your right with 6 people waiting")
s1305_LincolnSt = Room(title="1305 LincolnSt", description="You are at an intersection, please go left or right")


s1401_HamiltonSt = Room(title="1401_HamiltonSt", description="You are currently at 1401 Hamilton Street there are no bustops or intersections. Please drive forward")
s1402_HamiltonSt = Room(title="1402_HamiltonSt", description="You are currently at 1402 Hamilton Street there are no bustops or intersections. Please drive forward")
s1403_HamiltonSt = Room(title="1403_HamiltonSt", description="You are currently at 1403 Hamilton Street there are no bustops or intersections. Please drive forward")
s1404_HamiltonSt = Room(title="1404_HamiltonSt", description="There is an empty bus stop to your right.")
s1405_HamiltonSt = Room(title="1405_HamiltonSt", description="You are at an intersection, please go left or right")


s1501_GrahamSt = Room(title="1501_GrahamSt", description="You are currently at 1501 Graham Street there are no bustops or intersections. Please drive forward")
s1502_GrahamSt = Room(title="1502_GrahamSt", description="You are currently at 1502 Graham Street there are no bustops or intersections. Please drive forward")
s1503_GrahamSt = Room(title="1503_GrahamSt", description="You are currently at 1503 Graham Street there are no bustops or intersections. Please drive forward")
s1504_GrahamSt = Room(title="1504_GrahamSt", description="There is an empty bus stop to your right.")
s1505_GrahamSt = Room(title="1505_GrahamSt", description="You are at an intersection, please go left or right")

s1601_OrchidSt = Room(title="1601_OrchidSt", description="You are currently at 1601 Orchid Street there are no bustops or intersections. Please drive forward")
s1602_OrchidSt = Room(title="1602_OrchidSt", description="You are currently at 1602 Orchid Street there is an intersection to your right with an empty bus stop")
s1603_OrchidSt = Room(title="1603_OrchidSt", description="You are currently at 1603 Orchid Street there are no bustops or intersections. Please drive forward")
s1604_OrchidSt = Room(title="1604_OrchidSt", description="You are currently at 1604 Orchid Street there are no bustops or intersections. Please drive forward")
s1605_OrchidSt = Room(title="1605_OrchidSt", description="You are at an intersection, please go left or right")



s1701_SunriseSt = Room(title="1701_SunriseSt", description="You are currently at 1701 Sunrise Street there are no bustops or intersections. Please drive forward")
s1702_SunriseSt = Room(title="1702_SunriseSt", description="You are currently at 1702 Sunrise Street there are no bustops or intersections. Please drive forward")
s1703_SunriseSt = Room(title="1703_SunriseSt", description="You are currently at 1703 Sunrise Street there are no bustops or intersections. Please drive forward")
s1704_SunriseSt = Room(title="1704_SunriseSt", description="There is a bustop to your right with 6 people waiting")
s1705_SunriseSt = Room(title="1705_SunriseSt", description="You are at an intersection, please go left or right")


s1801_PoppySt = Room(title="1801_PoppySt", description="You are currently at 1801 Poppy Street there are no bustops or intersections. Please drive forward")
s1802_PoppySt = Room(title="1802_PoppySt", description="You are currently at 1802 Poppy Street there is an intersection to your right with an empty bus stop")
s1803_PoppySt = Room(title="1803_PoppySt", description="You are currently at 1803 Poppy Street there are no bustops or intersections. Please drive forward")
s1804_PoppySt = Room(title="1804_PoppySt", description="There is a bustop to your right with 5 people waiting")
s1805_PoppySt = Room(title="1805_PoppySt", description="You are at an intersection, please go left or right")


s1901_JacksonSt = Room(title="1901_JacksonSt", description="You are currently at 1901 Jackson Street there are no bustops or intersections. Please drive forward")
s1902_JacksonSt = Room(title="1902_JacksonSt", description="You are currently at 1902 Jackson Street there is an intersection to your right with an empty bus stop")
s1903_JacksonSt = Room(title="1903_JacksonSt", description="You are currently at 1903 Jackson Street there are no bustops or intersections. Please drive forward")
s1904_JacksonSt = Room(title="1904_JacksonSt", description="We are at the airport.")
s1905_JacksonSt = Room(title="1905_JacksonSt", description="There is a bus stop to your left with 2 people waiting")

s1905_JacksonSt.save()
#for i in room:
 #   i.save()


s912_MainSt.connectRooms(s913_MainSt, 'n')
s911_MainSt.connectRooms(s912_MainSt, 'n')
s913_MainSt.connectRooms(s914_MainSt, 'n')
s914_MainSt.connectRooms(s915_MainSt, 'n')

s915_MainSt.connectRooms(s914_MainSt, 's')
s914_MainSt.connectRooms(s913_MainSt, 's')
s913_MainSt.connectRooms(s912_MainSt, 's')
s912_MainSt.connectRooms(s911_MainSt, 's')

s915_MainSt.connectRooms(s811_SouthSt, 'e')
s811_SouthSt.connectRooms(s915_MainSt, 'w')

s811_SouthSt.connectRooms(s812_SouthSt, 'n')
s812_SouthSt.connectRooms(s813_SouthSt, 'n')
s813_SouthSt.connectRooms(s814_SouthSt, 'n')
s814_SouthSt.connectRooms(s815_SouthSt, 'n')

s815_SouthSt.connectRooms(s814_SouthSt, 's')
s814_SouthSt.connectRooms(s813_SouthSt, 's')
s813_SouthSt.connectRooms(s812_SouthSt, 's')
s812_SouthSt.connectRooms(s811_SouthSt, 's')

s815_SouthSt.connectRooms(s711_FrontSt, 'w')
s711_FrontSt.connectRooms(s815_SouthSt, 'e')

s711_FrontSt.connectRooms(s712_FrontSt, 'n')
s712_FrontSt.connectRooms(s713_FrontSt, 'n')
s713_FrontSt.connectRooms(s714_FrontSt, 'n')
s714_FrontSt.connectRooms(s715_FrontSt, 'n')

s715_FrontSt.connectRooms(s714_FrontSt, 's')
s714_FrontSt.connectRooms(s713_FrontSt, 's')
s713_FrontSt.connectRooms(s712_FrontSt, 's')
s712_FrontSt.connectRooms(s711_FrontSt, 's')

s715_FrontSt.connectRooms(s611_GrapeSt, 'e')
s611_GrapeSt.connectRooms(s715_FrontSt, 'w')

s611_GrapeSt.connectRooms(s612_GrapeSt, 'n')
s612_GrapeSt.connectRooms(s613_GrapeSt, 'n')
s613_GrapeSt.connectRooms(s614_GrapeSt, 'n')
s614_GrapeSt.connectRooms(s615_GrapeSt, 'n')

s615_GrapeSt.connectRooms(s614_GrapeSt, 's')
s614_GrapeSt.connectRooms(s613_GrapeSt, 's')
s613_GrapeSt.connectRooms(s612_GrapeSt, 's')
s612_GrapeSt.connectRooms(s611_GrapeSt, 's')

s615_GrapeSt.connectRooms(s511_ParkSt, 'e')
s511_ParkSt.connectRooms(s615_GrapeSt, 'w')

s511_ParkSt.connectRooms(s512_ParkSt, 'n')
s512_ParkSt.connectRooms(s513_ParkSt, 'n')
s513_ParkSt.connectRooms(s514_ParkSt, 'n')
s514_ParkSt.connectRooms(s515_ParkSt, 'n')

s515_ParkSt.connectRooms(s514_ParkSt, 's')
s514_ParkSt.connectRooms(s513_ParkSt, 's')
s513_ParkSt.connectRooms(s512_ParkSt, 's')
s512_ParkSt.connectRooms(s511_ParkSt, 's')

s515_ParkSt.connectRooms(s411_LakeSt, 'w')
s411_LakeSt.connectRooms(s515_ParkSt, 'e')

s411_LakeSt.connectRooms(s412_LakeSt, 'n')
s412_LakeSt.connectRooms(s413_LakeSt, 'n')
s413_LakeSt.connectRooms(s414_LakeSt, 'n')
s414_LakeSt.connectRooms(s415_LakeSt, 'n')

s415_LakeSt.connectRooms(s414_LakeSt, 's')
s414_LakeSt.connectRooms(s413_LakeSt, 's')
s413_LakeSt.connectRooms(s412_LakeSt, 's')
s412_LakeSt.connectRooms(s411_LakeSt, 's')

s415_LakeSt.connectRooms(s311_MagnoliaSt, 'e')
s311_MagnoliaSt.connectRooms(s415_LakeSt, 'w')

s311_MagnoliaSt.connectRooms(s312_MagnoliaSt, 'n')
s312_MagnoliaSt.connectRooms(s313_MagnoliaSt, 'n')
s313_MagnoliaSt.connectRooms(s314_MagnoliaSt, 'n')
s314_MagnoliaSt.connectRooms(s315_MagnoliaSt, 'n')

s315_MagnoliaSt.connectRooms(s314_MagnoliaSt, 's')
s314_MagnoliaSt.connectRooms(s313_MagnoliaSt, 's')
s313_MagnoliaSt.connectRooms(s312_MagnoliaSt, 's')
s312_MagnoliaSt.connectRooms(s311_MagnoliaSt, 's')

s315_MagnoliaSt.connectRooms(s211_SunsetSt, 'w')
s211_SunsetSt.connectRooms(s315_MagnoliaSt, 'e')

s211_SunsetSt.connectRooms(s212_SunsetSt, 'n')
s212_SunsetSt.connectRooms(s213_SunsetSt, 'n')
s213_SunsetSt.connectRooms(s214_SunsetSt, 'n')
s214_SunsetSt.connectRooms(s215_SunsetSt, 'n')

s215_SunsetSt.connectRooms(s214_SunsetSt, 's')
s214_SunsetSt.connectRooms(s213_SunsetSt, 's')
s213_SunsetSt.connectRooms(s212_SunsetSt, 's')
s212_SunsetSt.connectRooms(s211_SunsetSt, 's')

s215_SunsetSt.connectRooms(s111_ApacheSt, 'w')
s111_ApacheSt.connectRooms(s215_SunsetSt, 'e')

s111_ApacheSt.connectRooms(s112_ApacheSt, 'n')
s112_ApacheSt.connectRooms(s113_ApacheSt, 'n')
s113_ApacheSt.connectRooms(s114_ApacheSt, 'n')
s114_ApacheSt.connectRooms(s115_ApacheSt, 'n')

s115_ApacheSt.connectRooms(s114_ApacheSt, 's')
s114_ApacheSt.connectRooms(s113_ApacheSt, 's')
s113_ApacheSt.connectRooms(s112_ApacheSt, 's')
s112_ApacheSt.connectRooms(s111_ApacheSt, 's')

s115_ApacheSt.connectRooms(s011_AirportSt, 'e')
s011_AirportSt.connectRooms(s115_ApacheSt, 'w')

s011_AirportSt.connectRooms(s012_AirportSt, 'n')
s012_AirportSt.connectRooms(s013_AirportSt, 'n')
s013_AirportSt.connectRooms(s014_AirportSt, 'n')
s014_AirportSt.connectRooms(s015_AirportSt, 'n')

s015_AirportSt.connectRooms(s014_AirportSt, 's')
s014_AirportSt.connectRooms(s013_AirportSt, 's')
s013_AirportSt.connectRooms(s012_AirportSt, 's')
s012_AirportSt.connectRooms(s011_AirportSt, 's')

s015_AirportSt.connectRooms(s1001_DrewSt, 'w')
s1001_DrewSt.connectRooms(s015_AirportSt, 'e')

s1001_DrewSt.connectRooms(s1002_DrewSt, 'n')
s1002_DrewSt.connectRooms(s1003_DrewSt, 'n')
s1003_DrewSt.connectRooms(s1004_DrewSt, 'n')
s1004_DrewSt.connectRooms(s1005_DrewSt, 'n')

s1005_DrewSt.connectRooms(s1004_DrewSt, 's')
s1004_DrewSt.connectRooms(s1003_DrewSt, 's')
s1003_DrewSt.connectRooms(s1002_DrewSt, 's')
s1002_DrewSt.connectRooms(s1001_DrewSt, 's')

s1005_DrewSt.connectRooms(s1101_MangoSt, 'e')
s1101_MangoSt.connectRooms(s1005_DrewSt, 'w')

s1101_MangoSt.connectRooms(s1102_MangoSt, 'n')
s1102_MangoSt.connectRooms(s1103_MangoSt, 'n')
s1103_MangoSt.connectRooms(s1104_MangoSt, 'n')
s1104_MangoSt.connectRooms(s1105_MangoSt, 'n')

s1105_MangoSt.connectRooms(s1104_MangoSt, 's')
s1104_MangoSt.connectRooms(s1103_MangoSt, 's')
s1103_MangoSt.connectRooms(s1102_MangoSt, 's')
s1102_MangoSt.connectRooms(s1101_MangoSt, 's')

s1105_MangoSt.connectRooms(s1201_WashingtonSt, 'w')
s1201_WashingtonSt.connectRooms(s1105_MangoSt, 'e')

s1201_WashingtonSt.connectRooms(s1202_WashingtonSt, 'n')
s1202_WashingtonSt.connectRooms(s1203_WashingtonSt, 'n')
s1203_WashingtonSt.connectRooms(s1204_WashingtonSt, 'n')
s1204_WashingtonSt.connectRooms(s1205_WashingtonSt, 'n')

s1205_WashingtonSt.connectRooms(s1204_WashingtonSt,'s')
s1204_WashingtonSt.connectRooms(s1203_WashingtonSt, 's')
s1203_WashingtonSt.connectRooms(s1202_WashingtonSt, 's')
s1202_WashingtonSt.connectRooms(s1201_WashingtonSt, 's')

s1205_WashingtonSt.connectRooms(s1301_LincolnSt, 'e')
s1301_LincolnSt.connectRooms(s1205_WashingtonSt, 'w')

s1301_LincolnSt.connectRooms(s1302_LincolnSt, 'n')
s1302_LincolnSt.connectRooms(s1303_LincolnSt, 'n')
s1303_LincolnSt.connectRooms(s1304_LincolnSt, 'n')
s1304_LincolnSt.connectRooms(s1305_LincolnSt, 'n')

s1305_LincolnSt.connectRooms(s1304_LincolnSt, 's')
s1304_LincolnSt.connectRooms(s1303_LincolnSt, 's')
s1303_LincolnSt.connectRooms(s1302_LincolnSt, 's')
s1302_LincolnSt.connectRooms(s1301_LincolnSt, 's')

s1305_LincolnSt.connectRooms(s1401_HamiltonSt, 'e')
s1401_HamiltonSt.connectRooms(s1305_LincolnSt, 'w')

s1401_HamiltonSt.connectRooms(s1402_HamiltonSt, 'n')
s1402_HamiltonSt.connectRooms(s1403_HamiltonSt, 'n')
s1403_HamiltonSt.connectRooms(s1404_HamiltonSt, 'n')
s1404_HamiltonSt.connectRooms(s1405_HamiltonSt, 'n')

s1405_HamiltonSt.connectRooms(s1404_HamiltonSt, 's')
s1404_HamiltonSt.connectRooms(s1403_HamiltonSt, 's')
s1403_HamiltonSt.connectRooms(s1402_HamiltonSt, 's')
s1402_HamiltonSt.connectRooms(s1401_HamiltonSt, 's')

s1405_HamiltonSt.connectRooms(s1501_GrahamSt, 'w')
s1501_GrahamSt.connectRooms(s1405_HamiltonSt, 'e')

s1501_GrahamSt.connectRooms(s1502_GrahamSt, 'n')
s1502_GrahamSt.connectRooms(s1503_GrahamSt, 'n')
s1503_GrahamSt.connectRooms(s1504_GrahamSt, 'n')
s1504_GrahamSt.connectRooms(s1505_GrahamSt, 'n')

s1505_GrahamSt.connectRooms(s1504_GrahamSt, 's')
s1504_GrahamSt.connectRooms(s1503_GrahamSt, 's')
s1503_GrahamSt.connectRooms(s1502_GrahamSt, 's')
s1502_GrahamSt.connectRooms(s1501_GrahamSt, 's')

s1505_GrahamSt.connectRooms(s1601_OrchidSt, 'e')
s1601_OrchidSt.connectRooms(s1505_GrahamSt, 'w')

s1601_OrchidSt.connectRooms(s1602_OrchidSt, 'n')
s1602_OrchidSt.connectRooms(s1603_OrchidSt, 'n')
s1603_OrchidSt.connectRooms(s1604_OrchidSt, 'n')
s1604_OrchidSt.connectRooms(s1605_OrchidSt, 'n')

s1605_OrchidSt.connectRooms(s1604_OrchidSt, 's')
s1604_OrchidSt.connectRooms(s1603_OrchidSt, 's')
s1603_OrchidSt.connectRooms(s1602_OrchidSt, 's')
s1602_OrchidSt.connectRooms(s1601_OrchidSt, 's')

s1605_OrchidSt.connectRooms(s1701_SunriseSt, 'w')
s1701_SunriseSt.connectRooms(s1605_OrchidSt, 'e')

s1701_SunriseSt.connectRooms(s1702_SunriseSt, 'n')
s1702_SunriseSt.connectRooms(s1703_SunriseSt, 'n')
s1703_SunriseSt.connectRooms(s1704_SunriseSt, 'n')
s1704_SunriseSt.connectRooms(s1705_SunriseSt, 'n')

s1705_SunriseSt.connectRooms(s1704_SunriseSt, 's')
s1704_SunriseSt.connectRooms(s1703_SunriseSt, 's')
s1703_SunriseSt.connectRooms(s1702_SunriseSt, 's')
s1702_SunriseSt.connectRooms(s1701_SunriseSt, 's')

s1705_SunriseSt.connectRooms(s1801_PoppySt, 'w')
s1801_PoppySt.connectRooms(s1705_SunriseSt, 'e')

s1801_PoppySt.connectRooms(s1802_PoppySt, 'n')
s1802_PoppySt.connectRooms(s1803_PoppySt, 'n')
s1803_PoppySt.connectRooms(s1804_PoppySt, 'n')
s1804_PoppySt.connectRooms(s1805_PoppySt, 'n')

s1805_PoppySt.connectRooms(s1804_PoppySt, 's')
s1804_PoppySt.connectRooms(s1803_PoppySt, 's')
s1803_PoppySt.connectRooms(s1802_PoppySt, 's')
s1802_PoppySt.connectRooms(s1801_PoppySt, 's')

s1805_PoppySt.connectRooms(s1901_JacksonSt, 'e')
s1901_JacksonSt.connectRooms(s1805_PoppySt, 'w')

s1901_JacksonSt.connectRooms(s1902_JacksonSt, 'n')
s1902_JacksonSt.connectRooms(s1903_JacksonSt, 'n')
s1903_JacksonSt.connectRooms(s1904_JacksonSt, 'n')
s1904_JacksonSt.connectRooms(s1905_JacksonSt, 'n')

s1905_JacksonSt.connectRooms(s1904_JacksonSt, 's')
s1904_JacksonSt.connectRooms(s1903_JacksonSt, 's')
s1903_JacksonSt.connectRooms(s1902_JacksonSt, 's')
s1902_JacksonSt.connectRooms(s1901_JacksonSt, 's')

#for i in room:
 #   i.save()
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