# WEEK 8: Inheritance in Python

# In this session, we will explore how to use inheritance to create classes that share attributes and methods.

# Step 1: Define the ChefDerek class
class ChefDerek:
    def make_potatoes(self):
        print("The chef made a roast potato meal")

    def make_salad(self):
        print("The chef made a salad meal")

    def make_special_dish(self):
        print("The chef made egg fried rice")

# Step 2: Create an instance of ChefDerek
derek = ChefDerek()
derek.make_potatoes()
derek.make_salad()
derek.make_special_dish()

# Step 3: Define the ChefSandra class that inherits from ChefDerek
class ChefSandra(ChefDerek):
    def make_chicken_soup(self):
        print("The chef made a chicken soup meal")

    def make_smoothies(self):
        print("The chef made some smoothies")

    def make_special_dish(self):
        print("The chef made jollof rice")  # Overriding the special dish

# Step 4: Create an instance of ChefSandra and print meals
sandra = ChefSandra()
sandra.make_potatoes()
sandra.make_salad()
sandra.make_special_dish()
sandra.make_chicken_soup()
sandra.make_smoothies()

# Step 5: Create ItalianChef class inheriting from ChefDerek
class ItalianChef(ChefDerek):
    def make_spaghetti(self):
        print("The chef made spaghetti")

    def make_special_dish(self):
        print("The chef made ravioli")  # Overriding the special dish

# Step 6: Create an instance of ItalianChef and print meals
italian_chef = ItalianChef()
italian_chef.make_potatoes()
italian_chef.make_salad()
italian_chef.make_special_dish()
italian_chef.make_spaghetti()

# Step 7: Create IndianChef class inheriting from ChefSandra
class IndianChef(ChefSandra):
    def make_lamb_samosas(self):
        print("The chef made lamb samosas")

    def make_special_dish(self):
        print("The chef made chicken curry")  # Overriding the special dish

# Step 8: Create an instance of IndianChef and print meals
indian_chef = IndianChef()
indian_chef.make_potatoes()
indian_chef.make_salad()
indian_chef.make_special_dish()
indian_chef.make_chicken_soup()
indian_chef.make_lamb_samosas()
indian_chef.make_smoothies()

# Challenges:
# Challenge 1: Add a method to the ChefDerek class that returns a list of all the dishes Derek can make.
# Challenge 2: Implement a method in ChefSandra that lists her unique dishes.
# Challenge 3: Create a ChefMexican class that inherits from ChefDerek and adds tacos and enchiladas as meals.
# Challenge 4: Modify the IndianChef class to inherit from ChefDerek and create a method to make a vegetarian curry.
