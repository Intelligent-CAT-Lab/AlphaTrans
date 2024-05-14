# Imports Begin
import typing
from abc import ABC

# Imports End


class FromStringConverter(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:
        pass

    # Class Methods End
