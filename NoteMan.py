import os
import json
import datetime
note_dir = "notes"
task_dir = "tasks"


# Main action loop to select category of action
def get_category():
    while True:
        category = input("Select a category: | \"N\" for Notes | \"T\" for Tasks | \"X\" - exit |\n-- ").upper()
        if category in ["N", "T"]:
            return category
        elif category == "X":
            exit()
        else:
            print("\nInvalid selection. Please select a valid category.")


def note_taking():
    while True:
        print("\n| Note Taking | \"new\" for New Note | \"ls\" to List Notes and Note Options | \"X\" - main menu |")
        option = input("-- ").upper()

        if option == "NEW":
            new_note()
        elif option == "LS":
            list_notes()
        elif option == "X":
            print()
            break
        else:
            print("\nInvalid selection. Please select a valid option.")


def task_management():
    while True:
        print("\n| Task Management | \"new\" for New Task | \"ls\" to List Tasks and Manage Tasks | \"X\" - back |")
        option = input("-- ").upper()

        if option == "NEW":
            new_task()
        elif option == "LS":
            list_tasks()
        elif option == "X":
            print()
            break
        else:
            print("\nInvalid selection. Please select a valid option.")

    # TBD How to implement task management? Making it different from notes... (done as json format)
    # use of datetime module (maybe for notes as well) (implemented for tasks) (due needs work)
    # Different file format? No os text editor or different approach. (done as jsons and auto read)
    # Deadlines, priorities, marking tasks complete etc. (due and priority implemented, marking not yet done)

    # Later to be considered:
    # Calendar like look for tasks?
    # UI implementation using tkinter?
    # Extra features (classified)
    # - m3liiih


# txt editor implementation for windows
def new_note():
    while True:
        note_name = input("\n| New Note | Enter note name: | \"X\" - cancel |\n-- ")
        if note_name.upper() == "X":
            break
        # Remove .txt if user includes it in filename (worst case " fi le na me .txt ")
        note_name = note_name.strip().removesuffix(".txt").strip()
        filename = f"{note_name}.txt"
        filepath = os.path.join(note_dir, filename)

        if os.path.exists(filepath):
            print(f"\n Note '{note_name}' already exists. Opening note...")
        else:
            with open(filepath, "w") as file:
                file.write(f"| NoteMan | {note_name} | Ctrl+S to Save | Ctrl+W to Close |\n\n")
            print(f"\nNote '{note_name}' created successfully.")
        os.startfile(filepath)


def new_task():
    while True:
        task_name = input("\n| New Task | Enter task name: | \"X\" - cancel |\n-- ")
        if task_name.upper() == "X":
            break
        task_description = input("Enter task description (optional):\n-- ")
        while True:
            task_due = input("Enter task due date (optional): | (format: DD-MM-YYYY): |\n-- ")
            if task_due:
                try:
                    due_check = datetime.datetime.strptime(task_due, "%d-%m-%Y")
                    if due_check < datetime.datetime.now():
                        print("Warning: Due date can not be in the past. Please enter a valid due date.\n")
                except ValueError:
                    print("Invalid date format. Please use DD-MM-YYYY.")
        task_priority = input("Enter task priority (optional): | (format: 'H' High, 'M' Medium, 'L' Low) |\n-- ")
        # Removing .json is actually overkill but still
        task_name = task_name.strip().removesuffix(".txt").removesuffix(".json").strip()
        filename = f"{task_name}.json"
        filepath = os.path.join(task_dir, filename)

        if os.path.exists(filepath):
            print(f"\nTask '{task_name}' already exists.")
        else:
            task_data = {
                "name": task_name,
                "description": task_description.strip(),
                "created_at": datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),
                "completed": False,
                "due_date": task_due.strip(),
                "priority": task_priority.strip().upper()
            }
            with open(filepath, "w") as task:
                json.dump(task_data, task, indent=4)
            print(f"\nTask '{task_name}' created successfully.")
        break


def list_notes():
    print("\n| List of Notes |")

    notes = [f for f in os.listdir(note_dir) if f.endswith('.txt')]
    if notes:
        for note in notes:
            # Removed extension to not confuse the user while performing actions with note names
            note = note.removesuffix(".txt")
            print(f"- {note}")
    else:
        print("No notes found.")

    while True:
        print("\n| Options | \"op\" to Open Note | \"del\" to Delete Note | \"X\" - back |")
        option = input("-- ").upper()

        if option == "OP":
            open_note()
        elif option == "DEL":
            delete_notes()
        elif option == "X":
            break
        else:
            print("\nInvalid selection. Please select a valid option.")


def open_note():
    while True:
        note_name = input("\n| Open Note | Enter the name of the note to open: | \"X\" - cancel\n-- ")
        note_name = note_name.strip().removesuffix(".txt").strip()
        filename = f"{note_name}.txt"
        filepath = os.path.join(note_dir, filename)

        if note_name.upper() == "X":
            break
        elif os.path.exists(filepath):
                os.startfile(filepath)
        else:
            print(f"\nNote '{note_name}' does not exist.")


def list_tasks():
    print("\n| List of Tasks |")

    tasks = [f for f in os.listdir(task_dir) if f.endswith('.json')]
    if tasks:
        for task in tasks:
            filepath = os.path.join(task_dir, task)
            try:
                with open(filepath, 'r') as file:
                    task_data = json.load(file)
                    print(f"- {task_data['name']}\n\tPriority: {task_data['priority']}\n\tDue: {task_data['due_date']}")
                    print(f"\tDescription: {task_data['description'] if task_data['description'] else "None"}")
            except (json.JSONDecodeError, KeyError):
                print(f"- {task} (Invalid or corrupted task file)")
    else:
        print("No tasks found.")

    while True:
        print("\n| Options | \"cc\" to Mark Task Complete | \"del\" to Delete Task | \"X\" - back |")
        option = input("-- ").upper()

        if option == "CC":
            print("\n| Marking Task Complete Under Construction |")
        elif option == "DEL":
            delete_tasks()
        elif option == "X":
            break
        else:
            print("\nInvalid selection. Please select a valid option.")


def delete_notes():
    while True:
        note_name = input("\n| Delete Note | Enter the name of the note to delete: | \"X\" - cancel |\n-- ")
        if note_name.upper() == "X":
            break
        note_name = note_name.strip().removesuffix(".txt").strip()
        filename = f"{note_name}.txt"
        filepath = os.path.join(note_dir, filename)

        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"\nNote '{note_name}' deleted successfully.")
        else:
            print(f"\nNote '{note_name}' does not exist. Try again.")


def delete_tasks():
    while True:
        task_name = input("\n| Delete Task | Enter the name of the task to delete: | \"X\" - cancel |\n-- ")
        if task_name.upper() == "X":
            break
        task_name = task_name.strip().removesuffix(".json").strip()
        filename = f"{task_name}.json"
        filepath = os.path.join(task_dir, filename)

        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"\nTask '{task_name}' deleted successfully.")
        else:
            print(f"\nTask '{task_name}' does not exist. Try again.")


def main():
    if not os.path.exists(note_dir):
        os.makedirs(note_dir)

    if not os.path.exists(task_dir):
        os.makedirs(task_dir)

    print("\nWelcome to NoteMan, your personal Note Taking and Task Management Companion :)")

    while True:
        category = get_category()

        if category == "N":
            note_taking()
        elif category == "T":
            task_management()
main()