class Human:
    favorite_drink = "beer"

    def __init__(self, age):
        self.age = age

    def drink(self):
        if self.age < 18:
            self.favorite_drink = "juice"
        print(f"{self.__class__.__name__} likes to drink {self.favorite_drink}")


class Worker(Human):
    def __init__(self, age, salary):
        super().__init__(age)
        self.salary = salary
        if self.salary > 1000:
            self.favorite_drink = "whiskey"


worker1 = Worker(18, 1400)
worker1.drink()
