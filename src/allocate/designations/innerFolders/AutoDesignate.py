import json
from pathlib import Path


class DIFAutoDesignation:
    
    def __init__(self, file, pathTo, TypeOfRule) -> None:
        self.file:Path = file
        self.pathTo:Path = pathTo
        self.TypeOfRule:str = TypeOfRule
        
        
        
        self.RULES:dict = self.__readJSON(self.takeDirToReachAppointmentsJSON()) ####
    
    
    def takeDirToReachAppointmentsJSON(self):
        txt:str
        with open('src\data\dir_to_json_appointment.txt', 'r') as f:
            txt = f.read()
        return txt
    
        
    def __readJSON(self, config_path):
        with open(config_path, 'r', encoding='utf-8') as file:
            config_data = json.load(file)
        return config_data[self.TypeOfRule]
    

    def analyse(self):
        for key, folder in self.RULES.items():
            print('key: ', key)
            print('name: ', self.file.name)
            if key in self.file.name:
                self.newPathTo = self.pathTo / folder
                self.newPathTo.mkdir(parents=True, exist_ok=True)
                print("true: ", self.file.name)
                return True

        print('não foi possível alocar')
            

    def get(self) -> Path:
        return self.newPathTo
    

