from __future__ import annotations
import re
import io


class CheckDigitException(Exception):

    __serialVersionUID: int = -3519894732624685477

    @staticmethod
    def CheckDigitException2() -> CheckDigitException:
        return CheckDigitException(None, None)

    @staticmethod
    def CheckDigitException1(msg: str) -> CheckDigitException:
        return CheckDigitException(msg, None)

    def __init__(self, msg: str, cause: BaseException) -> None:
        super().__init__(msg, cause)
