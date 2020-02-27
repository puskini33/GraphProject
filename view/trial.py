from tkinter import *
from tkinter import ttk
from tkinter import filedialog

filename = ''

form = Tk()
form.geometry('1000x600')
form.title('Text Editor')
frame = ttk.Frame(form, padding="3 3 12 12")
frame.grid(column=0, row=0, sticky=(N, W, E, S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
textentry = Text(frame, width=95, height=35)
textentry.grid(column=0, row=0, columnspan=4, sticky=(N, W, E, S))
textentry.focus()


def file_new():
    global filename
    textentry.delete('1.0', 'end')
    filename = ''


def file_open():
    global filename
    filename = filedialog.askopenfile(mode='r+')
    if filename is not None:
        t = filename.read()
        textentry.delete('0.0', 'end')
        textentry.insert('0.0', t)
        textentry.focus()


def file_save():
    global filename
    if filename == '':
        filename = filedialog.asksaveasfile(mode='w')
    if filename is not None:
        data = textentry.get('1.0', 'end')
        filename.write(data)


def file_save_as():
    global filename
    filename = filedialog.asksaveasfile(mode='w')
    file_save()


btnNew = ttk.Button(frame, text='New', command=file_new)
btnNew.grid(column=0, row=1, sticky='S')
btnOpen = ttk.Button(frame, text='Open', command=file_open)
btnOpen.grid(column=1, row=1, sticky='S')
btnSave = ttk.Button(frame, text='Save', command=file_save)
btnSave.grid(column=2, row=1, sticky='S')
btnSaveAs = ttk.Button(frame, text='Save As', command=file_save_as)
btnSaveAs.grid(column=3, row=1, sticky='S')

form.mainloop()