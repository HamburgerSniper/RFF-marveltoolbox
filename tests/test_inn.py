import sys

sys.path.append('..')
import marveltoolbox as mt

if __name__ == '__main__':
    test = mt.inn.RealNVP(1, 2, 3, 2, 2, False)
    print(test)
    # test = mt.inn.Glow(2,2,2)
    # print(test)
