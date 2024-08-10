
from tkinter import messagebox
from src.GUI.alerts.alert import VisualAlert


class NoInternetConnection(FileNotFoundError, OSError):
        def __init__(self, message:str="Sem conexão com o SERVIDOR ou INTERNET") -> None:
            super().__init__(message)
            self.message = message
            self.messageBoxShow()
            self.log_approach()
                
                
        def messageBoxShow(self):
            messagebox.showerror('Conexão', 'Sem conexão com o SERVIDOR ou INTERNET')
            

        def log_approach(self):
            ...
        