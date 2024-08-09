import customtkinter

class ScriptSelectionArea:
    def __init__(self, master) -> None:
        self.master_instance = master
        
        
    def run(self):
        ...
    
    
    def ungridAll(self):
        self.frame.grid_forget()
        
        
    def gridAll(self):
        self.frame.grid(row=3, column=0, columnspan=2, padx=(50, 0), pady=(50, 0))
        self.SBox.grid(row=0, column=0)

    
    def buildFrame(self):
        self.frame = customtkinter.CTkFrame(master=self.master_instance)
        
        
    def buildSelectionBox(self):
        self.SBox = customtkinter.CTkComboBox(master=self.frame, values=[])
        
        
    def buildButton(self):
        ...
    
