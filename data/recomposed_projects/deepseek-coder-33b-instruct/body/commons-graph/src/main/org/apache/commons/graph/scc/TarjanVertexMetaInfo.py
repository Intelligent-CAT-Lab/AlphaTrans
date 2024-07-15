from __future__ import annotations
import re
import io


class TarjanVertexMetaInfo:

    __lowLink: int = -1
    __index: int = -1
    __UNDEFINED: int = -1

    def setLowLink(self, lowLink: int) -> None:
        self.__lowLink = lowLink

    def setIndex(self, index: int) -> None:
        self.__index = index

    def hasUndefinedIndex(self) -> bool:
        return self.__UNDEFINED == self.__index

    def getLowLink(self) -> int:
        return self.__lowLink

    def getIndex(self) -> int:
        return self.__index
