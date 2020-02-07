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



911_MainSt = Room(title="Starting Location", description="You are now ready to start driving. Please drive forward"),
912_MainSt = Room(title='912_MainSt', description="You are currently at 912 Main Street there are no bustops or intersections. Please drive forward"),
913_MainSt = Room(title='913_MainSt', description="There is a bustop to your right with 2 people waiting. Pick up the passengers and drop them off according to their instructions"),
914_MainSt = Room(title='914_MainSt', description="You are currently at 914 Main Street there are no bustops or intersections. Please drive forward"),
915_MainSt = Room(title='915_MainSt', description="You are at an intersection, please go left or right"),



811_SouthSt = Room(title='811_SouthSt', description="There is an empty bustop to your right."),
812_SouthSt = Room(title='812_SouthSt', description="You are currently at 812 South Street there are no bustops or intersections. Please drive forward"),
813_SouthSt = Room(title='813_SouthSt', description="You are currently at 813 South Street there are no bustops or intersections. Please drive forward"),
814_SouthSt = Room(title='814_SouthSt', description="You are currently at 814 South Street there are no bustops or intersections. Please drive forward"),
815_SouthSt = Room(title='815_SouthSt', description="You are at an intersection, please go left or right"),



711_FrontSt =  Room(title='711_FrontSt', description="You are currently at 711 Front Street there are no bustops or intersections. Please drive forward"),
712_FrontSt = Room(title='712_FrontSt', description="There is a bustop to your right with 4 people waiting"),
713_FrontSt = Room(title='713_FrontSt', description="You are currently at 713 Front Street there are no bustops or intersections. Please drive forward"),
714_FrontSt = Room(title='714_FrontSt', description="You are currently at 714 Front Street there are no bustops or intersections. Please drive forward"),
715_FrontSt = Room(title='715_FrontSt', description="You are at an intersection, please go left or right"),



611_GrapeSt = Room(title='611_GrapeSt', description="You are currently at 611 Grape Street there are no bustops or intersections. Please drive forward"),
612_GrapeSt = Room(title='612_GrapeSt', description="There is an empty bus stop to your right."),
613_GrapeSt = Room(title='613_GrapeSt', description="You are currently at 613 Grape Street there are no bustops or intersections. Please drive forward"),
614_GrapeSt = Room(title = '614_GrapeSt', description = "There is a bustop to your right with 6 people waiting"),
615_GrapeSt = Room(title='615_GrapeSt', description="You are at an intersection, please go left or right"),



511_ParkSt = Room(title='511_ParkSt', description="You are currently at 511 Park Street there are no bustops or intersections. Please drive forward"),
512_ParkSt = Room(title='512_ParkSt', description="You are currently at 512 Park Street there are no bustops or intersections. Please drive forward"),
513_ParkSt = Room(title='513_ParkSt', description="You are currently at 513 Park Street there are no bustops or intersections. Please drive forward"),
514_ParkSt = Room(title='514_ParkSt', description="There is an empty bus stop to your right."),
515_ParkSt = Room(title='515_ParkSt', description="You are at an intersection, please go left or right"),


411_LakeSt = Room(title='411_LakeSt', description="You are currently at 411 Lake Street there are no bustops or intersections. Please drive forward"),
412_LakeSt = Room(title='412_LakeSt', description="You are currently at 412 Lake Street there are no bustops or intersections. Please drive forward"),
413_LakeSt = Room(title='413_LakeSt', description="You are currently at 413 Lake Street there are no bustops or intersections. Please drive forward"),
414_LakeSt = Room(title='414_LakeSt', description="There is an empty bus stop to your right."),
415_LakeSt = Room(title='415_LakeSt', description="You are at an intersection, please go left or right"),


