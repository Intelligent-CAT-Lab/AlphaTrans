from __future__ import annotations

# Imports Begin
import io

# Imports End


class TarjanVertexMetaInfo:

    # Class Fields Begin
    __UNDEFINED: int = None
    __index: int = None
    __lowLink: int = None
    # Class Fields End

    # Class Methods Begin
    def setLowLink(self, lowLink: int) -> None:
        pass

    def setIndex(self, index: int) -> None:
        pass

    def hasUndefinedIndex(self) -> bool:
        pass

    def getLowLink(self) -> int:
        pass

    def getIndex(self) -> int:
        pass

    # Class Methods End
