import numpy as np
import matplotlib.pyplot as mplot

def draw(num):
    color = -1;
    roll = np.random.rand(1);
    if (roll < (1)):
        color = 1
    num = num + (color * np.random.randint(1, 10));
    return num


def environment(s, a):
    r = 0;
    sp = list(s)
    game_over = 0;
    if (sp == []):
        sp = np.zeros(2, dtype=int);
        sp[0] = np.random.randint(1,11);
        sp[1] = np.random.randint(1, 11);
        return sp, r, game_over;
    # For reference, 0 is hit and 1 is stick
    if (not a):
        sp[0] = draw(s[0])
        if (sp[0] < 1 or sp[0] > 21):
            r = -1
            game_over = 1
            while (sp[1] < 17 and sp[1] > 0):
                sp[1] = draw(sp[1])
            if (sp[1] > 21 or sp[1] < 1):
                r = 0
                return sp, r, game_over
            return sp, r, game_over
    if (a):
        game_over = 1
        while(sp[1] < 17 and sp[1] > 0):
            sp[1] = draw(sp[1]);
        if (sp[1] > 21 or sp[1] < 1):
            r = 1;
            return sp, r, game_over
        if(sp[1] > sp[0]):
            r = -1;
        if (sp[1] < sp[0]):
            r = 1;
    return sp, r, game_over

# Creates look-up table model defaults
NSA = np.zeros((2,21,10))
QSA = np.zeros((2,21,10))
pi = np.zeros((21,10), dtype=int)
gameCounter = 0

while(gameCounter < 500000):
    # Initializes game
    s, r, game_over = environment([], 0)
    episodes = []
    # Experience step (Plays through an episode)
    #print("playing")
    while(not game_over):
        policy_action = pi[s[0] - 1][s[1] - 1]
        sp, r, game_over = environment(s, policy_action)
        episodes.append(([s[0],s[1]], policy_action, r))
        s = sp
    gameCounter += 1
    wins = wins + (r > 0)
    losses = losses + (r < 0)
    # Learning step
    #print("learning from game")
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


wins = 0
losses = 0
gameTestCounter = 0

while(gameTestCounter < 1000):
    # Initializes game
    s, r, game_over = environment([], 0)
    episodes = []
    # Experience step (Plays through an episode)
    #print("playing")
    while(not game_over):
        policy_action = pi[s[0] - 1][s[1] - 1]
        sp, r, game_over = environment(s, policy_action)
        episodes.append(([s[0],s[1]], policy_action, r))
        s = sp
    gameTestCounter += 1
    wins = wins + (r > 0)
    losses = losses + (r < 0)
winRatio = wins/gameTestCounter
lossRatio = losses/gameTestCounter
#mplot.contour(NSA)
#mplot.show()


