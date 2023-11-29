from datetime import date


class Human:
    favorite_drink = "beer"

    def __init__(self, age):
        self.age = agegit

    def drink(self):
        if self.age < 18:
            self.favorite_drink = "juice"
        print(f"{self.__class__.__name__} likes to drink {self.favorite_drink}")


class Worker(Human):
    def __init__(self, age, salary):
        super().__init__(age)
        self.salary = salary
        if salary > 1000:
            self.favorite_drink = "whiskey"


worker1 = Worker(17, 1000)
worker1.drink()
worker2 = Worker(18, 1000)
worker2.drink()
worker3 = Worker(18, 1400)
worker3.drink()
