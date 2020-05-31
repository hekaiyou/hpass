import json
from tkinter import *


class HPassGui:
    def __init__(self, init_window_obj, primary, hello_password_data_dir):
        self.init_window_obj = init_window_obj
        self.primary = primary
        self.hello_password_data_dir = hello_password_data_dir
        with open(hello_password_data_dir, 'r', encoding='utf-8') as f:
            password_data_json = json.load(f)
        self.password_data_json = password_data_json

    def set_init_window(self):
        self.init_window_obj.title("Hello Password")
        frame_1 = Frame(self.init_window_obj)
        frame_1.pack(side=LEFT, fill=BOTH)
        frame_2 = Frame(self.init_window_obj)
        frame_2.pack(side=RIGHT, fill=BOTH)
        scroll_bar = Scrollbar(frame_1)
        listbox_1 = Listbox(frame_1, yscrollcommand=scroll_bar.set)
        listbox_1.pack()
        scroll_bar.config(command=listbox_1.yview)
        label_1 = Label(frame_2, text='Summary: '.rjust(16))
        entry_1 = Entry(frame_2)
        label_1.grid(row=0, column=0)
        entry_1.grid(row=0, column=1)
        label_2 = Label(frame_2, text='Website: '.rjust(16))
        entry_2 = Entry(frame_2)
        label_2.grid(row=1, column=0)
        entry_2.grid(row=1, column=1)
        label_3 = Label(frame_2, text='Username: '.rjust(16))
        entry_3 = Entry(frame_2)
        label_3.grid(row=2, column=0)
        entry_3.grid(row=2, column=1)
        label_4 = Label(frame_2, text='Phone: '.rjust(16))
        entry_4 = Entry(frame_2)
        label_4.grid(row=3, column=0)
        entry_4.grid(row=3, column=1)
        label_5 = Label(frame_2, text='E-mail: '.rjust(16))
        entry_5 = Entry(frame_2)
        label_5.grid(row=4, column=0)
        entry_5.grid(row=4, column=1)
        label_6 = Label(frame_2, text='Password: '.rjust(16))
        entry_6 = Entry(frame_2)
        label_6.grid(row=5, column=0)
        entry_6.grid(row=5, column=1)


def gui_start(primary, hello_password_data_dir):
    init_window = Tk()
    h_pass_gui = HPassGui(init_window, primary, hello_password_data_dir)
    h_pass_gui.set_init_window()
    init_window.mainloop()
