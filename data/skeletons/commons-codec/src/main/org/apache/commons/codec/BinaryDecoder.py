from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.Decoder import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class BinaryDecoder(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def decode(self, source: typing.List[int]) -> typing.List[int]:
        pass

    # Class Methods End
