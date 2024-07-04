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

        if not isinstance(source, str):
            raise EncoderException(
                "Parameter supplied to Caverphone encode is not of type java.lang.String",
                None,
            )
        return self.encode(source)

    def isEncodeEqual(self, str1: str, str2: str) -> bool:

        try:
            return self.encode(str1) == self.encode(str2)
        except EncoderException as e:
            raise e

    def __init__(self) -> None:
        pass
