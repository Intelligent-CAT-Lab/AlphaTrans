from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *


class ToStringConverter(ABC):

    def convertToString(self, object: typing.Any) -> str:

        if isinstance(object, str):
            return object
        elif isinstance(object, int) or isinstance(object, float):
            return str(object)
        elif isinstance(object, list):
            return ", ".join(map(str, object))
        elif isinstance(object, dict):
            return ", ".join(f"{k}: {v}" for k, v in object.items())
        else:
            return str(object)
