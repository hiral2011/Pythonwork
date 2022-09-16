class car():
    def __init__(self,color,miles):
        self.color = color
        self.miles = miles

    # def printname(self):
    #     print("The", self.color,"car has ",self.miles," miles")

# x = car("red",3000)
# y = car("blue",5000)
# x.printname()
# y.printname()


blue = car(color="blue", miles=20_000)
red = car(color="red", miles=30_000)

for car in (blue,red):
    print(f'the {car.color} car has {car.miles} miles')