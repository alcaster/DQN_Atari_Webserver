import io
import time

import gym
from PIL import Image
from cameras.base_camera import BaseCamera


class CameraGymGame1(BaseCamera):
    @staticmethod
    def frames():
        env = gym.make('Breakout-v0')
        while True:
            env.reset()
            done = False
            while not done:  # or i > max_steps:
                time.sleep(0.05)
                observation, reward, done, _ = env.step(env.action_space.sample())
                obs = env.render(mode='rgb_array')
                img = Image.fromarray(obs, 'RGB')
                imgByteArr = io.BytesIO()
                img.save(imgByteArr, format='PNG')
                yield imgByteArr.getvalue()


class CartPole(BaseCamera):
    @staticmethod
    def frames():
        env = gym.make('CartPole-v0')
        while True:
            env.reset()
            done = False
            while not done:  # or i > max_steps:
                time.sleep(0.05)
                observation, reward, done, _ = env.step(env.action_space.sample())
                obs = env.render(mode='rgb_array')
                img = Image.fromarray(obs, 'RGB')
                imgByteArr = io.BytesIO()
                img.save(imgByteArr, format='PNG')
                yield imgByteArr.getvalue()


class MsPacman(BaseCamera):
    @staticmethod
    def frames():
        env = gym.make('MsPacman-v0')
        while True:
            env.reset()
            done = False
            while not done:  # or i > max_steps:
                time.sleep(0.05)
                observation, reward, done, _ = env.step(env.action_space.sample())
                obs = env.render(mode='rgb_array')
                img = Image.fromarray(obs, 'RGB')
                imgByteArr = io.BytesIO()
                img.save(imgByteArr, format='PNG')
                yield imgByteArr.getvalue()


class Pong(BaseCamera):
    @staticmethod
    def frames():
        env = gym.make('Pong-v0')
        while True:
            env.reset()
            done = False
            while not done:  # or i > max_steps:
                time.sleep(0.05)
                observation, reward, done, _ = env.step(env.action_space.sample())
                obs = env.render(mode='rgb_array')
                img = Image.fromarray(obs, 'RGB')
                imgByteArr = io.BytesIO()
                img.save(imgByteArr, format='PNG')
                yield imgByteArr.getvalue()


class SpaceInvaders(BaseCamera):
    @staticmethod
    def frames():
        env = gym.make('SpaceInvaders-v0')
        while True:
            env.reset()
            done = False
            while not done:  # or i > max_steps:
                time.sleep(0.05)
                observation, reward, done, _ = env.step(env.action_space.sample())
                obs = env.render(mode='rgb_array')
                img = Image.fromarray(obs, 'RGB')
                imgByteArr = io.BytesIO()
                img.save(imgByteArr, format='PNG')
                yield imgByteArr.getvalue()


def test():
    env = gym.make('Breakout-v0')
    env.reset()
    while 1:
        env.step(env.action_space.sample())
        obs = env.render(mode='rgb_array')
        img = Image.fromarray(obs, 'RGB')
        imgByteArr = io.BytesIO()
        img.save(imgByteArr, format='PNG')
        img.show()  # to many
    env.close()


if __name__ == '__main__':
    test()
