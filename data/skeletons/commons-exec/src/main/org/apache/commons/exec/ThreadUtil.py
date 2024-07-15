from __future__ import annotations

# Imports Begin
import typing
from typing import *
import threading
import io

# Imports End


class ThreadUtil:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def newThread(
        threadFactory: threading.Thread,
        runnable: typing.Callable,
        prefix: str,
        daemon: bool,
    ) -> threading.Thread:
        pass

    # Class Methods End
