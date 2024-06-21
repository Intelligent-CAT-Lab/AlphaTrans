from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *


class ToStringConverter(ABC):

    def convertToString(self, object: typing.Any) -> str:

        return str(object)
