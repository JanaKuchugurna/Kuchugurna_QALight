from datetime import date
class Human():
    def __init__(self, age = 18, drink = 'beer'):
     self.age = age
     self.drink = drink

    def favorite_drink(self):
      print(self.drink)

    def age_permission(self):
        if self.age < 18:
            print('Human likes to drink juice')
        else:
            print("Human likes to drink beer")

#class Worker(Human):

    #def __init__(self, age=18, drink='beer'):
        #super().__init__(age, drink)
        #self.salery = None

    #def salery_info(self, salery= 1000, drink= 'whiskey'):

        #if self.salery > 1000
            #print('whiskey')
        #else:
            #print('beer')

human1 = Human()
#worker1 = Worker()
print(human1.drink  + "це напій, який п'є людина")
print(human1.favorite_drink())
#print(worker1.salery_info())
print(human1.age_permission())




