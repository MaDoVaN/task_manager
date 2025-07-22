from task import Task


class Database:
    def __init__(self):
        self.__tasks = list()

    def add(self, task: Task):
        if not isinstance(task, Task):
           raise TypeError('text')

        self.__tasks.append(task)

    def remove(self, task):
        pass

    def get_tasks(self):
        pass