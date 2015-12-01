import Prey
import Predator
import Obstacle


class Field:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.objects = [['.' for x in range(width)] for x in range(height)]

    def add_obstacle(self, x_coord, y_coord):
        self.objects[x_coord][y_coord] = Obstacle.Obstacle()

    def add_predator(self, x_coord, y_coord):
        self.objects[x_coord][y_coord] = Predator.Predator()

    def add_prey(self, x_coord, y_coord):
        self.objects[x_coord][y_coord] = Prey.Prey()

    def creatures_count(self):
        return self.predators_count() + self.preys_count()

    def predators_count(self):
        return self.objects.count(lambda x: x is Predator)

    def preys_count(self):
        return self.objects.count(lambda x: x is Prey)
