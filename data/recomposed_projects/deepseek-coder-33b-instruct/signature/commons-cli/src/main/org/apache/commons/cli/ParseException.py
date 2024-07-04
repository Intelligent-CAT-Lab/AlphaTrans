from __future__ import annotations
import re
import io


class ParseException(Exception):

    __serialVersionUID: int = 9112808380089253192

    def __init__(self, message: str) -> None:
        super().__init__(message)
