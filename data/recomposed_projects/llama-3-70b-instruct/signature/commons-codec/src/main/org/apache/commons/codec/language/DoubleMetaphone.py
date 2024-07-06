from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class DoubleMetaphoneResult:

    __maxLength: int = 0

    __alternate: str = ""
    __primary: str = ""

    def isComplete(self) -> bool:
        return (
            self.__primary.length() >= self.__maxLength
            and self.__alternate.length() >= self.__maxLength
        )

    def getAlternate(self) -> str:
        return self.__alternate

    def getPrimary(self) -> str:
        return self.__primary

    def appendAlternate1(self, value: str) -> None:
        addChars = self.__maxLength - len(self.__alternate)
        if len(value) <= addChars:
            self.__alternate += value
        else:
            self.__alternate += value[0:addChars]

    def appendPrimary1(self, value: str) -> None:
        addChars = self.__maxLength - len(self.__primary)
        if len(value) <= addChars:
            self.__primary += value
        else:
            self.__primary += value[0:addChars]

    def append3(self, primary: str, alternate: str) -> None:
        self.appendPrimary1(primary)
        self.appendAlternate1(alternate)

    def append2(self, value: str) -> None:
        self.appendPrimary1(value)
        self.appendAlternate1(value)

    def appendAlternate0(self, value: str) -> None:
        if len(self.__alternate) < self.__maxLength:
            self.__alternate += value

    def appendPrimary0(self, value: str) -> None:
        if len(self.__primary) < self.__maxLength:
            self.__primary += value

    def append1(self, primary: str, alternate: str) -> None:
        self.appendPrimary0(primary)
        self.appendAlternate0(alternate)

    def append0(self, value: str) -> None:
        self.appendPrimary0(value)
        self.appendAlternate0(value)

    def __init__(self, maxLength: int) -> None:
        self.__maxLength = maxLength


