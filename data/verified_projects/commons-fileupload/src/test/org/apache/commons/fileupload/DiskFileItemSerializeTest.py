import pytest

import unittest
import typing
from typing import *
from io import BytesIO 
from pathlib import Path
from pickle import Pickler, Unpickler
import os



class DiskFileItemSerializeTest(unittest.TestCase):

    __textContentType: str = "text/plain"
    __threshold: int = 16
    __REPO: Path = Path(os.getenv('TMPDIR', '/tmp')) / "diskfileitemrepo"
    

    def __deserialize(self, baos: bytearray) -> Any:

        byte_stream = BytesIO(baos)
        ois = Unpickler(byte_stream)
        result = ois.load()
        return result

    def __serialize(self, target: Any) -> bytearray:

        byte_stream = BytesIO()
        oos = Pickler(byte_stream)
        oos.dump(target)
        byte_array = byte_stream.getvalue()
        return byte_array

    def __createContentBytes(self, size: int) -> typing.List[int]:

        buffer = ""
        count = 0
        for i in range(size):
            buffer += str(count)
            count += 1
            if count > 9:
                count = 0
        return list(buffer.encode('utf-8'))

    def __compareBytes(
        self, text: str, origBytes: typing.List[int], newBytes: typing.List[int]
    ) -> None:

        assert origBytes is not None, f"{text} origBytes must not be None"
        assert newBytes is not None, f"{text} newBytes must not be None"
        assert len(origBytes) == len(newBytes), f"{text} lengths of origBytes and newBytes are not equal"
        for i in range(len(origBytes)):
            assert origBytes[i] == newBytes[i], f"{text} the {i}th entry of origBytes and newBytes do not match"

