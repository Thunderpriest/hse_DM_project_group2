import Field
import Predator
import Prey
import Obstacle
import Interface
import random

interface = Interface()

field, iter_max = interface.generate()
random.seed()

interface.draw(field)

#the main loop
for t in range(0, iter_max):

    #for each object
    for x in range(0, field.width):
        for y in range(0, field.height):

            obj = field.objects[x][y]

            if obj is Predator:

                #has it eaten?
                ate = False

                #eat everything within range
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        try:
                            if field.objects[x + i][y + j] is Prey and not ate:
                                field.objects[x + i][y + j] = None
                                field.objects[x + a][y + b].hitpoints = 20
                                ate = True
                        except:
                            continue

                #if hasn't eaten this turn, move
                if not ate:
                    while True:
                        a = random.randint(-1, 1)
                        b = random.randint(-1, 1)
                        if a == b == 0:
                            continue
                        try:
                            temp = field.objects[x + a][y + b]
                            if temp is Obstacle:
                                continue
                            elif temp is None:
                                field.objects[x + a][y + b] = field.objects[x][y]
                                field.objects[x][y] = None
                                field.objects[x + a][y + b].hitpoints -= 1
                                break
                        except:
                            continue


            elif obj is Prey:
                #move
                while True:
                    a = random.randint(-1, 1)
                    b = random.randint(-1, 1)
                    if a == b == 0:
                        continue
                    try:
                        temp = field.objects[x + a][y + b]
                        if temp is Obstacle:
                            continue
                        elif temp is None:
                            field.objects[x + a][y + b] = field.objects[x][y]
                            field.objects[x][y] = None
                            break
                    except:
                        continue

    interface.draw(field)

    if field.predators_count == 0 or field.preys_count == 0:
        break