class DoubleMetaphone(StringEncoder):

    __maxCodeLen: int = 4
    __L_T_K_S_N_M_B_Z: typing.List[str] = ["L", "T", "K", "S", "N", "M", "B", "Z"]
    __ES_EP_EB_EL_EY_IB_IL_IN_IE_EI_ER: typing.List[str] = [
        "ES",
        "EP",
        "EB",
        "EL",
        "EY",
        "IB",
        "IL",
        "IN",
        "IE",
        "EI",
        "ER",
    ]
    __L_R_N_M_B_H_F_V_W_SPACE: typing.List[str] = [
        "L",
        "R",
        "N",
        "M",
        "B",
        "H",
        "F",
        "V",
        "W",
        " ",
    ]
    __SILENT_START: typing.List[str] = ["GN", "KN", "PN", "WR", "PS"]
    __VOWELS: str = "AEIOUY"

    @staticmethod
    def _contains(
        value: str, start: int, length: int, criteria: typing.List[str]
    ) -> bool:
        result: bool = False
        if start >= 0 and start + length <= len(value):
            target: str = value[start : start + length]

            for element in criteria:
                if target == element:
                    result = True
                    break
        return result

    def _charAt(self, value: str, index: int) -> str:
        if index < 0 or index >= len(value):
            return chr(0)
        return value[index]

    def setMaxCodeLen(self, maxCodeLen: int) -> None:
        self.__maxCodeLen = maxCodeLen

    def getMaxCodeLen(self) -> int:
        return self.__maxCodeLen

    def isDoubleMetaphoneEqual1(
        self, value1: str, value2: str, alternate: bool
    ) -> bool:
        return StringUtils.equals(
            self.doubleMetaphone1(value1, alternate),
            self.doubleMetaphone1(value2, alternate),
        )

    def isDoubleMetaphoneEqual0(self, value1: str, value2: str) -> bool:
        return self.isDoubleMetaphoneEqual1(value1, value2, False)

    def encode1(self, value: str) -> str:
        return self.doubleMetaphone0(value)

    def encode0(self, obj: typing.Any) -> typing.Any:
        if not isinstance(obj, str):
            raise EncoderException(
                "DoubleMetaphone encode parameter is not of type String", None
            )
        return self.doubleMetaphone0(obj)

    def doubleMetaphone1(self, value: str, alternate: bool) -> str:
        value = self.__cleanInput(value)
        if value is None:
            return None

        slavoGermanic = self.__isSlavoGermanic(value)
        index = 0 if self.__isSilentStart(value) else 1

        result = DoubleMetaphoneResult(self.getMaxCodeLen())

        while not result.isComplete() and index <= len(value) - 1:
            if (
                value[index] == "A"
                or value[index] == "E"
                or value[index] == "I"
                or value[index] == "O"
                or value[index] == "U"
                or value[index] == "Y"
            ):
                index = self.__handleAEIOUY(result, index)
            elif value[index] == "B":
                result.append0("P")
                index = 2 if self._charAt(value, index + 1) == "B" else index + 1
            elif value[index] == "\u00C7":
                result.append0("S")
                index += 1
            elif value[index] == "C":
                index = self.__handleC(value, result, index)
            elif value[index] == "D":
                index = self.__handleD(value, result, index)
            elif value[index] == "F":
                result.append0("F")
                index = 2 if self._charAt(value, index + 1) == "F" else index + 1
            elif value[index] == "G":
                index = self.__handleG(value, result, index, slavoGermanic)
            elif value[index] == "H":
                index = self.__handleH(value, result, index)
            elif value[index] == "J":
                index = self.__handleJ(value, result, index, slavoGermanic)
            elif value[index] == "K":
                result.append0("K")
                index = 2 if self._charAt(value, index + 1) == "K" else index + 1
            elif value[index] == "L":
                index = self.__handleL(value, result, index)
            elif value[index] == "M":
                result.append0("M")
                index = 2 if self.__conditionM0(value, index) else index + 1
            elif value[index] == "N":
                result.append0("N")
                index = 2 if self._charAt(value, index + 1) == "N" else index + 1
            elif value[index] == "\u00D1":
                result.append0("N")
                index += 1
            elif value[index] == "P":
                index = self.__handleP(value, result, index)
            elif value[index] == "Q":
                result.append0("K")
                index = 2 if self._charAt(value, index + 1) == "Q" else index + 1
            elif value[index] == "R":
                index = self.__handleR(value, result, index, slavoGermanic)
            elif value[index] == "S":
                index = self.__handleS(value, result, index, slavoGermanic)
            elif value[index] == "T":
                index = self.__handleT(value, result, index)
            elif value[index] == "V":
                result.append0("F")
                index = 2 if self._charAt(value, index + 1) == "V" else index + 1
            elif value[index] == "W":
                index = self.__handleW(value, result, index)
            elif value[index] == "X":
                index = self.__handleX(value, result, index)
            elif value[index] == "Z":
                index = self.__handleZ(value, result, index, slavoGermanic)
            else:
                index += 1

        return result.getAlternate() if alternate else result.getPrimary()

    def doubleMetaphone0(self, value: str) -> str:
        return self.doubleMetaphone1(value, False)

    def __init__(self) -> None:
        self.__maxLength = 4

    def __cleanInput(self, input: str) -> str:
        if input is None:
            return None
        input = input.strip()
        if input == "":
            return None
        return input.upper()

    def __isSilentStart(self, value: str) -> bool:
        result: bool = False
        for element in self.__SILENT_START:
            if value.startswith(element):
                result = True
                break
        return result

    def __isVowel(self, ch: str) -> bool:
        return self.__VOWELS.find(ch) != -1

    def __isSlavoGermanic(self, value: str) -> bool:
        return (
            value.find("W") > -1
            or value.find("K") > -1
            or value.find("CZ") > -1
            or value.find("WITZ") > -1
        )

    def __conditionM0(self, value: str, index: int) -> bool:
        if self._charAt(value, index + 1) == "M":
            return True
        return self._contains(value, index - 1, 3, ["UMB"]) and (
            (index + 1) == len(value) - 1 or self._contains(value, index + 2, 2, ["ER"])
        )

    def __conditionL0(self, value: str, index: int) -> bool:
        if index == len(value) - 3 and self._contains(
            value, index - 1, 4, ["ILLO", "ILLA", "ALLE"]
        ):
            return True
        return (
            self._contains(value, len(value) - 2, 2, ["AS", "OS"])
            or self._contains(value, len(value) - 1, 1, ["A", "O"])
        ) and self._contains(value, index - 1, 4, ["ALLE"])

    def __conditionCH1(self, value: str, index: int) -> bool:
        return (
            (
                self._contains(value, 0, 4, ["VAN ", "VON "])
                or self._contains(value, 0, 3, ["SCH"])
            )
            or self._contains(value, index - 2, 6, ["ORCHES", "ARCHIT", "ORCHID"])
            or self._contains(value, index + 2, 1, ["T", "S"])
            or (
                (
                    self._contains(value, index - 1, 1, ["A", "O", "U", "E"])
                    or index == 0
                )
                and (
                    self._contains(value, index + 2, 1, self.__L_R_N_M_B_H_F_V_W_SPACE)
                    or index + 1 == len(value) - 1
                )
            )
        )

    def __conditionCH0(self, value: str, index: int) -> bool:
        if index != 0:
            return False
        if not self._contains(
            value, index + 1, 5, ["HARAC", "HARIS"]
        ) and not self._contains(value, index + 1, 3, ["HOR", "HYM", "HIA", "HEM"]):
            return False
        return not self._contains(value, 0, 5, ["CHORE"])

    def __conditionC0(self, value: str, index: int) -> bool:
        if self._contains(value, index, 4, ["CHIA"]):
            return True
        if index <= 1:
            return False
        if self.__isVowel(self._charAt(value, index - 2)):
            return False
        if not self._contains(value, index - 1, 3, ["ACH"]):
            return False
        c = self._charAt(value, index + 2)
        return (c != "I" and c != "E") or self._contains(
            value, index - 2, 6, ["BACHER", "MACHER"]
        )

    def __handleZ(
        self, value: str, result: DoubleMetaphoneResult, index: int, slavoGermanic: bool
    ) -> int:
        if self._charAt(value, index + 1) == "H":
            result.append0("J")
            index += 2
        else:
            if self._contains(value, index + 1, 2, ["ZO", "ZI", "ZA"]) or (
                slavoGermanic and (index > 0 and self._charAt(value, index - 1) != "T")
            ):
                result.append3("S", "TS")
            else:
                result.append0("S")
            index = self._charAt(value, index + 1) == "Z" and index + 2 or index + 1
        return index

    def __handleX(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:
        if index == 0:
            result.append0("S")
            index += 1
        else:
            if not (
                (index == len(value) - 1)
                and (
                    self._contains(value, index - 3, 3, ["IAU", "EAU"])
                    or self._contains(value, index - 2, 2, ["AU", "OU"])
                )
            ):
                result.append2("KS")
            index = (
                index + 2
                if self._contains(value, index + 1, 1, ["C", "X"])
                else index + 1
            )
        return index

    def __handleW(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:
        if self._contains(value, index, 2, ["WR"]):
            result.append0("R")
            index += 2
        elif index == 0 and (
            self.__isVowel(self._charAt(value, index + 1))
            or self._contains(value, index, 2, ["WH"])
        ):
            if self.__isVowel(self._charAt(value, index + 1)):
                result.append1("A", "F")
            else:
                result.append0("A")
            index += 1
        elif (
            (index == len(value) - 1 and self.__isVowel(self._charAt(value, index - 1)))
            or self._contains(value, index - 1, 5, ["EWSKI", "EWSKY", "OWSKI", "OWSKY"])
            or self._contains(value, 0, 3, ["SCH"])
        ):
            result.appendAlternate0("F")
            index += 1
        elif self._contains(value, index, 4, ["WICZ", "WITZ"]):
            result.append3("TS", "FX")
            index += 4
        else:
            index += 1
        return index

    def __handleT(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:
        if self._contains(value, index, 4, ["TION"]):
            result.append0("X")
            index += 3
        elif self._contains(value, index, 3, ["TIA", "TCH"]):
            result.append0("X")
            index += 3
        elif self._contains(value, index, 2, ["TH"]) or self._contains(
            value, index, 3, ["TTH"]
        ):
            if (
                self._contains(value, index + 2, 2, ["OM", "AM"])
                or self._contains(value, 0, 4, ["VAN ", "VON "])
                or self._contains(value, 0, 3, ["SCH"])
            ):
                result.append0("T")
            else:
                result.append1("0", "T")
            index += 2
        else:
            result.append0("T")
            index = (
                index + 2
                if self._contains(value, index + 1, 1, ["T", "D"])
                else index + 1
            )
        return index

    def __handleSC(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:

        pass  # LLM could not translate this method

    def __handleS(
        self, value: str, result: DoubleMetaphoneResult, index: int, slavoGermanic: bool
    ) -> int:
        if self._contains(value, index - 1, 3, ["ISL", "YSL"]):
            index += 1
        elif index == 0 and self._contains(value, index, 5, ["SUGAR"]):
            result.append1("X", "S")
            index += 1
        elif self._contains(value, index, 2, ["SH"]):
            if self._contains(value, index + 1, 4, ["HEIM", "HOEK", "HOLM", "HOLZ"]):
                result.append0("S")
            else:
                result.append0("X")
            index += 2
        elif self._contains(value, index, 3, ["SIO", "SIA"]) or self._contains(
            value, index, 4, ["SIAN"]
        ):
            if slavoGermanic:
                result.append0("S")
            else:
                result.append1("S", "X")
            index += 3
        elif (
            index == 0 and self._contains(value, index + 1, 1, ["M", "N", "L", "W"])
        ) or self._contains(value, index + 1, 1, ["Z"]):
            result.append1("S", "X")
            index = self._contains(value, index + 1, 1, ["Z"]) * 2 + index + 1
        elif self._contains(value, index, 2, ["SC"]):
            index = self.__handleSC(value, result, index)
        else:
            if index == len(value) - 1 and self._contains(
                value, index - 2, 2, ["AI", "OI"]
            ):
                result.appendAlternate0("S")
            else:
                result.append0("S")
            index = self._contains(value, index + 1, 1, ["S", "Z"]) * 2 + index + 1
        return index

    def __handleR(
        self, value: str, result: DoubleMetaphoneResult, index: int, slavoGermanic: bool
    ) -> int:
        if (
            index == len(value) - 1
            and not slavoGermanic
            and self._contains(value, index - 2, 2, ["IE"])
            and not self._contains(value, index - 4, 2, ["ME", "MA"])
        ):
            result.appendAlternate0("R")
        else:
            result.append0("R")
        return index + 2 if self._charAt(value, index + 1) == "R" else index + 1

    def __handleP(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:

        pass  # LLM could not translate this method

    def __handleL(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:

        pass  # LLM could not translate this method

    def __handleJ(
        self, value: str, result: DoubleMetaphoneResult, index: int, slavoGermanic: bool
    ) -> int:

        pass  # LLM could not translate this method

    def __handleH(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:

        pass  # LLM could not translate this method

    def __handleGH(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:
        if index > 0 and not self.__isVowel(self._charAt(value, index - 1)):
            result.append0("K")
            index += 2
        elif index == 0:
            if self._charAt(value, index + 2) == "I":
                result.append0("J")
            else:
                result.append0("K")
            index += 2
        elif (
            (index > 1 and self._contains(value, index - 2, 1, ["B", "H", "D"]))
            or (index > 2 and self._contains(value, index - 3, 1, ["B", "H", "D"]))
            or (index > 3 and self._contains(value, index - 4, 1, ["B", "H"]))
        ):
            index += 2
        else:
            if (
                index > 2
                and self._charAt(value, index - 1) == "U"
                and self._contains(value, index - 3, 1, ["C", "G", "L", "R", "T"])
            ):
                result.append0("F")
            elif index > 0 and self._charAt(value, index - 1) != "I":
                result.append0("K")
            index += 2
        return index

    def __handleG(
        self, value: str, result: DoubleMetaphoneResult, index: int, slavoGermanic: bool
    ) -> int:
        if self._charAt(value, index + 1) == "H":
            index = self.__handleGH(value, result, index)
        elif self._charAt(value, index + 1) == "N":
            if (
                index == 1
                and self.__isVowel(self._charAt(value, 0))
                and not slavoGermanic
            ):
                result.append3("KN", "N")
            elif (
                not self._contains(value, index + 2, 2, "EY")
                and self._charAt(value, index + 1) != "Y"
                and not slavoGermanic
            ):
                result.append3("N", "KN")
            else:
                result.append2("KN")
            index = index + 2
        elif self._contains(value, index + 1, 2, "LI") and not slavoGermanic:
            result.append3("KL", "L")
            index += 2
        elif index == 0 and (
            self._charAt(value, index + 1) == "Y"
            or self._contains(
                value, index + 1, 2, self.__ES_EP_EB_EL_EY_IB_IL_IN_IE_EI_ER
            )
        ):
            result.append1("K", "J")
            index += 2
        elif (
            (
                self._contains(value, index + 1, 2, "ER")
                or self._charAt(value, index + 1) == "Y"
            )
            and not self._contains(value, 0, 6, "DANGER", "RANGER", "MANGER")
            and not self._contains(value, index - 1, 1, "E", "I")
            and not self._contains(value, index - 1, 3, "RGY", "OGY")
        ):
            result.append1("K", "J")
            index += 2
        elif self._contains(value, index + 1, 1, "E", "I", "Y") or self._contains(
            value, index - 1, 4, "AGGI", "OGGI"
        ):
            if (
                self._contains(value, 0, 4, "VAN ", "VON ")
                or self._contains(value, 0, 3, "SCH")
                or self._contains(value, index + 1, 2, "ET")
            ):
                result.append0("K")
            elif self._contains(value, index + 1, 3, "IER"):
                result.append0("J")
            else:
                result.append1("J", "K")
            index += 2
        elif self._charAt(value, index + 1) == "G":
            index += 2
            result.append0("K")
        else:
            index += 1
            result.append0("K")
        return index

    def __handleD(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:
        if self._contains(value, index, 2, ["DG"]):
            if self._contains(value, index + 2, 1, ["I", "E", "Y"]):
                result.append0("J")
                index += 3
            else:
                result.append2("TK")
                index += 2
        elif self._contains(value, index, 2, ["DT", "DD"]):
            result.append0("T")
            index += 2
        else:
            result.append0("T")
            index += 1
        return index

    def __handleCH(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:

        pass  # LLM could not translate this method

    def __handleCC(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:
        if self._contains(value, index + 2, 1, ["I", "E", "H"]) and not self._contains(
            value, index + 2, 2, ["HU"]
        ):
            if (index == 1 and self._charAt(value, index - 1) == "A") or self._contains(
                value, index - 1, 5, ["UCCEE", "UCCES"]
            ):
                result.append2("KS")
            else:
                result.append0("X")
            index += 3
        else:  # Pierce's rule
            result.append0("K")
            index += 2
        return index

    def __handleC(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:

        pass  # LLM could not translate this method

    def __handleAEIOUY(self, result: DoubleMetaphoneResult, index: int) -> int:

        pass  # LLM could not translate this method
