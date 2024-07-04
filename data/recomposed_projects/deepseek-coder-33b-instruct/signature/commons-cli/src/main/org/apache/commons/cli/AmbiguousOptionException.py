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
        buffer = io.StringIO()
        buffer.write("Ambiguous option: '")
        buffer.write(option)
        buffer.write("'  (could be: ")
        iterator = iter(matchingOptions)
        while True:
            try:
                matchingOption = next(iterator)
            except StopIteration:
                break
            else:
                buffer.write("'")
                buffer.write(matchingOption)
                buffer.write("'")
                if iterator:
                    buffer.write(", ")
        buffer.write(")")
        return buffer.getvalue()

    @staticmethod
    def __createMessage(option: str, matchingOptions: typing.Collection[str]) -> str:

        buf = io.StringIO()
        buf.write("Ambiguous option: '")
        buf.write(option)
        buf.write("'  (could be: ")

        it = iter(matchingOptions)
        while True:
            try:
                item = next(it)
            except StopIteration:
                break
            buf.write("'")
            buf.write(item)
            buf.write("'")
            try:
                next(it)
            except StopIteration:
                pass
            else:
                buf.write(", ")

        buf.write(")")

        return buf.getvalue()
