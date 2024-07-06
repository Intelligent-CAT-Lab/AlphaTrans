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
        super().__init__(
            format(messagePattern, *arguments) if cause is not None else None, cause
        )
