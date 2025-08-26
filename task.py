from enum import Enum


class TaskPriority(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

    @staticmethod
    def _get_priority_order():
        return {
            TaskPriority.HIGH: 1,
            TaskPriority.MEDIUM: 2,
            TaskPriority.LOW: 3
        }

    def __str__(self):
        return self.value

    def __lt__(self, other):
        if isinstance(other, TaskPriority):
            order_map = TaskPriority._get_priority_order()
            return order_map[self] < order_map[other]
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, TaskPriority):
            return self.value == other.value
        return NotImplemented

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