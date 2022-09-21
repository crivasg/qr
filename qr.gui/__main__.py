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
        
        sticky = ( tk.N, tk.S, tk.E, tk.W )
        paddings = {'padx':5, 'pady':5}
        
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(**paddings, expand=True)
    
    def create_footer_frame(self):
        
        self.footer = ttk.Frame(self)
        sticky = ( tk.N, tk.S, tk.E, tk.W )
        paddings = {'padx':5, 'pady':5}

        # configure the grid
        self.footer.columnconfigure(0, weight=4,uniform='column')
        self.footer.columnconfigure(1, weight=1,uniform='column')
        self.footer.columnconfigure(2, weight=4,uniform='column')
        

        self.discard_button = ttk.Button(self.footer,
                                         text="Discard",
                                         command=lambda: self.destroy(),)
        self.discard_button.grid(column=1, row=0, sticky=sticky, **paddings)
        
        # attach the footer frame
        self.footer.pack(**paddings)
        
        

if __name__ == '__main__':
    app=App()
    app.mainloop()
