import logging
from pathlib import Path
from typing import Literal



class KingLog:
    def __init__(self) -> None:
        self.configureLogLevel()


    def input(self, message: str, typeLog: Literal['CRITICAL', 'ERROR', 'WARNING', 'INFO']):
        self.__captureType(typeLog, message)
        
    
    def configureLogLevel(self):
        log_file_path = Path('src/LOG/file/log.log')
        log_instance_file_path = Path('src/LOG/file/logInstance.log')

        log_dir = log_file_path.parent
        log_dir.mkdir(exist_ok=True, parents=True)

        # Configurar o handler para log.log com modo 'a'
        logHandler_A = logging.FileHandler(log_file_path, mode='a', encoding='utf-8')
        logHandler_A.setLevel(logging.INFO)

        # Configurar o handler para logInstance.log com modo 'w'
        logInstanceHandler_W = logging.FileHandler(log_instance_file_path, mode='w', encoding='utf-8')
        logInstanceHandler_W.setLevel(logging.INFO)

        # Definir o formato do log
        formatter = logging.Formatter('%(levelname)s | %(asctime)s | %(message)s')
        logHandler_A.setFormatter(formatter)
        logInstanceHandler_W.setFormatter(formatter)

        # Obter o logger e adicionar ambos os handlers
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logHandler_A)
        self.logger.addHandler(logInstanceHandler_W)


    def __captureType(self, typeLog: Literal['CRITICAL', 'ERROR', 'WARNING', 'INFO'], message: str):
        match typeLog:
            case 'CRITICAL':
                self.logger.critical(message)
            case 'ERROR':
                self.logger.error(message)
            case 'WARNING':
                self.logger.warning(message)
            case 'INFO':
                self.logger.info(message)
            case _:
                self.logger.info(message)


_instance = KingLog()
LOGGER = _instance.input
