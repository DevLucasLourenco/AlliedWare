import os
import shutil

from pathlib import Path

from src.data.exportDataWhichDidntRelocated import Archives
from src.allocate.designations.innerFolders.AutoDesignate import DIFAutoDesignation
from src.data.shareables import ShareHereby
# from src.allocate.relocate.relocating import RelocateProcess


# Quando criar DIFD, colocar uma verificação de só manter a 
# pasta (quando houver duplicidade) que 
# tiver a data de modificação mais recente

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
        
        self.passthrough()
        
        
    @staticmethod
    def getFolders(directory):
        return [folder for folder in directory.iterdir() if folder.is_dir()]
    
    
    @staticmethod
    def extractName(file:Path):
        return (file.name).split('-')[-1].strip().split('.')[0]
    
    
    @staticmethod  
    def __renamingOf(file):
        for key in ShareHereby.KEYS_TO_IDENTIFY.keys():
            file = file.replace(key,'')
        return file.strip()
    
    
    def passthrough(self):
        for arq in ShareHereby.ARCHIEVES_FILTERED['DIF']:
            folder_name_to_reach = DIF.extractName(arq)
            for path in self.FOLDER_UNION:
                if folder_name_to_reach in path.name:
                    DIF.moveTo(file=arq, pathTo=path)
                    

    def moveTo(file:Path, pathTo:Path, innerFolders=True):
        if innerFolders:
            DAD = DIFAutoDesignation(file, pathTo, 'DIF')
            validator = DAD.analyse()
            
            if validator:
                path = DAD.get()
                shutil.move(file, path / DIF.__renamingOf(file.name))
                print('Movido: ', path)
                
            elif not validator:
                Archives.NotRelocatedFromEmployee.append(file)
            
        elif not innerFolders:
            shutil.move(file, pathTo / DIF.__renamingOf(file.name))
            
            
        