import random


# define Sheep class
class Sheep():
    """Sheep with x and y coordinates, and the ability to move randomly
    within their environment
    Sheep can identify and communicate with each other

    Methods within Sheep class:
    - move: allow to move
    - eat: allow to nibble away at environment and increase personal 'store'
    - share_with_neighbours: allow sheep to share stores if at similar location
    - distance_between: calculate distance between sheep
    """

    def __init__(self, the_environment, sheep, y=None, x=None):
        self.environment = the_environment
        self.store = 0
        self.sheep = sheep
        if(y==None):
            self.y = random.randint(0, 99)
        else:
            self.y = y
        if(x==None):
            self.x = random.randint(0, 99)
        else:
            self.x = x

# create a 'move' method within the class
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

# create an 'eat' function
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            # print(self.store)          # Test self.store increases correctly

# create a 'share with others' function
    def share_with_neighbours(self, neighbourhood):
        for sheep in self.sheep:
            distance = self.distance_between(sheep)
            # print(distance)                         # Test distance
            if distance <= neighbourhood:
                sum = self.store + sheep.store
                average = sum / 2
                self.store = average
                sheep.store = average
                # print(sheep.store)    # Test sheep.store increases correctly

# calculate distance between sheep
    def distance_between(self, sheep):
        return(((self.x - sheep.x) ** 2) + ((self.y - sheep.y) ** 2)) ** 0.5


# define Wolves class

class Wolves():

    def __init__(self, sheep, y=None, x=None):
        self.sheep = sheep
        if(y==None):
            self.y = random.randint(0, 99)
        else:
            self.y = y
        if(x==None):
            self.x = random.randint(0, 99)
        else:
            self.x = x

# create a 'move' method within the class
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

# create an 'eat_sheep' function
    def eat_sheep(self):
        for sheep in self.sheep:
            distance = self.distance_between(sheep)
            # print(distance)                         # Test distance
            if distance <= 0.5:
                self.sheep.remove(sheep)
                print("A wolf ate a sheep")
                print("There are now " + str(len(self.sheep)) + " sheep left")
        return len(self.sheep)

# calculate distance between wolf and sheep
    def distance_between(self, sheep):
        return(((self.x - sheep.x) ** 2) + ((self.y - sheep.y) ** 2)) ** 0.5
