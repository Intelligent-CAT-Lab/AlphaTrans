from __future__ import annotations
import io
import typing
from typing import *


class CglibProxySource:

    __superclass: typing.Type[typing.Any] = None

    def toString(self) -> str:

        builder = io.StringIO()
        builder.write("CglibProxySource [superclass=")
        builder.write(str(self.__superclass))
        builder.write("]")
        return builder.getvalue()

    def __init__(self, superclass: typing.Type[typing.Any]) -> None:

        self.__superclass = superclass
