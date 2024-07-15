from __future__ import annotations
import re
import io


class CharSequenceUtils:

    @staticmethod
    def regionMatches(
        cs: str,
        ignoreCase: bool,
        thisStart: int,
        substring: str,
        start: int,
        length: int,
    ) -> bool:
        if isinstance(cs, str) and isinstance(substring, str):
            return (
                cs[thisStart : thisStart + length].casefold()
                == substring[start : start + length].casefold()
                if ignoreCase
                else cs[thisStart : thisStart + length]
                == substring[start : start + length]
            )
        index1 = thisStart
        index2 = start
        tmpLen = length
        while tmpLen > 0:
            c1 = cs[index1]
            c2 = substring[index2]
            if c1 == c2:
                index1 += 1
                index2 += 1
                tmpLen -= 1
                continue
            if not ignoreCase:
                return False
            if c1.upper() != c2.upper() and c1.lower() != c2.lower():
                return False
            index1 += 1
            index2 += 1
            tmpLen -= 1
        return True
