import unittest
import snake_ladder
from Config_changer import config_changer
from game_board import Game_board
from player import Player


class Test_calc(unittest.TestCase):
    def test_config(self):
        a = config_changer.snake_ladder()
        snakes, ladders = a

        def to_check(snake, ladder):
            L = []
            for x in snake:  # checking that head value of snake should be greater than tail
                L.append(x[0])
                L.append(x[1])
                if x[0] < x[1]:
                    return False
            for x in ladder:  # checking that bottom value > top value of ladder
                L.append(x[0])
                L.append(x[1])
                if x[0] > x[1]:
                    return False
            if len(L) != len(set(L)):  # checking whether any snake or ladder are in same place or not
                return False
            return True

        self.assertTrue(to_check(snakes, ladders))

    def test_dice_value(self):
        n = 50
        while n > 0:
            self.assertTrue(1 <= Game_board.dice() <= 6)
            n -= 1

    def test_move(self):  # testing move function
        self.assertEqual(snake_ladder.move(2, 3), 5)

    def test_Player(self):  # player object Creation and its method testing
        player = Player("nilesh")
        self.assertIsInstance(player, Player)
        player.update_position(10)
        self.assertEqual(player.position, 10)  # checking update method for player

    def test_Board(self):  # board object creation
        obj = Game_board()
        self.assertIsInstance(obj, Game_board)

    def test_snake_ladder_changer(self):
        """checking if we change the number of snakes and ladders then it is creating or not. """

        no_of_snake = 10
        no_of_ladder = 10
        snakes_list, ladders_list = config_changer.snake_ladder(no_of_snake,no_of_ladder)
        self.assertTrue((len(snakes_list), len(ladders_list), (10, 10)))


if __name__ == "__main__":
    unittest.main()
