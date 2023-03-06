import numpy as np

connect_four = [[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0]]

connect_four = np.array(connect_four)
def turn(m):
    print("Player " + str(m) + "'s turn!")
    c = int(input("Put your piece in one of the columns."))
    while c > 6 or c < 0:
        print("Invalid input.")
        c = int(input("Put your piece in one of the columns (0-6)."))
    check_column(c,m)

#checks if there is a piece in the column, starting from the bottom
#Then, a counter indicates whose turn it will be.
def check_column(n,p):
    if connect_four[5,n] == 0:
        connect_four[5,n] = p
    else:
        if connect_four[4,n] == 0:
            connect_four[4,n] = p
        else:
            if connect_four[3,n] == 0:
                connect_four[3,n] = p
            else:
                if connect_four[2,n] == 0:
                    connect_four[2,n] = p
                else:
                    if connect_four[1,n] == 0:
                        connect_four[1,n] = p
                    else:
                        if connect_four[0,n] == 0:
                            connect_four[0,n] = p
                        else:
                            print("Invalid input.")
                            turn(p)
    print(connect_four)
    if check_win() == True:
        return
    if p == 1:
        p = 2
        turn(p)
    elif p == 2:
        p = 1
        turn(p)

#checks for the win condition
def check_four(row):
    a = "".join([str(i) for i in row])
    if "2222" in a:
        print("Player 2 wins.")
        return True
    elif "1111" in a:
        print("Player 1 wins.")
        return True
    return False

#gives a boolean statement for the win condition check, which is used to ensure the game will end when someone has won
def check_win():
    for row in connect_four:
        # Check whether there is a four-in-a-row.
        f = check_four(row)
        if f == True:
            return True
    for row in connect_four.T:
        g = check_four(row)
        if g == True:
            return True
    return False
a = 1
#Player 1 will always go first.
turn(a)