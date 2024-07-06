from __future__ import annotations
import re
import unittest
import pytest
import pathlib
import io
from io import BytesIO
import typing
from typing import *
import os


class DiskFileItemSerializeTest:

    __threshold: int = 16
    __textContentType: str = "text/plain"
    __REPO: pathlib.Path = pathlib.Path(os.getenv("java.io.tmpdir"), "diskfileitemrepo")

    def __deserialize(self, baos: typing.Union[io.BytesIO, bytearray]) -> typing.Any:
        result = None
        bais = io.BytesIO(baos)
        ois = typing.cast(typing.IO[bytes], bais)
        result = ois.read()
        bais.close()

        return result

    def __serialize(self, target: typing.Any) -> typing.Union[io.BytesIO, bytearray]:
        baos = io.BytesIO()
        oos = io.ObjectOutputStream(baos)
        oos.writeObject(target)
        oos.flush()
        oos.close()
        return baos

    def __createContentBytes(self, size: int) -> typing.List[int]:
        buffer = []
        count = 0
        for i in range(size):
            buffer.append(str(count))
            count += 1
            if count > 9:
                count = 0
        return buffer

    def __compareBytes(
        self, text: str, origBytes: typing.List[int], newBytes: typing.List[int]
    ) -> None:
        assert origBytes is not None, "origBytes must not be null"
        assert newBytes is not None, "newBytes must not be null"
        assert len(origBytes) == len(newBytes), text + " byte[] length"
        for i in range(len(origBytes)):
            assert origBytes[i] == newBytes[i], text + " byte[" + str(i) + "]"
