# SAC+SNN
# python results/cost_of_transport.py --file cost_of_transport_sac_snn_0_seed_0 --file cost_of_transport_sac_snn_0_seed_1 --file cost_of_transport_sac_snn_0_seed_2 --file cost_of_transport_sac_snn_0_seed_3 --file cost_of_transport_sac_snn_0_seed_4 --file cost_of_transport_sac_snn_1_seed_0 --file cost_of_transport_sac_snn_1_seed_1 --file cost_of_transport_sac_snn_1_seed_2 --file cost_of_transport_sac_snn_1_seed_3 --file cost_of_transport_sac_snn_1_seed_4 --file cost_of_transport_sac_snn_2_seed_0 --file cost_of_transport_sac_snn_2_seed_1 --file cost_of_transport_sac_snn_2_seed_2 --file cost_of_transport_sac_snn_2_seed_3 --file cost_of_transport_sac_snn_2_seed_4

import csv
import argparse
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Needed to run without X-server
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

del matplotlib.font_manager.weight_dict['roman']
matplotlib.font_manager._rebuild()
parser = argparse.ArgumentParser()
parser.add_argument(
    "--file",
    action='append',
    default=[],
    type=str,
)
parser.add_argument(
    "--algo",
    type=str,
    default="sac"
)

parser.add_argument(
    "--dir",
    action='append',
    default=[],
    type=str,
)
parser.add_argument('--xrange', type=int, default=1000)

args = parser.parse_args()

file_dir = "D:/HayashibeLab/Ant_injury/results/cost_of_transport/"
plt.rcParams["font.family"] = "Times New Roman" 
com_pos = []
com_vel = []
com_pos_snn = []
com_vel_snn = []
with open(file_dir + args.dir[0] +"/" +args.file[0] + ".csv") as f:
    reader = list(csv.reader(f))
    for j in range(1,len(reader)-1):
        com_pos.append(round(float(reader[j][2]), 3))
        com_vel.append(round(float(reader[j][5]), 3))
with open(file_dir + args.dir[1] +"/" + args.file[1] + ".csv") as f:
    reader = list(csv.reader(f))
    for j in range(1,len(reader)-1):
        com_pos_snn.append(round(float(reader[j][2]), 3))
        com_vel_snn.append(round(float(reader[j][5]), 3))

fig = plt.figure()
time = [i for i in range(1,1000)]
from matplotlib import cm
jet = [cm.jet(i/999) for i in range(999)]

plt.scatter(com_pos, com_vel, marker='',c=time, s=0.00001, cmap=cm.jet, zorder=1)
for i in range(len(com_pos)-1):
    plt.plot(com_pos[i:i+2], com_vel[i:i+2], linewidth=0.7, zorder=1, color=cm.jet(i/999))
# plt.scatter(com_pos, com_vel, label=args.algo, c=time, cmap=cm.jet, s=15, facecolors='None', edgecolors=jet, zorder=2)
ax = plt.colorbar()
ax.set_label('time steps', fontsize=15)
plt.scatter(com_pos, com_vel, facecolor='none', edgecolors=jet, s=7, lw=0.5, zorder=2)
plt.xlabel('Z position [m]', fontsize=15)
plt.ylabel('Z velocity [m/s]' , fontsize=15)

plt.xlim(0.3, 0.8)
plt.ylim(-1.5, 1.5)
fig_name = file_dir + "com_"+ args.algo +"_z" +"_"+args.dir[0] +".png"
plt.savefig(fig_name)
print('Saved a figure as {}'.format(fig_name))


fig = plt.figure()
time = [i for i in range(1,1000)]
from matplotlib import cm
plt.scatter(com_pos_snn, com_vel_snn, marker='',c=time, s=0.00001, cmap=cm.jet, zorder=1)
for i in range(len(com_pos_snn)-1):
    plt.plot(com_pos_snn[i:i+2], com_vel_snn[i:i+2], linewidth=0.7, zorder=1, color=cm.jet(i/999))
ax = plt.colorbar()
ax.set_label('time steps', fontsize=15)
plt.scatter(com_pos_snn, com_vel_snn, facecolor='none', edgecolors=jet, s=7, lw=0.5, zorder=2)
plt.xlabel('Z position [m]', fontsize=15)
plt.ylabel('Z velocity [m/s]', fontsize=15)

plt.xlim(0.3, 0.8)
plt.ylim(-1.5, 1.5)
fig_name = file_dir + "com_"+ args.algo +"_z_snn"+ "_"+args.dir[1] + ".png"
plt.savefig(fig_name)
print('Saved a figure as {}'.format(fig_name))