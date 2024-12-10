from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.cli.ParseException import *
import io

# Imports End


class UnrecognizedOptionException(ParseException):

    # Class Fields Begin
    __serialVersionUID: int = None
    __option: str = None
    # Class Fields End

    # Class Methods Begin
    def getOption(self) -> str:
        pass

    @staticmethod
    def UnrecognizedOptionException1(message: str) -> UnrecognizedOptionException:
        pass

    def __init__(self, message: str, option: str) -> None:
        pass

    # Class Methods End
