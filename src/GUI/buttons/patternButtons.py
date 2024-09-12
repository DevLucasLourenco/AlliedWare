import customtkinter

class PATTERN_BUTTON():
    
    def __init__(self, buttonName:str, function:object, master:object, gridRow:int, gridColumn:int, padTuple:tuple) -> None:
        self.buttonName = buttonName
        self.master = master
        self.useFunction = function
        self.gridRow = gridRow
        self.gridColumn = gridColumn
        self.padTuple = padTuple
        
        self.run()

    
    def get(self):
        return self.button
    
        
    def run(self):
        self.buildButton()
        
        
    def buildButton(self):
        self.button = customtkinter.CTkButton(master=self.master, text=self.buttonName, 
                                              command=self.useFunction, width=220, height=40, 
                                              font=("Robolo", 16, "bold"), state='disabled', 
                                              fg_color='#616A6B', border_spacing=5, border_width=2)
        
    
    def grid_it(self):
        self.button.grid(row=self.gridRow, column=self.gridColumn, padx=self.padTuple[0], pady=self.padTuple[1])
        
        
    def ungrid_it(self):
        self.button.grid_forget()
  
    
class PATTERN_BUTTON_WITH_COLUMNSPAN():
    
    def __init__(self, buttonName:str, function:object, master:object, gridRow:int, gridColumn:int, gridColumnspan:int, padTuple:tuple, sticky:str) -> None:
        self.buttonName = buttonName
        self.master = master
        self.useFunction = function
        self.gridRow = gridRow
        self.gridColumn = gridColumn
        self.gridColumnspan = gridColumnspan
        self.padTuple = padTuple
        self.sticky = sticky
        
        self.run()
    
    
    def get(self):
        return self.button
    
        
    def run(self):
        self.buildButton()
        
        
    def buildButton(self):
        self.button = customtkinter.CTkButton(master=self.master, text=self.buttonName, 
                                              command=self.useFunction, width=220, height=40, 
                                              font=("Robolo", 16, "bold"), state='disabled', 
                                              fg_color='#616A6B', border_spacing=5, border_width=2)
        
        self.button.grid(row=self.gridRow, column=self.gridColumn, columnspan=self.gridColumnspan, padx=self.padTuple[0], pady=self.padTuple[1], sticky=self.sticky)
            
    