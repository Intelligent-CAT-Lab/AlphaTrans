from __future__ import annotations
import time
import re
from abc import ABC
import io
import datetime


class TrackedUse(ABC):

    def getLastUsed(self) -> int:

        # Assuming that the method is implemented in a subclass
        # and returns the last used time as a long integer
        # Here is a placeholder for the actual implementation
        pass

    def getLastUsedInstant(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(self.getLastUsed() / 1000.0)
