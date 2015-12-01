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

    # draws map in console
    def draw(self, field):
        self.clear_console()
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

    # clears console
    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # generates new field
    def generate(self):
        self.clear_console()
        print("GENERATING NEW MAP")
        iteration_number = self.enter_params()
        field = Field.Field(self.width, self.height)
        obstacles = floor(self.width * self.height * self.obstacle_density / 100)
        for i in range(obstacles):
            while True:
                xrand = randint(0, self.width - 1)
                yrand = randint(0, self.height - 1)
                if field.objects[yrand][xrand] == '.':
                    field.add_obstacle(xrand, yrand)
                    break
        for i in range(self.predator_number):
            while True:
                xrand = randint(0, self.width - 1)
                yrand = randint(0, self.height - 1)
                if field.objects[yrand][xrand] == '.':
                    field.add_predator(xrand, yrand)
                    break
        for i in range(self.prey_number):
            while True:
                xrand = randint(0, self.width - 1)
                yrand = randint(0, self.height - 1)
                if field.objects[yrand][xrand] == '.':
                    field.add_prey(xrand, yrand)
                    break
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
        print("   Enter width in symbols: ", end='')
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
        print("   Enter height in symbols: ", end='')
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
            self.obstacle_density = float(input())
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
