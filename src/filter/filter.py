from src.filter.byOptions import By
from src.data.shareables import ShareHereby


class Filter:
    
    def filtering(self):
        for arq in ShareHereby.ALL_ARCHIVES_VALIDATED:
            for searchKey in ShareHereby.KEYS_TO_IDENTIFY:
                if searchKey in arq.name:
                    ShareHereby.ARCHIVES_FILTERED[ShareHereby.KEYS_TO_IDENTIFY[searchKey]].append(arq)
                    break
        
    
