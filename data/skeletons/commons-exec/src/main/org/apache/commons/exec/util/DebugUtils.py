from __future__ import annotations

# Imports Begin
import io

# Imports End


class DebugUtils:

    # Class Fields Begin
    COMMONS_EXEC_LENIENT: str = None
    COMMONS_EXEC_DEBUG: str = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def isLenientEnabled() -> bool:
        pass

    @staticmethod
    def isDebugEnabled() -> bool:
        pass

    @staticmethod
    def handleException(msg: str, e: Exception) -> None:
        pass

    # Class Methods End
