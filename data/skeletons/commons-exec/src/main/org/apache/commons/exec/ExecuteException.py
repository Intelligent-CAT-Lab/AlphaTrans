from __future__ import annotations

# Imports Begin
import io

# Imports End


class ExecuteException:

    # Class Fields Begin
    __serialVersionUID: int = None
    __exitValue: int = None
    # Class Fields End

    # Class Methods Begin
    def getExitValue(self) -> int:
        pass

    def __init__(self, message: str, exitValue: int, cause: BaseException) -> None:
        pass

    # Class Methods End
