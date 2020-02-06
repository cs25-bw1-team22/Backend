class Room:
    def __init__(self, title, description):
        self.title = title 
        self.description = description
        self.passengers = []

    def where_am_i(self):
        print(f"*******************\n{self.title}\n\n\t{self.description}\n*******************")
        self.list_passengers()
        
    
    def list_passengers(self):
        if self.passengers ==[]:
            print(f"You don't see any passegers nearby")
        else:
            if len(self.passengers) > 1:
                print("You see several passengers")
                for x in self.passengers:
                    print(f"A {x.title}: it appears to be {x.description}")
            # else:
            #     print("You see passengers...")
            #     for x in self.passengers:
            #         print(f"A {x.title}: it appears to be {x.description}")


