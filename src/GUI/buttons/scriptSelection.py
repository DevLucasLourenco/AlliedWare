import customtkinter

from tkinter import messagebox

from src.LOG.LOG_manager import LOGGER
from src.data.dirSpotCheck import SpotCheck
from src.GUI.topLevels.tooltip.ToolTipForComboBox import ToolTip
from scripts.SortingFiles import SortGlobalFiles
from src.data.shareables import ShareHereby


class ScriptSelectionArea:
    
    lookupTable = {
        SortGlobalFiles.__name__ : SortGlobalFiles,
        
    }
    
    def __init__(self, master) -> None:
        self.master_instance = master
        self.run()
        
        
    def run(self):
        self.buildFrame()
        self.buildSelectionBox()
        self.buildButton()
        
    
    def ungridAll(self):
        self.frame.grid_forget()
        self.SBox.grid_forget()
        
        
    def gridAll(self):
        self.frame.grid(row=3, column=0, columnspan=2, padx=(50, 0), pady=(50, 0))
        self.SBox.grid(row=0, column=0)
        self.GoButton.grid(row=0, column=1)

    
    def buildFrame(self):
        self.frame = customtkinter.CTkFrame(master=self.master_instance)
        
        
    def buildSelectionBox(self):
        self.SBox = NonEditableCTkComboBox(master=self.frame, values=['', SortGlobalFiles.__name__, ], width=260, command=self.sendToShareables)
        self.SBox.set("")
        
        self.tooltip = ToolTip(self.SBox, ShareHereby.ToolTipDescription)
        
        
    def buildButton(self):
        self.GoButton = customtkinter.CTkButton(master=self.frame, text="Executar", width=70, border_spacing=5, border_width=2, command=self.__execute)
    

    def sendToShareables(self, *args):
        if self.SBox.get() != "":
            ShareHereby.ToolTipDescription = ScriptSelectionArea.lookupTable[args[0]].DESCRIPTION
            self.tooltip.update_text(ShareHereby.ToolTipDescription)
        elif self.SBox.get() == "":
            self.tooltip.update_text("")
        
        
    def __execute(self):
        
        
        if self.SBox.get() != "":
            res = messagebox.askquestion("Confirmação", "Tem certeza que deseja executar {}?".format(self.SBox.get()))
            if res=='yes':
                
                validator, path = SpotCheck.ReacheableJSON()
                if not validator:
                    messagebox.showwarning('Atenção - Diretório JSON inalcançável.', f'Dir: {path}\n\nIndique o diretório do JSON para apontamento de alocação.' )
                    SpotCheck.dir_appointment()
                    messagebox.showinfo("JSON", 'Diretório de JSON informado.')
                    
                if validator:
                    ScriptSelectionArea.lookupTable[self.SBox.get()].run()
                    messagebox.showinfo('Finalizado', f'{self.SBox.get()} foi executado.')
                    LOGGER(f'{self.SBox.get()} executado', "INFO")
            else:
                messagebox.showinfo('Recusado', f'{self.SBox.get()} não foi executado.')


class NonEditableCTkComboBox(customtkinter.CTkComboBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<Key>", lambda e: "break")