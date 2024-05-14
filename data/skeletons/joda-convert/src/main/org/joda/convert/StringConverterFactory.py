# Imports Begin
from src.main.org.joda.convert.StringConverter import *
import typing
from abc import ABC

# Imports End


class StringConverterFactory(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def findConverter(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:
        pass

    # Class Methods End
