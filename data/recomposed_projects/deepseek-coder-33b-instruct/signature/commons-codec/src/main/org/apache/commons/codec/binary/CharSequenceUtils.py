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

        index1 = thisStart
        index2 = start
        tmpLen = length

        while tmpLen > 0:
            c1 = cs[index1]
            index1 += 1
            c2 = substring[index2]
            index2 += 1

            if c1 == c2:
                tmpLen -= 1
                continue

            if not ignoreCase:
                return False

            if c1.upper() != c2.upper() and c1.lower() != c2.lower():
                return False

            tmpLen -= 1

        return True
