from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.language.bm.Rule import *
import io

# Imports End


class Rule1(Rule):

    # Class Fields Begin
    __pat: str = None
    __lCon: str = None
    __rCon: str = None
    __ph: PhonemeExpr = None
    __myLine: int = None
    __loc: str = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def __init__(
        self, pat: str, lCon: str, rCon: str, ph: PhonemeExpr, cLine: int, location: str
    ) -> None:
        pass

    # Class Methods End
