from Feature import feature


class Game_setup:
    def __init__(self, board):
        self.board = board

    def got_snake_bite(self, new_position, player_name):
        for snake in self.board.snakes:
            if snake[0] == new_position:
                snake_slogan(player_name, new_position, snake)
                return snake[1]

    def got_ladder_jump(self, new_position, player_name):
        for ladder in self.board.ladders:
            if ladder[0] == new_position:
                ladder_slogan(player_name, new_position, ladder)
                return ladder[1]

    def find_new_position(self, new_position, player_name):
        snake_bitten = self.got_snake_bite(new_position, player_name)
        ladder_jump = self.got_ladder_jump(new_position, player_name)
        if snake_bitten is not None:
            return snake_bitten
        elif ladder_jump is not None:
            return ladder_jump
        else:
            return new_position


def snake_slogan(player_name, new_position, snake):
    str1 = " got a snake bite. Down from "
    str2 = " to "
    str3 = " ~~~~~~~~>"
    print("\n" + feature.snake_slogan().upper() + '{}'.format(str3))
    print("\n" + player_name + '{}'.format(str1) + str(new_position) + '{}'.format(str2) + str(snake[1]))


def ladder_slogan(player_name, new_position, ladder):
    str1 = " climbed the ladder from "
    str2 = " to "
    str3 = " ########"
    print("\n" + feature.jump_slogan().upper() + '{}'.format(str3))
    print("\n" + player_name + '{}'.format(str1) + str(new_position) + '{}'.format(str2) + str(ladder[1]))
