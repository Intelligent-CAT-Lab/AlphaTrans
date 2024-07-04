from __future__ import annotations
import re
import io
import typing
from typing import *


class NameType:

    SEPHARDIC: NameType = None
    GENERIC: NameType = None
    ASHKENAZI: NameType = None
    __name: str = ""

    @staticmethod
    def initialize_fields() -> None:
        NameType.SEPHARDIC: NameType = None
        NameType.GENERIC: NameType = None
        NameType.ASHKENAZI: NameType = None

    def getName(self) -> str:
        return self.__name

    def __init__(self, name: str) -> None:

        self.__name = name

        if self.__name == "sep":
            self.SEPHARDIC = self
        elif self.__name == "gen":
            self.GENERIC = self
        elif self.__name == "ash":
            self.ASHKENAZI = self


NameType.initialize_fields()
