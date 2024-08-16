import json
from pathlib import Path
import re
import shutil
from tkinter import messagebox

from src.GUI.frames.lowerFrame import LowerFrameForUsage
from src.data.exportData import Archives
from src.LOG.LOG_manager import LOGGER
from src.data.dirSpotCheck import SpotCheck
from src.data.shareables import ShareHereby


class CC:
    
    FATHERPATH = Path(r'G:\Recursos Humanos\01 - PESSOAL\02 - FOLHA\CONTRACHEQUE')
    
    @staticmethod
    def readJSON(config_path):
        with open(config_path, 'r', encoding='utf-8') as file:
            config_data = json.load(file)
        return config_data["CC"]

     
    @staticmethod  
    def __renamingOf(file):
        for key in ShareHereby.KEYS_TO_IDENTIFY.keys():
            file = file.replace(key,'')
        return file.strip()
    
    
    @staticmethod
    def takeMonthAndYear(file):
        pattern = re.compile(r"\b(\d{2})\.(\d{4})\b")
        match = re.search(pattern, file)
        
        month = match.group(1)
        year = match.group(2)
        
        return (month, year)
        
    @staticmethod
    def passthroughCC():
        RULES:dict = CC.readJSON(SpotCheck.ReacheableJSON()[1])
        
        listage = ShareHereby.ARCHIEVES_FILTERED["CC"].copy()
        for file in listage:
            month, year = CC.takeMonthAndYear(file.name)
            
            try:
                orderedMonth = RULES[month]
            except KeyError as e:
                Archives.NotRelocatedCC.append(((file, str(e) + ' Parâmetro de Alocação Inexistente')))
                LOGGER(f"NÃO MOVIDO POR: <Parâmetro de Alocação Inexistente> = {e} - {file}", "ERROR")                
                continue
            
            try:
                pathToGo = CC.FATHERPATH / year / orderedMonth
                Path(pathToGo).mkdir(exist_ok=True, parents=True)
                path, uniqueFilename = CC.__move(pathToGo, file)
                Archives.RelocatedCC.append((uniqueFilename,path))
                LOGGER(f'ALOCAÇÃO CC:\nDE:\n{file}\nPARA: \n{path}\n--------------------', 'INFO')
            
            except PermissionError:
                messagebox.showerror('Pasta Influenciada', f'Impossível manusear visto que existe uma pasta que está sendo influenciada.\n{pathToGo}')
                LOGGER(f'NÃO MOVIDO POR: <Pasta influenciada> - {file}', 'WARNING')
                Archives.NotRelocatedCC.append(((file, str(e) + ' - Pasta Influenciada')))
            
        LowerFrameForUsage.updateTextCount()
        
        
        
    @staticmethod
    def __move(pathTo:Path, filename:Path):
        fileRenamed = CC.__renamingOf(filename.name)
        uniqueFilename = CC._generate_unique_filename(pathTo, fileRenamed)
        
        shutil.move(filename, uniqueFilename)
        return [uniqueFilename, filename]
        
        
            
    @staticmethod
    def _generate_unique_filename(destination: Path, filename: str) -> Path:
        base_name, ext = filename.rsplit('.', 1)
        counter = 1
        
        while (destination / f"{base_name}.{ext}").exists():
            while (destination / f"{base_name}_{counter}.{ext}").exists():
                counter += 1
            return destination / f"{base_name}_{counter}.{ext}"
        
        return destination / f"{base_name}.{ext}"
            
            
    
            
    
    
    
    
    
    
    
    
    