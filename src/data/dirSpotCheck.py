import os
import subprocess           

from tkinter import filedialog, messagebox
from pathlib import Path

from src.LOG.LOG_manager import LOGGER
from src.errors.DirNotFound import DirNotFound


class SpotCheck:
    
    @staticmethod
    def getDefaultPath():
        return Path(os.environ['USERPROFILE'])
    
    def defaultPathTo():
        return Path(SpotCheck.getDefaultPath() / "AlliedWareDataHouse")
        
    
    def CreateFileIfNotExists():
        try:
            # path = Path(r'src\data\dir_to_json_appointment.txt')
            SpotCheck.defaultPathTo().mkdir(exist_ok=True)
            path = SpotCheck.defaultPathTo() / 'dir_to_json_appointment.txt'
        
            if not path.is_file():
                with path.open('w') as file:
                    file.write('---')
                    
        except FileNotFoundError as e:
            messagebox.showerror("Error", e)
                  
    
    def ReacheableJSON() -> list[bool|str]:
        try:
            # with open(r'src\data\dir_to_json_appointment.txt', 'r') as f:
            with open(SpotCheck.defaultPathTo() / 'dir_to_json_appointment.txt', 'r') as f:
                txt = f.read()
            return [Path(txt).exists(), txt]
        except FileNotFoundError as e:
            messagebox.showerror("Error", e)
        
    
    def dir_appointment():
        dir = filedialog.askopenfilename(
            title="Selecione o Arquivo de Apontamento de Diretório - JSON",
            filetypes=[("Arquivos JSON", "*.json")],
        )
        
        if dir:
            with open(SpotCheck.defaultPathTo() / 'dir_to_json_appointment.txt', 'w') as f:
                f.write(dir)
            LOGGER(f'Nova Especificação de Indicador: {dir}', 'INFO')
        return dir
                
                
    def show_appointment():
        validator, path = SpotCheck.ReacheableJSON()
        if validator:            
            try:
                subprocess.run(["notepad.exe",path], check=True)
            except Exception as e:
                os.startfile(path)
                
        else:
            raise DirNotFound(dir=path)
            
            
