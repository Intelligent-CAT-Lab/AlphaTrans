from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.Decoder import *
import io
from abc import ABC

# Imports End


class StringDecoder(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def decode(self, source: str) -> str:
        pass

    # Class Methods End
