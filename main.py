import math
import random as rd
import numpy as np

# Create a 3D array (log) using NumPy
def GenerateLog(attendance):
    a = np.zeros((attendance, 18, 2))
    return a

def PrintLog():
    crewActions = {
        1: "Product",
        2: "Customer",
        3: "Bagger",
        4: "Helmsing",
        5: "Lot Helmsing",
        6: "Demo",
        7: "Wine Demo",
        8: "Art",
        9: "Section Leading",
        10: "Captain Meeting",
        11: "Mentor Meeting",
        12: "Bathroom Check"
    }


if __name__ == '__main__':
    crewNumber = int(input("Enter number of crew members:"))
    log = GenerateLog(crewNumber)
    log[0][0][0] = 1
    print(log)