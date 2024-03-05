# Imports Begin
import os
from abc import ABC

# Imports End


class Closeable(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def isClosed(self) -> bool:

        try:
            self.close()
            return True
        except IOError:
            return False

    def close(self) -> None:

        raise NotImplementedError()

    # Class Methods End
