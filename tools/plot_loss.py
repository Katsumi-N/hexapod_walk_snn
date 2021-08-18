#python tools/plot_scores.py --title Ant-v3_PPO --file D:\HayashibeLab\Ant_injury\results\d4208915733399bf58b22f3cfdecfc5d27cff6d1-b1685cd0-e9f0949d --label return
import argparse
import os

import matplotlib
matplotlib.use('Agg')  # Needed to run without X-server
import matplotlib.pyplot as plt
import pandas as pd


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--title', type=str, default='')
    parser.add_argument('--file', action='append', dest='files',
                        default=[], type=str,
                        help='specify paths of scores.txt')
    parser.add_argument('--label', action='append', dest='labels',
                        default=[], type=str,
                        help='specify labels for scores.txt files')
    args = parser.parse_args()

    assert len(args.files) > 0
    assert len(args.labels) == len(args.files)

    for fpath, label in zip(args.files, args.labels):
        if os.path.isdir(fpath):
            fpath = os.path.join(fpath, 'scores.txt')
        assert os.path.exists(fpath)
        scores = pd.read_csv(fpath, delimiter='\t')
        plt.plot(scores['steps'], (scores['average_q_func1_loss']+scores['average_q_func2_loss'])/2, label=label)
        # 表示範囲の変更
        plt.xlim(0, 1000000)

        # plt.fill_between(scores['steps'],scores['mean']-scores['stdev'],scores['mean']+scores['stdev'],alpha=0.3)

    plt.xlabel('steps', fontsize=15)
    plt.ylabel('loss', fontsize=15)
    plt.legend(loc='best')
    if args.title:
        plt.title(args.title)

    fig_fname = args.files[0] + args.title + '.png'
    plt.savefig(fig_fname)
    print('Saved a figure as {}'.format(fig_fname))

if __name__ == '__main__':
    main()
