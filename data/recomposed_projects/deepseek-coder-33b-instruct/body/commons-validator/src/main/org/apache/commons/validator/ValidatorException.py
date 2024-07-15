from __future__ import annotations
import re
import io


class ValidatorException(Exception):

    __serialVersionUID: int = 1025759372615616964

    @staticmethod
    def ValidatorException1() -> ValidatorException:
        return ValidatorException(None)

    def __init__(self, message: str) -> None:
        super().__init__(message)
