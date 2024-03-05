# Imports Begin
import unittest
import pickle
import os
import typing
from typing import *
import io
import pathlib

# Imports End


class DiskFileItemSerializeTest(unittest.TestCase):

    # Class Fields Begin
    __REPO: pathlib.Path = pathlib.Path(os.getenv("java.io.tmpdir"), "diskfileitemrepo")
    __textContentType: str = "text/plain"
    __threshold: int = 16
    # Class Fields End

    # Class Methods Begin
    def __deserialize(self, baos: typing.Union[io.BytesIO, bytearray]) -> typing.Any:

        result = None
        bais = io.BytesIO(baos.getvalue())
        ois = pickle.Unpickler(bais)
        result = ois.load()
        bais.close()
        return result

    def __serialize(self, target: typing.Any) -> typing.Union[io.BytesIO, bytearray]:

        with io.BytesIO() as baos:
            with ObjectOutputStream(baos, self) as oos:
                oos.writeObject(target)
                oos.flush()
                return baos.getvalue()

    def __createContentBytes(self, size: int) -> typing.List[int]:

        buffer = []
        count = 0
        for i in range(size):
            buffer.append(str(count))
            count += 1
            if count > 9:
                count = 0
        return bytes(buffer)

    def __compareBytes(
        self, text: str, origBytes: typing.List[int], newBytes: typing.List[int]
    ) -> None:

        assert origBytes is not None, f"{text} origBytes must not be None"
        assert newBytes is not None, f"{text} newBytes must not be None"
        assert len(origBytes) == len(newBytes), f"{text} byte[] length"
        for i in range(len(origBytes)):
            assert origBytes[i] == newBytes[i], f"{text} byte[{i}]"

    # Class Methods End
