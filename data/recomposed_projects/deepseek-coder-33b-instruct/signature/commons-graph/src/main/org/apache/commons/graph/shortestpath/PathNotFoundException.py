from __future__ import annotations
import re
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.GraphException import *


class PathNotFoundException(GraphException):

    __serialVersionUID: int = 2919520319054603708

    def __init__(self, messagePattern: str, arguments: typing.List[typing.Any]) -> None:
        super().__init__(messagePattern, None, arguments)
