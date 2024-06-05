import re
import unittest
from src.main.org.apache.commons.validator.routines.IBANValidator import *
from src.main.org.apache.commons.validator.routines.checkdigit.IBANCheckDigit import *

class IBANValidatorTest(unittest.TestCase):

    __VALIDATOR = IBANValidator.getInstance()

    def __init__(self, methodName='runTest') -> None:
        super().__init__(methodName)
        self.__validIBANFormat = [
            "AD1200012030200359100100",
            "AE070331234567890123456",
            "AL47212110090000000235698741",
            "AT611904300234573201",
            "AZ21NABZ00000000137010001944",
            "BA391290079401028494",
            "BE68539007547034",
            "BG80BNBG96611020345678",
            "BH67BMAG00001299123456",
            "BR1800000000141455123924100C2",
            "BR1800360305000010009795493C1",
            "BR9700360305000010009795493P1",
            "BY13NBRB3600900000002Z00AB00",
            "CH9300762011623852957",
            "CR05015202001026284066",
            "CY17002001280000001200527600",
            "CZ6508000000192000145399",
            "CZ9455000000001011038930",
            "DE89370400440532013000",
            "DK5000400440116243",
            "DO28BAGR00000001212453611324",
            "EE382200221020145685",
            "EG380019000500000000263180002",
            "ES9121000418450200051332",
            "FI2112345600000785",
            "FI5542345670000081",
            "FO6264600001631634",
            "FR1420041010050500013M02606",
            "GB29NWBK60161331926819",
            "GE29NB0000000101904917",
            "GI75NWBK000000007099453",
            "GL8964710001000206",
            "GR1601101250000000012300695",
            "GT82TRAJ01020000001210029690",
            "HR1210010051863000160",
            "HU42117730161111101800000000",
            "IE29AIBK93115212345678",
            "IL620108000000099999999",
            "IQ98NBIQ850123456789012",
            "IS140159260076545510730339",
            "IT60X0542811101000000123456",
            "JO94CBJO0010000000000131000302",
            "KW81CBKU0000000000001234560101",
            "KZ86125KZT5004100100",
            "LB62099900000001001901229114",
            "LC55HEMM000100010012001200023015",
            "LI21088100002324013AA",
            "LT121000011101001000",
            "LU280019400644750000",
            "LV80BANK0000435195001",
            "MC5811222000010123456789030",
            "MD24AG000225100013104168",
            "ME25505000012345678951",
            "MK07250120000058984",
            "MR1300020001010000123456753",
            "MT84MALT011000012345MTLCAST001S",
            "MU17BOMM0101101030300200000MUR",
            "NL91ABNA0417164300",
            "NO9386011117947",
            "PK36SCBL0000001123456702",
            "PL61109010140000071219812874",
            "PS92PALS000000000400123456702",
            "PT50000201231234567890154",
            "QA58DOHB00001234567890ABCDEFG",
            "RO49AAAA1B31007593840000",
            "RS35260005601001611379",
            "SA0380000000608010167519",
            "SC18SSCB11010000000000001497USD",
            "SE4550000000058398257466",
            "SI56191000000123438",
            "SI56263300012039086",
            "SK3112000000198742637541",
            "SM86U0322509800000000270100",
            "ST68000100010051845310112",
            "SV62CENR00000000000000700025",
            "SV43ACAT00000000000000123123",
            "TL380080012345678910157",
            "TN5910006035183598478831",
            "TR330006100519786457841326",
            "UA213223130000026007233566001",
            "UA213996220000026007233566001",
            "VA59001123000012345678",
            "VG96VPVG0000012345678901",
            "XK051212012345678906",
        ]

        self.__invalidIBANFormat = [
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

    
    def test_Valid(self) -> None:
        for f in self.__validIBANFormat:
            self.assertTrue(
                IBANCheckDigit.IBAN_CHECK_DIGIT.isValid(f),
                "Checksum fail: " + f
            )
            self.assertTrue(
                IBANValidatorTest.__VALIDATOR.hasValidator(f),
                "Missing validator: " + f
            )
            self.assertTrue(IBANValidatorTest.__VALIDATOR.isValid(f), f)

    
    def test_InValid(self) -> None:
        for f in self.__invalidIBANFormat:
            self.assertFalse(IBANValidatorTest.__VALIDATOR.isValid(f), f)

    
    def test_Null(self) -> None:
        self.assertFalse(IBANValidatorTest.__VALIDATOR.isValid(None), "isValid(null)")

    
    def test_HasValidator(self) -> None:
        self.assertTrue(IBANValidatorTest.__VALIDATOR.hasValidator("GB"), "GB")
        self.assertFalse(IBANValidatorTest.__VALIDATOR.hasValidator("gb"), "gb")

    
    def test_GetValidator(self) -> None:
        self.assertIsNotNone(IBANValidatorTest.__VALIDATOR.getValidator("GB"), "GB")
        self.assertIsNone(IBANValidatorTest.__VALIDATOR.getValidator("gb"), "gb")

    
    def test_SetDefaultValidator1(self) -> None:
        with self.assertRaises(RuntimeError):
            self.assertIsNotNone(IBANValidatorTest.__VALIDATOR.setValidator1("GB", 15, "GB"))

    
    def test_SetDefaultValidator2(self) -> None:
        with self.assertRaises(RuntimeError):
            self.assertIsNotNone(IBANValidatorTest.__VALIDATOR.setValidator1("GB", -1, "GB"))

    
    def test_SetValidatorLC(self) -> None:
        with self.assertRaises(ValueError):
            validator = IBANValidator.IBANValidator1()
            self.assertIsNotNone(validator.setValidator1("gb", 15, "GB"))

    
    def test_SetValidatorLen7(self) -> None:
        with self.assertRaises(ValueError):
            validator = IBANValidator.IBANValidator1()
            self.assertIsNotNone(validator.setValidator1("GB", 7, "GB"))

    
    def test_SetValidatorLen35(self) -> None:
        with self.assertRaises(ValueError):
            validator = IBANValidator.IBANValidator1()
            self.assertIsNotNone(validator.setValidator1("GB", 35, "GB"))

    
    def test_SetValidatorLen_1(self) -> None:
        validator = IBANValidator.IBANValidator1()
        self.assertIsNotNone(validator.setValidator1("GB", -1, ""), "should be present")
        self.assertIsNone(validator.setValidator1("GB", -1, ""), "no longer present")

    
    def test_Sorted(self) -> None:
        validator = IBANValidator.IBANValidator1()
        vals = validator.getDefaultValidators()
        self.assertIsNotNone(vals)
        for i in range(1, len(vals)):
            if vals[i].countryCode <= vals[i - 1].countryCode:
                self.fail(
                    "Not sorted: " + vals[i].countryCode + " <= " + vals[i - 1].countryCode
                )

    
    @staticmethod
    def __printEntry(ccode, length, ib, country) -> None:
        fmt = f"\"{ib}\""
        print(f"            new Validator(\"{ccode}\", {length}, {fmt:40}), // {country}")

    
    __IBAN_PART = r"(?:\d+![acn])"  # Assume all parts are fixed length
    __IBAN_PAT = re.compile(
        r"([A-Z]{2})"
        + __IBAN_PART
        + __IBAN_PART
        + __IBAN_PART
        + __IBAN_PART + "?"
        + __IBAN_PART + "?"
        + __IBAN_PART + "?"
        + __IBAN_PART + "?"
    )

    
    @staticmethod
    def __formatToRE(type, len_) -> str:
        ctype = type[0]  # assume type.length() == 1
        if ctype == 'n':
            return rf"\d{{{len_}}}"
        elif ctype == 'a':
            return rf"[A-Z]{{{len_}}}"
        elif ctype == 'c':
            return rf"[A-Z0-9]{{{len_}}}"
        else:
            raise ValueError(f"Unexpected type {type}")

    
    @staticmethod
    def __fmtRE(iban_pat, iban_len) -> str:
        m = IBANValidatorTest.__IBAN_PAT.match(iban_pat)
        if m:
            sb = []
            cc = m.group(1)  # country code
            totalLen = len(cc)
            sb.append(cc)
            len_ = int(m.group(2))  # length of part
            curType = m.group(3)  # part type
            for i in range(4, m.lastindex + 1, 2):
                if m.group(i) is None:  # reached an optional group
                    break
                count = int(m.group(i))
                type = m.group(i + 1)
                if type == curType:  # more of the same type
                    len_ += count
                else:
                    sb.append(IBANValidatorTest.__formatToRE(curType, len_))
                    totalLen += len_
                    curType = type
                    len_ = count
            sb.append(IBANValidatorTest.__formatToRE(curType, len_))
            totalLen += len_
            if iban_len != totalLen:
                raise ValueError(
                    f"IBAN pattern {iban_pat} does not match length {iban_len}")
            return ''.join(sb)
        else:
            raise ValueError(f"Unexpected IBAN pattern {iban_pat}")
