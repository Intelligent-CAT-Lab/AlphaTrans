from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.Hex import *
import typing
from typing import *
import io

# Imports End


class Digest:

    # Class Fields Begin
    __algorithm: str = None
    __args: typing.List[typing.List[str]] = None
    __inputs: typing.List[typing.List[str]] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def __println1(self, prefix: str, digest: typing.List[int], fileName: str) -> None:
        pass

    def __println0(self, prefix: str, digest: typing.List[int]) -> None:
        pass

    def __init__(self, args: typing.List[typing.List[str]]) -> None:
        pass

    # Class Methods End
