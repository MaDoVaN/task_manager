from task import Task


class TaskCreator:
    def create(self, name: str, text: str, priority):
        return Task(name, text, priority)
