from datetime import date
class Human():
    favorite_drink = "beer"

    def __init__ (self, age):
        self.age = age
        if self.age < 18:
            self.favorite_drink = "juce"

class Worker(Human):
  def __init__(self, age, drink, salery):
        self.age = age
        self.drink = drink
        self.salery = salery
        if self.age > 18 and self.salery > 1000:
            self.drink = "whiskey"

human1 = Human(18)
worker1 = Worker(18, "whiskey", 1000)
print(human1.favorite_drink)
print(human1.age)
print(human1)
print(worker1.salery)
print(worker1.drink)




