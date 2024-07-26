from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *


class FileItemHeaders(ABC):

    def getHeaderNames(self) -> typing.Iterator[str]:
        pass

    def getHeaders(self, name: str) -> typing.Iterator[str]:
        pass

    def getHeader(self, name: str) -> str:
        pass
