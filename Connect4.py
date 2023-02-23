import numpy as np

connect_four = [[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 2, 0, 0, 0, 0],
                [0, 0, 2, 0, 0, 0, 0],
                [0, 2, 2, 1, 2, 0, 0],
                [0, 1, 2, 2, 1, 0, 0]]

connect_four = np.array(connect_four)

def check_four(row):
    a = "".join([str(i) for i in row])
    if "2222" in a:
        print("Player 2 wins.")
    elif "1111" in a:
        print("Player 1 wins.")

for row in connect_four:
    # Check whether there is a four-in-a-row.
    check_four(row)

for row in connect_four.T:
    check_four(row)