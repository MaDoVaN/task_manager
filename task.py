from enum import Enum


class TaskPriority(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class Task:
    def __init__(self, name: str, input_massage: str, priority: TaskPriority):
        self.__name = name
        self.__massage = input_massage
        self.__priority = priority

    def is_correct_priority(self, priority: TaskPriority):
        return priority == TaskPriority.HIGH or priority == TaskPriority.MEDIUM or priority == TaskPriority.LOW

    def change_massage(self, new_massage):
        self.__massage = new_massage

    def change_priority(self, new_priority):
        if self.is_correct_priority:
            self.__priority = new_priority

    def get_massage(self):
        return self.__massage

    def get_priority(self):
        return self.__priority

    def get_name(self):
        return self.__name