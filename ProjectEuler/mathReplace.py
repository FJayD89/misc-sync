# mathReplace
from math import log10, floor


def mathReplace(x, digit, index):
    log = 10**(floor(log10(x)) - index)
    ret = x + log*(10*(x//(10*log)) - x//log + digit)
    return ret


if __name__ == '__main__':
    print(mathReplace(11, 2, 2))
