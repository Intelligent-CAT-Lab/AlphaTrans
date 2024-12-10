from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.DecoderException import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class Decoder(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def decode(self, source: typing.Any) -> typing.Any:
        pass

    # Class Methods End
