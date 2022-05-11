## Notes for Searching Algorithm
> Please refer to this page `https://www.redblobgames.com/pathfinding/a-star/introduction.html`

### Algorithm Notes
```
class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return not self.elements

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]
```
### 1. Breath First Search

- `Queue()` is the deque
- `came_from` is a dictionary.
    - `keys`: end point
    - `values`: start point
    - for example, `{(0, 0): None, (0, 1): (0, 0), (1, 0): (0, 0), (1, 1): (0, 1)}`
- `env.neighbors(current)`: return the available neighbors of the current position
    - First, find the 4 direction from the current position
    - Then, if the neighbors are in the  edge area or the wall area (using `filter function`), remove them
 
 
 ### 2. Dijkstra Search
 
 - In this experiment, we additionally defined the `cost map` to estimate the cost from the `start point` to `end point` 
 - `PriorityQueue()` is the priority queue
 - `came_from` is a dictionary.
    - `keys`: end point
    - `values`: start point
    - for example, `{(0, 0): None, (0, 1): (0, 0), (1, 0): (0, 0), (1, 1): (0, 1)}`
 - `cost_so_far` is also a dictionary.
    - `keys`: end point
    - `values`: cost value
    - for example, `{(0, 0): 0, (0, 1): 8, (1, 0): 9, (1, 1): 11, (2, 0): 14, (3, 0): 15, (4, 0): 18}`

 
 ### 3. Astar Search
 
 - In this experiment, we additionally defined the `cost map` to estimate the cost from the `start point` to `end point` 
 - `PriorityQueue()` is the priority queue
 - Besides, we defined the distance function: `heuristic distance`
 ```
def heuristic(location_a, location_b):
    (x1, y1) = location_a
    (x2, y2) = location_b
    return abs(x1 - x2) + abs(y1 - y2)
```
 - Contrast to `Dijkstra Search`, the cost function is different.:
    - First, calculate the cost: `new_cost = cost_so_far[current] + env.cost(current, next)`
    - The difference between these two method:
        - `Dijkstra Search`: `priority = new_cost`
        - `Astar Search`: `priority = new_cost + heuristic(next, goal)`
    - Then put them into the priority queue.

### 4. Dstar Search

> `TODOLIST`: Dstart = Dynamic Astar


### Visualization Notes

- Two kinds of visualization methods is provided:
    - `visualize_searching`
    - `visualize_result`
### 1. Dynamic Visualization

- After running the searching algorithm, we can get a `came_from` dictionary, such as `{end_point: start_point, ...}`
- So we need to backtrack or traverse this dictionary:
    - First, the last_point is the GOAL
    - Then, we can get the point (father nodes) before this last_point by the dictionary, `last_point = dict[last_point]`
    - Loop until the last_point is the START
- `matplotlib.pyplot` is used for dynamic visualization:
    - In the loop, we add the `plt.pause(0.01)` to shows the searching areas.
    - `WARNING`: In the larger map, searching is slower than smaller map.
    
### 2. Results Visualization

- Save the final searching area map and route map
- Visualize the cost map