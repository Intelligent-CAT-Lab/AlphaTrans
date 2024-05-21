from __future__ import annotations

# Imports Begin
import io
from abc import ABC

# Imports End


class KFactorBuilder(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def withKFactor(self, kFactor: int) -> None:
        pass

    def withDefaultKFactor(self) -> None:
        pass

    # Class Methods End
