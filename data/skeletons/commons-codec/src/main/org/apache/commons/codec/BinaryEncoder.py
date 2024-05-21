from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.Encoder import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class BinaryEncoder(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def encode(self, source: typing.List[int]) -> typing.List[int]:
        pass

    # Class Methods End
