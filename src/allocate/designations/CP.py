import os
import re
import json
import shutil
from pathlib import Path
from tkinter import messagebox
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


from src.GUI.frames.lowerFrame import LowerFrameForUsage
from src.LOG.LOG_manager import LOGGER
from src.data.exportData import Archives
from src.data.shareables import ShareHereby
from src.data.dirSpotCheck import SpotCheck



class CP:
    FATHERPATH:Path = Path(r'G:\Recursos Humanos\01 - PESSOAL\14 - CARTÃO PONTO')
    
    
    
        
    @staticmethod
    def readJSON(config_path):
        with open(config_path, 'r', encoding='utf-8') as file:
            config_data = json.load(file)
        return config_data["CP"]
    
    
    @staticmethod  
    def renamingOf(file):
        for key in ShareHereby.KEYS_TO_IDENTIFY.keys():
            file = file.replace(key,'')
        return file.strip()
    
    
    @staticmethod
    def identifyPeriod(file):
        pattern = re.compile(r"\b(\d{2})\.(\d{4})\b")
        match = re.search(pattern, file)
        
        month = match.group(1)
        year = match.group(2)
        
        return (month, year)
            
            
    @staticmethod
    def passthroughCP():
        RULES:dict = CP.readJSON(config_path=SpotCheck.ReacheableJSON()[1])
        
        listage = ShareHereby.ARCHIEVES_FILTERED["CP"].copy()
        
        for file in listage:
            removeFromList = False
            
            try:
                month, year = CP.identifyPeriod(file.name)
            except Exception as e:
                Archives.NotRelocatedCP.append(((file, str(e) + ' Datas Informadas Incoerentes')))
                LOGGER(f"NÃO MOVIDO POR: <Datas Informadas Incoerentes> {e} - {file}", "ERROR")  
                continue
            
            try:
                periodToFind = RULES[month]
            except KeyError as e:
                Archives.NotRelocatedCP.append(((file, str(e) + ' Parâmetro de Alocação Inexistente')))
                LOGGER(f"NÃO MOVIDO POR: <Parâmetro de Alocação Inexistente> = {e} - {file}", "ERROR")                
                continue
            
            try:
                subfolder = CP.reachingPath(periodToFind, year)
                pathToReachIn = CP.FATHERPATH / year / subfolder
                Path(pathToReachIn).mkdir(exist_ok=True, parents=True)
                shutil.move(file, pathToReachIn / CP.renamingOf(file.name))
                
                Archives.RelocatedCP.append((file, pathToReachIn))
                LOGGER(f'ALOCAÇÃO CP:\nDE:\n{file}\nPARA: \n{pathToReachIn}\n--------------------', 'INFO')

            except Exception as e:
                Archives.NotRelocatedCP.append(((file, str(e))))
                LOGGER(f"NÃO MOVIDO POR: {e} - {file}", "ERROR")  
                
            if removeFromList:
                ShareHereby.ARCHIEVES_FILTERED['CP'].remove(file)              
        
        
        LowerFrameForUsage.updateTextCount()
        ShareHereby.FRAMECP.destroyWindow()
        ShareHereby.buttonsFromTopFrame[2].configure(state='disabled')    
                
                
                
                        
    @staticmethod     
    def reachingPath(period, year):
        # toReachIn = CP.FATHERPATH / year
        # folders = [folder for folder in toReachIn.iterdir() if folder.is_dir()]
        
        # for folder in folders:
        #     if period in folder.name:
        #         return folder
            
        month = period.split(' - ')[0]
        
        day_first_period, day_second_period = CP.readJSON_aboutDays(SpotCheck.ReacheableJSON()[1])
        
        first_period = datetime(year=int(year), month=int(month), day=int(day_first_period))
        second_period = datetime(year=int(year), month=int(month), day=int(day_second_period))
        
        possibility = {
            "01":'{} À {}'.format((first_period - relativedelta(months=1)).strftime("%d.%m.%Y"), (second_period).strftime("%d.%m.%Y")),
            "02":'{} À {}'.format((first_period - relativedelta(months=1)).strftime("%d.%m.%Y"), (second_period).strftime("%d.%m.%Y")),
            "03":'{} À {}'.format((first_period - relativedelta(months=1)).strftime("%d.%m.%Y"), (second_period).strftime("%d.%m.%Y")),
            "04":'{} À {}'.format((first_period - relativedelta(months=1)).strftime("%d.%m.%Y"), (second_period).strftime("%d.%m.%Y")),
            "05":'{} À {}'.format((first_period - relativedelta(months=1)).strftime("%d.%m.%Y"), (second_period).strftime("%d.%m.%Y")),
            "06":'{} À {}'.format((first_period - relativedelta(months=1)).strftime("%d.%m.%Y"), (second_period).strftime("%d.%m.%Y")),
            "07":'{} À {}'.format((first_period - relativedelta(months=1)).strftime("%d.%m.%Y"), (second_period).strftime("%d.%m.%Y")),
            "08":'{} À {}'.format((first_period - relativedelta(months=1)).strftime("%d.%m.%Y"), (second_period).strftime("%d.%m.%Y")),
            "09":'{} À {}'.format((first_period - relativedelta(months=1)).strftime("%d.%m.%Y"), (second_period).strftime("%d.%m.%Y")),
            "10":'{} À {}'.format((first_period - relativedelta(months=1)).strftime("%d.%m.%Y"), (second_period).strftime("%d.%m.%Y")),
            "11":'{} À {}'.format((first_period - relativedelta(months=1)).strftime("%d.%m.%Y"), (second_period).strftime("%d.%m.%Y")),
            "12":'{} À {}'.format((first_period - relativedelta(months=1)).strftime("%d.%m.%Y"), (second_period).strftime("%d.%m.%Y")),
        }
        
        return f'{period} - {possibility[month]}'
        
        
    @staticmethod
    def readJSON_aboutDays(config_path):
        with open(config_path, 'r', encoding='utf-8') as file:
            config_data = json.load(file)
        return config_data["CP - Possibility"]['1DDPP'], config_data["CP - Possibility"]['2DDSP']
        
        