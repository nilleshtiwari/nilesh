import random


class Game_board:
    def __init__(self, size=100):
        self.size = 100
        self.snakes = []
        self.ladders = []

    @classmethod
    def dice(cls):
        return random.randint(1, 6)

    def add_snakes(self, snake):
        self.snakes = snake

    def add_ladders(self, ladder):
        self.ladders = ladder
