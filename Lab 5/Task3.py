class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, data, priority):
        self.queue.append([data, priority])

    