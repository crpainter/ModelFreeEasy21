import numpy as np

def draw(num):
    roll = np.random.rand(1);
    color = -1;
    if (roll < (2 / 3)):
        color = 1
    num = num + (color * np.random.randint(1, 10));
    return num


def environment(s, a):
    sp = s;
    if (s == []):
        sp[0] = np.random.randint(1,10);
        sp[1] = np.random.randint(1, 10);
        r = 0;
    if (a == 'hit'):
        sp[0] = draw(s[0])
        if (sp[0] < 1 or sp[0] > 21):
            r = -1
    if (a == 'stick'):
        while(sp[1] < 17):
            sp[1] = draw([sp[1]]);
        if(sp[1] > sp[0]):
            r = -1;
        if (sp[1] > sp[0]):
            r = -1;

    return sp, r

