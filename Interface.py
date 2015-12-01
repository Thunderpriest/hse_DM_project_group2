import os
import Field
from math import floor
from random import randint


class Interface:
    # constructor
    def __init__(self):
        self.width = 0
        self.height = 0
        self.obstacle_density = -1
        self.predator_number = 0
        self.prey_number = 0
        self.generate()

    # draws map in console
    def draw(self, field):
        os.system('cls')
        self.draw_top_bar(field)
        for i in range(len(field.objects)):
            print(''.join([str(obj) for obj in field.objects[i]]))
        print("Creatures: " + str(field.creatures_count()) + ". Predators: " + str(
            field.predators_count()) + ". Preys: " + str(field.preys_count())
              + ". ")

    # draws top bar
    def draw_top_bar(self, field):
        title = "The Fabulous Ocean Simulation Project"
        print("=" * ((field.width - len(title)) // 2) + title + "=" * (
            (field.width - len(title)) // 2 + (field.width - len(title)) % 2))
        subtitle = "2015"
        print("=" * ((field.width - len(subtitle)) // 2) + subtitle + "=" * (
            (field.width - len(subtitle)) // 2 + (field.width - len(subtitle)) % 2))

    # generates new field
    def generate(self):
        os.system('cls')
        print("GENERATING NEW MAP")
        iteration_number = self.enter_params()
        field = Field.Field(self.width, self.height)
        obstacles = floor(self.width * self.height * self.obstacle_density / 100)
        predators = self.predator_number
        preys = self.prey_number
        empty = self.width * self.height - obstacles - predators - preys
        for i in range(self.height):
            for j in range(self.height):
                rand = randint(0, obstacles + predators + preys + empty - 1)
                if rand < obstacles:
                    obstacles -= 1
                    field.add_obstacle(j, i)
                elif rand < predators + obstacles:
                    predators -= 1
                    field.add_predator(j, i)
                elif rand < preys + predators + obstacles:
                    preys -= 1
                    field.add_prey(j, i)
        return field, iteration_number

    # asks for params
    def enter_params(self):
        self.enter_width()
        self.enter_height()
        self.enter_obstacle_density()
        self.enter_predator_number()
        self.enter_prey_number()
        if self.width * self.height * (1 - self.obstacle_density / 100) < self.predator_number + self.prey_number:
            print("   Your whole input is wrong!!")
            return self.enter_params()
        return self.enter_iteration_number()

    # asks for width
    def enter_width(self):
        print("   Enter width in pixels: ", end='')
        try:
            self.width = int(input())
        except:
            print("   Your input is wrong!!")
            self.enter_width()
        if self.width <= 0:
            print("   Your input is wrong!!")
            self.enter_width()

    # asks for height
    def enter_height(self):
        print("   Enter height in pixels: ", end='')
        try:
            self.height = int(input())
        except:
            print("   Your input is wrong!!")
            self.enter_height()
        if self.height <= 0:
            print("   Your input is wrong!!")
            self.enter_height()

    # asks for obstacle density
    def enter_obstacle_density(self):
        print("   Enter obstacle density in percentage: ", end='')
        try:
            self.obstacle_density = int(input())
        except:
            print("   Your input is wrong!!")
            self.enter_obstacle_density()
        if self.obstacle_density < 0 or self.obstacle_density > 100:
            print("   Your input is wrong!!")
            self.enter_obstacle_density()

    # asks predator number
    def enter_predator_number(self):
        print("   Enter number of predators: ", end='')
        try:
            self.predator_number = int(input())
        except:
            print("   Your input is wrong!!")
            self.enter_predator_number()
        if self.predator_number <= 0:
            print("   Your input is wrong!!")
            self.enter_predator_number()

    # asks prey number
    def enter_prey_number(self):
        print("   Enter number of preys: ", end='')
        try:
            self.prey_number = int(input())
        except:
            print("   Your input is wrong!!")
            self.enter_prey_number()
        if self.prey_number <= 0:
            print("   Your input is wrong!!")
            self.enter_prey_number()

    # asks prey number
    def enter_iteration_number(self):
        print("   Enter number of iterations: ", end='')
        iteration_number = 0
        try:
            iteration_number = int(input())
        except:
            print("   Your input is wrong!!")
            return self.enter_iteration_number()
        if iteration_number <= 0:
            print("   Your input is wrong!!")
            return self.enter_iteration_number()
        return iteration_number
