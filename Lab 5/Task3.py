class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, data, priority):
        self.queue.append([data, priority])

    def pop(self):
        if len(self.queue) == 0:
            return None

        min_index = 0

        for i in range(len(self.queue)):
            if self.queue[i][1] < self.queue[min_index][1]:
                min_index = i

        return self.queue.pop(min_index)

    def is_empty(self):
        return len(self.queue) == 0

pq = PriorityQueue()

pq.push("Low Priority Task", 3)
pq.push("High Priority Task", 1)
pq.push("Medium Priority Task", 2)

while not pq.is_empty():
    print(pq.pop())