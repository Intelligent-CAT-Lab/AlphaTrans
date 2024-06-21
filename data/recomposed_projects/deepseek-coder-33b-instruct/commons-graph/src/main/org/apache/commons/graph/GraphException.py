from __future__ import annotations
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

        if cause is not None:
            message = self.format(messagePattern, arguments)
        else:
            message = None

        super().__init__(message, cause)
