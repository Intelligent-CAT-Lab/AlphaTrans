from __future__ import annotations
import re
import io
import typing
from typing import *


class GraphExportException(Exception):

    __serialVersionUID: int = 1

    def __init__(
        self,
        cause: BaseException,
        messagePattern: str,
        messageArguments: typing.List[typing.Any],
    ) -> None:
        super().__init__(format(messagePattern, messageArguments), cause)
