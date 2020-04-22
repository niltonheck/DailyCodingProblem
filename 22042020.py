# 22/04/2020

# You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.

class Log:
    def __init__(self):
        self.items = []

    def record(self, order_id):
        self.items.append(order_id)

    def get_last(self, i):
        return self.items[i - 1]

logger = Log()
logger.record("a")
logger.record("b")
logger.record("c")

print(logger.get_last(1))