class Partypeople :
    x = 0
    name = ""
    def __init__(self, z, name) :
        self.x = z
        self.name = name
        print("initializer operated", self.name)
    def party(self) :
        self.x += 1
    def __del__(self) :
        print(self.name, "is destructed")

an = Partypeople(3,"Kim")
an.party()
print(an.x)
an = 1