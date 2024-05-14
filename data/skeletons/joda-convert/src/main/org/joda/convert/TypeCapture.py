# Imports Begin
from src.main.org.joda.convert.Types import *
import typing
from abc import ABC

# Imports End


class TypeCapture(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def capture(self) -> typing.Type:
        pass

    # Class Methods End
