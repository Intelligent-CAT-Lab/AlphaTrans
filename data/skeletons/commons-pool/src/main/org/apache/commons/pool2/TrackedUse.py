# Imports Begin
import datetime
from abc import ABC

# Imports End


class TrackedUse(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getLastUsed(self) -> int:
        pass

    def getLastUsedInstant(self) -> datetime.datetime:
        pass

    # Class Methods End
