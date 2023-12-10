import sys

sys.path.append('..')
import marveltoolbox as mt

if __name__ == '__main__':
    loader = mt.datasets.load_moons(10000, 50, True)
    # print(next(iter(loader)))

    loader = mt.datasets.load_toy(2000, 50, True)
    print(next(iter(loader)))
