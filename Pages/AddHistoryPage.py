import tkinter as tk
from datetime import datetime

from Database import Food , History , HistoryEntry
from Utility.AutoCompleteComboBox import AutocompleteCombobox

class AddHistoryPage:
    
    def __init__(self, session, rootParent):
        self.database = session
        self.root = tk.Frame(rootParent.root)
        self.parent = rootParent
        self.combobox = None
        self.foods = {}
        
        self.init_add_history()
    
    def show(self):
        self.root.pack()
    
    def remove_food(self, food_to_remove):
        for x in self.foods[food_to_remove] :
            x.pack_forget()
            
        self.foods.pop(food_to_remove)
        
    def add_food(self):
        
        if(self.combobox.get() in self.foods):
            return
        
        if(self.combobox.get() not in self.combobox._hits): 
            return
        
        label = tk.Label(self.addFrame, text=self.combobox.selection_get())
        label.pack()
        
        entry = tk.Entry(self.addFrame, validate="key", validatecommand=(self.parent.validate_number, "%P"))
        entry.pack()
        
        selection = self.combobox.selection_get()
        button_to_remove = tk.Button(self.addFrame,text="Remove", command= lambda : self.remove_food(selection))
        button_to_remove.pack()
        
        self.foods[self.combobox.selection_get()] = [label,entry,button_to_remove]
    
    def add_history_entry(self):
        #TODO RENAME
        history_date = (self.database.query(History)
                                     .filter(History.day == self.add_history_dict["Date"].get())
                                     .filter(History.month == self.add_history_dict["Month"].get())
                                     .filter(History.year == self.add_history_dict["Year"].get())
                                     .all())
        if history_date == []:
            history_date = History()
            history_date.day = self.add_history_dict["Date"].get()
            history_date.month = self.add_history_dict["Month"].get()
            history_date.year = self.add_history_dict["Year"].get()
            self.database.add(history_date)
            self.database.commit()
        else:
            history_date = history_date[0]
        
        
        for x in self.foods:
            new_history_entry = HistoryEntry()
            new_history_entry.historyId = history_date.id
            
            food_id = self.database.query(Food).filter(Food.name == x).all()
            new_history_entry.foodId = food_id[0].id
            new_history_entry.amount = self.foods[x][1].get()
            self.database.add(new_history_entry)
            self.database.commit()
        
        self.parent.showPage("MainPage")
            
    
    def init_add_history(self):
        self.add_history_dict = {}
        
        tk.Label(self.root,text="Date").pack()
        entry_date = tk.Entry(self.root, validate="key", validatecommand=(self.parent.validate_number, "%P"))
        entry_date.insert(0,datetime.now().day)
        entry_date.pack(pady=5)
        self.add_history_dict["Date"] = entry_date
        
        tk.Label(self.root,text="Month").pack()
        entry_month = tk.Entry(self.root, validate="key", validatecommand=(self.parent.validate_number, "%P"))
        entry_month.insert(0,datetime.now().month)
        entry_month.pack(pady=5)
        self.add_history_dict["Month"] = entry_month
        
        tk.Label(self.root,text="Year").pack()
        entry_year = tk.Entry(self.root, validate="key", validatecommand=(self.parent.validate_number, "%P"))
        entry_year.insert(0,datetime.now().year)
        entry_year.pack(pady=5)
        self.add_history_dict["Year"] = entry_year
        
        self.addFrame = tk.Frame(self.root)
        
        dropbox = tk.Frame(self.addFrame)
        
        #TODO Rename
        self.combobox = AutocompleteCombobox(dropbox)
        all_users = self.database.query(Food.name).all()
        all_users_strings = [str(email[0]) for email in all_users]
        self.combobox.set_completion_list(all_users_strings)
        self.combobox.insert(0,"")
        self.combobox.pack(padx=10, pady=10,side=tk.LEFT)
        
        button_to_add_food = tk.Button(dropbox,text="Add", command= lambda : self.add_food())
        button_to_add_food.pack(side=tk.LEFT)
        dropbox.pack()
        
        self.addFrame.pack()
        
        button_to_add_history_entry = tk.Button(self.root,text="Add Entry", command=lambda : self.add_history_entry())
        button_to_add_history_entry.pack()
        
        button_to_back = tk.Button(self.root,text="Back", command=lambda : self.parent.showPage("MainPage"))
        button_to_back.pack(side=tk.TOP,pady=10)
        
        
    def hide(self):
        self.root.pack_forget()
