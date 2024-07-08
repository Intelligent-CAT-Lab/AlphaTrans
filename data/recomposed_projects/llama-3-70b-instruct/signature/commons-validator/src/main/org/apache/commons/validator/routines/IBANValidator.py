from __future__ import annotations
import copy
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.validator.ValidatorResources import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.IBANCheckDigit import *


class Validator:

    lengthOfIBAN: int = 0

    validator: RegexValidator = None

    countryCode: str = ""

    __MAX_LEN: int = 34
    __MIN_LEN: int = 8

    def __init__(self, cc: str, len: int, format: str) -> None:
        if not (len(cc) == 2 and cc[0].isupper() and cc[1].isupper()):
            raise ValueError(
                "Invalid country Code; must be exactly 2 upper-case characters"
            )
        if len > self.__MAX_LEN or len < self.__MIN_LEN:
            raise ValueError(
                "Invalid length parameter, must be in range "
                + str(self.__MIN_LEN)
                + " to "
                + str(self.__MAX_LEN)
                + " inclusive: "
                + str(len)
            )
        if not format.startswith(cc):
            raise ValueError(
                "countryCode '" + cc + "' does not agree with format: " + format
            )
        self.countryCode = cc
        self.lengthOfIBAN = len
        self.validator = RegexValidator.RegexValidator3(format)


