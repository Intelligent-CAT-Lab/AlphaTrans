from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.validator.routines.IBANValidator import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.IBANCheckDigit import *


class IBANValidatorTest(unittest.TestCase):

    __IBAN_PART: str = "(?:(\\d+)!([acn]))"
    __VALIDATOR: IBANValidator = IBANValidator.getInstance()
    __invalidIBANFormat: typing.List[str] = [
        "",  # empty
        "   ",  # empty
        "A",  # too short
        "AB",  # too short
        "FR1420041010050500013m02606",  # lowercase version
        "MT84MALT011000012345mtlcast001s",  # lowercase version
        "LI21088100002324013aa",  # lowercase version
        "QA58DOHB00001234567890abcdefg",  # lowercase version
        "RO49AAAA1b31007593840000",  # lowercase version
        "LC62HEMM000100010012001200023015",  # wrong in SWIFT
        "BY00NBRB3600000000000Z00AB00",  # Wrong in SWIFT v73
        "ST68000200010192194210112",  # ditto
        "SV62CENR0000000000000700025",  # ditto
    ]
    __validIBANFormat: typing.List[str] = None  # LLM could not translate this field

    __IBAN_PAT: re.Pattern = re.compile(
        "([A-Z]{2})"
        + __IBAN_PART
        + __IBAN_PART
        + __IBAN_PART
        + __IBAN_PART
        + "?"
        + __IBAN_PART
        + "?"
        + __IBAN_PART
        + "?"
        + __IBAN_PART
        + "?"
    )

    def testSorted(self) -> None:

        validator = IBANValidator.IBANValidator1()
        vals = validator.getDefaultValidators()
        assert vals is not None
        for i in range(1, len(vals)):
            if vals[i].countryCode <= vals[i - 1].countryCode:
                self.fail(
                    "Not sorted: "
                    + vals[i].countryCode
                    + " <= "
                    + vals[i - 1].countryCode
                )

    def testSetValidatorLen_1(self) -> None:

        validator = IBANValidator.IBANValidator1()
        self.assertIsNotNone(validator.setValidator1("GB", -1, ""), "should be present")
        self.assertIsNone(validator.setValidator1("GB", -1, ""), "no longer present")

    def testSetValidatorLen35(self) -> None:

        validator = IBANValidator.IBANValidator1()
        with pytest.raises(ValueError):
            assert validator.setValidator1("GB", 35, "GB") is not None

    def testSetValidatorLen7(self) -> None:

        validator = IBANValidator.IBANValidator1()
        with pytest.raises(ValueError):
            assert validator.setValidator1("GB", 7, "GB") is not None

    def testSetValidatorLC(self) -> None:

        validator = IBANValidator.IBANValidator1()
        self.assertIsNotNone(validator.setValidator1("gb", 15, "GB"))

    def testSetDefaultValidator2(self) -> None:

        with pytest.raises(RuntimeError):
            assert self.__VALIDATOR.setValidator1("GB", -1, "GB") is not None

    def testSetDefaultValidator1(self) -> None:

        with pytest.raises(RuntimeError):
            assert self.__VALIDATOR.setValidator1("GB", 15, "GB") is not None

    def testGetValidator(self) -> None:

        self.assertIsNotNone(self.__VALIDATOR.getValidator("GB"))
        self.assertIsNone(self.__VALIDATOR.getValidator("gb"))

    def testHasValidator(self) -> None:

        self.assertTrue(self.__VALIDATOR.hasValidator("GB"))
        self.assertFalse(self.__VALIDATOR.hasValidator("gb"))

    def testNull(self) -> None:
        self.assertFalse(self.__VALIDATOR.isValid(None), "isValid(null)")

    def testInValid(self) -> None:
        for f in self.__invalidIBANFormat:
            self.assertFalse(self.__VALIDATOR.isValid(f), f)

    def testValid(self) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def __fmtRE(iban_pat: str, iban_len: int) -> str:

        m = re.match(IBANValidatorTest.__IBAN_PAT, iban_pat)
        if m:
            sb = []
            cc = m.group(1)  # country code
            totalLen = len(cc)
            sb.append(cc)
            len_part = int(m.group(2))  # length of part
            curType = m.group(3)  # part type
            for i in range(4, m.lastindex + 1, 2):
                if m.group(i) is None:  # reached an optional group
                    break
                count = int(m.group(i))
                type = m.group(i + 1)
                if type == curType:  # more of the same type
                    len_part += count
                else:
                    sb.append(IBANValidatorTest.__formatToRE(curType, len_part))
                    totalLen += len_part
                    curType = type
                    len_part = count
            sb.append(IBANValidatorTest.__formatToRE(curType, len_part))
            totalLen += len_part
            if iban_len != totalLen:
                raise ValueError(
                    "IBAN pattern "
                    + iban_pat
                    + " does not match length "
                    + str(iban_len)
                )
            return "".join(sb)
        else:
            raise ValueError("Unexpected IBAN pattern " + iban_pat)

    @staticmethod
    def __formatToRE(type: str, len: int) -> str:

        ctype = type[0]  # assume len(type) == 1
        if ctype == "n":
            return f"\\d{{{len}}}"
        elif ctype == "a":
            return f"[A-Z]{{{len}}}"
        elif ctype == "c":
            return f"[A-Z0-9]{{{len}}}"
        else:
            raise ValueError(f"Unexpected type {type}")

    @staticmethod
    def __printEntry(ccode: str, length: str, ib: str, country: str) -> None:
        fmt = '"{}"'.format(ib)
        print(
            '            new Validator("{}", {}, {:<40s}), // {}'.format(
                ccode, length, fmt, country
            )
        )
