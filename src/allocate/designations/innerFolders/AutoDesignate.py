import json
from pathlib import Path

from src.data.shareables import ShareHereby
from src.data.dirSpotCheck import SpotCheck


class DIFAutoDesignation:
    
    def __init__(self, file, pathTo, TypeOfRule) -> None:
        self.file:Path = file
        self.pathTo:Path = pathTo
        self.TypeOfRule:str = TypeOfRule

        self.RULES:dict = self.__readJSON(SpotCheck.ReacheableJSON()[1]) 
        
    
    def __readJSON(self, config_path):
        with open(config_path, 'r', encoding='utf-8') as file:
            config_data = json.load(file)
        return config_data[self.TypeOfRule]
    

    def analyse(self):
        for key, folder in self.RULES.items():
            if key in DIFAutoDesignation.getMainFilename(str(self.file.name).upper()):
                ShareHereby.rulesKeyReached = key
                self.newPathTo = self.pathTo / folder
                self.newPathTo.mkdir(parents=True, exist_ok=True)
                return True
        return False


    def get(self) -> Path:
        return self.newPathTo
    
    
    @staticmethod
    def getMainFilename(file):
        listFile = file.split('-')
        try:
            if len(listFile) == 1:
                return file
            return file.replace(listFile[-1], "")
        
        except IndexError:
            return file

