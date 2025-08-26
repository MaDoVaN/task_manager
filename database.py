from task import Task
from typing import List, Optional

class Database:
    def __init__(self):
        self.__tasks: List[Task] = []

    def add(self, task: Task):

        if not isinstance(task, Task):
            raise TypeError("task must be an instance of Task")
        self.__tasks.append(task)

    def remove(self, task: Task):
        try:
            self.__tasks.remove(task)
        except ValueError:
            raise ValueError(f"Task '{task}' not found in database.")

    def get_tasks(self) -> List[Task]:
        return self.__tasks

    def is_task_list_empty(self) -> bool:
        return len(self.__tasks) == 0

    def get_task_by_name(self, name: str) -> Optional[Task]:
        for task in self.__tasks:

            if task.get_name() == name:
                return task
        return None

    def update_task(self, task: Task):

        if task in self.__tasks:
            index = self.__tasks.index(task)
            self.__tasks[index] = task
        else:
            print(f"Warning: Task '{task}' not found in database for update.")
