import random
import numpy as np # pip install numpy 
import time
r1 = []
r2 = []
r3 = []


# checks if there is a winner or not 
def check(row1, row2, row3):
    X= 'X'
    O= 'O'
    c1 = [row1[0],row2[0],row3[0]]
    c2 = [row1[1],row2[1],row3[1]]
    c3 = [row1[2],row2[2],row3[2]]
    d1 = [row1[2],row2[1],row3[0]]
    d2 = [row1[0],row2[1],row3[2]]

    if condition(row1,'X') or condition(row2,'X') or condition(row3,'X') or condition(c1,'X') or condition(c2,'X') or condition(c3,'X') or condition(d1,'X') or condition(d2,'X'):
        return 'X'
    elif condition(row1,'O') or condition(row2,'O') or condition(row3,'O') or condition(c1,'O') or condition(c2,'O') or condition(c3,'O') or condition(d1,'O') or condition(d2,'O'):
        return 'O'

    return None

# checks if a list contains 3 Xes or 3 Os basically the condition of TicTacToe 
def condition(list_ , str_ ):
    for elem in list_:
        if elem != str_:
            return False
    return True

#  as it is an automated program generating a random index 
def randomIndex():
    indexes = [0,1,2]
    random.shuffle(indexes)
    index1 = indexes[:1]
    random.shuffle(indexes)
    index2 = (indexes[:1])
    index = index1+index2
    return index

# checks if the randomIndex generated is occupied by a X or a O
def isnotOccupied(array,index):
    if array[index[0]][index[1]] == '':
        return True
    return False

# combines all the funtions and starts the game 
def startgame():
    array = np.empty((3,3),dtype='str')
    randomindices = []
    boxes = 9
    while boxes > 0:
        ranndom = randomIndex()
        while ranndom in randomindices:
            ranndom =randomIndex()
        randomindices.append(ranndom)
        if (isnotOccupied(array, ranndom)) and boxes%2 ==0:
            array[ranndom[0]][ranndom[1]] = 'X'
        elif (isnotOccupied(array,ranndom)) and boxes%2 !=0:
            array[ranndom[0]][ranndom[1]] = 'O'
        print("___________________________________________________________")
        print(array)
        if boxes<=5:
            isWinner = check(array[0], array[1],array[2])
            if isWinner is not None:
                print('the winner is ', isWinner)
                break
            if boxes == 1 and isWinner is None:
                print('Its a draw')
        boxes -= 1
        time.sleep(1)


startgame()


