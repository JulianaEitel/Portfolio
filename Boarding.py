# Creating a Dog Data Type

class Dog:
    def __init__(self, name, breed, age, weight_in_lbs, is_a_biter):
        self.name = name
        self.breed = breed
        self.age = age
        self.weight_in_lbs = weight_in_lbs
        self.is_a_biter = is_a_biter

    def board_with_small_dogs(self):
        if self.weight_in_lbs <= 20:
            return "Board with small dogs!"
        else:
            return "Board with big dogs!"




