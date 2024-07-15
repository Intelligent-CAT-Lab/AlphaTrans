from __future__ import annotations
import time
import re
import io


class MoneyFormatException(RuntimeError):

    __serialVersionUID: int = 87533576

    def rethrowIOException(self) -> None:

        if isinstance(self.getCause(), io.IOException):
            raise self.getCause()

    @staticmethod
    def MoneyFormatException1(message: str) -> MoneyFormatException:
        return MoneyFormatException(message, None)

    def __init__(self, message: str, cause: BaseException) -> None:
        super().__init__(message, cause)
