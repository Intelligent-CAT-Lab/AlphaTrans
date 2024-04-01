# Imports Begin
import tempfile
import unittest
import os
import typing
from typing import *
from io import BytesIO
import pathlib

# Imports End


class DiskFileItemSerializeTest(unittest.TestCase):

    # Class Fields Begin
    pathlib.Path(tempfile.gettempdir()).joinpath("diskfileitemrepo")
    __textContentType: str = "text/plain"
    __threshold: int = 16
    # Class Fields End

    # Class Methods Begin
    def __deserialize(self, baos: typing.Union[io.BytesIO, bytearray]) -> typing.Any:

        result = None
        bais = io.BytesIO(baos)
        ois = pickle.load(bais)
        result = ois
        bais.close()
        return result

    def __serialize(self, target: typing.Any) -> typing.Union[io.BytesIO, bytearray]:

        import io
        import pickle

        baos = io.BytesIO()
        pickle.dump(target, baos)
        baos.flush()
        baos.close()
        return baos.getvalue()

    def __createContentBytes(self, size: int) -> typing.List[int]:

        buffer = ""
        count = 0
        for i in range(size):
            buffer += str(count)
            count += 1
            if count > 9:
                count = 0
        return buffer.encode("utf-8")

    def __compareBytes(
        self, text: str, origBytes: typing.List[int], newBytes: typing.List[int]
    ) -> None:

        assert origBytes is not None, "origBytes must not be null"
        assert newBytes is not None, "newBytes must not be null"
        assert len(origBytes) == len(newBytes), f"{text} byte[] length"
        for i in range(len(origBytes)):
            assert origBytes[i] == newBytes[i], f"{text} byte[{i}]"

    # Class Methods End
