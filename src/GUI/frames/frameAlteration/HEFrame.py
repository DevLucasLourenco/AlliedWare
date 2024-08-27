from tkinter import messagebox
import customtkinter

from src.allocate.designations.HE import HE

class FrameHE:
    
    def __init__(self, master) -> None:
        self.masterForUsage = master
        
        self.run()
        
        
    def run(self):
        self.buildTopLevel()
        self.buildExecutionButton()
        
        self.PACK_ALL()
        
        
    def PACK_ALL(self):
        self.execButton.pack(side="bottom", fill="x", padx=0, pady=0)        
        
        
    def buildTopLevel(self):
        self.top = customtkinter.CTkToplevel(self.masterForUsage)
        self.top.grab_set()
        
        self.top.title("HE - Preparações")
        self.top.geometry("+%d+%d" % (self.masterForUsage.winfo_screenwidth() // 2 - 100, self.masterForUsage.winfo_screenheight() // 2 - 50))
        self.top.resizable(False, False)
        
        
    def buildExecutionButton(self):
        self.execButton = customtkinter.CTkButton(self.top, 
                                                  text="Executar HE", 
                                                  command=self._exec_func)

    def destroyWindow(self):
        self.top.destroy()
        
    def _exec_func(self):
        messagebox.showwarning('Atenção', 'Para esta aplicação, será necessário informar o diretório de atuação de distribuição.')
        HE.passthroughHE()