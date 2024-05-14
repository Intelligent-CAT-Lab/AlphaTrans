# Imports Begin
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *
import typing

# Imports End


class StringEncoderComparator(Comparator):

    # Class Fields Begin
    __stringEncoder: StringEncoder = None
    # Class Fields End

    # Class Methods Begin
    def compare(self, o1: typing.Any, o2: typing.Any) -> int:
        pass

    def __init__(self, constructorId: int, stringEncoder: StringEncoder) -> None:
        pass

    # Class Methods End
