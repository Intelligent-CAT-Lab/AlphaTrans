from __future__ import annotations

# Imports Begin
import threading
import io

# Imports End


class InterruptibleReentrantLock:

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def interruptWaiters(self, condition: threading.Condition) -> None:
        pass

    def __init__(self, fairness: bool) -> None:
        pass

    # Class Methods End
