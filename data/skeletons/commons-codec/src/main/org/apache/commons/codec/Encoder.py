# Imports Begin
from src.main.org.apache.commons.codec.EncoderException import *
import typing
from abc import ABC

# Imports End


class Encoder(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def encode(self, source: typing.Any) -> typing.Any:
        pass

    # Class Methods End
