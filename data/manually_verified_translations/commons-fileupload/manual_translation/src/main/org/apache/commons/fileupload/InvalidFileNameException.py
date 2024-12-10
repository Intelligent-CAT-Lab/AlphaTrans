from __future__ import annotations
import time
import re
import io


class InvalidFileNameException(RuntimeError):

    __name: str = ""

    __serialVersionUID: int = 7922042602454350470

    def getName(self) -> str:
        return self.__name

    def __init__(self, pName: str, pMessage: str) -> None:
        super().__init__(pMessage)
        self.__name = pName
