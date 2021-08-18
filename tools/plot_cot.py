#--file D:\HayashibeLab\Ant_injury\results\cost_of_transport\cot_sac_snn_light.csv --file D:\HayashibeLab\Ant_injury\results\cost_of_transport\cot_td3_snn_light.csv --file D:\HayashibeLab\Ant_injury\results\cost_of_transport\cot_ddpg_snn_light.csv --label SAC+SNN --label TD3+SNN --label DDPG+SNN

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
    parser.add_argument('--xrange', type=int, default=0.8)
    parser.add_argument('--yrange', type=list, default=[])

    args = parser.parse_args()

    assert len(args.files) > 0
    assert len(args.labels) == len(args.files)

    plt.rcParams["font.family"] = "Times New Roman" 
    for fpath, label in zip(args.files, args.labels):
        # if os.path.isdir(fpath):
        #     fpath = os.path.join(fpath, ".csv")
        assert os.path.exists(fpath)
        scores = pd.read_csv(fpath, header=0)
        plt.plot(scores['alpha'], scores['cot'], label=label, marker="o")
        plt.fill_between(scores['alpha'],scores['cot']-scores['std'],scores['cot']+scores['std'],alpha=0.3)
        # 表示範囲の変更
        plt.xlim(0, args.xrange)
        plt.ylim(1, 6)




    # # 薄い点線
    # plt.plot([i for i in range(1,args.xrange+1)], [1000 for _ in range(1,args.xrange+1)], linestyle="--", color="black", alpha=0.3)
    plt.xlabel('alpha', fontsize=15)
    plt.ylabel('Cost of Transport', fontsize=15)
    plt.legend(loc='best')
    # if args.title:
    #     plt.title(args.title, fontsize=20)

    fig_fname = args.files[0] + args.title
    plt.savefig(fig_fname + ".png")
    plt.savefig(fig_fname + ".pdf")
    print('Saved a figure as {}'.format(fig_fname))

if __name__ == '__main__':
    main()
