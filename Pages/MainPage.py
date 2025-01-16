import tkinter as tk
from tkinter import ttk

from Database import Food

class MainPage:
    
    def __init__(self,session,parentRoot):
        self.database = session
        self.root = tk.Frame(parentRoot.root)
        button_to_add_food = tk.Button(self.root,text="Add Food", command=lambda : parentRoot.showPage("AddFood"))
        button_to_add_food.pack()

        button_to_exit = tk.Button(self.root,text="Exit", command=self.exit_command)
        button_to_exit.pack()

        self.print_foods(self.root)
        
        button_to_add_history = tk.Button(self.root,text="Add History", command=lambda : parentRoot.showPage("AddHistory"))
        button_to_add_history.pack()
        
        self.root.pack()
    
    def print_foods(self,frame_to_attach):
        table_page = tk.Frame(frame_to_attach)
        table_frame = tk.Frame(table_page,width=600, height=400)
        table_frame.pack_propagate(False)
        table_frame.pack(padx=20, pady=20)
        tree = ttk.Treeview(table_frame, columns=("Name", "Calories", "Fat","Carbs","Protein"), show="headings")
        tree.heading("Name", text="NAME")
        tree.heading("Calories", text="CALORIES")
        tree.heading("Fat", text="FAT")
        tree.heading("Carbs", text="CARBS")
        tree.heading("Protein", text="PROTEIN")
        tree.column("Name",width=150,stretch=tk.YES)
        tree.column("Calories",width=150,stretch=tk.YES)
        tree.column("Fat",width=50,stretch=tk.YES)
        tree.column("Carbs",width=50,stretch=tk.YES)
        tree.column("Protein",width=50,stretch=tk.YES)
        all_users = self.database.query(Food).all()
        for row in all_users:
            tree.insert("", tk.END, values=[row.name,row.calories,row.fat,row.carbo,row.protein])
        
        scrollbar_y = tk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
        scrollbar_y.pack(side="right", fill="y")
        tree.config(yscrollcommand=scrollbar_y.set)
        tree.pack(fill="both", expand=True)
        table_page.pack()
    
    def show(self):
        self.root.pack()
        
    def hide(self):
        self.root.pack_forget()
        
    def exit_command(self):
        self.database.close()
        exit(0)