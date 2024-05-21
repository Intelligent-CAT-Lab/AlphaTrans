from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.GraphException import *
import typing
from typing import *
import io
import pathlib

# Imports End


class PathNotFoundException(GraphException):

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def __init__(self, messagePattern: str, arguments: typing.List[typing.Any]) -> None:
        pass

    # Class Methods End
