import os
import shutil

from pathlib import Path

from data.shareables import ShareHereby



class DIF:
    HIRING_FOLDER_NAME:str = r'0 - PROCESSO DE CONTRATAÇÃO'
    ADM_FOLDER_NAME:str = r'1 - ADMINISTRATIVO'
    OP_FOLDER_NAME:str = r'2 - OPERAÇÃO'
    
    FATHERDIR:Path = Path(r'G:\Recursos Humanos\01 - PESSOAL\01 - FUNCIONÁRIOS')
    HIRING_DIR:Path = FATHERDIR / HIRING_FOLDER_NAME
    ADM_DIR:Path = FATHERDIR / ADM_FOLDER_NAME
    OP_DIR:Path = FATHERDIR / OP_FOLDER_NAME
    
    
    def __init__(self):
        
        self.hiring_folders_inside:list[Path] = DIF.getFolders(DIF.HIRING_DIR)
        self.adm_folders_inside:list[Path] = DIF.getFolders(DIF.ADM_DIR)
        self.op_folders_inside:list[Path] = DIF.getFolders(DIF.OP_DIR)
        
        self.FOLDER_UNION = self.hiring_folders_inside + self.adm_folders_inside + self.op_folders_inside
        print(self.FOLDER_UNION)
        self.passthrough()
        
        
    @staticmethod
    def getFolders(directory):
        return [folder for folder in directory.iterdir() if folder.is_dir()]
    
    
    def extractName(self, archieve:Path):
        return (archieve.name).split('-')[-1].strip().split('.')[0]
    
    
    def passthrough(self):
        for arq in ShareHereby.ARCHIEVES_FILTERED['DIF']:
            print(arq)
            folder_name_to_reach = self.extractName(arq)
            for path in self.FOLDER_UNION:
                if folder_name_to_reach in path.name:
                    print('achei')
                    print(path)
                    break
                    # continue
                    
                    
    def moveTo(self):
        ...
        
    def renameIt(self):
        ...
    
    
    
    