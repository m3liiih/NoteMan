print("Welcome to NoteMan, your personal Note Taking and Task Management Companion :)")

def get_category():
    while True:
        category = input("Select a category: | \"N\" for Notes | \"T\" for Tasks | \"X\" - Exit |\n-- ").upper()
        if category in ["N", "T"]:
            return category
        elif category == "X":
            break
        else:
            print("\nInvalid selection. Please select a valid category.")

def note_taking():
    while True:
        option = input("\n| Note Taking | \"new\" for New Note | \"del\" to Delete Note | \"X\" - back | \n-- ").upper()
        if option == "NEW":
            print("NEW NOTE FUNCTION UNDER CONSTRUCTION")
        elif option == "DEL":
            print("DELETE NOTE FUNCTION UNDER CONSTRUCTION")
        elif option == "X":
            break
        else:
            print("\nInvalid selection. Please select a valid option.")


def main():
    category = get_category()

    if category == "N":
        note_taking()
    elif category == "T":
        print("TASK FUNCTION UNDER CONSTRUCTION")
main()