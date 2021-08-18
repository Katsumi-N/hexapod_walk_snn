#python tools/plot_scores.py --title Ant-v3_PPO --file D:\HayashibeLab\Ant_injury\results\d4208915733399bf58b22f3cfdecfc5d27cff6d1-b1685cd0-e9f0949d --label return
import argparse
import os

import matplotlib
matplotlib.use('Agg')  # Needed to run without X-server
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

del matplotlib.font_manager.weight_dict['roman']
matplotlib.font_manager._rebuild()
def main():
    x = [i for i in range(15)]
    y = [1, 1, 3, 2, 3, 8, 1, 1, 3, 2, 3, 8, 1, 1, 3]
    plt.plot(x, [5 for _ in range(15)], linestyle="--", color="black", alpha=0.3)
    plt.plot(x,y)
    # plt.xlabel("Time", fontsize=15)
    # plt.ylabel("Voltage", fontsize=15)
    plt.savefig("lif.pdf")
if __name__ == '__main__':
    main()
