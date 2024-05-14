# Imports Begin
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *
import typing
from abc import ABC

# Imports End


class AbstractCaverphone(StringEncoder, ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def encode(self, source: typing.Any) -> typing.Any:
        pass

    def isEncodeEqual(self, str1: str, str2: str) -> bool:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End
