import tkinter as tk
from tkinter import ttk
import time
from tkinter import messagebox
from tkinter import filedialog

def hello():
    print("hi")

def new_window():
    response = messagebox.askyesnocancel(title='Are you sure?', message='this is a new window')
    messagebox.showinfo(message='A message')
    return response

def for_tk():
    filename = filedialog.askopenfilename()



root = tk.Tk()
root.title('tkinter testing')

frame = ttk.Frame(root, padding=5)
btn_ok = ttk.Button(frame, text='OK', command=hello)
btn_cancel = ttk.Button(frame, text='Cancel', command=new_window)
btn_filebrowse = ttk.Button(frame, text='Open file', command=for_tk)
lbl_name = ttk.Label(frame, text="Username")

lbl_location = ttk.Label(frame)
lbl_location['text'] = "Location:"

ent_name = ttk.Entry(frame)
ent_location = ttk.Entry(frame)

combo_occupation = ttk.Combobox(frame)
combo_occupation['values'] = ['Policeman', 'Fireman']

btn_on_or_off = ttk.Checkbutton(frame, text='On or off')

# spinval = tk.StringVar()
# d = ttk.Spinbox(frame, from_=1.0, to=100.0, textvariable=spinval)
#
progress = ttk.Progressbar(frame, length=200, mode='determinate')

root.columnconfigure(0,weight=1)
root.rowconfigure(0, weight=1)

frame.columnconfigure(3, weight=1)
frame.rowconfigure(6, weight=1)





frame.grid(column=0, row=0, sticky='nswe')


lbl_name.grid(row=0, column=0, sticky='nw')
lbl_location.grid(row=1, column=0, sticky='nw')
btn_ok.grid(column=2, row=4,)
btn_cancel.grid(column=1, row=4)
btn_filebrowse.grid(column=0, row=4)
combo_occupation.grid(column=0, row=2, columnspan=2)
ent_name.grid(row=0, column=1, columnspan=2)
ent_location.grid(row=1, column=1, columnspan=2)
btn_on_or_off.grid(row=2, column=2)
# d.grid(row=0, column=4, columnspan=1)
progress.grid(row=3, column=0, columnspan=4)


root.mainloop()

