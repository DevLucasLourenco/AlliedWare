import logging
from pathlib import Path
from typing import Literal



class KingLog:
    def __init__(self, message: str, typeLog: Literal['CRITICAL', 'ERROR', 'WARNING', 'INFO']) -> None:
        self.configureLogLevel()
        self.__captureType(typeLog, message)

    def configureLogLevel(self):
        log_file_path = Path('src/LOG/file/log.log')
        log_dir = log_file_path.parent
        log_dir.mkdir(exist_ok=True, parents=True)

        logging.basicConfig(
            level=logging.INFO,
            filename=log_file_path,
            filemode='a',
            format='%(levelname)s | %(asctime)s | %(message)s',
            encoding='utf-8',
        )

    def __captureType(self, typeLog: Literal['CRITICAL', 'ERROR', 'WARNING', 'INFO'], message: str):
        match typeLog:
            case 'CRITICAL':
                logging.critical(message)
            case 'ERROR':
                logging.error(message)
            case 'WARNING':
                logging.warning(message)
            case 'INFO':
                logging.info(message)
            case _:
                logging.info(message)
