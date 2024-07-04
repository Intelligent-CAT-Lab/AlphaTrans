from __future__ import annotations
import re
import io
import threading


class InterruptibleReentrantLock:

    __serialVersionUID: int = 1

    def interruptWaiters(self, condition: threading.Condition) -> None:

        waiting_threads = self.getWaitingThreads(condition)
        for thread in waiting_threads:
            thread.interrupt()

    def __init__(self, fairness: bool) -> None:
        super().__init__(fairness)
