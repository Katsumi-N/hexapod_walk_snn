# hexapod_walk_snn
This is the repository for my paper "Spiking Neural Network Discovers Energy-efficient Hexapod Motion in Deep Reinforcement Learning".

# Requirement
* torch > 1.5.1
* pfrl > 0.1.0
* gym > 0.17.3
* dm_control
* dm2gym

# Setup
First, add hexapod.py and hexapod.xml in the "agent" of this repository to dm_control(for example, `C:\Users\Anaconda3\envs\(your envname)\Lib\site-packages\dm_control\suite`).

Next, add the following to init.py(`C:\Users\Anaconda3\envs\(your envname)\Lib\site-packages\dm_control\suite\__init__.py`)
`from dm_control.suite import hexapod`

# Usage
For example, run `python algo/soft_actor_critic/train_soft_actor_critic_snn_dm.py`
The learning results will be stored in the "result" folder.
