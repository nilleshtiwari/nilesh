import random


class config_changer:
    @classmethod
    def snake_ladder(cls, no_of_snake=8, no_of_ladder=8):
        """This function configures the snakes and ladders required for the Game.
        This ensures that no snake and ladder are on the same place and by default
        the minimum height of snakes and ladder is greater than 5"""
        L = list(range(1, 101))
        snake = []
        ladder = []
        while len(snake) != no_of_snake or len(ladder) != no_of_ladder:
            a = random.choice(L)
            b = random.choice(L)
            if a != b and (a, b) not in snake or (b, a) not in snake and (a, b) not in ladder or (b, a) not in ladder:
                if a - b > 5 and len(snake) < no_of_snake:
                    snake.append((a, b))
                    L.remove(a)
                    L.remove(b)
                elif a - b < -5 and len(ladder) < no_of_ladder:
                    ladder.append((a, b))
                    L.remove(b)
                    L.remove(a)
        return snake, ladder
