import numpy as np
#Is 2222 the only way you can win? I'm a little confused here, but that could just be me.
connect_four = [[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 2, 0, 0, 0, 0],
                [0, 0, 2, 0, 0, 0, 0],
                [0, 2, 2, 1, 2, 0, 0],
                [0, 1, 2, 2, 1, 0, 0]]

connect_four = np.array(connect_four)
#I know the code isn't complete, but would the player be able to put some kind input somewhere? How would the
#player actually play this game? Maybe incorporate that under the "def check_four" or in a loop somewhere.
def check_four(row):
    a = "".join([str(i) for i in row])
    if "2222" in a:
        print("Player 2 wins.")
    elif "1111" in a:
        print("Player 1 wins.")

for row in connect_four:
    # Check whether there is a four-in-a-row.
    check_four(row)

#I'm not sure what "connect_four.T" is?
for row in connect_four.T:
    check_four(row)