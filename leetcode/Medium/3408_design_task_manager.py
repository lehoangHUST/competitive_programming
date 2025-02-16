class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.queuePriority = []
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.queuePriority.append([userId, taskId, priority])

    def edit(self, taskId: int, newPriority: int) -> None:
        for task in self.queuePriority:
            if task[1] == taskId:
                task[2] = newPriority
                break

    def rmv(self, taskId: int) -> None:
        self.queuePriority = [task for task in self.queuePriority if task[1] != taskId]

    def execTop(self) -> int:
        self.queuePriority.sort(key=lambda x: (-x[2], -x[1]))
        if not self.queuePriority:
            return -1
        return self.queuePriority.pop(0)[0]