import logging
import os
from pathlib import Path
from typing import Literal


# from src.data.dirSpotCheck import SpotCheck



class KingLog:
    def __init__(self) -> None:
        self.configureLogLevel()


    def input(self, message: str, typeLog: Literal['CRITICAL', 'ERROR', 'WARNING', 'INFO']):
        self.__captureType(typeLog, message)
        
    
    def configureLogLevel(self):
        log_file_path = Path(os.environ['USERPROFILE']) / "AlliedWareDataHouse" / 'log.log'
        log_instance_file_path = Path(os.environ['USERPROFILE']) / "AlliedWareDataHouse" / 'logInstance.log'

        log_dir = log_file_path.parent
        log_dir.mkdir(exist_ok=True, parents=True)

        logHandler_A = logging.FileHandler(log_file_path, mode='a', encoding='utf-8')
        logHandler_A.setLevel(logging.INFO)

        logInstanceHandler_W = logging.FileHandler(log_instance_file_path, mode='w', encoding='utf-8')
        logInstanceHandler_W.setLevel(logging.INFO)

        formatter = logging.Formatter('%(levelname)s | %(asctime)s | %(message)s')
        logHandler_A.setFormatter(formatter)
        logInstanceHandler_W.setFormatter(formatter)

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
