# Imports Begin
from abc import ABC

# Imports End


class Closeable(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def isClosed(self) -> bool:
        pass

    def close(self) -> None:
        pass

    # Class Methods End
