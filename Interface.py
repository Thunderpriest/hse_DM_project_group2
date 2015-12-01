import os
import Field


class Interface:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.obstacle_density = -1
        self.predator_number = 0
        self.prey_number = 0
        self.generate()

    def draw(self, field):
        os.system('cls')
        title = "The Fabulous Ocean Simulation Project"
        print("=" * ((field.width - len(title)) // 2) + title + "=" * (
            (field.width - len(title)) // 2 + (field.width - len(title)) % 2))
        subtitle = "2015"
        print("=" * ((field.width - len(subtitle)) // 2) + subtitle + "=" * (
            (field.width - len(subtitle)) // 2 + (field.width - len(subtitle)) % 2))
        for i in range(len(field.objects)):
            print(''.join([str(obj) for obj in field.objects[i]]))
        print("Creatures: " + str(field.creatures_count()) + ". Predators: " + str(
            field.predators_count()) + ". Preys: " + str(field.preys_count())
+ ". ")

    def generate(self):
        os.system('cls')
        print("GENERATING NEW MAP")
        self.enter_params()

    def enter_params(self):
        self.enter_width()
        self.enter_height()
        self.enter_obstacle_density()
        self.enter_predator_number()
        self.enter_prey_number()

    def enter_width(self):
        while True:
            print("   Enter width in pixels: ", end='')
            try:
                self.width = int(input())
            except:
                self.width = 0
            if self.width > 0:
                break

    def enter_height(self):
        while True:
            print("   Enter height in pixels: ", end='')
            try:
                self.height = int(input())
            except:
                self.height = 0
            if self.height > 0:
                break

    def enter_obstacle_density(self):
        while True:
            print("   Enter obstacle density in percentage: ", end='')
            try:
                self.obstacle_density = float(input())
            except:
                self.obstacle_density = -1
            if (self.obstacle_density >= 0) and (self.obstacle_density <= 100):
                break

    def enter_predator_number(self):
        while True:
            print("   Enter number of predators: ", end='')
            try:
                self.predator_number = int(input())
            except:
                self.predator_number = 0
            if self.predator_number > 0:
                break

    def enter_prey_number(self):
        while True:
            print("   Enter number of preys: ", end='')
            try:
                self.prey_number = int(input())
            except:
                self.prey_number = 0
            if self.prey_number > 0:
                break
