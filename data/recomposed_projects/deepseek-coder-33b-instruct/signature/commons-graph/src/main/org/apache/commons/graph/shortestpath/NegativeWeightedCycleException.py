from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.GraphException import *


class NegativeWeightedCycleException(GraphException):

    __serialVersionUID: int = 3196711750285223435

    def __init__(
        self,
        messagePattern: str,
        cause: BaseException,
        arguments: typing.List[typing.Any],
    ) -> None:
        super().__init__(messagePattern, cause, arguments)
