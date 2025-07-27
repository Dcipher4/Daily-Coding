# import hashlib
# def hash_password(password):
#     return hashlib.sha256(password.encode()).hexdigest()
#
# def register():
#     username = input("Enter a username: ")
#
#     # Check if username already exists
#     with open("user.txt", "r") as file:
#         for line in file:
#             old_user, _ = line.strip().split(":")
#             if old_user == username:
#                 print("Username already exists!, Try again")
#                 return
#
#     password = input("Enter your password: ")
#     hashed_password = hash_password(password)
#
#     with open("user.txt", "a") as file:
#         file.write(f"{username}:{hashed_password}\n")
#     print("Registred!")
#
# def login():
#     username = input("Enter a username: ")
#     password = input("Enter your password: ")
#     hashed_password = hash_password(password)
#
#     with open("user.txt", "r") as file:
#         for line in file:
#             stored_username, stored_password = line.strip().split(":")
#             if stored_username == username and stored_password == hashed_password:
#                 print("Login successful!")
#                 return username
#             print("Login failed, try again")
#             return None
#
# def add_task(username):
#     task = input("Enter a task: ")
#     task_id = str(len(get_tasks(username)) + 1)
#
#     with open(f"tasks/{username}_tasks.txt","a") as file:
#         file.write(f"{task_id}, {task}, Pending\n")
#     print("Task added!")
#
# def get_tasks(username):
#     try:
#         with open(f"tasks/{username}_tasks.txt","r") as file:
#             tasks = [line.strip().split(",") for line in file]
#         return tasks
#     except []
#
# def view_tasks(username):
#     tasks = get_tasks(username)
#     if not tasks:
#         print("No tasks found!")
#     else:
#         print("\nYour Tasks:")
#         for task_id, desc, status in tasks:
#             print(f"{task_id}. {desc} [{status}]")
#
#
# def complete_task(username):
#     view_tasks(username)
#     task_id = input("Enter a task ID: ")
#
#     tasks = get_tasks(username)
#     updated_tasks = []
#     found_task = False
#
#     for task in tasks:
#         if task[0] == task_id:
#             task[2] =   "completed"
#             found = True
#         updated_tasks.append(task)
#
#     if found:
#         with open(f"tasks/{username}_tasks.txt","w") as file:
#             for task in updated_tasks:
#                 file.write(",".join(task)) + "\n")
#             print("Task marked as completed!")
#     else:
#         print( "Task ID not found")
#
# def delete_task(username):
#     view_tasks(username)
#     task_id = input("Enter a task ID: ")
#
#     tasks = get_tasks(username)
#     updated_tasks = [task for task in task if task[0] != task_id]
#
#     if len(updated_tasks) < len(tasks):
#         with open(f"tasks/{username}_tasks.txt","w") as file:
#             for task in updated_tasks:
#                 file.write(",".join(task)) + "\n")
#         print("Task deleted!")
#     else:
#         print( "Task ID not found")
#
# def task_manager_menu(username):
#     while True:
#         print("\n--- Task Manager Menu ---")
#         print("1. Add Task")
#         print("2. View Tasks")
#         print("3. Mark Task as Completed")
#         print("4. Delete Task")
#         print("5. Logout")
#
#         choice = input("Enter choice (1-5): ")
#
#         if choice == "1":
#             add_task(username)
#         elif choice == "2":
#             view_tasks(username)
#         elif choice == "3":
#             complete_task(username)
#         elif choice == "4":
#             delete_task(username)
#         elif choice == "5":
#             print("Logging out...")
#             break
#         else:
#             print("Invalid choice!")
#
# def main():
#     print("Welcome to Task Manager!")
#
#     while True:
#         print("\n1. Register")
#         print("2. Login")
#         print("3. Exit")
#
#         choice = input("Enter choice (1-3): ")
#
#         if choice == "1":
#             register()
#         elif choice == "2":
#             username = login()
#             if username:
#                 task_manager_menu(username)
#         elif choice == "3":
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice!")
# if __name__ == "__main__":
#     main()
#
#
#
#
#
import hashlib
import os


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register():
    username = input("Enter a username: ")

    # Check if username already exists
    try:
        with open("user.txt", "r") as file:
            for line in file:
                old_user, _ = line.strip().split(":")
                if old_user == username:
                    print("Username already exists! Try again")
                    return
    except FileNotFoundError:
        pass  # First user registration

    password = input("Enter your password: ")
    hashed_password = hash_password(password)

    with open("user.txt", "a") as file:
        file.write(f"{username}:{hashed_password}\n")
    print("Registered!")


def login():
    username = input("Enter a username: ")
    password = input("Enter your password: ")
    hashed_password = hash_password(password)

    try:
        with open("user.txt", "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(":")
                if stored_username == username and stored_password == hashed_password:
                    print("Login successful!")
                    return username
    except FileNotFoundError:
        pass

    print("Login failed, try again")
    return None


def get_tasks(username):
    try:
        with open(f"tasks/{username}_tasks.txt", "r") as file:
            tasks = [line.strip().split(",") for line in file if line.strip()]
        return tasks
    except FileNotFoundError:
        return []


def add_task(username):
    if not os.path.exists("tasks"):
        os.makedirs("tasks")

    task = input("Enter a task: ")
    tasks = get_tasks(username)
    task_id = str(len(tasks) + 1)

    with open(f"tasks/{username}_tasks.txt", "a") as file:
        file.write(f"{task_id},{task},Pending\n")
    print("Task added!")


def view_tasks(username):
    tasks = get_tasks(username)
    if not tasks:
        print("No tasks found!")
    else:
        print("\nYour Tasks:")
        for task in tasks:
            print(f"{task[0]}. {task[1]} [{task[2]}]")


def complete_task(username):
    view_tasks(username)
    task_id = input("Enter a task ID: ")

    tasks = get_tasks(username)
    updated_tasks = []
    found = False

    for task in tasks:
        if task[0].strip() == task_id.strip():
            task[2] = "Completed"
            found = True
        updated_tasks.append(task)

    if found:
        with open(f"tasks/{username}_tasks.txt", "w") as file:
            for task in updated_tasks:
                file.write(",".join(task) + "\n")
        print("Task marked as completed!")
    else:
        print("Task ID not found")


def delete_task(username):
    view_tasks(username)
    task_id = input("Enter a task ID: ")

    tasks = get_tasks(username)
    updated_tasks = [task for task in tasks if task[0].strip() != task_id.strip()]

    if len(updated_tasks) < len(tasks):
        with open(f"tasks/{username}_tasks.txt", "w") as file:
            for task in updated_tasks:
                file.write(",".join(task) + "\n")
        print("Task deleted!")
    else:
        print("Task ID not found")


def task_manager_menu(username):
    while True:
        print("\n--- Task Manager Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Logout")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            add_task(username)
        elif choice == "2":
            view_tasks(username)
        elif choice == "3":
            complete_task(username)
        elif choice == "4":
            delete_task(username)
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice!")


def main():
    print("Welcome to Task Manager!")

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            register()
        elif choice == "2":
            username = login()
            if username:
                task_manager_menu(username)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()