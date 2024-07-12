from __future__ import annotations
import re
import io


class EncoderException(Exception):

    __serialVersionUID: int = 1

    def __init__(self, message: str, cause: BaseException) -> None:
        super().__init__(message, cause)
