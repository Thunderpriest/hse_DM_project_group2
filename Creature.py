class Creature:

    DEFAULT_HP = 100
    DEFAULT_LOSS_PER_TURN = 1

    def __init__(self, hp=DEFAULT_HP,
                 loss_per_turn=DEFAULT_LOSS_PER_TURN):
        self.hitpoints = hp
