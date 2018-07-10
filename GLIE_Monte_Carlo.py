from environment import environment
import numpy as np
import matplotlib.pyplot as mplot

# Trains the GLIE Model-Free Controller

# Creates look-up table model defaults
NSA = np.zeros((2,21,10))
QSA = np.zeros((2,21,10))
pi = np.zeros((21,10), dtype=int)
gameCounter = 0

while(gameCounter < 100000):
    # Initializes game
    s, r, game_over = environment([], 0)
    episodes = []
    # Experience step (Plays through an episode)
    while(not game_over):
        policy_action = pi[s[0] - 1][s[1] - 1]
        sp, r, game_over = environment(s, policy_action)
        episodes.append(([s[0],s[1]], policy_action, r))
        s = list(sp)
    gameCounter += 1
    # Learning step
    for i in range(0,len(episodes)):
        s = episodes[i][0]
        a = episodes[i][1]
        r = episodes[i][2]
        player_state = s[0] - 1
        dealer_state = s[1] - 1
        NSA[a][player_state][dealer_state] = NSA[a][player_state][dealer_state] + 1
        SA_pair_val = QSA[a][player_state][dealer_state]
        alpha = (1/(NSA[a][player_state][dealer_state]))
        QSA[a][player_state][dealer_state] = SA_pair_val + alpha * (r - SA_pair_val)
        e = 100 / (100 + NSA[0][player_state][dealer_state] + NSA[1][player_state][dealer_state])
        if (e >= np.random.rand(1)):
            pi[player_state][dealer_state] = np.random.randint(0, 2)
        else:
            pi[player_state][dealer_state] = np.argmax([QSA[0][player_state][dealer_state],QSA[1][player_state][dealer_state]])


# Tests the GLIE Model-Free Controller

wins = 0
losses = 0
gameTestCounter = 0

while(gameTestCounter < 50000):
    # Initializes game
    s, r, game_over = environment([], 0)
    episodes = []
    # Experience step (Plays through an episode)
    #print("playing")
    while(not game_over):
        policy_action = pi[s[0] - 1][s[1] - 1]
        sp, r, game_over = environment(s, policy_action)
        episodes.append(([s[0],s[1]], policy_action, r))
        s = list(sp)
    gameTestCounter += 1
    wins = wins + (r > 0)
    losses = losses + (r < 0)
winRatio = wins/gameTestCounter
lossRatio = losses/gameTestCounter
mplot.contour(pi)
mplot.show()
