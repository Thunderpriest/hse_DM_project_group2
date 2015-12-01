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
                    dir = []
                    for a in range(-1, 2):
                        for b in range(-1, 2):
                            if not a == b == 0:
                                dir.append([a,b])

                    while len(dir) > 0:
                        d = dir[random.randint(0, len(dir)-1)]
                        a = d[0]
                        b = d[1]
                        try:
                            temp = field.objects[x + a][y + b]
                            if isinstance(temp, Obstacle.Obstacle):
                                dir.remove(d)
                                continue
                            elif isinstance(temp, str):
                                field.objects[x + a][y + b] = field.objects[x][y]
                                if t % birth_time != 0:
                                    field.objects[x][y] = '.'
                                break
                            dir.remove(d)
                        except:
                            dir.remove(d)
                            continue


            elif isinstance(obj, Prey.Prey):
                # move
                dir = []
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if not a == b == 0:
                            dir.append([a,b])

                while len(dir) > 0:
                    d = dir[random.randint(0, len(dir)-1)]
                    a = d[0]
                    b = d[1]
                    try:
                        temp = field.objects[x + a][y + b]
                        if isinstance(temp, Obstacle.Obstacle):
                            dir.remove(d)
                            continue
                        elif isinstance(temp, str):
                            field.objects[x + a][y + b] = field.objects[x][y]
                            if t % birth_time != 0:
                                field.objects[x][y] = '.'
                            break
                        dir.remove(d)
                    except:
                        dir.remove(d)
                        continue

    interface.draw(field)

    if field.predators_count() == 0 or field.preys_count() == 0:
        break

    time.sleep(0.3)
