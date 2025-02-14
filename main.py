import tkinter as tk
from tkinter import ttk
from task1 import plot_graph
from task2 import show_task2_inputs

def show_task_inputs():
    for widget in frame.winfo_children():
        widget.destroy()
    
    task = task_var.get()
    if task == 'Task 1':
        ttk.Button(frame, text="Plot Graph", command=plot_graph).grid(row=0, column=0)
    else:
        show_task2_inputs(frame)

root = tk.Tk()
root.title("Select Task")

main_frame = ttk.Frame(root, padding=10)
main_frame.grid(row=0, column=0)

task_var = tk.StringVar(value='Task 1')
task_menu = ttk.Combobox(main_frame, textvariable=task_var, values=['Task 1', 'Task 2'])
task_menu.grid(row=0, column=0)

ttk.Button(main_frame, text="Next", command=show_task_inputs).grid(row=0, column=1)

frame = ttk.Frame(root, padding=10)
frame.grid(row=1, column=0)

root.mainloop()