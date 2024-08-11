import os
import subprocess

from tkinter import filedialog
from pathlib import Path

from src.errors.DirNotFound import DirNotFound


class SpotCheck:
    
    def CreateFileIfNotExists():
        path = Path('src\data\dir_to_json_appointment.txt')
        
        if not path.is_file():
            with path.open('w') as file:
                file.write('---')
    
    
    def ReacheableJSON():
        with open('src\data\dir_to_json_appointment.txt', 'r') as f:
            txt = f.read()
        return [Path(txt).exists(), txt]
        
    
    def dir_appointment():
        dir = filedialog.askopenfilename(
            title="Selecione o Arquivo de Apontamente de Diretório - JSON",
            filetypes=[("Arquivos JSON", "*.json")],
        )
        
        if dir:
            with open("src\data\dir_to_json_appointment.txt", 'w') as f:
                f.write(dir)
                
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
            
            
    