# Imports Begin
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.Encoder import *
import typing
from abc import ABC

# Imports End


class BinaryEncoder(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def encode(self, source: typing.List[int]) -> typing.List[int]:
        pass

    # Class Methods End
