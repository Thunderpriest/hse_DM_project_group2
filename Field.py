import Prey
import Predator
import Obstacle


class Field:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.objects = [[None for x in range(width)] for x in range(height)]

    def add_obstacle(self, object, x_coord, y_coord):
        self.__objects[x_coord][y_coord] = Obstacle()

    def add_predator(self, object, x_coord, y_coord):
        self.__objects[x_coord][y_coord] = Predator()

    def add_prey(self, object, x_coord, y_coord):
        self.__objects[x_coord][y_coord] = Prey()

    def creatures_count(self):
        return self.predators_count() + self.preys_count()

    def predators_count(self):
        self.objects.count(lambda x: x is Predator)

    def preys_count(self):
        self.objects.count(lambda x: x is Prey)
