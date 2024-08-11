from tkinter import messagebox
from src.LOG.LOG_manager import KingLog


class DirNotFound(Exception):
    def __init__(self, message: str = "Diretório de Arquivo JSON inalcançável.\nFavor, instrua outro diretório.", dir='') -> None:
        super().__init__(message)
        self.dir = dir
        self.message = message
        self.messageBoxShow()
        self.log_approach()


    def messageBoxShow(self):
        if self.dir:
            messagebox.showerror("Diretório Inalcancável", f'Favor, instrua outro diretório para encontrar o JSON necessário.\nDiretório Informado:\n{self.dir}' )
        else:
            messagebox.showerror("Diretório Inalcancável", 'Favor, instrua outro diretório para encontrar o JSON necessário.' )
    
    
    def log_approach(self):
        KingLog(f'Diretório de Especificaçção de Indicador Inalcançável. Dir: {self.dir}', 'ERROR')
        
        