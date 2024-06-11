from __future__ import annotations
import io
import typing
from src.main.org.apache.commons.cli.UnrecognizedOptionException import *


class AmbiguousOptionException(UnrecognizedOptionException):

    __matchingOptions: typing.Collection[str] = None

    __serialVersionUID: int = 5829816121277947229

    def getMatchingOptions(self) -> typing.Collection[str]:

        return self.__matchingOptions

    def __init__(self, option: str, matchingOptions: typing.Collection[str]) -> None:

        # Call the superclass constructor
        super().__init__(self.__createMessage(option, matchingOptions), option)

        # Set the matching options
        self.__matchingOptions = matchingOptions

    @staticmethod
    def __createMessage(option: str, matchingOptions: typing.Collection[str]) -> str:
        # Create the message
        message = "Ambiguous option: '" + option + "'  (could be: "
        for i, matchingOption in enumerate(matchingOptions):
            if i > 0:
                message += ", "
            message += "'" + matchingOption + "'"
        message += ")"
        return message

    @staticmethod
    def __createMessage(option: str, matchingOptions: typing.Collection[str]) -> str:

        buf = io.StringIO()
        buf.write("Ambiguous option: '")
        buf.write(option)
        buf.write("'  (could be: ")

        it = iter(matchingOptions)
        for i, match in enumerate(it):
            buf.write("'")
            buf.write(match)
            buf.write("'")
            if next(it, None) is not None:
                buf.write(", ")

        buf.write(")")

        return buf.getvalue()
