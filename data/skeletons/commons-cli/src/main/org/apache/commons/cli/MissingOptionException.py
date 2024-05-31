from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.cli.ParseException import *
import typing
from typing import *
import io

# Imports End


class MissingOptionException(ParseException):

    # Class Fields Begin
    __serialVersionUID: int = None
    __missingOptions: typing.List[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def getMissingOptions(self) -> typing.List[typing.Any]:
        pass

    @staticmethod
    def MissingOptionException1(
        constructorId: int, missingOptions: typing.List[typing.Any], message: str
    ) -> MissingOptionException:
        pass

    def __init__(
        self, constructorId: int, missingOptions: typing.List[typing.Any], message: str
    ) -> None:
        pass

    @staticmethod
    def __createMessage(missingOptions: typing.List[typing.Any]) -> str:
        pass

    # Class Methods End
