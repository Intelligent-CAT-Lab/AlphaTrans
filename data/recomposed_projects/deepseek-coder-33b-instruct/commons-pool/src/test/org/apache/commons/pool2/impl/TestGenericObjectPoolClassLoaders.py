from __future__ import annotations
import urllib
import io
import typing
from typing import *


class CustomClassLoader:

    __n: int = None

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

        self.__n = n


class TestGenericObjectPoolClassLoaders:

    __BASE_URL: typing.Union[
        urllib.parse.ParseResult,
        urllib.parse.SplitResult,
        urllib.parse.DefragResult,
        str,
    ] = urllib.parse.urljoin(
        os.path.dirname(__file__), "/org/apache/commons/pool2/impl/"
    )
