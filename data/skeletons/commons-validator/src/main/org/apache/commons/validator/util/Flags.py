from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io

# Imports End


class Flags:

    # Class Fields Begin
    __serialVersionUID: int = None
    __flags: int = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def hashCode(self) -> int:
        pass

    def equals(self, obj: typing.Any) -> bool:
        pass

    def clone(self) -> typing.Any:
        pass

    def turnOnAll(self) -> None:
        pass

    def clear(self) -> None:
        pass

    def turnOffAll(self) -> None:
        pass

    def turnOff(self, flag: int) -> None:
        pass

    def turnOn(self, flag: int) -> None:
        pass

    def isOff(self, flag: int) -> bool:
        pass

    def isOn(self, flag: int) -> bool:
        pass

    def getFlags(self) -> int:
        pass

    def __init__(self, constructorId: int, flags: int) -> None:
        pass

    # Class Methods End
