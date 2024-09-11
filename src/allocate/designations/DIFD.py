import shutil

from pathlib import Path
from tkinter import messagebox

from src.LOG.LOG_manager import LOGGER
from src.data.exportData import Archives
from src.data.shareables import ShareHereby
from src.GUI.frames.lowerFrame import LowerFrameForUsage
from src.errors.NoInternetConnection import NoInternetConnection
from src.allocate.designations.innerFolders.AutoDesignate import DIFAutoDesignation


class DIFD:
    FIRED_FOLDER_DIR = Path(r'G:\Recursos Humanos\01 - PESSOAL\01 - FUNCIONÁRIOS\5 - EX FUNCIONÁRIOS')

    def __init__(self, validations) -> None:
        ShareHereby.VALIDATIONS = validations
        self.fired_folders_inside:list[Path] = DIFD.getFolders(DIFD.FIRED_FOLDER_DIR)
        
        
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
    
    
    def passthroughDIFD(self):
        listage = ShareHereby.ARCHIVES_FILTERED['DIFD'].copy()
        
        for file in listage:
            targetedFile = False # Arquivo direcionado
            self.removeFromList = False
            
            folder_name_to_reach = DIFD.extractName(file)
            for path in self.fired_folders_inside:
                if folder_name_to_reach in path.name:
                    targetedFile = True
                    self.moveTo(file=file, pathTo=path)
                    self.removeFromList = True
            
            if not targetedFile:
                LOGGER(f'NÃO MOVIDO POR: <Pasta Inexistente> - {file}', 'WARNING')
                Archives.NotRelocatedFromEmployeeFired.append((file, f"Pasta Inexistente - {folder_name_to_reach}"))
            
            if self.removeFromList:
                ShareHereby.ARCHIVES_FILTERED['DIFD'].remove(file)

            
        messagebox.showinfo("Concluído", "Alocações realizadas")
        # ShareHereby.FRAMEDIF.destroyWindow()
        ShareHereby.buttonsFromTopFrame[0].configure(state='disabled')
        
        
    def moveTo(self, file:Path, pathTo:Path):
        DIF_AD = DIFAutoDesignation(file, pathTo, 'DIF')
        validator = DIF_AD.analyse()
        
        if validator:
            path = DIF_AD.get()
            
            try:
                if ShareHereby.VALIDATIONS["InnerFolder"].get():
                    self.__move(path, file)
                    
                    Archives.RelocatedFromEmployeeFired.append((file, path))
                    LOGGER(f'ALOCAÇÃO DIFD:\nDE:\n{file}\nPARA: \n{path}\n--------------------', 'INFO')
                    self.removeFromList = True
                    
                elif not ShareHereby.VALIDATIONS["InnerFolder"].get():
                    self.__move(pathTo, file)
                    
                    Archives.RelocatedFromEmployeeFired.append((file, pathTo))
                    LOGGER(f'ALOCAÇÃO DIFD:\nDE:\n{file}\nPARA: \n{pathTo}\n--------------------', 'INFO')
                    self.removeFromList = True
                
                
            except PermissionError:
                # messagebox.showerror('Pasta Influenciada', f'Impossível manusear visto que existe uma pasta que está sendo influenciada.\n{pathTo}')
                LOGGER(f'NÃO MOVIDO POR: <Pasta influenciada> - {file}', 'WARNING')
                Archives.NotRelocatedFromEmployeeFired.append((file, str(path) + "Pasta influenciada"))
                
                
            except Exception as e:
                LOGGER(e.with_traceback(), "ERROR")
                messagebox.showerror("Error", e)
                messagebox.showinfo("Recarregar", "Recarregar - Tente selecionar a pasta novamente.")
            
        else:
            try:
                Archives.NotRelocatedFromEmployeeFired.append((file, str(path) + 'Parâmetro de Alocação Inexistente'))
            except UnboundLocalError:
                Archives.NotRelocatedFromEmployeeFired.append((file, 'Parâmetro de Alocação Inexistente'))
                
            LOGGER(f'NÃO MOVIDO POR: <Parâmetro de Alocação Inexistente> - {file}', 'WARNING')
        LowerFrameForUsage.updateTextCount()
    
    
    def __move(self, pathTo:Path, file:Path):
        if ShareHereby.VALIDATIONS['RemovePreffix'].get():
            filename_renamed = DIFD.__renamingOf(file.name)

        if ShareHereby.VALIDATIONS['DuplicatedFile'].get():
            if ShareHereby.VALIDATIONS['RemovePreffix'].get():
                pathTo = DIFD._generate_unique_filename(pathTo, filename_renamed)
            else:
                pathTo = DIFD._generate_unique_filename(pathTo, file.name)
            
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
    