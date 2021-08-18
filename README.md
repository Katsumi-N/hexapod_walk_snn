# hexapod_walk_snn
This is the repository for my paper "Spiking Neural Network Discovers Energy-efficient Hexapod Motion in Deep Reinforcement Learning".

# Requirement
* torch > 1.5.1
* pfrl > 0.1.0
* gym > 0.17.3
* dm_control
* dm2gym

# Setup
1. Add hexapod.py and hexapod.xml in the "agent" of this repository to dm_control(for example, `C:\Users\Anaconda3\envs\(your envname)\Lib\site-packages\dm_control\suite`).

2. add the following to init.py(`C:\Users\Anaconda3\envs\(your envname)\Lib\site-packages\dm_control\suite\__init__.py`)
`from dm_control.suite import hexapod`

3. Change dm_suite_env.py in dm2gym(`C:\Users\Anaconda3\envs\(your envname)\Lib\site-packages\dm2gym\envs`) to the "dm_suite_env.py" in the repository.
If you want to calculate the CoT (Cost of Transport), uncomment out the following statement.


```
        # import csv
        # file_name = "cot_sac_snn"
        # if not os.path.exists("results/cost_of_transport/alpha_6/" + file_name + ".csv"):
        #     with open("results/cost_of_transport/alpha_6/" + file_name + ".csv", 'w') as cot:
        #         w = csv.writer(cot, lineterminator="\n")
        #         w.writerow(["Energy", "Distance"])
        # else:
        #     with open("results/cost_of_transport/alpha_6/" + file_name + ".csv", 'a', newline='') as cot:
        #         w = csv.writer(cot)
        #         if not done:
        #             w.writerow([info['energy'], info['distance']])
        #         else:
        #             w.writerow(["end"])
```


# Usage
1. Training
 For example, run `python algo/soft_actor_critic/train_soft_actor_critic_snn_dm.py`
The learning results will be stored in the "result" folder.

2. Calculating CoT
 Uncomment the above description before starting the training. The energy and distance traveled will be written in a csv file.
Next, run "cost_of_transport.py". For example, `python cost_of_transport.py --file cot_sac_snn --alpha alpha_6`


# Acknowledgments
The code in this repository is based on the code at https://github.com/combra-lab/pop-spiking-deep-rl
