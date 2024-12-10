from __future__ import annotations
import re
import io
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.ParseException import *


class AlreadySelectedException(ParseException):

    __option: Option = None

    __group: OptionGroup = None

    __serialVersionUID: int = 3674381532418544760

    def getOptionGroup(self) -> OptionGroup:
        return self.__group

    def getOption(self) -> Option:
        return self.__option

    @staticmethod
    def AlreadySelectedException1(
        group: OptionGroup, option: Option
    ) -> AlreadySelectedException:
        return AlreadySelectedException(
            "The option '"
            + option.getKey()
            + "' was specified but an option from this group "
            + "has already been selected: '"
            + group.getSelected()
            + "'",
            group,
            option,
        )

    @staticmethod
    def AlreadySelectedException0(message: str) -> AlreadySelectedException:
        return AlreadySelectedException(message, None, None)

    def __init__(self, message: str, group: OptionGroup, option: Option) -> None:
        super().__init__(message)
        self.__group = group
        self.__option = option
