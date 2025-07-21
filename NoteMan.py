print("Welcome to NoteMan, your personal Note Taking and Task Management Companion :)")
def action_type():
    act_type = input("Select a category: | \"N\" for Notes | \"T\" for Tasks |\n-- ")
    if act_type.upper() == "N":
        return act_type
    elif act_type.upper() == "T":
        return act_type
    else:
        print("\nSelection error, please retry with a valid option.")
        return action_type()
act_category = action_type()
print("\n" + act_category)
