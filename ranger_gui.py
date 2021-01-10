import os
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk, THEMES
from ttkwidgets import ScaleEntry
from ttkwidgets.autocomplete import AutocompleteCombobox
from PIL import Image

current_path = "/home/niksart/"

class Example(ThemedTk):
    def __init__(self, theme):
        ThemedTk.__init__(self, fonts=True, themebg=True)
        self.set_theme(theme)
        # Create widgets
        
        #ttk.Style().configure("TButton", padding=(0, 5, 0, 5),
        #    font='serif 10')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        
        paths_to_show = self.get_paths_to_show(current_path)

        l1 = self.get_folder_listbox(paths_to_show[0])
        l1.grid(row=0, column=0, sticky='nsew')
        l2 = self.get_folder_listbox(paths_to_show[1])
        l2.grid(row=0, column=1, sticky='nsew')
        l3 = self.get_folder_listbox(paths_to_show[1])
        l3.grid(row=0, column=2, sticky='nsew')


    def get_paths_to_show(self, current_path):
        from pathlib import Path
        path = Path(current_path)

        path1 = str(path.parent) + "/"
        path2 = current_path
        #path3 = ...
        return [path1, path2]


    def get_folder_listbox(self, p):
        l = self.get_list_folders_files(p)
        print(l)
        lb = tk.Listbox(self)
        for i,(f, type_f) in enumerate(l):
            lb.insert(i,f)
            lb.itemconfig(i, foreground=("blue" if type_f == "D" else "black"))
        
        return lb
    

    def get_list_folders_files(self, p, show_hidden=False):
        listdirfiles = os.listdir(path=p)
        listdir = []
        listfiles = []
        for f in listdirfiles:
            if os.path.isdir(p+f):
                listdir.append(f)
            if os.path.isfile(p+f):
                listfiles.append(f)
        listdir.sort(key=lambda v: v.upper())
        listfiles.sort(key=lambda v: v.upper())

        listdir = list(zip(listdir, len(listdir) * "D"))
        listfiles = list(zip(listfiles, len(listfiles) * "F"))

        total_list = listdir + listfiles
        if show_hidden:
            return total_list
        else:
            return [t for t in total_list if t[0][0] != "."]


if __name__ == '__main__':
    example = Example("breeze")
    example.mainloop()
