from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io

# Imports End


class VisitTracker:

    # Class Fields Begin
    __validateCount: int = None
    __activateCount: int = None
    __passivateCount: int = None
    __destroyed: bool = None
    __id: int = None
    __key: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def validate(self) -> bool:
        pass

    def reset(self) -> None:
        pass

    def passivate(self) -> None:
        pass

    def isDestroyed(self) -> bool:
        pass

    def getValidateCount(self) -> int:
        pass

    def getPassivateCount(self) -> int:
        pass

    def getKey(self) -> typing.Any:
        pass

    def getId(self) -> int:
        pass

    def getActivateCount(self) -> int:
        pass

    def destroy(self) -> None:
        pass

    def activate(self) -> None:
        pass

    def __init__(self, constructorId: int, key: typing.Any, id_: int) -> None:
        pass

    def __fail(self, message: str) -> None:
        pass

    # Class Methods End