311_MagnoliaSt = Room(title='311_MagnoliaSt', description="You are currently at 311 Magnolia Street there are no bustops or intersections. Please drive forward"),
312_MagnoliaSt = Room(title='312_MagnoliaSt', description="You are currently at 312 Magnolia Street there is an intersection to your right with an empty bus stop"),
313_MagnoliaSt = Room(title='313_MagnoliaSt', description="You are currently at 313 Magnolia Street there are no bustops or intersections. Please drive forward"),
314_MagnoliaSt = Room(title='314_MagnoliaSt', description="You are currently at 314 Magnolia Street there are no bustops or intersections. Please drive forward"),
315_MagnoliaSt = Room(title='315_MagnoliaSt', description="You are at an intersection, please go left or right"),


211_SunsetSt = Room(title='211_SunsetSt', description="You are currently at 211 Sunset Street there are no bustops or intersections. Please drive forward"),
212_SunsetSt = Room(title='212_SunsetSt', description="You are currently at 212 Sunset Street there are no bustops or intersections. Please drive forward"),
213_SunsetSt = Room(title='213_SunsetSt', description="You are currently at 213 Sunset Street there are no bustops or intersections. Please drive forward"),
214_SunsetSt = Room(title='214_SunsetSt', description="There is a bustop to your right with 6 people waiting"),
215_SunsetSt = Room(title='215_SunsetSt', description="You are at an intersection, please go left or right"),


111_ApacheSt = Room(title='111_ApacheSt', description="You are currently at 111 Apache Street there are no bustops or intersections. Please drive forward"),
112_ApacheSt = Room(title='112_ApacheSt', description="You are currently at 112 Apache Street there is an intersection to your right with an empty bus stop"),
113_ApacheSt = Room(title='113_ApacheSt', description="You are currently at 113 Apache Street there are no bustops or intersections. Please drive forward"),
114_ApacheSt = Room(title='114_ApacheSt', description="There is a bustop to your right with 5 people waiting"),
115_ApacheSt = Room(title='115_ApacheSt', description="You are at an intersection, please go left or right" ),


011_AirportSt = Room(title='011_AirportSt', description="You are currently at 011 Airport Street there are no bustops or intersections. Please drive forward"),
012_AirportSt = Room(title='012_AirportSt', description="You are currently at 012 Airport Street there is an intersection to your right with an empty bus stop"),
013_AirportSt = Room(title='013_AirportSt', description="You are currently at 013 Airport Street there are no bustops or intersections. Please drive forward"),
014_AirportSt = Room(title='014_AirportSt', description="We are at the airport."),
015_AirportSt = Room(title='015_AirportSt', description="There is a bus stop to your left with 2 people waiting"),

1001_DrewSt = Room(title="1001_DrewSt", description="You are now ready to start driving. Please drive forward"),
1002_DrewSt = Room(title="1002_DrewSt", description="You are currently at 1002 Drew Street there are no bustops or intersections. Please drive forward"),
1003_DrewSt = Room(title="1003_DrewSt", description="There is a bustop to your right with 2 people waiting. Pick up the passengers and drop them off according to their instructions"), 
1004_DrewSt = Room(title="1004_DrewSt", description="You are currently at 1004 Drew Street there are no bustops or intersections. Please drive forward"),
1005_DrewSt = Room(title="1005_DrewSt", description="You are at an intersection, please go left or right"),


1101_MangoSt = Room(title="1101_MangoSt", description="There is an empty bustop to your right."),
1102_MangoSt = Room(title="1102_MangoSt", description="You are currently at 1102 Mango Street there are no bustops or intersections. Please drive forward"),
1103_MangoSt = Room(title="1103_MangoSt", description="You are currently at 1103 Mango Street there are no bustops or intersections. Please drive forward"),
1104_MangoSt = Room(title="1104_MangoSt", description="You are currently at 1104 Mango Street there are no bustops or intersections. Please drive forward"),
1105_MangoSt =  Room(title="1105_MangoSt", description="You are at an intersection, please go left or right"),


