from __future__ import annotations
from abc import ABC
import io


class KFactorBuilder(ABC):

    def withKFactor(self, kFactor: int) -> None:

        pass

    def withDefaultKFactor(self) -> None:

        pass
