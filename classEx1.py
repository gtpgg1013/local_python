class Partyanimal :
    x = 0

    def party(self) :
        self.x = self.x + 1
        print(self.x)

an = Partyanimal()
an.party()
an.party()
an.party()
print(an.x)

print(dir(an))
print(type(an))