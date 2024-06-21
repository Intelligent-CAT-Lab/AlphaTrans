from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.joda.convert.StringConvert import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.factory.ByteObjectArrayStringConverterFactory import *


class TestByteObjectArrayStringConverterFactory:

    def test_ByteArray(self) -> None:

        def __doTest(self, array: typing.List[int], str: str) -> None:
            pass

        __doTest(self, [0], "00")
        __doTest(self, [None], "--")
        __doTest(self, [0, 1, None, None, 15, 16, 127, -128, -1], "0001----0F107F80FF")

    def __doTest(self, array: typing.List[int], str: str) -> None:

        pass  # LLM could not translate this method
