class AbstractGlobalObject():
    'Absolute Class for patterns'
    
    def __init__(self, object) -> None:
        from guiManagement.GUI import GUIMain
        self.object_main:GUIMain = object
        self.master = self.object_main.master
        self.run()


    def run(self):
        'Abstract Run'
