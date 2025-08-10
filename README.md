# NoteMan

NoteMan is a lightweight, easy-to-use **command-line** application designed to help you manage personal **notes** and **tasks** efficiently. It supports creating, listing, editing, and deleting plain text notes, as well as task management with priorities and due dates in JSON format.

---

## 🚀 Features

- **Note Taking**
    
    - Create, open, list, and delete plain text notes (`.txt` files).
    - Notes are stored in the `notes/` directory.
    - Open notes seamlessly in your default text editor (Windows only for now).
    
- **Task Management**
    
    - Create tasks with descriptions, due dates, and priority levels (`High`, `Medium`, `Low`).
    - Tasks are saved as JSON files in the `tasks/` directory.
    - List all tasks with detailed information, including remaining time until due date.
    - Mark tasks as complete or delete them.
    - Supports date and time validation for due dates.
    
- **Intuitive CLI Interface**  
    Simple menus guide you through note-taking and task management with easy commands.
    

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.x installed on your system
- Windows OS recommended for note-taking feature (`os.startfile`)

---

## 🎯 How to Use

On launch, select a category:

- **`N`** — Manage Notes
    
- **`T`** — Manage Tasks
    
- **`X`** — Exit the program

### Notes

- Create new notes with a name (saved as `.txt` files).
    
- List existing notes and open or delete them.
    
- Notes open in your default system editor.

### Tasks

- Create new tasks with description, due date (format: `DD-MM-YYYY`), and priority (`H`, `M`, `L`).
    
- View task details, including time left before due date.
    
- Mark tasks complete or delete them.

---

## 🔮 Future Enhancements

- Cross-platform support for opening notes (Linux/macOS).
- GUI interface with `tkinter` or similar with additional features.
- Listing options (due, priority etc.)
