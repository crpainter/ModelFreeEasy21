import numpy as np

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
