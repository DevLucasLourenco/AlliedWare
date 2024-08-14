import os
import shutil

from pathlib import Path
from tkinter import messagebox

from src.GUI.frames.lowerFrame import LowerFrameForUsage
from src.LOG.LOG_manager import KingLog
from src.errors.NoInternetConnection import NoInternetConnection
from src.data.exportData import Archives
from src.allocate.designations.innerFolders.AutoDesignate import DIFAutoDesignation
from src.data.shareables import ShareHereby

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
    
    
    def __init__(self, *args):
        self.args = args
        
        self.hiring_folders_inside:list[Path] = DIF.getFolders(DIF.HIRING_DIR)
        self.adm_folders_inside:list[Path] = DIF.getFolders(DIF.ADM_DIR)
        self.op_folders_inside:list[Path] = DIF.getFolders(DIF.OP_DIR)
        
        ShareHereby.FOLDER_UNION = self.hiring_folders_inside + self.adm_folders_inside + self.op_folders_inside
        
        self.passthrough()
        
        
    
    @staticmethod
    def getFolders(directory):
        try:
            return [folder for folder in directory.iterdir() if folder.is_dir()]
        except FileNotFoundError:
            raise NoInternetConnection()
    
    
    
    @staticmethod
    def extractName(file:Path):
        return (file.name).split('-')[-1].strip().split('.')[0]
    
    
    
    @staticmethod  
    def __renamingOf(file):
        for key in ShareHereby.KEYS_TO_IDENTIFY.keys():
            file = file.replace(key,'')
        return file.strip()
    
    
    
    def passthrough(self):
        listage = ShareHereby.ARCHIEVES_FILTERED['DIF'].copy()
        for file in listage:
            targetedFile = False # Arquivo direcionado
            
            folder_name_to_reach = DIF.extractName(file)
            for path in ShareHereby.FOLDER_UNION:
                self.removeFromList = False
                if folder_name_to_reach in path.name:
                    targetedFile = True
                    self.moveTo(file=file, pathTo=path, innerFolders=self.args)
            
            if not targetedFile:
                KingLog(f'NÃO MOVIDO POR: <Pasta Inexistente> - {file}', 'WARNING')
                Archives.NotRelocatedFromEmployee.append((file, f"Pasta Inexistente - {folder_name_to_reach}"))
            
            if self.removeFromList:
                ShareHereby.ARCHIEVES_FILTERED['DIF'].remove(file)
        
        messagebox.showinfo("Concluído", "Alocações realizadas")
        ShareHereby.FRAMEDIF.destroyWindow()
                    


    def moveTo(self, file:Path, pathTo:Path, innerFolders=True):
        if innerFolders:
            DAD = DIFAutoDesignation(file, pathTo, 'DIF')
            validator = DAD.analyse()
            
            if validator:
                path = DAD.get()
                
                try:
                    # shutil.move(file, path / DIF.__renamingOf(file.name))
                    DIF.__move(path, file)
                    
                    Archives.RelocatedFromEmployee.append((file, path))
                    KingLog(f'ALOCAÇÃO:\nDE:\n{file}\nPARA: \n{path}\n--------------------', 'INFO')
                    self.removeFromList = True
                    
                except PermissionError:
                    messagebox.showerror('Pasta Influenciada', f'Impossível manusear visto que existe uma pasta que está sendo influenciada.\n{pathTo}')
                    KingLog(f'NÃO MOVIDO POR: <Pasta influenciada> - {file}', 'WARNING')
                    Archives.NotRelocatedFromEmployee.append((file, str(path) + "Pasta influenciada"))
                    
                except Exception as e:
                    messagebox.showerror("Error", e)
                    messagebox.showinfo("Recarregar", "Tente selecionar a pasta novamente.")
                    KingLog(e, "ERROR")
                
            else:
                try:
                    Archives.NotRelocatedFromEmployee.append((file, str(path) + 'Parâmetro de Alocação Inexistente'))
                except UnboundLocalError:
                    Archives.NotRelocatedFromEmployee.append((file, 'Parâmetro de Alocação Inexistente'))
                KingLog(f'NÃO MOVIDO POR: <Parâmetro de Alocação Inexistente> - {file}', 'WARNING')

            
        elif not innerFolders:
            # shutil.move(file, pathTo / DIF.__renamingOf(file.name))
            DIF.__move(path, file)
        
        LowerFrameForUsage.updateTextCount()
            
            
    @staticmethod    
    def __move(pathTo:Path, filename:Path):
        fileRenamed = DIF.__renamingOf(filename.name)
        uniqueFilename = DIF._generate_unique_filename(pathTo, fileRenamed)
        shutil.move(filename, uniqueFilename)
        
        
        
    # @staticmethod
    # def _generate_unique_filename(destination: Path, filename: str) -> Path:
    #     base_name, ext = filename.rsplit('.', 1)
        
    #     while (destination / f"{base_name}.{ext}").exists():
    #         counter = 1
    #         while (destination / f"{base_name}_{counter}.{ext}").exists():
    #             counter += 1
                
    #     return destination / f"{base_name}_{counter}.{ext}"
    
    @staticmethod
    def _generate_unique_filename(destination: Path, filename: str) -> Path:
        base_name, ext = filename.rsplit('.', 1)
        counter = 1
        
        while (destination / f"{base_name}.{ext}").exists():
            while (destination / f"{base_name}_{counter}.{ext}").exists():
                counter += 1
            return destination / f"{base_name}_{counter}.{ext}"
        
        return destination / f"{base_name}.{ext}"
