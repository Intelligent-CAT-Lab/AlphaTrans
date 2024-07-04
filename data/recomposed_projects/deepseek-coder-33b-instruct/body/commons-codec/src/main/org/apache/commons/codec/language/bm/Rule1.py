from __future__ import annotations
import re
from io import StringIO
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

        sb = io.StringIO()
        sb.write("Rule")
        sb.write("{line=")
        sb.write(str(self.__myLine))
        sb.write(", loc='")
        sb.write(self.__loc)
        sb.write("'")
        sb.write(", pat='")
        sb.write(self.__pat)
        sb.write("'")
        sb.write(", lcon='")
        sb.write(self.__lCon)
        sb.write("'")
        sb.write(", rcon='")
        sb.write(self.__rCon)
        sb.write("'")
        sb.write("}")
        return sb.getvalue()

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
