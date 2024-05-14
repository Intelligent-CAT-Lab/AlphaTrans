# Imports Begin
from src.main.org.joda.convert.FromStringConverter import *
import typing
from abc import ABC

# Imports End


class TypedFromStringConverter(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getEffectiveType(self) -> typing.Type[typing.Any]:
        pass

    # Class Methods End
