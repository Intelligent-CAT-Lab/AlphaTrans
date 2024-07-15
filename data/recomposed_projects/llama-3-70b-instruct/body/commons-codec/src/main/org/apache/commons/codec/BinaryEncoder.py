from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.Encoder import *
from src.main.org.apache.commons.codec.EncoderException import *


class BinaryEncoder(ABC):

    def encode(self, source: typing.List[int]) -> typing.List[int]:
        return source
