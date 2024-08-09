import customtkinter

from src.data.shareables import ShareHereby

from src.GUI.frames.patternAbstractClass import AbstractGlobalObject
from src.GUI.buttons.scriptSelection import ScriptSelectionArea
from src.GUI.buttons.patternButtons import (PATTERN_BUTTON, 
                                        PATTERN_BUTTON_WITH_COLUMNSPAN)


from src.allocate.allocate import Allocate
from src.filter.filter import Filter
from src.filter.byOptions import By



class TopFrameForUsage(AbstractGlobalObject):
    
    def __init__(self, object) -> None:
        super().__init__(object)
    
    
    def get(self) -> customtkinter.CTkFrame:
        return self.frameForUsage
        
        
    def run(self):
        self.buildFrame()
        
        
    def buildFrame(self):
        self.frameForUsage = customtkinter.CTkFrame(master=self.master, corner_radius=20, width=570, height=450)
        self.frameForUsage.grid(row=1, column=1, sticky='nsew', padx=(0,0), pady=(20,0))
    
    

class MainInterfaceTopFrame:
    
    def __init__(self, frameForUsage) -> None:
        self.frameForUsageFromInstance = frameForUsage
        
        self.run()
    
        
    def run(self):
        self.buildLabel()
        self.buildButtons()
    
    
    def buildButtons(self):
        self.buttonDIF = PATTERN_BUTTON(buttonName="DOC. INF. FUNCIONÁRIOS", master=self.frameForUsageFromInstance, gridRow=1, gridColumn=0, 
                                  function=lambda:Allocate(By.DIF, self.buttonDIF), padTuple=((50, 0), (75, 0))) #lambda:Allocate(By.DFI)
        
        self.buttonCC = PATTERN_BUTTON(buttonName="CONTRACHEQUE", master=self.frameForUsageFromInstance, gridRow=1, gridColumn=1, 
                                  function=lambda:Allocate(By.CC, self.buttonCC), padTuple=((35, 0), (75, 0)))
        
        self.buttonCP = PATTERN_BUTTON(buttonName="CARTÃO DE PONTO", master=self.frameForUsageFromInstance, gridRow=2, gridColumn=0, 
                                  function=lambda:Allocate(By.CP, self.buttonCP), padTuple=((50, 0), (25, 0)))

        self.buttonHE = PATTERN_BUTTON(buttonName="SOLICITAÇÃO DE HE", master=self.frameForUsageFromInstance, gridRow=2, gridColumn=1, 
                                  function=lambda:Allocate(By.HE, self.buttonHE), padTuple=((35, 0), (25, 0)))

        # self.buttonAll = PATTERN_BUTTON_WITH_COLUMNSPAN(buttonName="REALIZAR TODOS", master=self.frameForUsageFromInstance, gridRow=3, gridColumn=0, gridColumnspan=2,
        #                                function=print, padTuple=((50, 0), (50, 0)), sticky='ew')
       
        self.buttonSelectScript = ScriptSelectionArea(master=self.frameForUsageFromInstance)
        self.buttonSelectScript.gridAll()
        
        ShareHereby.buttonsFromTopFrame = [self.buttonDIF.get(), self.buttonCC.get(), self.buttonCP.get(), self.buttonHE.get()]
        # ver oq é esse get e implementar ShareHereby.buttonsFromTopFrame = [self.buttonDIF.get(), self.buttonCC.get(), self.buttonCP.get(), self.buttonHE.get(), self.buttonSelectScript.get()] 
        
        
    def buildLabel(self):
        self.label = customtkinter.CTkLabel(master=self.frameForUsageFromInstance, text='', font=("Robolo", 20, "bold"), corner_radius=20)
        
        ShareHereby.labelFromTopFrame = self.label
        
        
    def GRID_ALL(self):
        self.frameForUsageFromInstance.grid_propagate(False)
        self.label.grid(row=0, column=0, columnspan=2, padx=(50, 0), pady=(45, 0), sticky='ew')
        
        self.buttonDIF.grid_it()
        self.buttonCC.grid_it()
        self.buttonCP.grid_it()
        self.buttonHE.grid_it()
        
        # self.buttonSelectScript.gridAll()
        
        
    def UNGRID_ALL(self):
        # self.frameForUsageFromInstance.grid_forget()
        self.label.grid_forget()
        
        self.buttonDIF.ungrid_it()
        self.buttonCC.ungrid_it()
        self.buttonCP.ungrid_it()
        self.buttonHE.ungrid_it()
        
        # self.buttonSelectScript.ungridAll()