from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *


class StringEncoderComparator:

    __stringEncoder: StringEncoder = None

    def compare(self, o1: typing.Any, o2: typing.Any) -> int:

        compare_code = 0

        try:
            s1 = self.__stringEncoder.encode(o1)
            s2 = self.__stringEncoder.encode(o2)
            compare_code = s1.compareTo(s2)
        except EncoderException:
            compare_code = 0

        return compare_code

    def __init__(self, constructorId: int, stringEncoder: StringEncoder) -> None:

        if constructorId == 0:
            self.__stringEncoder = stringEncoder
        else:
            self.__stringEncoder = None
