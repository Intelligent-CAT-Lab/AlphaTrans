# Imports Begin
import typing
from abc import ABC

# Imports End


class FromStringFactory(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def factory(self) -> typing.Type[typing.Any]:
        pass

    # Class Methods End
