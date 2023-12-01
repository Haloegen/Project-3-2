# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random 


class GameBoard:
    def __init__(self, board):
        self.board = board
    
    def get_letters_to_numbers():
        letters_to_numbers = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}
        return  letters_to_numbers
    

    def print_board(self):
        print("  A B C D E F G H")
        print("  +-+-+-+-+-+-+-+")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number +=1
            