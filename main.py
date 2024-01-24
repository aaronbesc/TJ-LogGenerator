import math
import random as rd
import numpy as np

# Create a 3D array (log) using NumPy
def GenerateBoard(attendance):
    a = np.zeros((attendance, 18, 2))
    return a


if __name__ == '__main__':
    crewNumber = int(input("Enter number of crew members:"))
    board = GenerateBoard(crewNumber)
    print(board)