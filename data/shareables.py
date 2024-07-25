from pathlib import WindowsPath


class ShareHereby:
    # Keys
    #----------
    MAIN_INSTANCE_OF_GUI:object
    #----------
    
    # Keys
    #----------
    KEYS = ['DIF', 'HE', 'CC', 'CP'] ## falta acrescentar o DIFD
    #----------
    
    # Objects from Frames
    #----------
    buttonsFromTopFrame:list
    labelFromTopFrame:str
    #----------
    
    # Lists
    #----------
    ALL_ARCHIEVES_VALIDATED:list[WindowsPath] = list()
    
    ARCHIEVES_FILTERED:dict = dict() # em generateDynamicKeys é propagada e criado com as chaves de "KEYS"
    ARCHIEVES_CONCLUTED:dict = dict() # em generateDynamicKeys é propagada e criado com as chaves de "KEYS"
    #----------
    
    # Keys Variables
    #----------
    countedSection = {k:0 for k in KEYS}
    countedSection.update({"Total":0})
    
    KEYS_TO_IDENTIFY:dict = {
            'DIF -':'DIF',
            'DIF-':'DIF',
            #----------
            'CC -':'CC',
            'CC-':'CC',
            #----------
            'CP -':'CP',
            'CP-':'CP',
            #----------
            'SOLICITAÇÃO DE HE -':'HE',
            'SOLICITAÇÃO DE HE-':'HE',
            'SOLICITACAO DE HE -':'HE',
            'SOLICITACAO DE HE-':'HE',
        }
    #----------
    
    
    def generateDynamicKeys(self):
        for key in ShareHereby.KEYS:
            ShareHereby.ARCHIEVES_FILTERED[key] = list()
            ShareHereby.ARCHIEVES_CONCLUTED[key] = list()
    
    
    
    
    
    
    
    