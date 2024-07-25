
from GUI.alerts.alert import VisualAlert


class NoInternetConnection(FileNotFoundError):
        def __init__(self, message:str="Sem conexão com o SERVIDOR ou INTERNET") -> None:
            super().__init__(message)
                
                
        def InicializeGUI(self):
            ...
            VisualAlert()
            

        # def log():
        #     ...