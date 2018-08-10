from environment import environment
import numpy as np
import matplotlib.pyplot as mplot

# Trains the Sarsa Lambda Model-Free Controller

# Creates look-up table model defaults
pi = np.zeros((21,10), dtype=int)
gameCounter = 0
lamb = 1
theta = np.zeros((36))

while(gameCounter < 5000):
    # Initializes game
    s, r, game_over = environment([], 0)
    episodes = []
    ESA = np.zeros((36))
    # Experience step (Plays through an episode)
    while(not game_over):

        # Playing a single turn
        policy_action = pi[s[0] - 1][s[1] - 1]
        sp, r, game_over = environment(s, policy_action)

        # Sarsa updates after each turn
        player_state = s[0]
        dealer_state = s[1]
        a = policy_action
        ESA = ESA + state_vec(player_state,dealer_state,a)
        SA_pair_val = np.dot(np.transpose(state_vec(player_state,dealer_state,a)),theta)

        alpha = 0.01
        if (game_over):
            delta = r - SA_pair_val
        else:
            next_state_val = np.argmax([np.dot(np.transpose(state_vec(sp[0],sp[1],0)),theta),np.dot(np.transpose(state_vec(sp[0],sp[1],1)),theta)])
            delta = r + next_state_val - SA_pair_val
        theta = theta + alpha * delta * state_vec(player_state,dealer_state,a)
        # ESA = lamb * ESA
        # Updating the policy table epsilon greedily
        e = 0.05
        if (e >= np.random.rand(1)):
            pi[player_state - 1][dealer_state - 1] = np.random.randint(0, 2)
        else:
            pi[player_state - 1][dealer_state - 1] = np.argmax([np.dot(np.transpose(state_vec(player_state,dealer_state,0)),theta), np.dot(np.transpose(state_vec(player_state,dealer_state,1)),theta)])

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

# QDiff = QSA_GLIE - QSA_Sarsa
# QDSquare = np.square(QDiff)
# QMean = np.mean(QDSquare)
