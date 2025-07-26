from application import Application

app = Application()

while True:
    print("\nTask Manager Menu:")
    print("1. Create Task")
    print("2. Change Task")
    print("3. List Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        app.create_task()
    elif choice == "2":
        app.change_task()
    elif choice == "3":
        app.get_tasks()
    elif choice == "4":
        print("Exiting Task Manager...")
        break
    else:
        print("Invalid choice. Please try again.")
