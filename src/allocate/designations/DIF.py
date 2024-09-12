import shutil

from pathlib import Path
from tkinter import messagebox

from src.LOG.LOG_manager import LOGGER
from src.data.exportData import Archives
from src.data.shareables import ShareHereby
from src.GUI.frames.lowerFrame import LowerFrameForUsage
from src.errors.NoInternetConnection import NoInternetConnection
from src.allocate.designations.innerFolders.AutoDesignate import DIFAutoDesignation


class DIF:
    FATHERDIR:Path = Path(r'G:\Recursos Humanos\01 - PESSOAL\01 - FUNCIONÁRIOS')
    
    HIRING_FOLDER_NAME:str = r'0 - PROCESSO DE CONTRATAÇÃO'
    ADM_FOLDER_NAME:str = r'1 - ADMINISTRATIVO'
    OP_FOLDER_NAME:str = r'2 - OPERAÇÃO'
    
    
    HIRING_DIR:Path = FATHERDIR / HIRING_FOLDER_NAME
    ADM_DIR:Path = FATHERDIR / ADM_FOLDER_NAME
    OP_DIR:Path = FATHERDIR / OP_FOLDER_NAME
    
    RPA_DIR:Path = Path(r'G:\Recursos Humanos\05 - RPA\01 - DOCUMENTOS COLABORADORES')
    
    def __init__(self, validations):
        ShareHereby.VALIDATIONS = validations
        
        self.hiring_folders_inside:list[Path] = DIF.getFolders(DIF.HIRING_DIR)
        self.adm_folders_inside:list[Path] = DIF.getFolders(DIF.ADM_DIR)
        self.op_folders_inside:list[Path] = DIF.getFolders(DIF.OP_DIR)
        self.rpa_folders_inside:list[Path] = DIF.getFolders(DIF.RPA_DIR)
        
        ShareHereby.FOLDER_UNION = self.hiring_folders_inside + self.adm_folders_inside + self.op_folders_inside + self.rpa_folders_inside
        
    
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
            listage = ShareHereby.ARCHIVES_FILTERED['DIF'].copy()
            
        for file in listage:
            targetedFile = False # Arquivo direcionado
            self.removeFromList = False
            
            folder_name_to_reach = DIF.extractName(file)
            for path in ShareHereby.FOLDER_UNION:
                if folder_name_to_reach in path.name:
                    targetedFile = True
                    self.moveTo(file=file, pathTo=path)
                    self.removeFromList = True
                    
                    continue
            
            if not targetedFile:
                LOGGER(f'NÃO MOVIDO POR: <Pasta Inexistente> - {file}', 'WARNING')
                Archives.NotRelocatedFromEmployee.append((file, f"Pasta Inexistente - {folder_name_to_reach}"))
            
            
            if self.removeFromList:
                if file not in Path(ShareHereby.DIR_ORIENTATION).iterdir():
                    ShareHereby.ARCHIVES_FILTERED['DIF'].remove(file)
        
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
                    self.__move(path, file)
                    
                    Archives.RelocatedFromEmployee.append((file, path))
                    LOGGER(f'ALOCAÇÃO DIF:\nDE:\n{file}\nPARA: \n{path}\n--------------------', 'INFO')
                    self.removeFromList = True
                    
                elif not ShareHereby.VALIDATIONS["InnerFolder"].get():
                    self.__move(pathTo, file)
                    
                    Archives.RelocatedFromEmployee.append((file, pathTo))
                    LOGGER(f'ALOCAÇÃO DIF:\nDE:\n{file}\nPARA: \n{pathTo}\n--------------------', 'INFO')
                    self.removeFromList = True
                
                
            except PermissionError:
                # messagebox.showerror('Pasta Influenciada', f'Impossível manusear visto que existe uma pasta que está sendo influenciada.\n{pathTo}')
                LOGGER(f'NÃO MOVIDO POR: <Pasta influenciada> - {file}', 'WARNING')
                Archives.NotRelocatedFromEmployee.append((file, str(path) + "Pasta influenciada"))
                self.removeFromList = False
                
                
            except Exception as e:
                LOGGER(e, "ERROR")
                messagebox.showerror("Error", str(e) + '\n' + file.name)
                messagebox.showinfo("Recarregar", "Recarregar - Tente selecionar a pasta novamente.")
                self.removeFromList = False
            
        else:
            try:
                Archives.NotRelocatedFromEmployee.append((file, str(path) + 'Parâmetro de Alocação Inexistente'))
            except UnboundLocalError:
                Archives.NotRelocatedFromEmployee.append((file, 'Parâmetro de Alocação Inexistente'))
                
            LOGGER(f'NÃO MOVIDO POR: <Parâmetro de Alocação Inexistente> - {file}', 'WARNING')
            self.removeFromList = False

        LowerFrameForUsage.updateTextCount()
    

    
    def __move(self, pathTo:Path, file:Path):
        if ShareHereby.VALIDATIONS['RemovePreffix'].get():
            filename_renamed = DIF.__renamingOf(file.name)

        if ShareHereby.VALIDATIONS['DuplicatedFile'].get():
            if ShareHereby.VALIDATIONS['RemovePreffix'].get():
                pathTo = DIF._generate_unique_filename(pathTo, filename_renamed)
            else:
                pathTo = DIF._generate_unique_filename(pathTo, file.name)
            
        shutil.move(file, pathTo)



    @staticmethod
    def _generate_unique_filename(destination: Path, filename: str) -> Path:
        base_name, ext = filename.rsplit('.', 1)
        counter = 1
        
        while (destination / f"{base_name}.{ext}").exists():
            while (destination / f"{base_name}_{counter}.{ext}").exists():
                counter += 1
            return destination / f"{base_name}_{counter}.{ext}"
        
        return destination / f"{base_name}.{ext}"
