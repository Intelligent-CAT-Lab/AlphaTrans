# Imports Begin
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.Encoder import *
from abc import ABC

# Imports End


class StringEncoder(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def encode(self, source: str) -> str:
        pass

    # Class Methods End
