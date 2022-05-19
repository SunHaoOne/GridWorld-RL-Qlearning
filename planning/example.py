import heapq
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

if __name__ == "__main__":

    pq = PriorityQueue()

    positions = [(0, 0), (0, 1), (0, 2), (1, 1)]
    values = [2, 3, 4, 5]

    for i in range(len(values)):
        pq.put(positions[i], values[i]);


    for i in range(len(values)):
        print(pq.get())


    cost_so_far = {}
    start = (0, 0)
    cost_so_far[start] = ['new', 10, 10]
    print(cost_so_far[start])

    print("state:", cost_so_far[start][0])
    print("k:", cost_so_far[start][1])
    print("h:", cost_so_far[start][2])

    openlist = PriorityQueue()

