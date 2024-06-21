from __future__ import annotations
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
            if obj is not None:
                result = multiplierNonZeroOddNumber * result + obj.hashCode()
            else:
                result = multiplierNonZeroOddNumber * result
        return result

    @staticmethod
    def eq(o1: typing.Any, o2: typing.Any) -> bool:

        if o1 is not None:
            return o1.equals(o2)
        else:
            return o2 is None

    def __init__(self) -> None:

        pass  # LLM could not translate this method
