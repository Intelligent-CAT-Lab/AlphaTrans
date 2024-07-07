from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.language.Caverphone2 import *


class Caverphone(StringEncoder):

    __encoder: Caverphone2 = None

    @staticmethod
    def initialize_fields() -> None:
        Caverphone.__encoder: Caverphone2 = Caverphone2()

    def isCaverphoneEqual(self, str1: str, str2: str) -> bool:
        return self.caverphone(str1) == self.caverphone(str2)

    def encode1(self, str: str) -> str:
        return self.caverphone(str)

    def encode0(self, obj: typing.Any) -> typing.Any:

        if not isinstance(obj, str):
            raise EncoderException(
                "Parameter supplied to Caverphone encode is not of type java.lang.String",
                None,
            )
        return self.caverphone(obj)

    def caverphone(self, source: str) -> str:
        return self.__encoder.encode(source)

    def __init__(self) -> None:
        super().__init__()


Caverphone.initialize_fields()
