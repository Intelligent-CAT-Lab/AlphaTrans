from __future__ import annotations
import re
import io
from src.main.org.apache.commons.cli.ParseException import *


class UnrecognizedOptionException(ParseException):

    __option: str = ""

    __serialVersionUID: int = -252504690284625623

    def getOption(self) -> str:
        return self.__option

    @staticmethod
    def UnrecognizedOptionException1(message: str) -> UnrecognizedOptionException:
        return UnrecognizedOptionException(message, None)

    def __init__(self, message: str, option: str) -> None:
        super().__init__(message)
        self.__option = option
