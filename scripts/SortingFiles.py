import os
import shutil
import pandas as pd

from datetime import datetime
from tkinter import messagebox
from pathlib import Path, WindowsPath


from src.data.dirSpotCheck import SpotCheck
from src.LOG.LOG_manager import LOGGER
from src.data.exportData import Archives
from src.allocate.designations.innerFolders.AutoDesignate import DIFAutoDesignation
from src.data.shareables import ShareHereby
from src.allocate.designations.DIF import DIF


class SortGlobalFiles:
    NAME:str = "Organizador de Pastas"
    
    DESCRIPTION = """Organiza a documentação de todas as pastas internas de:
    
0 - PROCESSO DE CONTRATAÇÃO
1 - ADMINISTRATIVO
2 - OPERAÇÃO
"""
    
    @staticmethod
    def run():
        SortGlobalFiles.permutate()
            
        
    @staticmethod
    def permutate():
        SortGlobalFiles.prepareConfigurations()
        filesConcluded:list = list()
        filesNotConcluded:list = list()
        
        for folder in ShareHereby.FOLDER_UNION:
            filesAtCurrentFolder:list = SortGlobalFiles.findAllFilesAtFile(folder)

            for file in filesAtCurrentFolder:            
                DIF_AD = DIFAutoDesignation(file, folder, "DIF")
                validator = DIF_AD.analyse()
                
                try:
                    if validator:
                        path = DIF_AD.get()
                        pathTo = DIF._generate_unique_filename(path, file.name)
                        shutil.move(file, pathTo)
                        filesConcluded.append((file, path, ShareHereby.rulesKeyReached))
                    
                    else:
                        filesNotConcluded.append((file, 'Parâmetro de Alocação Inexistente'))
                except Exception as e:
                    filesNotConcluded.append((file, e))
                
        
        data = {
            "filesConcluded": [("File", "Destination", "Key Triggered")] + [(str(file), str(destination), str(key)) for file, destination, key in filesConcluded],
            "filesNotConcluded": [("File", "Destination")] + [(str(file), str(destination)) for file, destination in filesNotConcluded],
        }
        
        SortGlobalFiles.__export(data)
        messagebox.showinfo("Exportar",'exportando arquivo XLSX...')

            
    @staticmethod
    def findAllFilesAtFile(path):
        folder = Path(path)
        
        if folder.exists() and folder.is_dir():
            arquivos = [arquivo for arquivo in folder.glob('*') if arquivo.is_file() and arquivo.name != 'Thumbs.db']
            return arquivos
        
        else:
            return []     
                
        
        
    @staticmethod
    def prepareConfigurations() -> DIF:
        validatorToInnerFolder = GetBoolean(value=True)
        validatorToRemovePreffixDIF = GetBoolean(value=True)
        validatorDuplicatedFilename = GetBoolean(value=True)
        
        validations = {
            "InnerFolder":validatorToInnerFolder,
            "RemovePreffix":validatorToRemovePreffixDIF,
            "DuplicatedFile":validatorDuplicatedFilename
        }
        
        app = DIF(validations)
    
    
    @staticmethod
    def __export(data):
        filename = Archives.PATH / f'SortGlobalFiles_XLSX_{SortGlobalFiles.__prepareSuffix()}.xlsx'
        with pd.ExcelWriter(filename) as writer:
            for sheet_name, rows in data.items():
                df = pd.DataFrame(rows[1:], columns=rows[0])
                df.to_excel(writer, sheet_name=sheet_name, index=False)
                
        LOGGER(f'XLSX exportado: {filename}', 'INFO')
        os.startfile(filename)
        
        
    @staticmethod
    def __prepareSuffix():
        return datetime.now().strftime('%d%m%Y_%H%M%S')

    
class GetBoolean():
    
    def __init__(self, value) -> None:
        self.getValue = value
    
    def get(self):
        return self.getValue