
from datetime import date
class Human:
    age = 18
    drink = "beer"

  def favorite_drink(self):
       print(self.drink)

class Worker(Human):
    salery = 1000

human1 = Human()
worker1 = Worker()
print(human1.drink)
print(worker1.salery)