1201_WashingtonSt = Room(title="1201_WashingtonSt", description="You are currently at 1201 Washington Street there are no bustops or intersections. Please drive forward"),
1202_WashingtonSt = Room(title="1202_WashingtonSt", description="There is a bustop to your right with 4 people waiting"),
1203_WashingtonSt = Room(title="1203_WashingtonSt", description="You are currently at 1203 Washington Street there are no bustops or intersections. Please drive forward"),
1204_WashingtonSt = Room(title="1204_WashingtonSt", description="You are currently at 1204 Washington Street there are no bustops or intersections. Please drive forward"),
1205_WashingtonSt = Room(title="1205_WashingtonSt", description="You are at an intersection, please go left or right"),


1301_LincolnSt = Room(title="1301_LincolnSt", description="You are currently at 1301 Lincoln Street there are no bustops or intersections. Please drive forward"),
1302_LincolnSt = Room(title="1302_LincolnSt", description="There is an empty bus stop to your right."),
1303_LincolnSt = Room(title="1303_LincolnSt", description="You are currently at 1303 Lincoln Street there are no bustops or intersections. Please drive forward"),
1304_LincolnSt = Room(title="1304_LincolnSt", description = "There is a bustop to your right with 6 people waiting"),
1305_LincolnSt = Room(title="1305 LincolnSt", description="You are at an intersection, please go left or right"),


1401_HamiltonSt = Room(title="1401_HamiltonSt", description="You are currently at 1401 Hamilton Street there are no bustops or intersections. Please drive forward"),
1402_HamiltonSt = Room(title="1402_HamiltonSt", description="You are currently at 1402 Hamilton Street there are no bustops or intersections. Please drive forward"),
1403_HamiltonSt = Room(title="1403_HamiltonSt", description="You are currently at 1403 Hamilton Street there are no bustops or intersections. Please drive forward"),
1404_HamiltonSt = Room(title="1404_HamiltonSt", description="There is an empty bus stop to your right."),
1405_HamiltonSt = Room(title="1405_HamiltonSt", description="You are at an intersection, please go left or right"),


1501_GrahamSt = Room(title="1501_GrahamSt", description="You are currently at 1501 Graham Street there are no bustops or intersections. Please drive forward"),
1502_GrahamSt = Room(title="1502_GrahamSt", description="You are currently at 1502 Graham Street there are no bustops or intersections. Please drive forward"),
1503_GrahamSt = Room(title="1503_GrahamSt", description="You are currently at 1503 Graham Street there are no bustops or intersections. Please drive forward"),
1504_GrahamSt = Room(title="1504_GrahamSt", description="There is an empty bus stop to your right."),
1505_GrahamSt = Room(title="1505_GrahamSt", description="You are at an intersection, please go left or right"),


1601_OrchidSt = Room(title="1601_OrchidSt", description="You are currently at 1601 Orchid Street there are no bustops or intersections. Please drive forward"),
1602_OrchidSt = Room(title="1602_OrchidSt", description="You are currently at 1602 Orchid Street there is an intersection to your right with an empty bus stop"),
1603_OrchidSt = Room(title="1603_OrchidSt", description="You are currently at 1603 Orchid Street there are no bustops or intersections. Please drive forward"),
1604_OrchidSt = Room(title="1604_OrchidSt", description="You are currently at 1604 Orchid Street there are no bustops or intersections. Please drive forward"),
1605_OrchidSt = Room(title="1605_OrchidSt", description="You are at an intersection, please go left or right"),


1701_SunriseSt = Room(title="1701_SunriseSt", description="You are currently at 1701 Sunrise Street there are no bustops or intersections. Please drive forward"),
1702_SunriseSt = Room(title="1702_SunriseSt", description="You are currently at 1702 Sunrise Street there are no bustops or intersections. Please drive forward"),
1703_SunriseSt = Room(title="1703_SunriseSt", description="You are currently at 1703 Sunrise Street there are no bustops or intersections. Please drive forward"),
1704_SunriseSt = Room(title="1704_SunriseSt", description="There is a bustop to your right with 6 people waiting"),
1705_SunriseSt = Room(title="1705_SunriseSt", description="You are at an intersection, please go left or right"),


