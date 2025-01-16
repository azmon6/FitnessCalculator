import tkinter as tk
from tkinter import ttk

from Database import Food

class AutocompleteCombobox(ttk.Combobox):
    def set_completion_list(self, completion_list):
        self._hits = completion_list
        self._hits_lower = [x.lower() for x in completion_list]
        self['values'] = self._hits
        self.bind('<KeyRelease>', self.handle_keyrelease)

    def handle_keyrelease(self, event):
        # Filter the list based on the user input
        typed = self.get().lower()
        if typed == '':
            hits = self._hits
        else:
            hits = [item for item in self._hits if typed in item.lower()]
        
        # Update the Combobox dropdown list
        self['values'] = hits

class AddHistoryPage:
    
    def __init__(self, session, rootParent):
        self.database = session
        self.root = tk.Frame(rootParent.root)
        self.parent = rootParent
        self.init_add_history()
    
    def show(self):
        self.root.pack()
    
    
    def init_add_history(self):
        self.add_history_dict = {}
        
        tk.Label(self.root,text="Date").pack()
        entry_date = tk.Entry(self.root, validate="key", validatecommand=(self.parent.validate_number, "%P"))
        entry_date.pack(pady=5)
        self.add_history_dict["Date"] = entry_date
        
        tk.Label(self.root,text="Month").pack()
        entry_month = tk.Entry(self.root, validate="key", validatecommand=(self.parent.validate_number, "%P"))
        entry_month.pack(pady=5)
        self.add_history_dict["Month"] = entry_month
        
        tk.Label(self.root,text="Year").pack()
        entry_year = tk.Entry(self.root, validate="key", validatecommand=(self.parent.validate_number, "%P"))
        entry_year.pack(pady=5)
        self.add_history_dict["Year"] = entry_year
        
        addFrame = tk.Frame(self.root)
        
        combobox = AutocompleteCombobox(addFrame)
        all_users = self.database.query(Food.name).all()
        all_users_strings = [str(email[0]) for email in all_users]
        combobox.set_completion_list(all_users_strings)
        combobox.insert(0,"")
        combobox.pack(padx=10, pady=10,side=tk.LEFT)
        
        button_to_add_food = tk.Button(addFrame,text="Add", command= lambda : self.parent.showPage("MainPage"))
        button_to_add_food.pack(side=tk.LEFT)
        
        addFrame.pack()
        
        button_to_back = tk.Button(self.root,text="Back", command=lambda : self.parent.showPage("MainPage"))
        button_to_back.pack(side=tk.TOP,pady=10)
        
    def hide(self):
        self.root.pack_forget()
