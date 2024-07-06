from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *


class AbstractCaverphone(StringEncoder, ABC):

    def encode(self, source: typing.Any) -> typing.Any:

        pass  # LLM could not translate this method

    def isEncodeEqual(self, str1: str, str2: str) -> bool:
        return self.encode(str1) == self.encode(str2)

    def __init__(self) -> None:
        pass
