import gym
from gym import spaces

from dm_control import suite
from dm_env import specs
import os

def convert_dm_control_to_gym_space(dm_control_space):
    r"""Convert dm_control space to gym space. """
    if isinstance(dm_control_space, specs.BoundedArray):
        space = spaces.Box(low=dm_control_space.minimum, 
                           high=dm_control_space.maximum, 
                           dtype=dm_control_space.dtype)
        assert space.shape == dm_control_space.shape
        return space
    elif isinstance(dm_control_space, specs.Array) and not isinstance(dm_control_space, specs.BoundedArray):
        space = spaces.Box(low=-float('inf'), 
                           high=float('inf'), 
                           shape=dm_control_space.shape, 
                           dtype=dm_control_space.dtype)
        return space
    elif isinstance(dm_control_space, dict):
        space = spaces.Dict({key: convert_dm_control_to_gym_space(value)
                             for key, value in dm_control_space.items()})
        #space = spaces.Box([convert_dm_control_to_gym_space(value) for value in dm_control_space.values()])
        return space


class DMSuiteEnv(gym.Env):
    def __init__(self, domain_name, task_name, task_kwargs=None, environment_kwargs=None, visualize_reward=False):
        self.env = suite.load(domain_name, 
                              task_name, 
                              task_kwargs=task_kwargs,
                              environment_kwargs=environment_kwargs, 
                              visualize_reward=visualize_reward)
        self.metadata = {'render.modes': ['human', 'rgb_array'],
                         'video.frames_per_second': round(1.0/self.env.control_timestep())}
        self.domain_name = domain_name
        self.task_name = task_name
        self.observation_space = convert_dm_control_to_gym_space(self.env.observation_spec())
        self.action_space = convert_dm_control_to_gym_space(self.env.action_spec())
        self.viewer = None
    
    def seed(self, seed):
        return self.env.task.random.seed(seed)

    def step(self, action):
        timestep = self.env.step(action)
        observation = timestep.observation

        reward = timestep.reward
        done = timestep.last()
        if self.domain_name=="hexapod" and self.env.physics.torso_upright() < -0.8:
            done = True


        # Add control cost
        import numpy as np
        ctrl_cost = 0.6 * np.sum(np.square(action))


        reward -= ctrl_cost
        info = {
            'energy': self.env.physics.get_energy(),
            'distance': self.env.physics.torso_velocity()[0],
        }

        # csvファイルにエネルギーと移動距離を書き込み
        # Write the energy and distance that agent moved to CSS file.
        # If you want to calculate the CoT (Cost of Transport), comment it out
        
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

    


        return observation, reward, done, info
    
    def reset(self):
        timestep = self.env.reset()
        return timestep.observation
    
    def render(self, mode='human', **kwargs):
        if 'camera_id' not in kwargs:
            kwargs['camera_id'] = 2  # Tracking camera
        use_opencv_renderer = kwargs.pop('use_opencv_renderer', True)

        img = self.env.physics.render(**kwargs)
        if mode == 'rgb_array':
            return img
        elif mode == 'human':
            if self.viewer is None:
                if not use_opencv_renderer:
                    from gym.envs.classic_control import rendering
                    self.viewer = rendering.SimpleImageViewer(maxwidth=1024)
                else:
                    from . import OpenCVImageViewer
                    
                    self.viewer = OpenCVImageViewer()
            self.viewer.imshow(img)
            return self.viewer.isopen
        else:
            raise NotImplementedError

    def close(self):
        if self.viewer is not None:
            self.viewer.close()
            self.viewer = None
        return self.env.close()
