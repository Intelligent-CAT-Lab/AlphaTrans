from __future__ import annotations
import re
import io
from src.main.org.apache.commons.codec.language.bm.Rule import *


class Rule1(Rule):

    __loc: str = ""

    __myLine: int = 0

    __ph: PhonemeExpr = None

    __rCon: str = ""

    __lCon: str = ""

    __pat: str = ""

    def toString(self) -> str:
        sb: StringBuilder = StringBuilder()
        sb.append("Rule")
        sb.append("{line=").append(self.__myLine)
        sb.append(", loc='").append(self.__loc).append("'")
        sb.append(", pat='").append(self.__pat).append("'")
        sb.append(", lcon='").append(self.__lCon).append("'")
        sb.append(", rcon='").append(self.__rCon).append("'")
        sb.append("}")
        return sb.toString()

    def __init__(
        self, pat: str, lCon: str, rCon: str, ph: PhonemeExpr, cLine: int, location: str
    ) -> None:
        super().__init__(pat, lCon, rCon, ph)
        self.__pat = pat
        self.__lCon = lCon
        self.__rCon = rCon
        self.__ph = ph
        self.__myLine = cLine
        self.__loc = location
