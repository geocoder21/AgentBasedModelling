import random


# define Sheep class
class Sheep():
    """Sheep with x and y coordinates, and the ability to move randomly
    within their environment
    Sheep can identify and communicate with each other

    Methods within Sheep class:
    - move: allow to move
    - eat: allow to nibble away at environment
    - share_with_neighbours: allow sheep to exchange information
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


# create a 'share with others' function
    def share_with_neighbours(self, neighbourhood):
        for sheep in self.sheep:
            distance = self.distance_between(sheep)
            if distance <= neighbourhood:
                sum = self.store + sheep.store
                average = sum / 2
                self.store = average
                sheep.store = average
                # print("Sharing " + str(distance) + " " + str(average))

# calculate distance between agents
    def distance_between(self, agent):
        return(((self.x - agent.x) ** 2) + ((self.y - agent.y) ** 2)) ** 0.5


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
            if distance <= 0.5:
                self.sheep.remove(sheep)
                print("A wolf ate a sheep")
                print("There are now " + str(len(self.sheep)) + " sheep left")
        return len(self.sheep)

# calculate distance between wolf and sheep
    def distance_between(self, sheep):
        return(((self.x - sheep.x) ** 2) + ((self.y - sheep.y) ** 2)) ** 0.5
