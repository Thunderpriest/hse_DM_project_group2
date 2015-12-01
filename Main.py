import Field
import Predator
import Prey
import Obstacle
import random

field = #get field from generator
iter_max = #get max iteration number from generator
random.seed()

for t in range(0, iter_max):
    for x in range(0, field.width):
        for y in range(0, field.height):
            obj = field.objects[x][y]
            if obj is Predator:
                ate = False

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        try:
                            if field.objects[x + i][y + j] is Prey:
                                field.objects[x + i][y + j] = None
                                field.objects[x + a][y + b].hitpoints = 20
                                ate = True
                        except:
                            continue
                if not ate:
                    while true:
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
                while true:
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
    #draw
    if field.predators_count == 0 or field.preys_count == 0:
        break