import customtkinter
from pathlib import Path
from tkinter import filedialog
from guiManagement.config.shareables import ShareHereby
from guiManagement.frames.patternAbstractClass import AbstractGlobalObject


class ProgressBarDeploy:
    
    def __init__(self, lowerFrameObjectShared) -> None:
        self.frame = lowerFrameObjectShared
    
    
    def buildProgressBar(self):
        progressBar = customtkinter.CTkProgressBar(master=self.frame, width=500)
        progressBar.grid(row=2, column=0, pady=(20, 0))
    
    

class LowerFrameForUsage(AbstractGlobalObject):
    
    def __init__(self, object) -> None:
        self.__initialInstance()
        super().__init__(object)
        
    
    @staticmethod
    def __personalizedString(item):
        return f'{item[0]}: {item[1]}'
    
    
    def __initialInstance(self):
        self.ALL_ARCHIEVES = list()
        ShareHereby.ALL_ARCHIEVES_VALIDATED = list()
        
        self.countedInfosDict:dict = {
            'DIF':0,
            'HE':0,
            'CC':0,
            'CP':0,
            'Total':0,
        } # If something here has been changed, pay attention to change in "__treatKeys" underneath too.
        
        
        
    def run(self):
        self.buildFrame()
        self.buildAreaToBrowse()
        self.buildLabelToShowCountedInfos()
        progressBar = ProgressBarDeploy(self.frameForUsage).buildProgressBar()
        
    
    def buildFrame(self):
        self.frameForUsage = customtkinter.CTkFrame(master=self.master, corner_radius=20, width=570)
        self.frameForUsage.grid(row=1, column=1, sticky='nsew', padx=(0,0), pady=(20,0))
        self.frameForUsage.grid_propagate(False)
        
        
    def buildAreaToBrowse(self):
        frame = customtkinter.CTkFrame(master=self.frameForUsage, fg_color='transparent')
        frame.grid(row=0, column=0)
        
        self.directoryArea = customtkinter.CTkEntry(master=frame, width=490)
        self.updateTextFromDirectoryArea('Insira o diretório de inicialização')
        self.directoryArea.grid(row=0, column=0, padx=(10, 0), pady=(70, 0))
        
        button = customtkinter.CTkButton(master=frame, text='Browse',font=("Robolo", 13, "bold"), width=70, 
                                         command=self.__searchDir, border_spacing=5, border_width=2)
        button.grid(row=0, column=1, padx=(0, 0), pady=(70, 0))
    
    
    def buildLabelToShowCountedInfos(self):
        self.countInfos()
        self.labelShow = customtkinter.CTkLabel(master=self.frameForUsage, font=('Roboto', 11, 'bold'))
        self.updateTextCount()
        self.labelShow.grid(row=1, column=0)
    
    
    def updateTextCount(self):
        self.textToShow = " - ".join([LowerFrameForUsage.__personalizedString(item) for item in self.countedInfosDict.items()])
        self.labelShow.configure(text=self.textToShow)
    
    
    def updateTextFromDirectoryArea(self, text):
        self.directoryArea.configure(state='normal')
        self.directoryArea.configure(placeholder_text=text)
        self.directoryArea.configure(state='disabled')
    
    
    def countInfos(self, *dir):
        if dir:
            self.__initialInstance()
            self.ALL_ARCHIEVES = list(Path(dir[0]).glob('*.pdf'))
            
            for archieve in self.ALL_ARCHIEVES:
                for key, value in self.__treatKeys().items():
                    if key in archieve.name:
                        self.countedInfosDict[value] += 1
                        self.countedInfosDict['Total'] += 1
                        ShareHereby.ALL_ARCHIEVES_VALIDATED.append(archieve)

            
    def __treatKeys(self):
        newKeysTreat = {
            'DIF -':'DIF',
            'DIF-':'DIF',
            #----------
            'CC -':'CC',
            'CC-':'CC',
            #----------
            'CP -':'CP',
            'CP-':'CP',
            #----------
            'SOLICITAÇÃO DE HE -':'HE',
            'SOLICITAÇÃO DE HE-':'HE',
            'SOLICITACAO DE HE -':'HE',
            'SOLICITACAO DE HE-':'HE',
        }

        return newKeysTreat


    def __searchDir(self):
        dir = filedialog.askdirectory()
        if dir:
            self.updateExternalInfos(dir)
        
    
    def updateExternalInfos(self, dir):
        self.updateTextFromDirectoryArea(dir)
        self.countInfos(dir)
        self.updateTextCount()
        self.updateButtonsAndLabel()
        
        
    def updateButtonsAndLabel(self):
        for button in ShareHereby.buttonsFromTopFrame:
            button.configure(state='normal')
            button.configure(fg_color='#1f538d')
        
        ShareHereby.labelFromTopFrame.configure(text='Selecione uma tarefa para a realização')
        