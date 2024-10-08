import customtkinter

from src.data.shareables import ShareHereby
from src.allocate.designations.DIFD import DIFD


class FrameDIFD():

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
        self.buttonCBInnerFolder.pack(padx=(0, 0), 
                                      pady=(10, 0))
        
        self.buttonCBRename.pack(padx=(18, 0), 
                                 pady=(10, 0))
        
        self.buttonCBDuplicatedFilename.pack(padx=(43, 10), 
                                             pady=(10, 15))
        
        self.execButton.pack(side="bottom", fill="x", padx=0, pady=0)

    
    def buildTopLevel(self):
        self.top = customtkinter.CTkToplevel(self.masterForUsage)
        self.top.grab_set()
        
        self.top.title("DIFD - Preparações")
        self.top.geometry("+%d+%d" % (self.masterForUsage.winfo_screenwidth() // 2 - 100, self.masterForUsage.winfo_screenheight() // 2 - 50))
        self.top.resizable(False, False)
        # self.top.pack_propagate(False)

        
    def buildCheckBoxInnerFolder(self):
        self.buttonCBInnerFolder = customtkinter.CTkCheckBox(self.top, 
                                                        text='Pastas Internas', 
                                                        variable=self.validatorToInnerFolder)
        
    def buildCheckBoxRename(self):
        self.buttonCBRename = customtkinter.CTkCheckBox(self.top, 
                                                        text='Retirar Código DIFD', 
                                                        variable=self.validatorToRemovePreffixDIF)
        
    def buildCheckBoxDuplicatedFilename(self):
        self.buttonCBDuplicatedFilename = customtkinter.CTkCheckBox(self.top, 
                                                        text='Renomear Duplicidade', 
                                                        variable=self.validatorDuplicatedFilename)
        
    def buildExecutionButton(self):
        self.validations = {
            "InnerFolder":self.validatorToInnerFolder,
            "RemovePreffix":self.validatorToRemovePreffixDIF,
            "DuplicatedFile":self.validatorDuplicatedFilename
        }
        
        self.execButton = customtkinter.CTkButton(self.top, 
                                                  text="Executar DIFD", 
                                                  command=self.execution)
    
    def destroyWindow(self):
        self.top.destroy()
        

    def execution(self):
        app = DIFD(self.validations)
        app.passthroughDIFD()
        