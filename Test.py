class Taco():
   def __init__(self, meat, toppings):
       self.meat = meat
       self.toppings = toppings

   def printResult(self):
       print("Getting items from the freezer")
       print("Your 2 year old" +" "+ self.meat + " " + self.toppings + " " + "Taco is ready.")


meat = raw_input ("What kind of meat do you want?")
topping = raw_input ("What kind of topping do you want?")


myTaco = Taco(meat,topping )
print(myTaco.meat)
print(myTaco.toppings)
(myTaco.printResult())