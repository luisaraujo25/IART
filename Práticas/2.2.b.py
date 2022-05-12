import random

def generateBoard():
    goal = [1,2,3,4,5,6,7,8,0]
    puzzle = []
    size = 9

    for i in range(size):
        puzzle.append(i)

    random.shuffle(puzzle)

    print("PUZZLE: ", puzzle)
    print("GOAL: ", goal)

generateBoard()
