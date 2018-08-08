from State_Vector import state_vec
from environment import environment
import numpy as np
import matplotlib.pyplot as mplot

# Trains the Sarsa Lambda Model-Free Controller

# Creates look-up table model defaults
NSA = np.zeros((2,21,10))
QSA = np.zeros((2,21,10))
pi = np.zeros((21,10), dtype=int)
gameCounter = 0
lamb = 0
theta = np.zeros((36))

while(gameCounter < 100):
    # Initializes game
    s, r, game_over = environment([], 0)
    episodes = []
    ESA = np.zeros((2, 21, 10))
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
        SA_pair_val = np.multiply(np.transpose(state_vec(player_state,dealer_state,a)),theta)

        alpha = 0.01
        ap = pi[sp[0] - 1][sp[1] - 1]
        if (game_over):
            delta = r - SA_pair_val
        else:
            #ap = np.argmax([QSA[0][sp[0] - 1][sp[1] - 1], QSA[1][sp[0] - 1][sp[1] - 1]])
            delta = r + QSA[ap][sp[0] - 1][sp[1] - 1] - SA_pair_val
        QSA = QSA + alpha * delta * ESA
        ESA = lamb * ESA
        # Updating the policy table epsilon greedily
        e = 0.05
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
QSA_Sarsa = np.copy(QSA)
mplot.contour(pi)
mplot.show()

# QDiff = QSA_GLIE - QSA_Sarsa
# QDSquare = np.square(QDiff)
# QMean = np.mean(QDSquare)
