import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
import json
from datetime import datetime

class TodoListApp(tk.Tk):
    def __init__(self):
        super(). __init__()

        self.title("Todo List App")
        self.geometry("500x400")
        style = Style(theme="cyborg")
        style.configure("Custom.TEntry", foreground="grey")

        # Create input field for adding tasks
        self.task_input = ttk.Entry(self, font=("TkDefaultFont", 16), width=30, style="Custom.TEntry")
        self.task_input.pack(pady=10)

        # Create entry field for adding deadline date
        self.deadline_input = ttk.Entry(self, font=("TkDefaultFont", 16), width=15, style="Custom.TEntry")
        self.deadline_input.pack(pady=5)

        # Set placeholders for input fields
        self.task_input.insert(0, "Enter your todo here...")
        self.deadline_input.insert(0, "YYYY-MM-DD")

        # Bind events to clear placeholders when input fields are clicked
        self.task_input.bind("<FocusIn>", self.clear_placeholder)
        self.deadline_input.bind("<FocusIn>", self.clear_placeholder)

        # Bind events to restore placeholders when input fields lose focus
        self.task_input.bind("<FocusOut>", self.restore_placeholder)
        self.deadline_input.bind("<FocusOut>", self.restore_placeholder)

        # Create button for adding tasks
        ttk.Button(self, text="Add", command=self.add_task).pack(pady=5)

        # Create listbox to display added tasks
        self.task_list = tk.Listbox(self, font=("TkDefaultFont", 16), height=10, selectmode=tk.NONE)
        self.task_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create buttons for marking tasks as done or deleting them
        ttk.Button(self, text="Done", style="success.TButton", command=self.mark_done).pack(side=tk.LEFT, padx=10, pady=10)
        ttk.Button(self, text="Delete", style="danger.TButton", command=self.delete_task).pack(side=tk.RIGHT, padx=10, pady=10)

        # Create button for displaying task statistics
        ttk.Button(self, text="View Status", style="info.TButton", command=self.view_stats).pack(side=tk.BOTTOM, pady=10)

        self.load_tasks()

    def view_stats(self):
        done_count = 0
        total_count = self.task_list.size()
        for i in range(total_count):
            if self.task_list.itemcget(i, "fg") == "green":
                done_count += 1
        messagebox.showinfo("Task Statistics", f"Total tasks: {total_count}\nCompleted tasks: {done_count}")

    def add_task(self):
        task = self.task_input.get()
        deadline = self.deadline_input.get()

        if task != "Enter your todo here..." and deadline != "YYYY-MM-DD":
            self.task_list.insert(tk.END, f"{task} (Deadline: {deadline})")
            self.task_list.itemconfig(tk.END, fg="orange")
            self.task_input.delete(0, tk.END)
            self.deadline_input.delete(0, tk.END)
            self.save_tasks()

    def mark_done(self):
        task_index = self.task_list.curselection()
        if task_index:
            self.task_list.itemconfig(task_index, fg="green")
            self.save_tasks()

    def delete_task(self):
        task_index = self.task_list.curselection()
        if task_index:
            self.task_list.delete(task_index)
            self.save_tasks()

    def clear_placeholder(self, event):
        if self.task_input.get() == "Enter your todo here...":
            self.task_input.delete(0, tk.END)
            self.task_input.configure(style="TEntry")

        if self.deadline_input.get() == "YYYY-MM-DD":
            self.deadline_input.delete(0, tk.END)
            self.deadline_input.configure(style="TEntry")

    def restore_placeholder(self, event):
        if self.task_input.get() == "":
            self.task_input.insert(0, "Enter your todo here...")
            self.task_input.configure(style="Custom.TEntry")

        if self.deadline_input.get() == "":
            self.deadline_input.insert(0, "YYYY-MM-DD")
            self.deadline_input.configure(style="Custom.TEntry")

    def load_tasks(self):
        try:
            with open(r"C:\Users\Admin\Downloads\Task_1\list_of_tasks.json", "r") as f:
                data = json.load(f)
                for task_entry in data:
                    task_description = task_entry.get("task", "")
                    task_color = task_entry.get("color", "white")
                    self.task_list.insert(tk.END, f"{task_description} (Deadline: {task_entry.get('deadline', 'No deadline')})")
                    self.task_list.itemconfig(tk.END, fg=task_color)
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            print("Error: The JSON file is empty or contains invalid data.")
            pass

    def save_tasks(self):
        data = []
        for i in range(self.task_list.size()):
            text_with_deadline = self.task_list.get(i)
            text, _, deadline = text_with_deadline.partition(" (Deadline: ")
            color = self.task_list.itemcget(i, "fg")
            data.append({"task": text, "color": color, "deadline": deadline.rstrip(")")})
        with open(r"C:\Users\Admin\Downloads\Task_1\list_of_tasks.json", "w") as f:
            json.dump(data, f)

if __name__ == '__main__':
    app = TodoListApp()
    app.mainloop()


