import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, description, due_date=None, priority=None):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.description} (Due: {self.due_date}, Priority: {self.priority}, Status: {status})"

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List Application")

        self.tasks = []
        self.completed_tasks = []

        # Widgets
        self.task_label = tk.Label(master, text="Task Description:")
        self.task_entry = tk.Entry(master, width=40)
        self.due_date_label = tk.Label(master, text="Due Date (optional, format: YYYY-MM-DD):")
        self.due_date_entry = tk.Entry(master, width=20)
        self.priority_label = tk.Label(master, text="Priority (optional):")
        self.priority_entry = tk.Entry(master, width=20)
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white")
        self.display_button = tk.Button(master, text="Display Tasks", command=self.display_tasks, bg="#008CBA", fg="white")
        self.completed_button = tk.Button(master, text="Display Completed Tasks", command=self.display_completed_tasks, bg="#555555", fg="white")
        self.mark_completed_button = tk.Button(master, text="Mark as Completed", command=self.mark_completed, bg="#f44336", fg="white")
        self.update_button = tk.Button(master, text="Update Task", command=self.update_task, bg="#FFC107", fg="black")
        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task, bg="#d9534f", fg="white")

        # Listbox
        self.task_listbox = tk.Listbox(master, selectmode=tk.SINGLE, height=10)
        self.task_listbox.bind("<<ListboxSelect>>", self.load_selected_task)

        # Grid layout
        self.task_label.grid(row=0, column=0, pady=(10, 0), padx=(10, 0), sticky="w")
        self.task_entry.grid(row=0, column=1, pady=(10, 0), padx=(0, 10), columnspan=2)
        self.due_date_label.grid(row=1, column=0, pady=(5, 0), padx=(10, 0), sticky="w")
        self.due_date_entry.grid(row=1, column=1, pady=(5, 0), padx=(0, 10), columnspan=2)
        self.priority_label.grid(row=2, column=0, pady=(5, 0), padx=(10, 0), sticky="w")
        self.priority_entry.grid(row=2, column=1, pady=(5, 0), padx=(0, 10), columnspan=2)
        self.add_button.grid(row=3, column=0, pady=(10, 0), padx=(10, 0), sticky="w")
        self.display_button.grid(row=3, column=1, pady=(10, 0))
        self.completed_button.grid(row=3, column=2, pady=(10, 0), padx=(0, 10), sticky="e")
        self.mark_completed_button.grid(row=4, column=0, pady=(10, 0), padx=(10, 0), sticky="w")
        self.update_button.grid(row=4, column=1, pady=(10, 0))
        self.remove_button.grid(row=4, column=2, pady=(10, 0), padx=(0, 10), sticky="e")
        self.task_listbox.grid(row=5, column=0, columnspan=3, pady=(10, 0), padx=(10, 10))

    def add_task(self):
        description = self.task_entry.get()
        due_date = self.due_date_entry.get()
        priority = self.priority_entry.get()
        task = Task(description, due_date, priority)
        self.tasks.append(task)
        self.task_listbox.insert(tk.END, str(task))
        self.clear_entries()
        messagebox.showinfo("Task Added", "Task added successfully.")

    def display_tasks(self):
        if not self.tasks:
            messagebox.showinfo("Task List", "No tasks in the to-do list.")
        else:
            task_list = "\n".join([str(task) for task in self.tasks])
            messagebox.showinfo("Task List", f"Pending Tasks:\n{task_list}")

    def display_completed_tasks(self):
        if not self.completed_tasks:
            messagebox.showinfo("Completed Tasks", "No completed tasks.")
        else:
            completed_task_list = "\n".join([str(task) for task in self.completed_tasks])
            messagebox.showinfo("Completed Tasks", f"Completed Tasks:\n{completed_task_list}")

    def mark_completed(self):
        selected_task = self.get_selected_task()
        if selected_task:
            selected_task.completed = True
            self.completed_tasks.append(selected_task)
            self.tasks.remove(selected_task)
            self.task_listbox.delete(tk.ACTIVE)
            self.clear_entries()
            messagebox.showinfo("Task Completed", f"Task '{selected_task.description}' marked as completed.")
        else:
            messagebox.showwarning("No Task Selected", "Please select a task to mark as completed.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            description = self.task_entry.get()
            due_date = self.due_date_entry.get()
            priority = self.priority_entry.get()

            selected_task = self.tasks[selected_task_index]
            selected_task.description = description
            selected_task.due_date = due_date
            selected_task.priority = priority

            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(selected_task_index, str(selected_task))
            self.clear_entries()
            messagebox.showinfo("Task Updated", "Task updated successfully.")
        else:
            messagebox.showwarning("No Task Selected", "Please select a task to update.")

    def remove_task(self):
        selected_task = self.get_selected_task()
        if selected_task:
            self.tasks.remove(selected_task)
            self.task_listbox.delete(tk.ACTIVE)
            self.clear_entries()
            messagebox.showinfo("Task Removed", f"Task '{selected_task.description}' removed from the to-do list.")
        else:
            messagebox.showwarning("No Task Selected", "Please select a task to remove.")

    def get_selected_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            return self.tasks[int(selected_task_index[0])]
        return None

    def load_selected_task(self, event):
        selected_task = self.get_selected_task()
        if selected_task:
            self.clear_entries()
            self.task_entry.insert(tk.END, selected_task.description)
            self.due_date_entry.insert(tk.END, selected_task.due_date)
            self.priority_entry.insert(tk.END, selected_task.priority)

    def clear_entries(self):
        self.task_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
