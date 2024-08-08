import json
import os
from pathlib import Path
import shutil

from src.data.exportDataWhichHasntBeenRelocated import Archives


class DIFTreatment:
    
    def __init__(self, path_base):
        self.path_base = path_base
        self.regras_dif = self.readJSON(r'GENERAL_CONFIGURATIONS.json')
        
    
    def readJSON(self, config_path):
        with open(config_path, 'r') as file:
            config_data = json.load(file)
        return config_data['DIF']
    
    
    def alocateFile(self, arquivo, regras):
        for chave, pasta in regras.items():
            # Cria a pasta caso não exista
            if chave.lower() in arquivo.lower():
                caminho_destino = self.path_base / pasta
                caminho_destino.mkdir(parents=True, exist_ok=True)
                
                return caminho_destino / arquivo
        return None


    def organize(self):
        for arquivo in os.listdir(self.path_base):
            arquivo_path = self.path_base / arquivo
            
            # Ignorar pastas
            if arquivo_path.is_dir():
                continue

            # Tentar alocar com as regras "DIF"
            destino = self.alocateFile(arquivo, self.regras_dif)
            if destino:
                shutil.move(Path(self.path_base) / arquivo,destino)
                
                return destino
            else:
                print(f"Nenhuma regra aplicada para {arquivo}")

            Archives.NotRelocatedFromEmployee.append(arquivo)
            
