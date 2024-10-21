class food :          #base class
    def __init__(self , name, price):
        self.name=name
        self.price = price

        print(f"{self.name} is created from base class and the price is {self.price}")

    def eat(self):
        print("Eat method from main class")


class apple(food):          #derived class
    def __init__(self, name, price) :

        self.name=name
        self.price = price

        #food.__init__(self,name,price) 

        #super().__init__(name,price)

        print(f"{self.name} is created from derived class and the price is {self.price}")


food_one = food("Pizza","100")
food_two = apple("Burgur","300")
food_two.eat()




        