class RecentCounter:

    def __init__(self):
        self.queue = []     #队列思想

    def ping(self, t: int) -> int:
        self.queue.append(t)
        
        while (len(self.queue) != 0):
            if (self.queue[0] + 3000 < t):
                self.queue.pop(0)
            else:
                break
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
