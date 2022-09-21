'''__main__.py'''

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class App(tk.Tk):
    
    def __init__(self):
        self.resizable(0, 0)
        self.title('QR Encode/Decode')
        
    def create_header_frame(self):
        pass
    
    def create_body_frame(self):
        '''will contain a notebook with two tabs, encode and decode'''
        
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(padx=5, pady=5, expand=True)
    
    def create_footer_frame(self):
        pass
        

if __name__ == '__main__':
    app=App()
    app.mainloop()
