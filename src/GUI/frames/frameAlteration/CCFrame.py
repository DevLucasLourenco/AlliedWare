import customtkinter

from src.allocate.designations.CC import CC


class FrameCC:
    
    def __init__(self, master):
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
        
        self.top.title("CC - Preparações")
        self.top.geometry("+%d+%d" % (self.masterForUsage.winfo_screenwidth() // 2 - 100, self.masterForUsage.winfo_screenheight() // 2 - 50))
        self.top.resizable(False, False)
    
    
    def buildExecutionButton(self):
        self.execButton = customtkinter.CTkButton(self.top, 
                                                  text="Executar CC", 
                                                  command=CC.passthroughCC)
        
    def destroyWindow(self):
        self.top.destroy()