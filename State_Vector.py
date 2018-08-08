import numpy as np

# The gist here is going to be to take the index of the input in each vector and multiply that index by the product of the length of all previous rows
# Realized the above only works in the case of non-overlapping cubes


def state_vec(player_state,dealer_state, a):

    fVector = np.zeros((36))
    if(a):
        if (dealer_state < 5):
            if (1 < player_state & player_state < 7):
                fVector[0] = 1
            if (3 < player_state & player_state < 10):
                fVector[1] = 1
            if (6 < player_state & player_state < 13):
                fVector[2] = 1
            if (9 < player_state & player_state < 16):
                fVector[3] = 1
            if (12 < player_state & player_state < 19):
                fVector[4] = 1
            if (15 < player_state & player_state < 22):
                fVector[5] = 1
        if (dealer_state > 6):
            if (1 < player_state & player_state < 7):
                fVector[6] = 1
            if (3 < player_state & player_state < 10):
                fVector[7] = 1
            if (6 < player_state & player_state < 13):
                fVector[8] = 1
            if (9 < player_state & player_state < 16):
                fVector[9] = 1
            if (12 < player_state & player_state < 19):
                fVector[10] = 1
            if (15 < player_state & player_state < 22):
                fVector[11] = 1
        if ((3 < dealer_state) & (dealer_state < 8)):
            if (1 < player_state & player_state < 7):
                fVector[12] = 1
            if (3 < player_state & player_state < 10):
                fVector[13] = 1
            if (6 < player_state & player_state < 13):
                fVector[14] = 1
            if (9 < player_state & player_state < 16):
                fVector[15] = 1
            if (12 < player_state & player_state < 19):
                fVector[16] = 1
            if (15 < player_state & player_state < 22):
                fVector[17] = 1
    else:
        if (dealer_state < 5):
            if (1 < player_state & player_state < 7):
                fVector[18] = 1
            if (3 < player_state & player_state < 10):
                fVector[19] = 1
            if (6 < player_state & player_state < 13):
                fVector[20] = 1
            if (9 < player_state & player_state < 16):
                fVector[21] = 1
            if (12 < player_state & player_state < 19):
                fVector[22] = 1
            if (15 < player_state & player_state < 22):
                fVector[23] = 1
        if (dealer_state > 6):
            if (1 < player_state & player_state < 7):
                fVector[24] = 1
            if (3 < player_state & player_state < 10):
                fVector[25] = 1
            if (6 < player_state & player_state < 13):
                fVector[26] = 1
            if (9 < player_state & player_state < 16):
                fVector[27] = 1
            if (12 < player_state & player_state < 19):
                fVector[28] = 1
            if (15 < player_state & player_state < 22):
                fVector[29] = 1
        if ((3 < dealer_state) & (dealer_state < 8)):
            if (1 < player_state & player_state < 7):
                fVector[30] = 1
            if (3 < player_state & player_state < 10):
                fVector[31] = 1
            if (6 < player_state & player_state < 13):
                fVector[32] = 1
            if (9 < player_state & player_state < 16):
                fVector[33] = 1
            if (12 < player_state & player_state < 19):
                fVector[34] = 1
            if (15 < player_state & player_state < 22):
                fVector[35] = 1
    return fVector



