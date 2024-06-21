from __future__ import annotations
import io


class MoneyFormatException(RuntimeError):

    __serialVersionUID: int = 87533576

    def rethrowIOException(self) -> None:

        if isinstance(self.__cause__, io.UnsupportedOperation):
            raise self.__cause__

    @staticmethod
    def MoneyFormatException1(message: str) -> MoneyFormatException:

        return MoneyFormatException(message, None)

    def __init__(self, message: str, cause: BaseException) -> None:

        super().__init__(message, cause)
