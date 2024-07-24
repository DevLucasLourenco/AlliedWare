import customtkinter

from pathlib import Path
from tkinter import filedialog

from data.shareables import ShareHereby
from GUI.frames.patternAbstractClass import AbstractGlobalObject

from src.filter.filter import Filter



class ProgressBarDeploy:
    
    def __init__(self, lowerFrameObjectShared) -> None:
        self.frame = lowerFrameObjectShared
    
    
    def buildProgressBar(self):
        progressBar = customtkinter.CTkProgressBar(master=self.frame, width=500)
        progressBar.grid(row=3, column=0, pady=(20, 0))
    
    

class LowerFrameForUsage(AbstractGlobalObject):
    
    def __init__(self, object) -> None:
        self.__initialInstance()
        super().__init__(object)
        
    
    @staticmethod
    def __personalizedString(item):
        return f'|{item[0]}: {item[1]}|'
    
    
    def __initialInstance(self):        
        self.ALL_ARCHIEVES = list()
        ShareHereby.ALL_ARCHIEVES_VALIDATED = list()
        
        for key in ShareHereby.countedSection:
            ShareHereby.countedSection[key] = 0
        
        
    def run(self):
        self.buildFrame()
        self.buildLabelToInstruciate()
        self.buildAreaToBrowse()
        self.buildLabelToShowCountedInfos()
        
    
    def buildFrame(self):
        self.frameForUsage = customtkinter.CTkFrame(master=self.master, corner_radius=20, width=570)
        self.frameForUsage.grid(row=1, column=1, sticky='nsew', padx=(0,0), pady=(20,0))
        self.frameForUsage.grid_propagate(False)
        
        
    def buildAreaToBrowse(self):
        frame = customtkinter.CTkFrame(master=self.frameForUsage, fg_color='transparent')
        frame.grid(row=1, column=0)
        
        self.directoryArea = customtkinter.CTkEntry(master=frame, width=490)
        self.updateTextFromDirectoryArea('Insira o diretório de orientação')
        self.directoryArea.grid(row=0, column=0, padx=(10, 0), pady=(50, 0))
        
        button = customtkinter.CTkButton(master=frame, text='Browse',font=("Robolo", 13, "bold"), width=70, 
                                         command=self.__searchDir, border_spacing=5, border_width=2)
        button.grid(row=0, column=1, padx=(0, 0), pady=(50, 0))
    
    
    def buildLabelToShowCountedInfos(self):
        self.countInfos()
        self.labelShow = customtkinter.CTkLabel(master=self.frameForUsage, font=('Roboto', 11, 'bold'))
        self.updateTextCount()
        self.labelShow.grid(row=2, column=0)
        
        
    def buildLabelToInstruciate(self):
        self.labelToInstruciate = customtkinter.CTkLabel(master=self.frameForUsage, text='Defina um Diretório de Orientação', 
                                       font=("Robolo", 16, "bold"), corner_radius=20, fg_color='#154360')
        self.labelToInstruciate.grid(row=0, column=0, columnspan=2, pady=(15,0))
    
    
    def countInfos(self, *dir):
        if dir:
            self.__initialInstance()
            self.ALL_ARCHIEVES = list(Path(dir[0]).glob('*.pdf'))
            
            for archieve in self.ALL_ARCHIEVES:
                for key, value in ShareHereby.KEYS_TO_IDENTIFY.items():
                    if key in archieve.name:
                        ShareHereby.countedSection[value] += 1
                        ShareHereby.countedSection['Total'] += 1
                        ShareHereby.ALL_ARCHIEVES_VALIDATED.append(archieve)


    def __searchDir(self):
        dir = filedialog.askdirectory()
        if dir:
            self.aglomerateUpdates(dir)
        

    def aglomerateUpdates(self, dir):
        self.countInfos(dir) # dps mudar pra quantidade q foi filtrada e adc uma maneira de contar totais (mt simples)
        self.updateTextFromDirectoryArea(dir)
        self.updateTextCount()
        self.updateButtonsAndLabel()
        
        ShareHereby.generateDynamicKeys(self)
        Filter.filtering(self)
        
        progressBar = ProgressBarDeploy(self.frameForUsage).buildProgressBar()
   
        
    def updateTextCount(self):
        self.textToShow = " - ".join([LowerFrameForUsage.__personalizedString(item) for item in ShareHereby.countedSection.items()])
        self.labelShow.configure(text=self.textToShow)
    
    
    def updateTextFromDirectoryArea(self, text):
        self.directoryArea.configure(state='normal')
        self.directoryArea.configure(placeholder_text=text)
        self.directoryArea.configure(state='disabled')
    
    
    def updateButtonsAndLabel(self):
        # on TopFrame
        for button in ShareHereby.buttonsFromTopFrame:
            button.configure(state='normal')
            button.configure(fg_color='#1f538d')
        
        ShareHereby.labelFromTopFrame.configure(text='Selecione uma Tarefa para a Realização', fg_color='#154360')
        
        self.labelToInstruciate.destroy()
        

        
        