class Interface:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.obstacle_density = -1
        self.predator_number = 0
        self.prey_number = 0
        generate()

    def generate(self):

        os.system('cls')

        print("GENERATING NEW MAP")

        while True:
            print("   Enter width in pixels: ", end = '')
            try:
                self.width = int(input())
            except:
                self.width = 0
            if self.width > 0:
                break

        while True:
            print("   Enter height in pixels: ", end = '')
            try:
                self.height = int(input())
            except:
                self.height = 0
            if self.height > 0:
                break

        while True:
            print("   Enter obstacle density in percentage: ", end = '')
            try:
                self.obstacle_density = float(input())
            except:
                self.obstacle_density = -1
            if (self.obstacle_density >= 0) and (self.obstacle_density <= 100):
                break

        while True:
            print("   Enter number of predators: ", end = '')
            try:
                self.predator_number = int(input())
            except:
                self.predator_number = 0
            if self.predator_number > 0:
                break

        while True:
            print("   Enter number of preys: ", end = '')
            try:
                self.prey_number = int(input())
            except:
                self.prey_number = 0
            if self.prey_number > 0:
                break
