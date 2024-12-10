from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.cli.UnrecognizedOptionException import *
import typing
import io

# Imports End


class AmbiguousOptionException(UnrecognizedOptionException):

    # Class Fields Begin
    __serialVersionUID: int = None
    __matchingOptions: typing.Collection[str] = None
    # Class Fields End

    # Class Methods Begin
    def getMatchingOptions(self) -> typing.Collection[str]:
        pass

    def __init__(self, option: str, matchingOptions: typing.Collection[str]) -> None:
        pass

    @staticmethod
    def __createMessage(option: str, matchingOptions: typing.Collection[str]) -> str:
        pass

    # Class Methods End
