from src.allocate.designations.DIF import DIF

import customtkinter

class FrameDIF():

    def __init__(self, master):
        self.masterForUsage = master
        
        self.validatorToInnerFolder = customtkinter.BooleanVar(value=True)
        self.validatorToRemovePreffixDIF = customtkinter.BooleanVar(value=True)
        self.validatorDuplicatedFilename = customtkinter.BooleanVar(value=True)
        
        self.run()

    
    def run(self):
        self.buildTopLevel()
        self.buildCheckBoxInnerFolder()
        self.buildCheckBoxRename()
        self.buildCheckBoxDuplicatedFilename()
        self.buildExecutionButton()
        
        self.PACK_ALL()
        
        
    def PACK_ALL(self):
        self.buttonCBInnerFolder.pack(padx=(10, 0), pady=(30, 0))
        # self.buttonCBRename.pack(padx=(10, 0), pady=(10, 0))
        # self.buttonCBDuplicatedFilename.pack(padx=(10, 0), pady=(10, 0))
        self.execButton.pack(side="bottom", fill="x", padx=0, pady=0)

    
    def buildTopLevel(self):
        self.top = customtkinter.CTkToplevel(self.masterForUsage)
        self.top.grab_set()
        
        self.top.title("DIF - Preparações")
        self.top.geometry("+%d+%d" % (self.masterForUsage.winfo_screenwidth() // 2 - 100, self.masterForUsage.winfo_screenheight() // 2 - 50))
        self.top.resizable(False, False)
        # self.top.pack_propagate(False)

        
    def buildCheckBoxInnerFolder(self):
        self.buttonCBInnerFolder = customtkinter.CTkCheckBox(self.top, 
                                                        text='Pastas Internas', 
                                                        variable=self.validatorToInnerFolder)
        
    def buildCheckBoxRename(self):
        self.buttonCBRename = customtkinter.CTkCheckBox(self.top, 
                                                        text='Retirar Código DIF', 
                                                        variable=self.validatorToRemovePreffixDIF)
        
    def buildCheckBoxDuplicatedFilename(self):
        self.buttonCBDuplicatedFilename = customtkinter.CTkCheckBox(self.top, 
                                                        text='Renomear Duplicidade\nTERMIANARLOGICA', 
                                                        variable=self.validatorDuplicatedFilename)
        
    def buildExecutionButton(self):
        self.execButton = customtkinter.CTkButton(self.top, 
                                                  text="Executar DIF", 
                                                  command=lambda:DIF(self.validatorToInnerFolder).passthrough())
    
    def destroyWindow(self):
        self.top.destroy()
        
    