from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *


class FromStringConverter(ABC):

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:
        return cls(str)
