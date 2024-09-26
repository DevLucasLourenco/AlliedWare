from pathlib import Path, WindowsPath
import sys


class ShareHereby:
    # Instances & Objects Shared
    #----------
    MAIN_INSTANCE_OF_GUI:object
    LabelToShowTheCountOfFiles=...
    FRAMEDIF = ...
    FRAMEDIFD = ...
    FRAMECC = ...
    FRAMECP = ...
    FRAMEHE = ...
    #----------
        
    # Keys
    #----------
    KEYS = ['DIF', 'DIFD', 'HE', 'CC', 'CP']
    #----------
    
    # Objects from Frames
    #----------
    buttonsFromTopFrame:list
    labelFromTopFrame:str
    #----------
    
    # Lists
    #----------
    ALL_ARCHIVES_VALIDATED:list[WindowsPath] = list()
    
    ARCHIVES_FILTERED:dict = dict() # em generateDynamicKeys é propagada e criado com as chaves de "KEYS"
    
    FOLDER_UNION:list = list()
    #----------
    
    # Keys Variables
    #----------
    countedSection = {k:0 for k in KEYS}
    countedSection.update({"Total":0})
    
    KEYS_TO_IDENTIFY:dict = {
            'DIF -':'DIF',
            'DIF-':'DIF',
            #----------
            'DIFD -':'DIFD',
            'DIFD-':'DIFD',
            #----------
            'CC -':'CC',
            'CC-':'CC',
            #----------
            'CP -':'CP',
            'CP-':'CP',
            #----------
            'SOLICITAÇÃO DE HE':'HE',
            'SOLICITAÇÃO DE HE':'HE',
            'SOLICITACAO DE HE':'HE',
            'SOLICITACAO DE HE':'HE',
        }
    #----------
    
    # Description to ToolTip
    #----------
    ToolTipDescription:str = ""
    #----------
    
    # Validations of DIF
    #----------
    VALIDATIONS = dict()
    #----------
    
    # DIR - Orientation 
    #----------
    DIR_ORIENTATION:str
    #----------
    
    # Rule's Key Reached
    #----------
    rulesKeyReached = ...
    #----------
    
    
    
    def generateDynamicKeys(self):
        for key in ShareHereby.KEYS:
            ShareHereby.ARCHIVES_FILTERED[key] = list()


    @staticmethod
    def reset_counter():
        for key in ShareHereby.countedSection:
            ShareHereby.countedSection[key] = 0
            
            
    def resource_path(relative_path):
        base_path = getattr(sys, '_MEIPASS', Path(__file__).parent)
        return Path(base_path).joinpath(relative_path)