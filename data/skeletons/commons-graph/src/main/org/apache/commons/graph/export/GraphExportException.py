from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io

# Imports End


class GraphExportException(Exception):

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def __init__(
        self,
        cause: BaseException,
        messagePattern: str,
        messageArguments: typing.List[typing.Any],
    ) -> None:
        pass

    # Class Methods End
