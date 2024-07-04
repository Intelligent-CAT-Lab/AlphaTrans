from __future__ import annotations
import re
import io
import numbers
import typing
from typing import *


class Objects:

    @staticmethod
    def hash(
        initialNonZeroOddNumber: int,
        multiplierNonZeroOddNumber: int,
        objs: typing.List[typing.Any],
    ) -> int:

        result = initialNonZeroOddNumber
        for obj in objs:
            result = multiplierNonZeroOddNumber * result + (
                obj.hashCode() if obj is not None else 0
            )
        return result

    @staticmethod
    def eq(o1: typing.Any, o2: typing.Any) -> bool:
        return o1 != None if o1 is not None else o2 is None

    def __init__(self) -> None:
        pass
