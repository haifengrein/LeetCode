from collections import deque
from typing import Deque

class MovingAverage:
    __slots__ = ['queue', 'sum']

    def __init__(self, size: int):
        if size <= 0:
            raise ValueError("Size must be positive")
        self.queue: Deque[int] = deque(maxlen=size)
        self.sum: float = 0

    def next(self, val: int) -> float:
        if len(self.queue) == self.queue.maxlen:
            self.sum -= self.queue[0]
        self.queue.append(val)
        self.sum += val
        return self.sum / len(self.queue)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)