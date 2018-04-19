# Agent playing atari games using Deep Q-Learning with web visualization of playing.
### Project for Artificial Intelligence course 2018.

based on DeepMind [paper](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf)
---
# Running
Go to directory src
```bash
cd src
```

## Server
Install requirements
```bash
pip install -r server/requirements.txt
```
Launch web server with model weight saved in out directory
```bash
python app.py
```
## Training
Install requirements
```bash
pip install -r trainer/requirements.txt
```
Run with default parameters
```bash
python atari.py
```
*TODO
~~For decription of parameters run with~~
```bash
python atari.py --help
```
