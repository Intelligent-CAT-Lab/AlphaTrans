from __future__ import annotations
import io
import threading


class InterruptibleReentrantLock:

    __serialVersionUID: int = 1

    def interruptWaiters(self, condition: threading.Condition) -> None:

        # Get all waiting threads
        waiting_threads = self.getWaitingThreads(condition)

        # Interrupt each thread
        for thread in waiting_threads:
            thread.interrupt()

    def __init__(self, fairness: bool) -> None:

        super().__init__(None, threading.RLock())
