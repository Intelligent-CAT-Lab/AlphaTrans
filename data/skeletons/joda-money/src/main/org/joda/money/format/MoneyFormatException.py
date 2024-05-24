from __future__ import annotations

# Imports Begin
import io

# Imports End


class MoneyFormatException(RuntimeError):

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def rethrowIOException(self) -> None:
        pass

    @staticmethod
    def MoneyFormatException1(message: str) -> MoneyFormatException:
        pass

    def __init__(self, message: str, cause: BaseException) -> None:
        pass

    # Class Methods End
