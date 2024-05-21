from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io

# Imports End


class GraphException(RuntimeError):

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
