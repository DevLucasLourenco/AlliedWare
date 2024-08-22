import time
from tkinter import messagebox

from src.GUI.frames.frameAlteration.CPFrame import FrameCP
from src.GUI.frames.frameAlteration.CCFrame import FrameCC
from src.GUI.frames.frameAlteration.DIFFrame import FrameDIF
from src.filter.byOptions import By
from src.data.shareables import ShareHereby



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
                    messagebox.showinfo('Atenção', 'Lembre-se de garantir que não haja nenhuma pasta aberta ou em utilização.')
                    ShareHereby.FRAMEDIF = FrameDIF(self.request.frameForUsage)
                    
                    
                case By.CC:
                    messagebox.showinfo('Atenção', 'Lembre-se de garantir que não haja nenhuma pasta aberta ou em utilização.')
                    ShareHereby.FRAMECC = FrameCC(self.request.frameForUsage)
                    
                                        
                case By.CP:
                    messagebox.showinfo('Atenção', 'Lembre-se de garantir que não haja nenhuma pasta aberta ou em utilização.')
                    ShareHereby.FRAMECP = FrameCP(self.request.frameForUsage)
                                        
                case By.HE:
                    print('HE')
                    
                case _:
                    print("Off")
                    

