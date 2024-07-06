from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *


class FileItemHeaders(ABC):

    def getHeaderNames(self) -> typing.Iterator[str]:
        return self.headers.keys()

    def getHeaders(self, name: str) -> typing.Iterator[str]:
        return self.getHeaders(name)

    def getHeader(self, name: str) -> str:
        return self._headers.get(name)
