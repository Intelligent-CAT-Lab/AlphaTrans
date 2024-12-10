from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.Field import *
import typing
from typing import *
import io

# Imports End


class Form:

    # Class Fields Begin
    __serialVersionUID: int = None
    _name: str = None
    _lFields: typing.List[Field] = None
    _inherit: str = None
    __processed: bool = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def isExtending(self) -> bool:
        pass

    def setExtends(self, inherit: str) -> None:
        pass

    def getExtends(self) -> str:
        pass

    def isProcessed(self) -> bool:
        pass

    def getFields(self) -> typing.List[Field]:
        pass

    def setName(self, name: str) -> None:
        pass

    def getName(self) -> str:
        pass

    # Class Methods End
