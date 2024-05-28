from __future__ import annotations

# Imports Begin
import os
import typing
from typing import *
import io

# Imports End


class Arg:

    # Class Fields Begin
    __serialVersionUID: int = None
    _bundle: str = None
    _key: str = None
    _name: str = None
    _position: int = None
    _resource: bool = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def clone(self) -> typing.Any:
        pass

    def setResource(self, resource: bool) -> None:
        pass

    def setPosition(self, position: int) -> None:
        pass

    def setName(self, name: str) -> None:
        pass

    def setKey(self, key: str) -> None:
        pass

    def setBundle(self, bundle: str) -> None:
        pass

    def isResource(self) -> bool:
        pass

    def getPosition(self) -> int:
        pass

    def getName(self) -> str:
        pass

    def getKey(self) -> str:
        pass

    def getBundle(self) -> str:
        pass

    # Class Methods End
