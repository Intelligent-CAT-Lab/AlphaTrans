from __future__ import annotations
import time
import re
import io
import typing
from typing import *


class GraphException(RuntimeError):

    __serialVersionUID: int = 6356965258279945475

    def __init__(
        self,
        messagePattern: str,
        cause: BaseException,
        arguments: typing.List[typing.Any],
    ) -> None:

        # Python does not have a direct equivalent to Java's String.format() method.
        # Instead, we can use the str.format() method or f-strings (formatted string literals)
        # Here, we use f-strings for simplicity
        message = messagePattern.format(*arguments) if cause is not None else None

        super().__init__(message, cause)
