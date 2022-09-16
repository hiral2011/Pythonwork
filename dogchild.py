class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class JackRussellTerrier(Dog):
     def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

class GoldenRetriever(Dog):
     def speak(self, sound="Bark"):
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

max = GoldenRetriever("max",3)
miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(max.age)
print(miles.species)
print(buddy.name)
print(type(miles))
print(miles.speak())
print(miles.speak('grrrr')) #miles is angree


print(isinstance(miles, Dog))