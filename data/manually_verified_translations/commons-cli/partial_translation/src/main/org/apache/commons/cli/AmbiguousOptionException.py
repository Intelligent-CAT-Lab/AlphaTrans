from __future__ import annotations
import re
from io import StringIO
import io
import typing
from src.main.org.apache.commons.cli.UnrecognizedOptionException import *


class AmbiguousOptionException(UnrecognizedOptionException):

    __matchingOptions: typing.Collection[str] = None

    __serialVersionUID: int = 5829816121277947229

    def getMatchingOptions(self) -> typing.Collection[str]:
        return self.__matchingOptions

    def __init__(self, option: str, matchingOptions: typing.Collection[str]) -> None:
        super().__init__(self.__createMessage(option, matchingOptions), option)
        self.__matchingOptions = matchingOptions

    @staticmethod
    def __createMessage(option: str, matchingOptions: typing.Collection[str]) -> str:

        buf = io.StringIO()
        buf.write("Ambiguous option: '")
        buf.write(option)
        buf.write("'  (could be: ")

        it = iter(matchingOptions)
        while True:
            try:
                buf.write("'")
                buf.write(next(it))
                buf.write("'")
            except StopIteration:
                break
            if next(it, None) is not None:
                buf.write(", ")

        buf.write(")")

        return buf.getvalue()
