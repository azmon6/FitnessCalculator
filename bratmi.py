import sys
sys.path.insert(1, 'Pages')

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DATE, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from Database import Food, History, HistoryEntry, Base
from MainPage import MainPage
from AddHistoryPage import AddHistoryPage
from AddFoodPage import AddFoodPage

import tkinter as tk
from tkinter import ttk

class App:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("The Fitness Pal")
        self.root.geometry("800x600")
        self.root.resizable(False,False) 
        self.validate_number = self.root.register(self.validate_number_input)
        self.activePage = None

        engine = create_engine('sqlite:///my_database.db')

        # Create the users table (if it doesn't already exist)
        Base.metadata.create_all(engine)

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        self.database = Session()
    
    def showPage(self, page):
        if(self.activePage != None):
            self.activePage.hide()
        
        if page == "AddFood":
            self.activePage = AddFoodPage(session=self.database,rootParent=self)
        elif page == "AddHistory":
            self.activePage = AddHistoryPage(session=self.database,rootParent=self)
        elif page == "MainPage":
            self.activePage = MainPage(session=self.database,parentRoot=self)
        
        self.activePage.show()
        
    def start(self):
        self.activePage = MainPage(session=self.database,parentRoot=self)
        self.activePage.show()
        self.root.mainloop()
        
    def validate_number_input(self,input_value):
        if input_value == "" or input_value.replace(".", "", 1).isdigit():  # Allow empty string and numbers with one decimal
            return True
        return False  

tracker = App()
tracker.start()