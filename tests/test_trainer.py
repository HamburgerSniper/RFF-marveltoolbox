import sys

sys.path.append('..')
import marveltoolbox as mt

if __name__ == '__main__':
    confs = mt.BaseConfs()
    trainer = mt.BaseTrainer(confs)
