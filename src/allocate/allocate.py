import time

from src.GUI.alerts.alert import VisualAlert
from src.filter.byOptions import By
from src.data.shareables import ShareHereby
from src.allocate.designations.DIF import DIF



class Allocate:
    def __init__(self, By:By, objectOfButton) -> None:
        self.By = Allocate.__verifyIntegrity(By)
        self.objectOfButton = objectOfButton
        
        self.ALLOCATION_OF_ARCHIEVES()
        
        
    @staticmethod
    def __verifyIntegrity(by):
        if isinstance(by, By):
            return by
        raise
    
    def ALLOCATION_OF_ARCHIEVES(self):
        if self.By:
            match(self.By):
                case By.DIF:
                    # alert = VisualAlert(status='I', message=f'\nAguarde...\nProcesso {By.DIF} está sendo executado.', 
                                    #   color_appearance='dark', windowTitle='teste')
                    # alert.build()
                    DIF()
                    # alert.destroy()
                    
                case By.CC:
                    print('CC')
                    
                case By.CP:
                    print('CP')
                    
                case By.HE:
                    print('HE')
                    
                case _:
                    print("Off")
                    
    