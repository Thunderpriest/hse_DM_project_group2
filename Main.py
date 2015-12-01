import Predator
import Prey
import Obstacle
import Interface
import random
import time

interface = Interface.Interface()

field, iter_max = interface.generate()
random.seed()
birth_time = 40

interface.draw(field)

# the main loop
for t in range(0, iter_max):

    # for each object
    for x in range(0, field.height):
        for y in range(0, field.width):

            obj = field.objects[x][y]

            if isinstance(obj, Predator.Predator):
                if field.objects[x][y].hitpoints == 0:
                    field.objects[x][y] = '.'
                    continue

                field.objects[x][y].hitpoints -= 1

                # has it eaten?
                ate = False

                # eat within range
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        try:
                            if isinstance(field.objects[x + i][y + j], Prey.Prey) and not ate:
                                field.objects[x + i][y + j] = '.'
                                field.objects[x + a][y + b].hitpoints = 20
                                ate = True
                        except:
                            continue

                # if hasn't eaten this turn, move
                if not ate:
                    for a in range(-1, 2):
                        for b in range(-1, 2):
                            if a == b == 0:
                                continue
                            try:
                                temp = field.objects[x + a][y + b]
                                if isinstance(temp, Obstacle.Obstacle):
                                    continue
                                elif isinstance(temp, str):
                                    field.objects[x + a][y + b] = field.objects[x][y]
                                    if t % birth_time != 0:
                                        field.objects[x][y] = '.'
                                    break
                            except:
                                continue


            elif isinstance(obj, Prey.Prey):
                # move
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if a == b == 0:
                            continue
                        try:
                            temp = field.objects[x + a][y + b]
                            if isinstance(temp, Obstacle.Obstacle):
                                continue
                            elif isinstance(temp, str):
                                field.objects[x + a][y + b] = field.objects[x][y]
                                if t % birth_time != 0:
                                    field.objects[x][y] = '.'
                                break
                        except:
                            continue

    interface.draw(field)

    if field.predators_count() == 0 or field.preys_count() == 0:
        break

    time.sleep(0.3)