class IBANValidator:

    DEFAULT_IBAN_VALIDATOR: IBANValidator = None
    __DEFAULT_FORMATS: typing.List[Validator] = None
    __formatValidators: typing.Dict[str, Validator] = None

    @staticmethod
    def initialize_fields() -> None:
        IBANValidator.DEFAULT_IBAN_VALIDATOR: IBANValidator = (
            IBANValidator.IBANValidator1()
        )

        IBANValidator.__DEFAULT_FORMATS: typing.List[Validator] = [
            Validator("AD", 24, "ADd{10}[A-Z0-9]{12}"),
            Validator("AE", 23, "AEd{21}"),
            Validator("AL", 28, "ALd{10}[A-Z0-9]{16}"),
            Validator("AT", 20, "ATd{18}"),
            Validator("AZ", 28, "AZd{2}[A-Z]{4}[A-Z0-9]{20}"),
            Validator("BA", 20, "BAd{18}"),
            Validator("BE", 16, "BEd{14}"),
            Validator("BG", 22, "BGd{2}[A-Z]{4}d{6}[A-Z0-9]{8}"),
            Validator("BH", 22, "BHd{2}[A-Z]{4}[A-Z0-9]{14}"),
            Validator("BR", 29, "BRd{25}[A-Z]{1}[A-Z0-9]{1}"),
            Validator("BY", 28, "BYd{2}[A-Z0-9]{4}d{4}[A-Z0-9]{16}"),
            Validator("CH", 21, "CHd{7}[A-Z0-9]{12}"),
            Validator("CR", 22, "CRd{20}"),
            Validator("CY", 28, "CYd{10}[A-Z0-9]{16}"),
            Validator("CZ", 24, "CZd{22}"),
            Validator("DE", 22, "DEd{20}"),
            Validator("DK", 18, "DKd{16}"),
            Validator("DO", 28, "DOd{2}[A-Z0-9]{4}d{20}"),
            Validator("EE", 20, "EEd{18}"),
            Validator("EG", 29, "EGd{27}"),
            Validator("ES", 24, "ESd{22}"),
            Validator("FI", 18, "FId{16}"),
            Validator("FO", 18, "FOd{16}"),
            Validator("FR", 27, "FRd{12}[A-Z0-9]{11}d{2}"),
            Validator("GB", 22, "GBd{2}[A-Z]{4}d{14}"),
            Validator("GE", 22, "GEd{2}[A-Z]{2}d{16}"),
            Validator("GI", 23, "GId{2}[A-Z]{4}[A-Z0-9]{15}"),
            Validator("GL", 18, "GLd{16}"),
            Validator("GR", 27, "GRd{9}[A-Z0-9]{16}"),
            Validator("GT", 28, "GTd{2}[A-Z0-9]{24}"),
            Validator("HR", 21, "HRd{19}"),
            Validator("HU", 28, "HUd{26}"),
            Validator("IE", 22, "IEd{2}[A-Z]{4}d{14}"),
            Validator("IL", 23, "ILd{21}"),
            Validator("IQ", 23, "IQd{2}[A-Z]{4}d{15}"),
            Validator("IS", 26, "ISd{24}"),
            Validator("IT", 27, "ITd{2}[A-Z]{1}d{10}[A-Z0-9]{12}"),
            Validator("JO", 30, "JOd{2}[A-Z]{4}d{4}[A-Z0-9]{18}"),
            Validator("KW", 30, "KWd{2}[A-Z]{4}[A-Z0-9]{22}"),
            Validator("KZ", 20, "KZd{5}[A-Z0-9]{13}"),
            Validator("LB", 28, "LBd{6}[A-Z0-9]{20}"),
            Validator("LC", 32, "LCd{2}[A-Z]{4}[A-Z0-9]{24}"),
            Validator("LI", 21, "LId{7}[A-Z0-9]{12}"),
            Validator("LT", 20, "LTd{18}"),
            Validator("LU", 20, "LUd{5}[A-Z0-9]{13}"),
            Validator("LV", 21, "LVd{2}[A-Z]{4}[A-Z0-9]{13}"),
            Validator("MC", 27, "MCd{12}[A-Z0-9]{11}d{2}"),
            Validator("MD", 24, "MDd{2}[A-Z0-9]{20}"),
            Validator("ME", 22, "MEd{20}"),
            Validator("MK", 19, "MKd{5}[A-Z0-9]{10}d{2}"),
            Validator("MR", 27, "MRd{25}"),
            Validator("MT", 31, "MTd{2}[A-Z]{4}d{5}[A-Z0-9]{18}"),
            Validator("MU", 30, "MUd{2}[A-Z]{4}d{19}[A-Z]{3}"),
            Validator("NL", 18, "NLd{2}[A-Z]{4}d{10}"),
            Validator("NO", 15, "NOd{13}"),
            Validator("PK", 24, "PKd{2}[A-Z]{4}[A-Z0-9]{16}"),
            Validator("PL", 28, "PLd{26}"),
            Validator("PS", 29, "PSd{2}[A-Z]{4}[A-Z0-9]{21}"),
            Validator("PT", 25, "PTd{23}"),
            Validator("QA", 29, "QAd{2}[A-Z]{4}[A-Z0-9]{21}"),
            Validator("RO", 24, "ROd{2}[A-Z]{4}[A-Z0-9]{16}"),
            Validator("RS", 22, "RSd{20}"),
            Validator("SA", 24, "SAd{4}[A-Z0-9]{18}"),
            Validator("SC", 31, "SCd{2}[A-Z]{4}d{20}[A-Z]{3}"),
            Validator("SE", 24, "SEd{22}"),
            Validator("SI", 19, "SId{17}"),
            Validator("SK", 24, "SKd{22}"),
            Validator("SM", 27, "SMd{2}[A-Z]{1}d{10}[A-Z0-9]{12}"),
            Validator("ST", 25, "STd{23}"),
            Validator("SV", 28, "SVd{2}[A-Z]{4}d{20}"),
            Validator("TL", 23, "TLd{21}"),
            Validator("TN", 24, "TNd{22}"),
            Validator("TR", 26, "TRd{8}[A-Z0-9]{16}"),
            Validator("UA", 29, "UAd{8}[A-Z0-9]{19}"),
            Validator("VA", 22, "VAd{20}"),
            Validator("VG", 24, "VGd{2}[A-Z]{4}d{16}"),
            Validator("XK", 20, "XKd{18}"),
        ]

    def setValidator1(self, countryCode: str, length: int, format: str) -> Validator:
        if self == IBANValidator.DEFAULT_IBAN_VALIDATOR:
            raise RuntimeError("The singleton validator cannot be modified")
        if length < 0:
            return self.__formatValidators.pop(countryCode)
        return self.setValidator0(Validator(countryCode, length, format))

    def setValidator0(self, validator: Validator) -> Validator:
        if self == IBANValidator.DEFAULT_IBAN_VALIDATOR:
            raise RuntimeError("The singleton validator cannot be modified")
        return self.__formatValidators.put(validator.countryCode, validator)

    def getValidator(self, code: str) -> Validator:
        if code is None or len(code) < 2:
            return None
        key = code[0:2]
        return self.__formatValidators.get(key)

    def getDefaultValidators(self) -> typing.List[Validator]:
        return self.__DEFAULT_FORMATS.copy()

    def hasValidator(self, code: str) -> bool:
        return self.getValidator(code) != None

    def isValid(self, code: str) -> bool:
        formatValidator: Validator = self.getValidator(code)
        if (
            formatValidator == None
            or len(code) != formatValidator.lengthOfIBAN
            or not formatValidator.validator.isValid(code)
        ):
            return False
        return IBANCheckDigit.IBAN_CHECK_DIGIT.isValid(code)

    @staticmethod
    def IBANValidator1() -> IBANValidator:
        return IBANValidator(IBANValidator.__DEFAULT_FORMATS)

    def __init__(self, formatMap: typing.List[Validator]) -> None:
        self.__formatValidators = self.__createValidators(formatMap)

    @staticmethod
    def getInstance() -> IBANValidator:
        return IBANValidator.DEFAULT_IBAN_VALIDATOR

    def __createValidators(
        self, formatMap: typing.List[Validator]
    ) -> typing.Dict[str, Validator]:
        m: typing.Dict[str, Validator] = {}
        for v in formatMap:
            m[v.countryCode] = v
        return m


IBANValidator.initialize_fields()
