from application_view import ApplicationView
from database import Database
from task import Task, TaskPriority
from task_creator import TaskCreator


class Application:
    def __init__(self):
        self.__task_creator = TaskCreator()
        self.__database = Database()
        self.__application_view = ApplicationView()

    def create_task(self):
        try:
            name = self.__application_view.read_task_name()
            text = self.__application_view.read_task_text()
            priority = self.__application_view.read_task_priority()

            task = self.__task_creator.create(name, text, priority)
            self.__database.add(task)
            self.__application_view.show_message("Task created successfully!")

        except ValueError as e:
            self.__application_view.show_error(str(e))
        except Exception as e:
            self.__application_view.show_error(f"An unexpected error occurred: {e}")

    def change_task(self):
        task_name = self.__application_view.read_task_name_to_change()
        task_to_change = self.__database.get_task_by_name(task_name)
        if task_to_change is None:
            self.__application_view.show_error(f"Task with name '{task_name}' not found.")
            return
        new_message = self.__application_view.read_new_task_text()
        new_priority = self.__application_view.read_new_task_priority()
        try:

            task_to_change.change_massage(new_message)
            task_to_change.change_priority(new_priority)
            self.__database.update_task(task_to_change)
            self.__application_view.show_message("Task changed successfully!")

        except ValueError as e:
            self.__application_view.show_error(str(e))
        except Exception as e:
             self.__application_view.show_error(f"An unexpected error occurred during task change: {e}")


    def get_tasks(self):
        tasks = self.__database.get_tasks()
        self.__application_view.show_tasks(tasks)

    def sort_tasks_by_name(self):
        tasks = self.__database.get_tasks()
        tasks.sort(key=lambda task: task.get_name())
        self.__application_view.show_tasks(tasks)

    def sort_tasks_by_priority(self):
        tasks = self.__database.get_tasks()
        tasks.sort(key=lambda task: task.get_priority())
        self.__application_view.show_tasks(tasks)

    def remove_task(self):
        try:
            task_name_to_remove = self.__application_view.read_task_name_to_remove()
            task_to_remove = self.__database.get_task_by_name(task_name_to_remove)

            if task_to_remove is None:
                self.__application_view.show_error(f"Task with name '{task_name_to_remove}' not found.")
                return

            self.__database.remove(task_to_remove)
            self.__application_view.show_message(f"Task '{task_name_to_remove}' removed successfully!")

        except ValueError as e:
            self.__application_view.show_error(str(e))
        except Exception as e:
            self.__application_view.show_error(f"An unexpected error occurred during task removal: {e}")