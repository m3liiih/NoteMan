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
            break
        else:
            print("\nInvalid selection. Please select a valid option.")

    # TBD How to implement task management? Making it different from notes...
    # use of datetime module (maybe for notes as well)
    # Different file format? No os text editor or different approach.
    # Deadlines, priorities, marking tasks complete etc.

    # Later to be considered:
    # Calendar like look for tasks?
    # UI implementation using tkinter?
    # Extra features (classified)
    # - m3liiih



# txt editor implementation for windows
def new_note():
    while True:
        note_name = input("\n| New Note | Enter note name: | \"X\" - cancel |\n-- ")
        # Remove .txt if user includes it in filename (worst case " fi le na me .txt ")
        note_name = note_name.strip().removesuffix(".txt").strip()
        filename = f"{note_name}.txt"
        filepath = os.path.join(note_dir, filename)

        if note_name.upper() == "X":
            break
        elif os.path.exists(filepath):
            print(f"\n Note '{note_name}' already exists. Opening note...")
        else:
            with open(filepath, "w") as file:
                file.write(f"| NoteMan | {note_name} | Ctrl+S to Save | Ctrl+W to Close |\n\n")
            print(f"\nNote '{note_name}' created successfully.")
        os.startfile(filepath)


def new_task():
    while True:
        task_name = input("\n| New Task | Enter task name: | \"X\" - cancel\n-- ")
        task_description = input("Enter task description (optional):\n-- ")
        task_name = task_name.strip().removesuffix(".txt").strip()
        filename = f"{task_name}.json"
        filepath = os.path.join(task_dir, filename)

        if task_name.upper() == "X":
            break
        elif os.path.exists(filepath):
            print(f"\nTask '{task_name}' already exists.")
        else:
            task_data = {
                "name": task_name,
                "description": task_description.strip(),
                "created_at": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                "completed": False,
                "due_date": None,
                "priority": None
            }
            with open(filepath, "w") as task:
                json.dump(task_data, task, indent=4)
            print(f"\nTask '{task_name}' created successfully.")


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
    print("Task listing is under construction.")


def delete_notes():
    while True:
        note_name = input("\n| Delete Note | Enter the name of the note to delete: | \"X\" - cancel |\n-- ")
        note_name = note_name.strip().removesuffix(".txt").strip()
        filename = f"{note_name}.txt"
        filepath = os.path.join(note_dir, filename)

        if note_name.upper() == "X":
            break
        elif os.path.exists(filepath):
            os.remove(filepath)
            print(f"\nNote '{note_name}' deleted successfully.")
        else:
            print(f"\nNote '{note_name}' does not exist.")


def delete_tasks():
    print("Delete task functionality is under construction.")


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