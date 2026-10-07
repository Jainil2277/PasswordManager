# 🔐 Desktop Password Manager & Generator
A secure and easy-to-use desktop application built in Python using **Tkinter** to generate strong, randomized passwords and store them safely in a local data file.
---

## ✨ Features
- **Password Generator:** Instantly creates highly secure passwords using a balanced mix of random letters, numbers, and symbols.
- **Local JSON Database:** Securely stores your login information (Website, Email/Username, and Password) directly on your machine.
- **Quick Search:** Look up saved credentials instantly by typing the website name.
- **User Validation:** Prevents accidental blank entries and alerts you via pop-up messages.
---

## 🛠️ Required Libraries
This project relies entirely on Python's **built-in library system**. You do **not** need to install any external dependencies or packages using `pip`. 
The following modules are utilized:
- **`tkinter`** — Handles the core Graphical User Interface (GUI) windows, labels, entries, and inputs.
- **`random`** (`choice`, `shuffle`, `randint`) — Powers the password generation algorithms.
- **`json`** — Reads, creates, updates, and structures the local data storage file (`data.json`).
---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.x installed on your computer. You can check your version by running:
```bash
python --version
```

### 2. Setup & Installation
Clone this repository to your local machine:
```bash
git clone https://github.com
cd your-repo-name
```

> ⚠️ **Important Note:** Make sure you have a image asset named `logo.png` in the exact root folder of the project, as the interface relies on it to load visually.

### 3. Run the Application
Execute the Python script using your terminal or favorite IDE (like PyCharm):
```bash
python main.py
```
---

## 🔒 Security & Privacy

- Your passwords are saved **locally** in a file named `data.json` generated in your project root.
- The `data.json` file is explicitly included in the `.gitignore` configuration, meaning your private passwords will **never** be tracked, uploaded, or exposed on GitHub.
