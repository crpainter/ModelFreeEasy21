import numpy as np

def draw(num):
    color = -1;
    roll = np.random.rand(1);
    if (roll < (2 / 3)):
        color = 1
    num = num + (color * np.random.randint(1, 10));
    return num


def environment(s, a):
    sp = s;
    r = 0;
    if (sp == []):
        sp = np.zeros(2);
        sp[0] = np.random.randint(1,10);
        sp[1] = np.random.randint(1, 10);
        return sp, r;
    if (a == 'hit'):
        sp[0] = draw(s[0])
        if (sp[0] < 1 or sp[0] > 21):
            r = -1
            return sp, r;
    if (a == 'stick'):
        while(sp[1] < 17):
            sp[1] = draw(sp[1]);
        if (sp[1] > 21):
            r = 1;
            return sp, r
        if(sp[1] > sp[0]):
            r = -1;
        if (sp[1] < sp[0]):
            r = 1;
    return sp, r




