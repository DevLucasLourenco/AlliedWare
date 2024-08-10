from tkinter import messagebox
from src.GUI.alerts.alert import VisualAlert

class DirNotFound(Exception):
    def __init__(self, message: str = "Diretório de Arquivo JSON inalcançável.\nFavor, instrua outro diretório.", dir='') -> None:
        super().__init__(message)
        self.dir = dir
        self.message = message
        self.messageBoxShow()
        self.log_approach()


    def messageBoxShow(self):
        print(self.dir)
        if self.dir:
            print(1)
            messagebox.showerror("Diretório Inalcancável", f'Favor, instrua outro diretório para encontrar o JSON necessário.\nDiretório Informado:\n{self.dir}' )
        else:
            messagebox.showerror("Diretório Inalcancável", 'Favor, instrua outro diretório para encontrar o JSON necessário.' )
    
    
    def log_approach(self):
        # print('log: ' + self.message)
        ...
