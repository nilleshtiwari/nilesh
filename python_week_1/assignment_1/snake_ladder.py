import random
import time
import sys
import pickle
import os
from player import Player
from game_board import Game_board
from game_setup import Game_setup
from Config_changer import config_changer
from Feature import feature

#  Assigning the current path where the game information will be stored.
write_path = r"C:\Users\nileshtiwari\PycharmProjects\Python_week _1\python_week_1\player info"
write_path_1 = r"C:\Users\nileshtiwari\PycharmProjects\Python_week _1\python_week_1\board info"


def welcome_msg():
    msg = """
    Welcome to Snake and Ladder Game.
    Version: 1.0.0
    Developed by: Nilesh Tiwari

    Rules:
      1. At the start of the game all players will be at starting position i.e. 0
         Take it in turns to roll the dice. 
         Move forward the number of position shown on the dice.
      2. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
      3. If you lands on the head of a snake, you must slide down to the tail of the snake.
      4. The first player to get to the FINAL position is the winner.
      5. The game will automatically complete itself once it gets the number of players and their names.
      6. If you need to stop the game press ctrl+C and you can resume the game afterwards with the same state.
      7. Snakes and Ladders are automatically configured everytime by the machine.
      8. By default there are 8 snakes and 8 ladders in the Game or You can change the configuration as well.
      9. The game is played with single Dice.
    """
    print(msg)



if __name__ == "__main__":
    welcome_msg()
    
    def move(curr_position, dice_value):
        return curr_position + dice_value
    
    
    def start_game(players_list, k, board, setup):
        """ This function starts the game with the players, board & Game setup.
            this function controls the game functionalities in all aspects"""
    
        while k > 1:
            turn = 0
            while turn < k:
                player = players_list[turn]
                curr_position = player.position
                if curr_position < board.size:
                    # input_1 = input("\n" + player.name + ": " + feature.player_slogan() + " Hit the enter to roll dice: ")
                    print("\nRolling dice...")
                    dice_value = Game_board.dice()
                    new_position = move(curr_position, dice_value)
                    if new_position <= board.size:
                        feature.delay()
                        print(player.name, "moving from", curr_position, 'to', new_position)
                        new_position = setup.find_new_position(new_position, player.name)
                        player.update_position(new_position)
                    else:
                        print(player.name, 'cannot move')
    
                    if new_position == board.size:
                        print(player.name, "Wins!")
                        players_list.remove(player)
                        turn -= 1
                        feature.delay()  # giving a delay of 1s.
                        player.update_position(new_position + 10)
                        k -= 1
                if k < 2:  # making sure the for loop doesn't iterate again if no of remaining players become 1
                    os.remove(write_path)
                    os.remove(write_path_1)  # game ends hence player information will be deleted
                    break
                turn += 1
    
    
    def game_initializer_checks():  # function to check for hard exit of the game to restore from the last state of game
    
        if os.path.exists(write_path) and os.path.exists(write_path_1):
            print("Do you want to resume from the last game(Yes/NO):")
            input1 = input()
            if input1.lower() != 'yes':
                os.remove(write_path)
                os.remove(write_path_1)
                return False
            print("\n restoring the data of the last game........")
            f = open("player info", 'rb')
            players_list = pickle.load(f)
            f.close()
            if len(players_list) == 0:
                print("\nSorry! No previous game found, resetting the Game...\n")
                feature.delay()
                return False
            f1 = open("board info", 'rb')
            board = pickle.load(f1)
            f1.close()
            return players_list, board
        return False
    
    
    def snake_ladder_config():
        print("Do you want to change the number of snakes and ladder (Yes/No):")
        user_value = input()
        if 'yes' == user_value.lower():
            no_of_snake = int(input("Enter no. of snakes you want: "))
            no_of_ladder = int(input("Enter no. of ladders you want: "))
            return config_changer.snake_ladder(no_of_snake, no_of_ladder)
        return config_changer.snake_ladder()
    
    
    def final_check():
        """"
        this function perform all initial checks such
        as last state of game and board configuration, it also takes input from the user
        such as no of players, player name to finally start the game"""
        checks = game_initializer_checks()  # game_initializer_checks
    
        if checks is False:  # then we will take inputs from the user.
            num_players = int(input("Enter no. of Players: "))
            players_list = []
    
            while num_players > 0:
                player_name = input("Enter name of Player one by one: ")
                a = Player(player_name)
                players_list.append(a)
                num_players -= 1
            board = Game_board()
            f1 = open("board info", 'wb')
            pickle.dump(board, f1)
            f1.close()
            snake_list, ladder_list = snake_ladder_config()  # configuring snakes and ladder
            board.add_snakes(snake_list)  # adding snakes to the board
            board.add_ladders(ladder_list)  # adding ladders to the board
            setup = Game_setup(board)  # setting up the game with all checks and conditions
            k = len(players_list)
    
            start_game(players_list, k, board, setup)  # starting the game here
    
        else:
            players_list, board = checks
            setup = Game_setup(board)
            k = len(players_list)
            start_game(players_list, k, board, setup)  # starting the game again
    
    
    final_check()  # execution of Game starts here with the checks
