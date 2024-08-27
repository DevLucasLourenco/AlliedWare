import re
import json

from pathlib import Path
from tkinter import filedialog, messagebox

from src.GUI.frames.lowerFrame import LowerFrameForUsage
from src.data.dirSpotCheck import SpotCheck
from src.LOG.LOG_manager import LOGGER
from src.data.exportData import Archives
from src.data.shareables import ShareHereby


class HE:
    FATHERPATH = Path(r'G:\Recursos Humanos\01 - PESSOAL\14 - CARTÃO PONTO')
    
    
    @staticmethod
    def readJSON(config_path):
        with open(config_path, 'r', encoding='utf-8') as file:
            config_data = json.load(file)
        return config_data["HE"]
    

    @staticmethod
    def passthroughHE():
        dir = HE._ASK_DIR_TO_GO()
        
        RULES_TO_ALOCATION_SUBFOLDER = HE.readJSON(config_path=SpotCheck.ReacheableJSON()[1])
        
        listage = ShareHereby.ARCHIEVES_FILTERED["HE"].copy()
        
        for file in listage:
            removeFromList = False
            
            #...
        
        
        
        
            
            if removeFromList:
                ShareHereby.ARCHIEVES_FILTERED['HE'].remove(file) 
                
        LowerFrameForUsage.updateTextCount()
        ShareHereby.FRAMEHE.destroyWindow()
        ShareHereby.buttonsFromTopFrame[3].configure(state='disabled')

            
         
    @staticmethod
    def _ASK_DIR_TO_GO():
        dir = filedialog.askdirectory(title='Selecione o diretório de distribuição.', initialdir=HE.FATHERPATH)
        print("diretório de distribuição:",dir)
        messagebox.showinfo("Diretório de Distribuição", f"{dir}\n\nEste será o diretório de distribuição de todas as Solicitações de HE encontradas.")
        return dir
                
                
            
        
    