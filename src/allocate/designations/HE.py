import re
import json
import shutil

from pathlib import Path
from tkinter import filedialog, messagebox

from src.GUI.frames.lowerFrame import LowerFrameForUsage
from src.LOG.LOG_manager import LOGGER
from src.data.exportData import Archives
from src.data.dirSpotCheck import SpotCheck
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
        if dir != "":
            RULES_TO_ALOCATE_SUBFOLDER = HE.readJSON(config_path=SpotCheck.ReacheableJSON()[1])
            
            listage = ShareHereby.ARCHIVES_FILTERED["HE"].copy()
            
            for file in listage:
                removeFromList = False
                
                for key, dirToGo in RULES_TO_ALOCATE_SUBFOLDER.items():
                    # print(file, key, sep=' | ')
                    try:
                        if key in file.name:
                            newPath = Path(dir) / dirToGo
                            shutil.move(file, newPath)
                            print(file, newPath, sep=' | ')
                            Archives.RelocatedHE.append((file, newPath))
                            LOGGER(f'ALOCAÇÃO HE:\nDE:\n{file}\nPARA: \n{newPath}\n--------------------', 'INFO')
                            removeFromList = True

                        else:
                            Archives.NotRelocatedHE.append((file, 'Parâmetro de Alocação Inexistente'))
                            LOGGER(f'NÃO MOVIDO POR: <Parâmetro de Alocação Inexistente> - {file}',"WARNING")
                    
                    except Exception as e:
                            Archives.NotRelocatedHE.append((file, f'Erro | {e}'))
                            LOGGER(f'NÃO MOVIDO POR: <{e}> - {file}',"WARNING")
                            
                if removeFromList:
                    ShareHereby.ARCHIVES_FILTERED['HE'].remove(file) 
                    
            LowerFrameForUsage.updateTextCount()
            ShareHereby.FRAMEHE.destroyWindow()
            ShareHereby.buttonsFromTopFrame[3].configure(state='disabled')

                
         
    @staticmethod
    def _ASK_DIR_TO_GO():
        dir = filedialog.askdirectory(title='Selecione o diretório de distribuição.', initialdir=HE.FATHERPATH)
        print("diretório de distribuição:",dir)
        messagebox.showinfo("Diretório de Distribuição", f"{dir}\n\nEste será o diretório de distribuição de todas as Solicitações de HE encontradas.")
        return dir
                
                
            
        
    