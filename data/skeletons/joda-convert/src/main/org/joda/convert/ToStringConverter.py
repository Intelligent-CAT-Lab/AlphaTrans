# Imports Begin
import typing
from abc import ABC

# Imports End


class ToStringConverter(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def convertToString(self, object: typing.Any) -> str:
        pass

    # Class Methods End
