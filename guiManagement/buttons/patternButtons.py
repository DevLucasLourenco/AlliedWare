import customtkinter

class PATTERNBUTTON():
    
    def __init__(self, buttonName:str, function:function, master, gridRow:int, gridColumn:int) -> None:
        self.buttonName = buttonName
        self.master = master
        self.useFunction:function = function
        self.gridRow = gridRow
        self.gridColumn = gridColumn
        
        
    def run(self):
        self.buildButton()
        
        
    def buildButton(self):
        self.button = customtkinter.CTkButton(master=self.master, text=self.buttonName, 
                                              command=self.useFunction)
        self.button.grid(row=self.gridRow, column=self.gridColumn)
    