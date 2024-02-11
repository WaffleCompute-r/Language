class potato:
    horses = 10

    def addHorses(self, num):
        self.horses += num
        return self.horses

p = potato()
num = int(input("How many horses do you want to add? "))
print(p.addHorses(num))