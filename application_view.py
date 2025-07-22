from task import Task, TaskPriority


class ApplicationView:

    def display(self, tasks: list[Task]):
        if not tasks:
            print("No tasks to display.")
            return

        for task in tasks:
            print(f"Task: {task}")

    def read_task_name(self) -> str:
        return input("Enter task name: ")

    def read_task_text(self) -> str:
        return input("Enter task description: ")

    def read_task_priority(self) -> TaskPriority:
        while True:
            priority_str = input("Enter task priority (high, medium, low): ").lower()
            try:
                return TaskPriority(priority_str)
            except ValueError:
                print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

    def show_message(self, message: str):
        print(message)

    def show_error(self, message: str):
        print(f"Error: {message}")

    def read_task_name_to_change(self) -> str:
        return input("Enter the name of the task you want to change: ")

    def read_new_task_text(self) -> str:
        return input("Enter the new task description: ")

    def read_new_task_priority(self) -> TaskPriority:
        while True:
            priority_str = input("Enter the new task priority (high, medium, low): ").lower()
            try:
                return TaskPriority(priority_str)
            except ValueError:
                print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
