from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import urllib


class CustomClassLoader:

    __n: int = 0

    def findResource(self, name: str) -> typing.Union[
        urllib.parse.ParseResult,
        urllib.parse.SplitResult,
        urllib.parse.DefragResult,
        str,
    ]:

        if not name.endswith(str(self.__n)):
            return None

        return super().findResource(name)

    def __init__(self, n: int) -> None:
        super().__init__([])
        self.__n = n


class TestGenericObjectPoolClassLoaders:

    __BASE_URL: typing.Union[
        urllib.parse.ParseResult,
        urllib.parse.SplitResult,
        urllib.parse.DefragResult,
        str,
    ] = urllib.parse.urlparse("/org/apache/commons/pool2/impl/")
