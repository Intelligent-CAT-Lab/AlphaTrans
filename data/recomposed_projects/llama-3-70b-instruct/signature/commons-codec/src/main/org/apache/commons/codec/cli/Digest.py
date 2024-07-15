from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.binary.Hex import *


class Digest:

    __inputs: typing.List[str] = None

    __args: typing.List[str] = None

    __algorithm: str = ""

    def toString(self) -> str:
        return f"{super().toString()} {self.__args}"

    def __println1(self, prefix: str, digest: typing.List[int], fileName: str) -> None:
        print(
            prefix
            + Hex.encodeHexString0(digest)
            + (fileName if fileName != None else "")
        )

    def __println0(self, prefix: str, digest: typing.List[int]) -> None:
        self.__println1(prefix, digest, None)

    def __init__(self, args: typing.List[str]) -> None:

        pass  # LLM could not translate this method
