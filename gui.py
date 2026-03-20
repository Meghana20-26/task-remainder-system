print("RUNNING NEW GUI FILE")

import tkinter as tk
from task_manager import add_task, get_tasks

def create_gui():

    root = tk.Tk()
    root.title("Task Remainder system")
    root.geometry("400x400")

    tk.Label(root,text="Task Name").pack()
    task_entry = tk.Entry(root)
    task_entry.pack()

    tk.Label(root,text="Description").pack()
    desc_entry = tk.Entry(root)
    desc_entry.pack()

    tk.Label(root,text="Deadline(YYYY-MM-DD)").pack()
    deadline_entry = tk.Entry(root)
    deadline_entry.pack()

    tk.Label(root,text="Email").pack()
    email_entry = tk.Entry(root)
    email_entry.pack()

    def add_task_button():

        task = task_entry.get()
        desc = desc_entry.get()
        deadline = deadline_entry.get()
        email = email_entry.get()

        add_task(task, desc, deadline, email)

        print("Task added successfully")

    tk.Button(root,text="Add Task",command=add_task_button).pack()

    root.mainloop()    







