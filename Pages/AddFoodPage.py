import tkinter as tk
from tkinter import ttk

from Database import Food

class AddFoodPage:
    
    def __init__(self, session, rootParent):
        self.database = session
        self.root = tk.Frame(rootParent.root)
        self.parent = rootParent
        self.input_widgets = []
        self.init_add_food()
        
    def submit_form(self):
        new_food = Food()
        new_food.name = self.input_widgets[0].get()
        new_food.calories = int(self.input_widgets[1].get())/(int(self.input_widgets[5].get())/100)
        new_food.fat = int(self.input_widgets[2].get())/(int(self.input_widgets[5].get())/100)
        new_food.carbo = int(self.input_widgets[3].get())/(int(self.input_widgets[5].get())/100)
        new_food.protein = int(self.input_widgets[4].get())/(int(self.input_widgets[5].get())/100)
        self.database.add(new_food)
        self.database.commit()
        
    def init_add_food(self):
        input_types = [
            ("Name", "text"),
            ("Calories", "number"),
            ("Fat", "number"),
            ("Carbo", "number"),
            ("Protein","number"),
            ("Weight","number")
        ]
        for label, input_type in input_types:
            tk.Label(self.root, text=label).pack(pady=5)
            
            if input_type == "text":
                entry = tk.Entry(self.root)
                entry.pack(pady=5)
                self.input_widgets.append(entry)
            elif input_type == "number":
                # Create a number input field with validation
                entry = tk.Entry(self.root, validate="key", validatecommand=(self.parent.validate_number, "%P"))
                if(label == "Weight"):
                    entry.insert(0,100)
                else:
                    entry.insert(0,0)
                entry.pack(pady=5)
                self.input_widgets.append(entry)
            elif input_type == "checkbox":
                var = tk.BooleanVar()
                checkbox = tk.Checkbutton(self.root, text=label, variable=var)
                checkbox.pack(pady=5)
                self.input_widgets.append(var)

        # Submit button
        submit_button = tk.Button(self.root, text="Submit", command=self.submit_form)
        submit_button.pack(pady=20)
        
        button_to_back = tk.Button(self.root,text="Back", command=lambda : self.parent.showPage("MainPage"))
        button_to_back.pack()
        
    def show(self):
        self.root.pack()
        
    def hide(self):
        self.root.pack_forget()
