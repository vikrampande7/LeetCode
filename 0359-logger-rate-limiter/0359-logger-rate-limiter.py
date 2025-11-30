class Logger:

    def __init__(self):
        self.next_allowed_hashmap = {}
        self.curr_hashmap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.curr_hashmap:
            self.curr_hashmap[message] = 0
        if message not in self.next_allowed_hashmap:
            self.next_allowed_hashmap[message] = 0

        if message in self.curr_hashmap:
            self.curr_hashmap[message] = timestamp
            if self.curr_hashmap[message] >= self.next_allowed_hashmap[message]:
                self.next_allowed_hashmap[message] = timestamp + 10
                return True
            else:
                return False
        
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)