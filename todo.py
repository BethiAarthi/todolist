import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = task_entry.get()
    if task and task != placeholder_text:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        task_entry.insert(0, placeholder_text)  # Reset placeholder text
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a selected task
def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to clear all tasks
def clear_tasks():
    task_listbox.delete(0, tk.END)

# Function to handle focus in event for the entry field
def on_entry_click(event):
    if task_entry.get() == placeholder_text:
        task_entry.delete(0, tk.END)
        task_entry.config(fg='black')

# Function to handle focus out event for the entry field
def on_focusout(event):
    if not task_entry.get():
        task_entry.insert(0, placeholder_text)
        task_entry.config(fg='grey')

# Create the main application window
root = tk.Tk()
root.title("Simple To-Do List")

# Placeholder text
placeholder_text = "Enter your task here..."

# Create the task entry field
task_entry = tk.Entry(root, width=50, fg='grey')
task_entry.insert(0, placeholder_text)
task_entry.bind('<FocusIn>', on_entry_click)
task_entry.bind('<FocusOut>', on_focusout)
task_entry.pack(pady=10)

# Create the add task button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Create the task listbox
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

# Create the delete task button
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Create the clear all tasks button
clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks)
clear_button.pack(pady=5)

# Run the application
root.mainloop()
