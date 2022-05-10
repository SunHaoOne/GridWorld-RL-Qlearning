# GridWorld-RL-Qlearning
A simple reinforcement learning environment based on `numpy`. 

<div align=center>
<img src="https://github.com/SunHaoOne/GridWorld-RL-Qlearning/blob/main/img/vis_q_table.png" width="80%" height="80%"> 
</div>


## About The Project

This repo includes a reinforcement learning environment `GridWorld` and `Q-learning` algorithm. And some files for visualize the train and test `reward`, `Q-table`, `value table` and `route map`. The agent will born from a `random` position in this GridWorld, and the destination is the `dense` area in this map.

Besides, we have added a environment for searching. The methods include 'Breath First Search', 'Dijkstra', 'Astar'

### Action Space
- `Action`: (4, )

| Index | 0    | 1    | 2    | 3     |
| ----- | ---- | ---- | ---- | ----- |
| Value | up   | down | left | right |
### State Space
- `State`: (2, )

| Index | 0    | 1    |
| ----- | ---- | ---- | 
| Value | x_pos| y_pos |

### Reward Shaping

There are 4 kinds of reward in this environment, including:
- `Time penalty reward` (Encourage the agent to reach the destination quickly)
- `Distance reward` (Encourage the agent to reach the dense area)
- `Max step reward` (if the step > MAX_STEP, reward = -?, done = True)
- `Success reward` (if the agent reach the destination, reward = ?, done = True)

## Getting Started

Just download the repositories. And you can also use `conda` to create a new conda enviroment.
```bash
git clone https://github.com/SunHaoOne/GridWorld-RL-Qlearning.git
cd GridWorld-RL-Qlearning
pip install requirements.txt
```


### Train and Test Agent

- Train agent:
```bash
python train.py
```
- Test agent:
```bash
python test.py
```

### Visulize Environment

Warning: The agent only chose a `random` action for the agent.

```bash
python -m utils.visStaticEnv
```
<div align=center>
<img src="https://github.com/SunHaoOne/GridWorld-RL-Qlearning/blob/main/img/visStaticEnv.gif" width="20%" height="20%"> 
</div>
<p align="center"> Fig.1 Visualize GridWorld Static Environment</p>

### Show Results

```bash
python vis_q_table.py
python vis_reward.py
python vis_route.py
```


<div align=center>
<img src="https://github.com/SunHaoOne/GridWorld-RL-Qlearning/blob/main/img/vis_q_table.png" width="80%" height="80%"> 
</div>
<p align="center"> Fig.2 Visualize GridWorld Map, Q table and Value table</p>

<div align=center>
<img src="https://github.com/SunHaoOne/GridWorld-RL-Qlearning/blob/main/img/vis_reward.png" width="50%" height="50%"> 
</div>
<p align="center"> Fig.3 Visualize train and test reward</p>

<div align=center>
<img src="https://github.com/SunHaoOne/GridWorld-RL-Qlearning/blob/main/img/vis_route.png" width="80%" height="80%">                 
</div>
<p align="center"> Fig.4 Visualize GridWorld Map and agent route</p>

<div align=center>
<img src="https://github.com/SunHaoOne/GridWorld-RL-Qlearning/blob/main/img/vis_route_large.png" width="80%" height="80%">                 
</div>
<p align="center"> Fig.5 Visualize Large GridWorld Map and agent route</p>


### Searching Method

Two kinds of visualization methods is provided in the following codes. Show the `dynamic searching process` or the `final searching result`, the default mode is `final searching result` 
- `Breath First Search`
- `Dijkstra`
- `Astar`

```bash
python -m planning.breadth_first_search
python -m planning.dijkstra_search
python -m planning.a_star_search
```

<div align=center>
<img src="https://github.com/SunHaoOne/GridWorld-RL-Qlearning/blob/main/img/breath_first_search.png" width="80%" height="80%"> 
</div>
<p align="center"> Fig.6 Breach First Search</p>

<div align=center>
<img src="https://github.com/SunHaoOne/GridWorld-RL-Qlearning/blob/main/img/test.png" width="80%" height="80%"> 
</div>
<p align="center"> Fig.6 Breach First Search</p>

<div align=center>
<img src="https://github.com/SunHaoOne/GridWorld-RL-Qlearning/blob/main/img/dijkstra_search.png" width="80%" height="80%"> 
</div>
<p align="center"> Fig.7 Dijkstar Search</p>

<div align=center>
<img src="https://github.com/SunHaoOne/GridWorld-RL-Qlearning/blob/main/img/a_star_search.png" width="80%" height="80%"> 
</div>
<p align="center"> Fig.8 Astar Search</p>
