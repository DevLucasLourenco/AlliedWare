import os
import shutil

from pathlib import Path
from tkinter import messagebox

from src.LOG.LOG_manager import LOGGER
from src.data.exportData import Archives
from src.data.shareables import ShareHereby
from src.GUI.frames.lowerFrame import LowerFrameForUsage
from src.errors.NoInternetConnection import NoInternetConnection
from src.allocate.designations.innerFolders.AutoDesignate import DIFAutoDesignation

# Quando criar DIFD, colocar uma verificação de só manter a 
# pasta (quando houver duplicidIF_ade) que 
# tiver a data de modificação mais recente

class DIF:
    HIRING_FOLDER_NAME:str = r'0 - PROCESSO DE CONTRATAÇÃO'
    ADM_FOLDER_NAME:str = r'1 - ADMINISTRATIVO'
    OP_FOLDER_NAME:str = r'2 - OPERAÇÃO'
    
    FATHERDIR:Path = Path(r'G:\Recursos Humanos\01 - PESSOAL\01 - FUNCIONÁRIOS')
    HIRING_DIR:Path = FATHERDIR / HIRING_FOLDER_NAME
    ADM_DIR:Path = FATHERDIR / ADM_FOLDER_NAME
    OP_DIR:Path = FATHERDIR / OP_FOLDER_NAME
    
    
    def __init__(self, validations):
        ShareHereby.VALIDATIONS = validations
        
        self.hiring_folders_inside:list[Path] = DIF.getFolders(DIF.HIRING_DIR)
        self.adm_folders_inside:list[Path] = DIF.getFolders(DIF.ADM_DIR)
        self.op_folders_inside:list[Path] = DIF.getFolders(DIF.OP_DIR)
        
        ShareHereby.FOLDER_UNION = self.hiring_folders_inside + self.adm_folders_inside + self.op_folders_inside
        
        # self.passthrough()
        
    
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
    
    
    
    def passthrough(self, *newList):
        # print('NEW list:', newList)
        
        # print('innerFolder:', ShareHereby.VALIDATIONS["InnerFolder"].get())
        # print('PREFIX:', ShareHereby.VALIDATIONS["RemovePreffix"].get())
        # print('DUPLICATE:', ShareHereby.VALIDATIONS["DuplicatedFile"].get())
        
        if newList:
            listage = newList[0]
        else:   
            listage = ShareHereby.ARCHIEVES_FILTERED['DIF'].copy()
            
        for file in listage:
            targetedFile = False # Arquivo direcionado
            self.removeFromList = False
            
            folder_name_to_reach = DIF.extractName(file)
            for path in ShareHereby.FOLDER_UNION:
                if folder_name_to_reach in path.name:
                    targetedFile = True
                    self.moveTo(file=file, pathTo=path)
                    self.removeFromList = True
            
            if not targetedFile:
                LOGGER(f'NÃO MOVIDO POR: <Pasta Inexistente> - {file}', 'WARNING')
                Archives.NotRelocatedFromEmployee.append((file, f"Pasta Inexistente - {folder_name_to_reach}"))
            
            
            if self.removeFromList:
                ShareHereby.ARCHIEVES_FILTERED['DIF'].remove(file)
        
        messagebox.showinfo("Concluído", "Alocações realizadas")
        ShareHereby.FRAMEDIF.destroyWindow()
        ShareHereby.buttonsFromTopFrame[0].configure(state='disabled')
                    


    def moveTo(self, file:Path, pathTo:Path):
        DIF_AD = DIFAutoDesignation(file, pathTo, 'DIF')
        validator = DIF_AD.analyse()
        
        if validator:
            path = DIF_AD.get()
            
            try:
                if ShareHereby.VALIDATIONS["InnerFolder"].get():
                    DIF.__move(path, file)
                    
                    Archives.RelocatedFromEmployee.append((file, path))
                    LOGGER(f'ALOCAÇÃO DIF:\nDE:\n{file}\nPARA: \n{path}\n--------------------', 'INFO')
                    self.removeFromList = True
                    
                elif not ShareHereby.VALIDATIONS["InnerFolder"].get():
                    DIF.__move(pathTo, file)
                    # shutil.move(file, pathTo) ## fazer um outro __moveNotInnerFolder para esse caso aqui porque para esse caso não permite retirar o código
                    
                    Archives.RelocatedFromEmployee.append((file, pathTo))
                    LOGGER(f'ALOCAÇÃO DIF:\nDE:\n{file}\nPARA: \n{pathTo}\n--------------------', 'INFO')
                    self.removeFromList = True
                
                
            except PermissionError:
                messagebox.showerror('Pasta Influenciada', f'Impossível manusear visto que existe uma pasta que está sendo influenciada.\n{pathTo}')
                LOGGER(f'NÃO MOVIDO POR: <Pasta influenciada> - {file}', 'WARNING')
                Archives.NotRelocatedFromEmployee.append((file, str(path) + "Pasta influenciada"))
                
                
            except Exception as e:
                LOGGER(e, "ERROR")
                messagebox.showerror("Error", e)
                messagebox.showinfo("Recarregar", "Recarregar - Tente selecionar a pasta novamente.")
            
        else:
            try:
                Archives.NotRelocatedFromEmployee.append((file, str(path) + 'Parâmetro de Alocação Inexistente'))
            except UnboundLocalError:
                Archives.NotRelocatedFromEmployee.append((file, 'Parâmetro de Alocação Inexistente'))
            LOGGER(f'NÃO MOVIDO POR: <Parâmetro de Alocação Inexistente> - {file}', 'WARNING')


        LowerFrameForUsage.updateTextCount()
    
        
            
    @staticmethod    
    def __move(pathTo:Path, filename:Path):
        PATH:Path = pathTo
        FILENAME:Path = filename
        # print('inicio', FILENAME, PATH, '----------',sep="\n")
        
        if ShareHereby.VALIDATIONS['RemovePreffix'].get():
            print(FILENAME)
            FILENAME = DIF.__renamingOf(filename.name)
            print(FILENAME)
            
        if ShareHereby.VALIDATIONS['DuplicatedFile'].get():
            PATH = DIF._generate_unique_filename(PATH, FILENAME.name)
        
        print('fim', FILENAME, PATH,  '----------',sep="\n")
        # shutil.move(filename, pathTo)


    @staticmethod
    def _generate_unique_filename(destination: Path, filename: str) -> Path:
        base_name, ext = filename.rsplit('.', 1)
        counter = 1
        
        while (destination / f"{base_name}.{ext}").exists():
            while (destination / f"{base_name}_{counter}.{ext}").exists():
                counter += 1
            return destination / f"{base_name}_{counter}.{ext}"
        
        return destination / f"{base_name}.{ext}"
