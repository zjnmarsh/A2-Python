import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog

def close_window():
    response = messagebox.askyesno(title='Are you sure', message='Do you want to close')
    if response:
        root.destroy()

def save_as():
    text = main_text.get('1.0', tk.END)
    filename = filedialog.asksaveasfilename()
    with open(filename, 'w') as textfile:
        textfile.write(text)

def open_file():
    main_text.delete('1.0', tk.END)
    filename = filedialog.askopenfilename()
    with open(filename, 'r') as file:
        text = file.readline()
        main_text.insert(tk.END, text)


root = tk.Tk()
root.title('Text Editor')

frame = ttk.Frame(root, padding=5)

main_text = scrolledtext.ScrolledText(frame)
contents = main_text.get('1.0', tk.END)

btn_close = ttk.Button(frame, text='Close', command=close_window)
btn_save = ttk.Button(frame, text='Save', command=save_as)
btn_open = ttk.Button(frame, text='Open', command=open_file)


# Resize column and row 0,0 for both frame and root when resizing
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


frame.grid(column=0, row=0, sticky='nsew')
main_text.grid(column=0, row=0, columnspan=5, sticky='nesw') # sticky textbox to all corners
btn_close.grid(column=4, row=1)
btn_save.grid(column=3, row=1)
btn_open.grid(column=2, row=1)




root.mainloop()
