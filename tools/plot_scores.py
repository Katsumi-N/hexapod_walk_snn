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
    parser = argparse.ArgumentParser()
    parser.add_argument('--title', type=str, default='')
    parser.add_argument('--file', action='append', dest='files',
                        default=[], type=str,
                        help='specify paths of scores.txt')
    parser.add_argument('--group1', action='append', dest='files',
                        default=[], type=str,
                        help='specify paths of scores.txt')
    parser.add_argument('--group2', action='append', dest='files',
                        default=[], type=str,
                        help='specify paths of scores.txt')
    parser.add_argument('--group3', action='append', dest='files',
                        default=[], type=str,
                        help='specify paths of scores.txt')

    parser.add_argument('--label', action='append', dest='labels',
                        default=[], type=str,
                        help='specify labels for scores.txt files')
    parser.add_argument('--xrange', type=int, default=5 * 10 ** 5)
    parser.add_argument('--yrange', type=list, default=[])

    args = parser.parse_args()

    assert len(args.files) > 0
    assert len(args.labels) == len(args.files)

    plt.rcParams["font.family"] = "Times New Roman" 
    for fpath, label in zip(args.files, args.labels):
        if os.path.isdir(fpath):
            fpath = os.path.join(fpath, 'scores.txt')
        assert os.path.exists(fpath)
        scores = pd.read_csv(fpath, delimiter='\t')
        plt.plot(scores['steps'], scores['mean'], label=label)
        plt.fill_between(scores['steps'],scores['mean']-scores['stdev'],scores['mean']+scores['stdev'],alpha=0.3)
        # 表示範囲の変更
        plt.xlim(0, args.xrange)
        plt.ylim(-5000, 3000)


    # for fpath in args.group1:
    #     if os.path.isdir(fpath):
    #         fpath = os.path.join(fpath, 'scores.txt')
    #     assert os.path.exists(fpath)
    #     scores = pd.read_csv(fpath, delimiter='\t')
    #     reward = 
    # plt.plot(scores['steps'], scores['mean'], label=label)
    # plt.fill_between(scores['steps'],scores['mean']-scores['stdev'],scores['mean']+scores['stdev'],alpha=0.3)
    #     # 表示範囲の変更
    # plt.xlim(0, args.xrange)
    # plt.ylim(-2000, 3000)


    # # 薄い点線
    plt.plot([i for i in range(1,args.xrange+1)], [1000 for _ in range(1,args.xrange+1)], linestyle="--", color="black", alpha=0.3)
    plt.xlabel('steps', fontsize=15)
    plt.ylabel('rewards', fontsize=15)
    plt.legend(loc='best')
    if args.title:
        plt.title(args.title, fontsize=15)

    fig_fname = args.files[0] + args.title
    plt.savefig(fig_fname + ".png")
    plt.savefig(fig_fname + ".pdf")
    print('Saved a figure as {}'.format(fig_fname))

if __name__ == '__main__':
    main()
