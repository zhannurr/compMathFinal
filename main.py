import tkinter as tk
from tkinter import ttk
from task1 import plot_graph
from task2 import show_task2_inputs
from task3 import show_task3_inputs
from task8 import task8

def cutie_style(widget):
    style = ttk.Style()
    style.configure("TFrame", background="#baf6ff")
    style.configure("TButton", font=("Arial", 15), padding=6)
    style.configure("TLabel", font=("Arial", 17), background="#f0f0f0")
    style.configure("TCombobox", font=("Arial", 20), padding=5)
    
    widget.configure(background="#baf6ff")

def show_task_inputs(*args):
    for widget in frame.winfo_children():
        widget.destroy()
    
    task = task_var.get()
    if task == 'Task 1':
        ttk.Button(frame, text="Plot Graph", command=plot_graph).pack(pady=10)
    elif task == 'Task 2':
        show_task2_inputs(frame)
    elif task == 'Task 3':
        show_task3_inputs(frame)
    elif task == 'Task 8':
        task8()

root = tk.Tk()
root.title("Select Task")
root.anchor("center")
root.geometry("900x600")          # TODO Consider making app smaller
# root.justify = "center"
# root.eval('tk::PlaceWindow . center')
cutie_style(root)

main_frame = ttk.Frame(root, padding=10)
main_frame.place(relx=0.5, rely=0.15, anchor="center")  # Поднял выбор выше

task_var = tk.StringVar(value='Task 1')
task_var.trace_add("write", show_task_inputs)  

task_menu = ttk.Combobox(main_frame, textvariable=task_var, values=['Task 1', 'Task 2', 'Task 3', 'Task 8'], font=("Arial", 20), width=25)
task_menu.pack(pady=10)

frame = ttk.Frame(root, padding=10)
frame.place(relx=0.5, rely=0.6, anchor="center") 

show_task_inputs() 

root.mainloop()