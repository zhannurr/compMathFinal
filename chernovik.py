from tkinter import *


root = Tk()                                                     # Не помню

root['bg'] = '#baf6ff'                                          # Цвет заднего фона окна
root.geometry('900x600')                                        # Размер окна
root.title('Computational Mathematics - Final Project')         # Название приложения
# root.wm_attributes('-alpha', 0.9)                               # Прозрачность

root.resizable(False, False)                        # Не изменяемое окно

canvas = Canvas(root, width=300, height=300)                    # Канвас для рисования в нутри окна
canvas.pack()                                                   # Располагаем канвас

frame = Frame(root, bg='black')                                   # Фрейм, хз для чего
frame.pack()                         #

title = Label(frame, text="Text", bg="gray", font=40)
title.pack()

def btn_click():
    print(entry.get())
btn = Button(frame, text="Button", bg="yellow", command=btn_click)
btn.pack()

entry = Entry(root, bg="white")
entry.pack()



# frm = Frame(root, padding=100)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()