from __future__ import annotations
import re
import io


class IllegalCurrencyException(ValueError):

    __serialVersionUID: int = 1

    def __init__(self, message: str) -> None:
        super().__init__(message)