1801_PoppySt = Room(title="1801_PoppySt", description="You are currently at 1801 Poppy Street there are no bustops or intersections. Please drive forward"),
1802_PoppySt = Room(title="1802_PoppySt", description="You are currently at 1802 Poppy Street there is an intersection to your right with an empty bus stop"),
1803_PoppySt = Room(title="1803_PoppySt", description="You are currently at 1803 Poppy Street there are no bustops or intersections. Please drive forward"),
1804_PoppySt = Room(title="1804_PoppySt", description="There is a bustop to your right with 5 people waiting"),
1805_PoppySt = Room(title="1805_PoppySt", description="You are at an intersection, please go left or right"),


1901_JacksonSt = Room(title="1901_JacksonSt", description="You are currently at 1901 Jackson Street there are no bustops or intersections. Please drive forward"),
1902_JacksonSt = Room(title="1902_JacksonSt", description="You are currently at 1902 Jackson Street there is an intersection to your right with an empty bus stop"),
1903_JacksonSt = Room(title="1903_JacksonSt", description="You are currently at 1903 Jackson Street there are no bustops or intersections. Please drive forward"),
1904_JacksonSt = Room(title="1904_JacksonSt", description="We are at the airport."),
1905_JacksonSt = Room(title="1905_JacksonSt", description="There is a bus stop to your left with 2 people waiting"),



#for i in room:
 #   i.save()


912_MainSt.connectRooms(913_MainSt, 'n')
911_MainSt.connectRooms(912_MainSt, 'n')
913_MainSt.connectRooms(914_MainSt, 'n')
914_MainSt.connectRooms(915_MainSt, 'n')

915_MainSt.connectRooms(914_MainSt, 's')
914_MainSt.connectRooms(913_MainSt, 's')
913_MainSt.connectRooms(912_MainSt, 's')
912_MainSt.connectRooms(911_MainSt, 's')

915_MainSt.connectRooms(811_SouthSt, 'e')
811_SouthSt.connectRooms(915_MainSt, 'w')

811_SouthSt.connectRooms(812_SouthSt, 'n')
812_SouthSt.connectRooms(813_SouthSt, 'n')
813_SouthSt.connectRooms(814_SouthSt, 'n')
814_SouthSt.connectRooms(815_SouthSt, 'n')

815_SouthSt.connectRooms(814_SouthSt, 's')
814_SouthSt.connectRooms(813_SouthSt, 's')
813_SouthSt.connectRooms(812_SouthSt, 's')
812_SouthSt.connectRooms(811_SouthSt, 's')

815_SouthSt.connectRooms(711_FrontSt, 'w')
711_FrontSt.connectRooms(815_SouthSt, 'e')

711_FrontSt.connectRooms(712_FrontSt, 'n')
712_FrontSt.connectRooms(713_FrontSt, 'n')
713_FrontSt.connectRooms(714_FrontSt, 'n')
714_FrontSt.connectRooms(715_FrontSt, 'n')

715_FrontSt.connectRooms(714_FrontSt, 's')
714_FrontSt.connectRooms(713_FrontSt, 's')
713_FrontSt.connectRooms(712_FrontSt, 's')
712_FrontSt.connectRooms(711_FrontSt, 's')

715_FrontSt.connectRooms(611_GrapeSt, 'e')
611_GrapeSt.connectRooms(715_FrontSt, 'w')

611_GrapeSt.connectRooms(612_GrapeSt, 'n')
612_GrapeSt.connectRooms(613_GrapeSt, 'n')
613_GrapeSt.connectRooms(614_GrapeSt, 'n')
614_GrapeSt.connectRooms(615_GrapeSt, 'n')

615_GrapeSt.connectRooms(614_GrapeSt, 's')
614_GrapeSt.connectRooms(613_GrapeSt, 's')
613_GrapeSt.connectRooms(612_GrapeSt, 's')
612_GrapeSt.connectRooms(611_GrapeSt, 's')

