from __future__ import annotations
import re
import io
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.ParseException import *


class MissingArgumentException(ParseException):

    __option: Option = None

    __serialVersionUID: int = -7098538588704965017

    def getOption(self) -> Option:
        return self.__option

    @staticmethod
    def MissingArgumentException1(
        constructorId: int, message: str, option: Option
    ) -> MissingArgumentException:
        if constructorId == 1:
            return MissingArgumentException(
                constructorId, "Missing argument for option: " + option.getKey(), option
            )
        return MissingArgumentException(constructorId, message, option)

    def __init__(self, constructorId: int, message: str, option: Option) -> None:
        super().__init__(message)
        if constructorId == 1:
            self.__option = option
