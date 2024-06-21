from __future__ import annotations
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

        # Python's str.format() method is used to format the messagePattern with the messageArguments
        message = messagePattern.format(*messageArguments)

        # The super() function is used to call the __init__() method of the parent class (Exception)
        super().__init__(message, cause)