615_GrapeSt.connectRooms(511_ParkSt, 'e')
511_ParkSt.connectRooms(615_GrapeSt, 'w')

511_ParkSt.connectRooms(512_ParkSt, 'n')
512_ParkSt.connectRooms(513_ParkSt, 'n')
513_ParkSt.connectRooms(514_ParkSt, 'n')
514_ParkSt.connectRooms(515_ParkSt, 'n')

515_ParkSt.connectRooms(514_ParkSt, 's')
514_ParkSt.connectRooms(513_ParkSt, 's')
513_ParkSt.connectRooms(512_ParkSt, 's')
512_ParkSt.connectRooms(511_ParkSt, 's')

515_ParkSt.connectRooms(411_LakeSt, 'w')
411_LakeSt.connectRooms(515_ParkSt, 'e')

411_LakeSt.connectRooms(412_LakeSt, 'n')
412_LakeSt.connectRooms(413_LakeSt, 'n')
413_LakeSt.connectRooms(414_LakeSt, 'n')
414_LakeSt.connectRooms(415_LakeSt, 'n')

415_LakeSt.connectRooms(414_LakeSt, 's')
414_LakeSt.connectRooms(413_LakeSt, 's')
413_LakeSt.connectRooms(412_LakeSt, 's')
412_LakeSt.connectRooms(411_LakeSt, 's')

415_LakeSt.connectRooms(311_MagnoliaSt, 'e')
311_MagnoliaSt.connectRooms(415_LakeSt, 'w')

311_MagnoliaSt.connectRooms(312_MagnoliaSt, 'n')
312_MagnoliaSt.connectRooms(313_MagnoliaSt, 'n')
313_MagnoliaSt.connectRooms(314_MagnoliaSt, 'n')
314_MagnoliaSt.connectRooms(315_MagnoliaSt, 'n')

315_MagnoliaSt.connectRooms(314_MagnoliaSt, 's')
314_MagnoliaSt.connectRooms(313_MagnoliaSt, 's')
313_MagnoliaSt.connectRooms(312_MagnoliaSt, 's')
312_MagnoliaSt.connectRooms(311_MagnoliaSt, 's')

315_MagnoliaSt.connectRooms(211_SunsetSt, 'w')
211_SunsetSt.connectRooms(315_MagnoliaSt, 'e')

211_SunsetSt.connectRooms(212_SunsetSt, 'n')
212_SunsetSt.connectRooms(213_SunsetSt, 'n')
213_SunsetSt.connectRooms(214_SunsetSt, 'n')
214_SunsetSt.connectRooms(215_SunsetSt, 'n')

215_SunsetSt.connectRooms(214_SunsetSt, 's')
214_SunsetSt.connectRooms(213_SunsetSt, 's')
213_SunsetSt.connectRooms(212_SunsetSt, 's')
212_SunsetSt.connectRooms(211_SunsetSt, 's')

215_SunsetSt.connectRooms(111_ApacheSt, 'w')
111_ApacheSt.connectRooms(215_SunsetSt, 'e')

111_ApacheSt.connectRooms(112_ApacheSt, 'n')
112_ApacheSt.connectRooms(113_ApacheSt, 'n')
113_ApacheSt.connectRooms(114_ApacheSt, 'n')
114_ApacheSt.connectRooms(115_ApacheSt, 'n')

115_ApacheSt.connectRooms(114_ApacheSt, 's')
114_ApacheSt.connectRooms(113_ApacheSt, 's')
113_ApacheSt.connectRooms(112_ApacheSt, 's')
112_ApacheSt.connectRooms(111_ApacheSt, 's')

115_ApacheSt.connectRooms(011_AirportSt, 'e')
011_AirportSt.connectRooms(115_ApacheSt, 'w')

011_AirportSt.connectRooms(012_AirportSt, 'n')
012_AirportSt.connectRooms(013_AirportSt, 'n')
013_AirportSt.connectRooms(014_AirportSt, 'n')
014_AirportSt.connectRooms(015_AirportSt, 'n')

