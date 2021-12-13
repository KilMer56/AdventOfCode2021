# Advent of code Year 2021 Star 7
# Author : Killian Mer

from os import remove


with open("input.txt", "r") as fp:
    input = fp.read().splitlines()

draws = input[0].split(",")

boards = []
trackers = []
wins = []


def prepare_board():
    current_board = []

    for i in range(2, len(input)+1):
        if i == len(input) or len(input[i]) == 0: # If end or empty line -> Push the boards
            boards.append(current_board)
            trackers.append([[len(current_board)]*len(current_board) for i in range(2)])
            wins.append([[False]*len(current_board) for i in range(len(current_board))])

            current_board = []
        else:
            current_board.append(input[i].split())


def remove_from_board(draw, board, tracker, win):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == draw:
                tracker[0][i] -= 1 # Column count tracker
                tracker[1][j] -= 1 # Row count tracker

                win[i][j] = True # Win tracker

                if tracker[0][i] == 0 or tracker[1][j] == 0:
                    return True
                else:
                    return False

    return False


def count_total_board(board, win):
    count = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if win[i][j] == False:
                count += int(board[i][j])
    
    return count


def bingo():
    for draw in draws:
        for i in range(len(boards)):
            result = remove_from_board(draw, boards[i], trackers[i], wins[i])

            if result is True:
                return int(draw) * count_total_board(boards[i], wins[i])


prepare_board()
res = bingo()

print("Result : " + str(res))