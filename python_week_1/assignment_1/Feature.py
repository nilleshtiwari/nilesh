import random
import time


class feature:  # to make the game more interactive.
    @classmethod
    def delay(cls, sleep_time=1):  # will cause the delay in program execution.
        time.sleep(sleep_time)

    @classmethod
    def player_slogan(cls):
        player_turn_text = [
            "Your turn.",
            "Go.",
            "Please proceed.",
            "Lets win this.",
            "Are you ready?",
            "",
        ]
        return random.choice(player_turn_text)

    @classmethod
    def snake_slogan(cls):
        snake_bite = [
            "boohoo",
            "bummer",
            "snake bite",
            "oh no",
            "dang"
        ]
        return random.choice(snake_bite)

    @classmethod
    def jump_slogan(cls):
        ladder_jump = [
            "woohoo",
            "woww",
            "nailed it",
            "oh my God...",
            "yaayyy"
        ]
        return random.choice(ladder_jump)