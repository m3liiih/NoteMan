print("Welcome to NoteMan, your personal Note Taking and Task Management Companion :)")

def get_category():
    while True:
        category = input("Select a category: | \"N\" for Notes | \"T\" for Tasks |\n-- ").upper()
        if category in ["N", "T"]:
            return category
        else:
            print("\nInvalid selection. Please select a valid category.")

def main():
    category = get_category()

    if category == "N":
        print("NOTE FUNCTION UNDER CONSTRUCTION")
    elif category == "T":
        print("TASK FUNCTION UNDER CONSTRUCTION")
main()