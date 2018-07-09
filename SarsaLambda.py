from environment import environment
import numpy as np
import matplotlib.pyplot as mplot

# Trains the Sarsa Lambda Model-Free Controller

# Creates look-up table model defaults
NSA = np.zeros((2,31,27))
QSA = np.zeros((2,31,27))
pi = np.zeros((31,27), dtype=int)
gameCounter = 0
lamb = 0

while(gameCounter < 50000):
    # Initializes game
    s, r, game_over = environment([], 0)
    episodes = []
    ESA = np.zeros((2, 31, 27))
    # Experience step (Plays through an episode)
    while(not game_over):

        # Playing a single turn
        policy_action = pi[s[0] - 1][s[1] - 1]
        sp, r, game_over = environment(s, policy_action)

        # Sarsa updates after each turn
        player_state = s[0] - 1
        dealer_state = s[1] - 1
        a = policy_action
        NSA[a][player_state][dealer_state] = NSA[a][player_state][dealer_state] + 1
        ESA[a][player_state][dealer_state] = ESA[a][player_state][dealer_state] + 1
        SA_pair_val = QSA[a][player_state][dealer_state]
        alpha = (1 / (NSA[a][player_state][dealer_state]))
        ap = pi[sp[0] - 1][sp[1] - 1]
        delta = r + QSA[ap][sp[0] - 1][sp[1] - 1] - SA_pair_val
        for inc_act in range (0,2):
            for inc_s0 in range (0,31):
                for inc_s1 in range(0, 27):
                    QSA[inc_act][inc_s0][inc_s1] = QSA[inc_act][inc_s0][inc_s1] + alpha*delta*ESA[inc_act][inc_s0][inc_s1]
                    ESA[inc_act][inc_s0][inc_s1] = lamb*ESA[inc_act][inc_s0][inc_s1]

        # Updating the policy table epsilon greedily
        e = 100 / (100 + NSA[0][player_state][dealer_state] + NSA[1][player_state][dealer_state])
        if (e >= np.random.rand(1)):
            pi[player_state][dealer_state] = np.random.randint(0, 2)
        else:
            pi[player_state][dealer_state] = np.argmax([QSA[0][player_state][dealer_state],QSA[1][player_state][dealer_state]])

        s = list(sp)
    gameCounter += 1

# Tests the Sarsa Lambda Model-Free Controller

wins = 0
losses = 0
gameTestCounter = 0

while(gameTestCounter < 50000):
    # Initializes game
    s, r, game_over = environment([], 0)
    episodes = []
    # Experience step (Plays through an episode)
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
