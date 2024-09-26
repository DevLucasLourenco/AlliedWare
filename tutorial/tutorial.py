import os
from pathlib import Path

from src.data.shareables import ShareHereby
from src.LOG.LOG_manager import LOGGER


def tutorial_exec():
    os.startfile(Path(ShareHereby.resource_path(r'tutorial\data\AlliedWare f5151b230af14072ba167f094c270c89.html')))
    LOGGER("Tutorial aberto", "INFO")