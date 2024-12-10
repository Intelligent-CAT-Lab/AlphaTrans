from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Option import *
import io

# Imports End


class AlreadySelectedException(ParseException):

    # Class Fields Begin
    __serialVersionUID: int = None
    __group: OptionGroup = None
    __option: Option = None
    # Class Fields End

    # Class Methods Begin
    def getOptionGroup(self) -> OptionGroup:
        pass

    def getOption(self) -> Option:
        pass

    @staticmethod
    def AlreadySelectedException1(
        group: OptionGroup, option: Option
    ) -> AlreadySelectedException:
        pass

    @staticmethod
    def AlreadySelectedException0(message: str) -> AlreadySelectedException:
        pass

    def __init__(self, message: str, group: OptionGroup, option: Option) -> None:
        pass

    # Class Methods End
