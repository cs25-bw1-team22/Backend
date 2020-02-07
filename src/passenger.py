class Passenger:
    def __init__(self, title, description):
        self.title = title
        self.description = description
    def __str__(self):
        return f"{self.title} : {self.description}"


    def on_take(self):
        print(f"PICKED UP {self.title} {self.description}")

