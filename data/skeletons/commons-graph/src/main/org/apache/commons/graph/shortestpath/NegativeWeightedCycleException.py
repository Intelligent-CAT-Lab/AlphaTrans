from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.GraphException import *
import typing
from typing import *
import io

# Imports End


class NegativeWeightedCycleException(GraphException):

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def __init__(
        self,
        messagePattern: str,
        cause: BaseException,
        arguments: typing.List[typing.Any],
    ) -> None:
        pass

    # Class Methods End