015_AirportSt.connectRooms(014_AirportSt, 's')
014_AirportSt.connectRooms(013_AirportSt, 's')
013_AirportSt.connectRooms(012_AirportSt, 's')
012_AirportSt.connectRooms(011_AirportSt, 's')

015_AirportSt.connectRooms(1001_DrewSt, 'w')
1001_DrewSt.connectRooms(015_AirportSt, 'e')

1001_DrewSt.connectRooms(1002_DrewSt, 'n')
1002_DrewSt.connectRooms(1003_DrewSt, 'n')
1003_DrewSt.connectRooms(1004_DrewSt, 'n')
1004_DrewSt.connectRooms(1005_DrewSt, 'n')

1005_DrewSt.connectRooms(1004_DrewSt, 's')
1004_DrewSt.connectRooms(1003_DrewSt, 's')
1003_DrewSt.connectRooms(1002_DrewSt, 's')
1002_DrewSt.connectRooms(1001_DrewSt, 's')

1005_DrewSt.connectRooms(1101_MangoSt, 'e')
1101_MangoSt.connectRooms(1005_DrewSt, 'w')

1101_MangoSt.connectRooms(1102_MangoSt, 'n')
1102_MangoSt.connectRooms(1103_MangoSt, 'n')
1103_MangoSt.connectRooms(1104_MangoSt, 'n')
1104_MangoSt.connectRooms(1105_MangoSt, 'n')

1105_MangoSt.connectRooms(1104_MangoSt, 's')
1104_MangoSt.connectRooms(1103_MangoSt, 's')
1103_MangoSt.connectRooms(1102_MangoSt, 's')
1102_MangoSt.connectRooms(1101_MangoSt, 's')

1105_MangoSt.connectRooms(1201_WashingtonSt, 'w')
1201_WashingtonSt.connectRooms(1105_MangoSt, 'e')

1201_WashingtonSt.connectRooms(1202_WashingtonSt, 'n')
1202_WashingtonSt.connectRooms(1203_WashingtonSt, 'n')
1203_WashingtonSt.connectRooms(1204_WashingtonSt, 'n')
1204_WashingtonSt.connectRooms(1205_WashingtonSt, 'n')

1205_WashingtonSt.connectRooms(1204_WashingtonSt,'s')
1204_WashingtonSt.connectRooms(1203_WashingtonSt, 's')
1203_WashingtonSt.connectRooms(1202_WashingtonSt, 's')
1202_WashingtonSt.connectRooms(1201_WashingtonSt, 's')

1205_WashingtonSt.connectRooms(1301_LincolnSt, 'e')
1301_LincolnSt.connectRooms(1205_WashingtonSt, 'w')

1301_LincolnSt.connectRooms(1302_LincolnSt, 'n')
1302_LincolnSt.connectRooms(1303_LincolnSt, 'n')
1303_LincolnSt.connectRooms(1304_LincolnSt, 'n')
1304_LincolnSt.connectRooms(1305_LincolnSt, 'n')

1305_LincolnSt.connectRooms(1304_LincolnSt, 's')
1304_LincolnSt.connectRooms(1303_LincolnSt, 's')
1303_LincolnSt.connectRooms(1302_LincolnSt, 's')
1302_LincolnSt.connectRooms(1301_LincolnSt, 's')

1305_LincolnSt.connectRooms(1401_HamiltonSt, 'e')
1401_HamiltonSt.connectRooms(1305_LincolnSt, 'w')

1401_HamiltonSt.connectRooms(1402_HamiltonSt, 'n')
1402_HamiltonSt.connectRooms(1403_HamiltonSt, 'n')
1403_HamiltonSt.connectRooms(1404_HamiltonSt, 'n')
1404_HamiltonSt.connectRooms(1405_HamiltonSt, 'n')

1405_HamiltonSt.connectRooms(1404_HamiltonSt, 's')
1404_HamiltonSt.connectRooms(1403_HamiltonSt, 's')
1403_HamiltonSt.connectRooms(1402_HamiltonSt, 's')
1402_HamiltonSt.connectRooms(1401_HamiltonSt, 's')

