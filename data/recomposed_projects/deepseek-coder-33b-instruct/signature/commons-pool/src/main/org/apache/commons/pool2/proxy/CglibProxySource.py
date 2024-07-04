from __future__ import annotations
import re
import io
import typing
from typing import *


class CglibProxySource:

    __superclass: typing.Type[typing.Any] = None

    def toString(self) -> str:
        return f"CglibProxySource [superclass={self.__superclass}]"

    def __init__(self, superclass: typing.Type[typing.Any]) -> None:
        self.__superclass = superclass
