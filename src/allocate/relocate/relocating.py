from pathlib import Path
import shutil


from src.allocate.designations.innerFolders.DIFTreatment import DIFTreatment
from src.data.shareables import ShareHereby


class RelocateProcess:
    
    def moveTo(archieve:str, pathTo:Path, innerFolders=True):
        shutil.move(archieve, pathTo / RelocateProcess.__renamingOf(archieve.name))

        if innerFolders:
            sorter = DIFTreatment(pathTo)
            sorter.organize()
        
        
    def __renamingOf(archieve):
        for key in ShareHereby.KEYS_TO_IDENTIFY.keys():
            archieve = archieve.replace(key,'')
        return archieve.strip()
    
