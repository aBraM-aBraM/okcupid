from pathlib import Path
from typing import Any
import json

class Config:

    def __init__(self) -> None:
        self._cfg: dict = dict() 

    def load(self, cfg_path: Path) -> None:
        with open(cfg_path) as cfg_fd:
            self._cfg = json.load(cfg_fd)

    def get(self, key: str, default = None) -> Any:
        if self._cfg is None:
            raise ValueError("config not initialized!")
        if value := self._cfg.get(key):
            return value
        return default
        

config = Config()