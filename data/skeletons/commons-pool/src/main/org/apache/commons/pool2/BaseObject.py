# Imports Begin
from abc import ABC

# Imports End


class BaseObject(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def _toStringAppendFields(self, builder: str) -> None:
        pass

    # Class Methods End
