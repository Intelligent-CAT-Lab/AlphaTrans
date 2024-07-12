from __future__ import annotations
import re
from abc import ABC
import io


class KFactorBuilder(ABC):

    def withKFactor(self, kFactor: int) -> None:
        self.kFactor = kFactor

    def withDefaultKFactor(self) -> None:
        pass
