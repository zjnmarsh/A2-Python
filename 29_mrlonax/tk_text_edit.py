import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog


class TextEditor(ttk.Frame):
    """
    This class inherits from ttk.Frame. It behaves like a Frame, but also takes care of all the additional
    GUI stuff for the text editor window.
    """
    def __init__(self, parent, *args, **kwargs):
        """
        All the code for creating the various widgets goes here.
        """
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self['padding'] = 5
        self.main_window_title = "Mr Lomax's Text Editor"
        self.parent.title(self.main_window_title)

        # Creaxte the menu
        self.parent.option_add('*tearOff', False)
        self.menubar = tk.Menu(self.parent)
        self.parent['menu'] = self.menubar

        # Add individual menu options
        self.file_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(menu=self.file_menu, label='File')

        # Add commands to the menu
        self.file_menu.add_command(label="Open...", command=self.open_text)
        self.file_menu.add_command(label="Save As...", command=self.save_text)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quit", command=self.parent.destroy)

        # Create Widgets
        self.txt_main_text = scrolledtext.ScrolledText(self)
        self.txt_main_text.configure(font=("Ariel", 12))
        self.btn_save = ttk.Button(self, text='Save', command=self.save_text)
        self.btn_open = ttk.Button(self, text='Open', command=self.open_text)
        self.btn_quit = ttk.Button(self, text='Quit', command=parent.destroy)

        # Place
        self.txt_main_text.grid(row=0, column=0, columnspan=3, sticky='news')
        self.btn_save.grid(row=1, column=0, sticky='e')
        self.btn_open.grid(row=1, column=1)
        self.btn_quit.grid(row=1, column=2)

        # Configure column resizing
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def save_text(self):
        """
        Gets a file name and writes the current contents of the text box to that file.
        """
        filename = filedialog.asksaveasfilename()
        text = self.txt_main_text.get('1.0', tk.END)
        with open(filename, 'w') as text_file:
            text_file.write(text)

    def open_text(self):
        """
        Gets a file name, reads it to a string and then replaces the current contents of the
        text box with the new text.
        """
        filename = filedialog.askopenfilename()
        with open(filename, 'r') as text_file:
            text = text_file.read()
            self.txt_main_text.delete('1.0', tk.END)
            self.txt_main_text.insert(tk.END, text)
            self.parent.title(self.main_window_title + ' - ' + filename)

if __name__ == "__main__":
    root = tk.Tk()
    text_editor = TextEditor(root)
    text_editor.grid(column=0, row=0, sticky='nsew')
    window2 = tk.Toplevel(root)
    text_editor2 = TextEditor(window2)
    text_editor.grid(column=0, row=0, sticky='nsew')
    root.mainloop()
