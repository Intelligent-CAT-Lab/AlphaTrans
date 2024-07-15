from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.GraphException import *


class NotEnoughColorsException(GraphException):

    __serialVersionUID: int = -8782950517745777605

    def __init__(self, colors: typing.Set[typing.Any]) -> None:
        super().__init__(
            format(
                "Input color set %s has not enough colors to color the given graph",
                colors,
            ),
            None,
            None,
        )
