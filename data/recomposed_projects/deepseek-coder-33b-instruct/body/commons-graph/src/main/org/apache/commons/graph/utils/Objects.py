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
                hash(obj) if obj is not None else 0
            )
        return result

    @staticmethod
    def eq(o1: typing.Any, o2: typing.Any) -> bool:
        return o1 == o2

    def __init__(self) -> None:
        pass
