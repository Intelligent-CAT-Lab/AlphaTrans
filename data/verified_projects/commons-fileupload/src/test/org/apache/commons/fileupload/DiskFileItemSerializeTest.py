import pytest

import unittest
import typing
from typing import *
import io
from io import BytesIO 
from pathlib import Path
from pickle import Pickler, Unpickler
import os



class DiskFileItemSerializeTest(unittest.TestCase):

    __textContentType: str = "text/plain"
    __threshold: int = 16
    __REPO: Path = Path(os.getenv('TMPDIR', '/tmp')) / "diskfileitemrepo"
    

    def __deserialize(self, baos: typing.Union[io.BytesIO, bytearray]) -> Any:

        result = None
        byte_stream = BytesIO(baos) if isinstance(baos, bytearray) else baos
        try:
            ois = Unpickler(byte_stream)
            result = ois.load()
        finally:
            if isinstance(baos, bytearray):
                byte_stream.close()
        return result

    def __serialize(self, target: Any) -> typing.Union[io.BytesIO, bytearray]:

        baos = BytesIO()
        oos = Pickler(baos)
        oos.dump(target)
        byte_array = baos.getvalue()
        baos.close()
        return byte_array

    def __createContentBytes(self, size: int) -> typing.List[int]:

        buffer = ""
        count = 0
        for i in range(size):
            buffer += str(count)
            count += 1
            if count > 9:
                count = 0
        return [ord(c) for c in buffer]

    def __compareBytes(
        self, text: str, origBytes: typing.List[int], newBytes: typing.List[int]
    ) -> None:

        unittest.TestCase().assertIsNotNone(origBytes, f"{text} origBytes must not be None")
        unittest.TestCase().assertIsNotNone(newBytes, f"{text} newBytes must not be None")
        unittest.TestCase().assertEqual(len(origBytes), len(newBytes), f"{text} lengths of origBytes and newBytes are not equal")
        for i in range(len(origBytes)):
            unittest.TestCase().assertEqual(origBytes[i], newBytes[i], f"{text} the {i}th entry of origBytes and newBytes do not match")

