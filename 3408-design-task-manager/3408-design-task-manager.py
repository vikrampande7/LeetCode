class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.priority_queue = []
        self.priority = {}
        self.users = {}
        for task in tasks:
            self.add(task[0], task[1], task[2])

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.priority_queue, (-priority, -taskId))
        self.priority[taskId] = priority
        self.users[taskId] = userId

    def edit(self, taskId: int, newPriority: int) -> None:
        heapq.heappush(self.priority_queue, (-newPriority, -taskId))
        self.priority[taskId] = newPriority

    def rmv(self, taskId: int) -> None:
        self.priority[taskId] = -1

    def execTop(self) -> int:
        while self.priority_queue:
            p, t_id = heapq.heappop(self.priority_queue)
            p, t_id = -p, -t_id
            if self.priority.get(t_id, -2) == p:
                self.priority[t_id] = -1
                return self.users.get(t_id, -1)
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()