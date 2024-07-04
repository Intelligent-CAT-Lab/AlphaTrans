from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *


class FromStringConverter(ABC):

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:

        # Here, you need to implement the logic to convert the string to the desired class type.
        # For example, if the class is int, you can use int(str) to convert the string to an integer.
        # Similarly, for other classes, you can use appropriate conversion methods.
        # For simplicity, I'll use int(str) as an example.

        if cls == int:
            return int(str)
        elif cls == float:
            return float(str)
        elif cls == str:
            return str
        else:
            raise ValueError(f"Unsupported class type: {cls}")
