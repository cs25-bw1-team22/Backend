class Room:
    def __init__(self, title, description, passengers=None):
        self.title = title
        self.description = description
        self.passengers = passengers
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def where_am_i(self):
        print(f"***********************\n{self.title}\n\n\t{self.description}\n***********************")
        self.list_passengers()
        
    
    def list_passengers(self):
        if self.passengers == None:
            print(f"You don't see any passengers nearby")
        else:
            if len(self.passengers) >= 1:
                print("There are passengers here")
                for x in self.passengers:
                    print(f"\nName: {x.title}")
                    print(f"Dropoff Location: {x.description}\n")
        
        
    def get_room_in_direction(self, direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f"{direction}_to")
        return None

