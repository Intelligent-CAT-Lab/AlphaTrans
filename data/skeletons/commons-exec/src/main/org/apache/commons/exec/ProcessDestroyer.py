from __future__ import annotations

# Imports Begin
import io
from abc import ABC

# Imports End


class ProcessDestroyer(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def size(self) -> int:
        pass

    def remove(self, process: subprocess.Popen) -> bool:
        pass

    def add(self, process: subprocess.Popen) -> bool:
        pass

    # Class Methods End
