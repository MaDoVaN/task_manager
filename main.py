from application import Application

app = Application()
app_is_running = True

while app_is_running:
    print("\nTask Manager Menu:")
    print("1. Create Task")
    print("2. Delete Task")
    print("3. Change Task")
    print("4. List Tasks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        app.create_task()
    elif choice == "2":
        app.change_task()
    elif choice == "3":
        app.change_task()
    elif choice == "4":
        app.get_tasks()

        choice = input("You can sort tasks: 1 - by name, 2 - by priority. Enter your choice: ")
        if choice == '1':
            app.sort_tasks_by_name()
        elif choice == '2':
            app.sort_tasks_by_priority()

    elif choice == "5":
        print("Exiting Task Manager...")
        app_is_running = False
    else:
        print("Invalid choice. Please try again.")
