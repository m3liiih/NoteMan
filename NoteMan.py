import os
note_dir = "notes"


# Main action loop to select category of action
def get_category():
    while True:
        category = input("Select a category: | \"N\" for Notes | \"T\" for Tasks | \"X\" - exit |\n-- ").upper()
        if category in ["N", "T"]:
            return category
        elif category == "X":
            break
        else:
            print("\nInvalid selection. Please select a valid category.")


def note_taking():
    while True:
        print("\n| Note Taking | \"new\" for New Note | \"ls\" to List Notes | \"del\" to Delete Note | \"X\" - back |")
        option = input("-- ").upper()

        if option == "NEW":
            new_note()
        elif option == "LS":
            list_notes()
        elif option == "DEL":
            list_notes()
            delete_notes()
        elif option == "X":
            break
        else:
            print("\nInvalid selection. Please select a valid option.")


# txt editor implementation for windows
def new_note():
    note_name = input("\n| New Note | Enter note name:\n-- ")
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


def list_notes():
    print("\n| List of Notes |")
    notes = [f for f in os.listdir(note_dir) if f.endswith('.txt')]
    if notes:
        for note in notes:
            print(f"- {note}")
    else:
        print("No notes found.")


def delete_notes():
    note_name = input("\n| Delete Note | Enter the name of the note to delete:\n-- ")
    note_name = note_name.strip().removesuffix(".txt").strip()
    filename = f"{note_name}.txt"
    filepath = os.path.join(note_dir, filename)

    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"\nNote '{note_name}' deleted successfully.")
    else:
        print(f"\nNote '{note_name}' does not exist.")


def main():
    if not os.path.exists(note_dir):
        os.makedirs(note_dir)

    print("\nWelcome to NoteMan, your personal Note Taking and Task Management Companion :)")

    while True:
        category = get_category()

        if category == "N":
            note_taking()
        elif category == "T":
            print("TASK FUNCTION UNDER CONSTRUCTION")
main()