import time
from tkinter import messagebox

from src.GUI.frames.frameAlteration.DIFFrame import FrameDIF
from src.GUI.alerts.alert import VisualAlert
from src.filter.byOptions import By
from src.data.shareables import ShareHereby
from src.allocate.designations.DIF import DIF


class Request:
    def __init__(self) -> None:
        self.By:By
        self.ButtonObject=...
        self.frameForUsage=...
        

class Allocate:
    def __init__(self, request:Request) -> None:
        self.request = request
        self.By = Allocate.__verifyIntegrity(request.By)
        self.frame = request.frameForUsage
        # self.objectOfButton = request.ButtonObject
        
        self.ALLOCATION_OF_ARCHIEVES()
        
        
    @staticmethod
    def __verifyIntegrity(by):
        if isinstance(by, By):
            return by
        raise
    
    def ALLOCATION_OF_ARCHIEVES(self):
        if self.request.By:
            match(self.request.By):
                case By.DIF:
                    FrameDIF(self.request.frameForUsage)
                    
                case By.CC:
                    print('CC')
                    
                case By.CP:
                    print('CP')
                    
                case By.HE:
                    print('HE')
                    
                case _:
                    print("Off")
                    

