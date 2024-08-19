import os
from pathlib import Path

from src.LOG.LOG_manager import LOGGER



def tutorial_exec():
    os.startfile(Path(r'tutorial\data\AlliedWare f5151b230af14072ba167f094c270c89.html'))
    LOGGER("Tutorial aberto", "INFO")