1405_HamiltonSt.connectRooms(1501_GrahamSt, 'w')
1501_GrahamSt.connectRooms(1405_HamiltonSt, 'e')

1501_GrahamSt.connectRooms(1502_GrahamSt, 'n')
1502_GrahamSt.connectRooms(1503_GrahamSt, 'n')
1503_GrahamSt.connectRooms(1504_GrahamSt, 'n')
1504_GrahamSt.connectRooms(1505_GrahamSt, 'n')

1505_GrahamSt.connectRooms(1504_GrahamSt, 's')
1504_GrahamSt.connectRooms(1503_GrahamSt, 's')
1503_GrahamSt.connectRooms(1502_GrahamSt, 's')
1502_GrahamSt.connectRooms(1501_GrahamSt, 's')

1505_GrahamSt.connectRooms(1601_OrchidSt, 'e')
1601_OrchidSt.connectRooms(1505_GrahamSt, 'w')

1601_OrchidSt.connectRooms(1602_OrchidSt, 'n')
1602_OrchidSt.connectRooms(1603_OrchidSt, 'n')
1603_OrchidSt.connectRooms(1604_OrchidSt, 'n')
1604_OrchidSt.connectRooms(1605_OrchidSt, 'n')

1605_OrchidSt.connectRooms(1604_OrchidSt, 's')
1604_OrchidSt.connectRooms(1603_OrchidSt, 's')
1603_OrchidSt.connectRooms(1602_OrchidSt, 's')
1602_OrchidSt.connectRooms(1601_OrchidSt, 's')

1605_OrchidSt.connectRooms(1701_SunriseSt, 'w')
1701_SunriseSt.connectRooms(1605_OrchidSt, 'e')

1701_SunriseSt.connectRooms(1702_SunriseSt, 'n')
1702_SunriseSt.connectRooms(1703_SunriseSt, 'n')
1703_SunriseSt.connectRooms(1704_SunriseSt, 'n')
1704_SunriseSt.connectRooms(1705_SunriseSt, 'n')

1705_SunriseSt.connectRooms(1704_SunriseSt, 's')
1704_SunriseSt.connectRooms(1703_SunriseSt, 's')
1703_SunriseSt.connectRooms(1702_SunriseSt, 's')
1702_SunriseSt.connectRooms(1701_SunriseSt, 's')

1705_SunriseSt.connectRooms(1801_PoppySt, 'w')
1801_PoppySt.connectRooms(1705_SunriseSt, 'e')

1801_PoppySt.connectRooms(1802_PoppySt, 'n')
1802_PoppySt.connectRooms(1803_PoppySt, 'n')
1803_PoppySt.connectRooms(1804_PoppySt, 'n')
1804_PoppySt.connectRooms(1805_PoppySt, 'n')

1805_PoppySt.connectRooms(1804_PoppySt, 's')
1804_PoppySt.connectRooms(1803_PoppySt, 's')
1803_PoppySt.connectRooms(1802_PoppySt, 's')
1802_PoppySt.connectRooms(1801_PoppySt, 's')

1805_PoppySt.connectRooms(1901_JacksonSt, 'e')
1901_JacksonSt.connectRooms(1805_PoppySt, 'w')

1901_JacksonSt.connectRooms(1902_JacksonSt, 'n')
1902_JacksonSt.connectRooms(1903_JacksonSt, 'n')
1903_JacksonSt.connectRooms(1904_JacksonSt, 'n')
1904_JacksonSt.connectRooms(1905_JacksonSt, 'n')

1905_JacksonSt.connectRooms(1904_JacksonSt, 's')
1904_JacksonSt.connectRooms(1903_JacksonSt, 's')
1903_JacksonSt.connectRooms(1902_JacksonSt, 's')
1902_JacksonSt.connectRooms(1901_JacksonSt, 's')

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