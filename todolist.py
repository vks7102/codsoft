import tkinter as tk
from tkinter import messagebox
import json
import os

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = self.load_tasks()

        # Frame for task input
        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.task_frame, width=40)
        self.task_entry.pack(side=tk.LEFT)

        self.add_task_button = tk.Button(self.task_frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack(side=tk.LEFT)

        # Listbox for displaying tasks
        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Buttons for updating and deleting tasks
        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(self.root, text="Mark as Completed", command=self.mark_as_completed)
        self.complete_button.pack(pady=5)

        # Refresh the task list on startup
        self.refresh_task_list()

    def load_tasks(self):
        """Load tasks from JSON file."""
        if os.path.exists('todo.json'):
            with open('todo.json', 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        """Save tasks to JSON file."""
        with open('todo.json', 'w') as file:
            json.dump(self.tasks, file)

    def refresh_task_list(self):
        """Refresh the task list displayed in the listbox."""
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✔️" if task['completed'] else "❌"
            display_text = f"{status} {task['task']}"
            self.task_listbox.insert(tk.END, display_text)

    def add_task(self):
        """Add a new task."""
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append({"task": task_text, "completed": False})
            self.save_tasks()
            self.refresh_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task!")

    def update_task(self):
        """Update the selected task."""
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_text = self.task_entry.get()
            if task_text:
                self.tasks[selected_index[0]]['task'] = task_text
                self.save_tasks()
                self.refresh_task_list()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task!")
        else:
            messagebox.showwarning("Warning", "Select a task to update!")

    def delete_task(self):
        """Delete the selected task."""
        selected_index = self.task_listbox.curselection()
        if selected_index:
            del self.tasks[selected_index[0]]
            self.save_tasks()
            self.refresh_task_list()
        else:
            messagebox.showwarning("Warning", "Select a task to delete!")

    def mark_as_completed(self):
        """Mark the selected task as completed."""
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks[selected_index[0]]['completed'] = True
            self.save_tasks()
            self.refresh_task_list()
        else:
            messagebox.showwarning("Warning", "Select a task to mark as completed!")

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()
