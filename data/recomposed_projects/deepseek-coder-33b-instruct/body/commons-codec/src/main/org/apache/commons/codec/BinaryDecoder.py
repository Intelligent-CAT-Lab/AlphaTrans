from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.Decoder import *
from src.main.org.apache.commons.codec.DecoderException import *


class BinaryDecoder(ABC):

    def decode(self, source: typing.List[int]) -> typing.List[int]:

        # Your implementation here
        pass
