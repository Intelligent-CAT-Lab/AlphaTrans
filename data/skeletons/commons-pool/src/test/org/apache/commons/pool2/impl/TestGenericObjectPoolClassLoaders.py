from __future__ import annotations

# Imports Begin
import urllib
import typing
from typing import *
import io

# Imports End


class CustomClassLoader:

    # Class Fields Begin
    __n: int = None
    # Class Fields End

    # Class Methods Begin
    def findResource(self, name: str) -> typing.Union[
        urllib.parse.ParseResult,
        urllib.parse.SplitResult,
        urllib.parse.DefragResult,
        str,
    ]:
        pass

    def __init__(self, n: int) -> None:
        pass

    # Class Methods End


class TestGenericObjectPoolClassLoaders:

    # Class Fields Begin
    __BASE_URL: typing.Union[
        urllib.parse.ParseResult,
        urllib.parse.SplitResult,
        urllib.parse.DefragResult,
        str,
    ] = None
    # Class Fields End

    # Class Methods Begin
    # Class Methods End
