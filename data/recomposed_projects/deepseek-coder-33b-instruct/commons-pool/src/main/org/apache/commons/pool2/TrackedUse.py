from __future__ import annotations
from abc import ABC
import io
import datetime


class TrackedUse(ABC):

    def getLastUsed(self) -> int:

        # The actual implementation of this method depends on the specifics of your application.
        # Here is a placeholder implementation that returns the current time as an integer.
        return int(datetime.datetime.now().timestamp())

    def getLastUsedInstant(self) -> datetime.datetime:

        return datetime.datetime.fromtimestamp(self.getLastUsed() / 1000.0)
