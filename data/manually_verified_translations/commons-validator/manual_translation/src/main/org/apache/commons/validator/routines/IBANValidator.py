from __future__ import annotations
import time
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

    def __init__(self, cc: str, len_: int, format_: str) -> None:

        if not (len(cc) == 2 and cc[0].isupper() and cc[1].isupper()):
            raise ValueError(
                "Invalid country Code; must be exactly 2 upper-case characters"
            )
        if len_ > self.__MAX_LEN or len_ < self.__MIN_LEN:
            raise ValueError(
                "Invalid length parameter, must be in range "
                + str(self.__MIN_LEN)
                + " to "
                + str(self.__MAX_LEN)
                + " inclusive: "
                + str(len_)
            )
        if not format_.startswith(cc):
            raise ValueError(
                "countryCode '" + cc + "' does not agree with format: " + format_
            )
        self.countryCode = cc
        self.lengthOfIBAN = len_
        self.validator = RegexValidator.RegexValidator3(format_)


class IBANValidator:

    DEFAULT_IBAN_VALIDATOR: IBANValidator = None
    __DEFAULT_FORMATS: typing.List[Validator] = [
        Validator("AD", 24, "AD\\d{10}[A-Z0-9]{12}"), # Andorra
        Validator("AE", 23, "AE\\d{21}"), # United Arab Emirates (The)
        Validator("AL", 28, "AL\\d{10}[A-Z0-9]{16}"), # Albania
        Validator("AT", 20, "AT\\d{18}"), # Austria
        Validator("AZ", 28, "AZ\\d{2}[A-Z]{4}[A-Z0-9]{20}"), # Azerbaijan
        Validator("BA", 20, "BA\\d{18}"), # Bosnia and Herzegovina
        Validator("BE", 16, "BE\\d{14}"), # Belgium
        Validator("BG", 22, "BG\\d{2}[A-Z]{4}\\d{6}[A-Z0-9]{8}"), # Bulgaria
        Validator("BH", 22, "BH\\d{2}[A-Z]{4}[A-Z0-9]{14}"), # Bahrain
        Validator("BR", 29, "BR\\d{25}[A-Z]{1}[A-Z0-9]{1}"), # Brazil
        Validator("BY", 28, "BY\\d{2}[A-Z0-9]{4}\\d{4}[A-Z0-9]{16}"), # Republic of Belarus
        Validator("CH", 21, "CH\\d{7}[A-Z0-9]{12}"), # Switzerland
        Validator("CR", 22, "CR\\d{20}"), # Costa Rica
        Validator("CY", 28, "CY\\d{10}[A-Z0-9]{16}"), # Cyprus
        Validator("CZ", 24, "CZ\\d{22}"), # Czechia
        Validator("DE", 22, "DE\\d{20}"), # Germany
        Validator("DK", 18, "DK\\d{16}"), # Denmark
        Validator("DO", 28, "DO\\d{2}[A-Z0-9]{4}\\d{20}"), # Dominican Republic
        Validator("EE", 20, "EE\\d{18}"), # Estonia
        Validator("EG", 29, "EG\\d{27}"), # Egypt
        Validator("ES", 24, "ES\\d{22}"), # Spain
        Validator("FI", 18, "FI\\d{16}"), # Finland
        Validator("FO", 18, "FO\\d{16}"), # Faroe Islands
        Validator("FR", 27, "FR\\d{12}[A-Z0-9]{11}\\d{2}"), # France
        Validator("GB", 22, "GB\\d{2}[A-Z]{4}\\d{14}"), # United Kingdom
        Validator("GE", 22, "GE\\d{2}[A-Z]{2}\\d{16}"), # Georgia
        Validator("GI", 23, "GI\\d{2}[A-Z]{4}[A-Z0-9]{15}"), # Gibraltar
        Validator("GL", 18, "GL\\d{16}"), # Greenland
        Validator("GR", 27, "GR\\d{9}[A-Z0-9]{16}"), # Greece
        Validator("GT", 28, "GT\\d{2}[A-Z0-9]{24}"), # Guatemala
        Validator("HR", 21, "HR\\d{19}"), # Croatia
        Validator("HU", 28, "HU\\d{26}"), # Hungary
        Validator("IE", 22, "IE\\d{2}[A-Z]{4}\\d{14}"), # Ireland
        Validator("IL", 23, "IL\\d{21}"), # Israel
        Validator("IQ", 23, "IQ\\d{2}[A-Z]{4}\\d{15}"), # Iraq
        Validator("IS", 26, "IS\\d{24}"), # Iceland
        Validator("IT", 27, "IT\\d{2}[A-Z]{1}\\d{10}[A-Z0-9]{12}"), # Italy
        Validator("JO", 30, "JO\\d{2}[A-Z]{4}\\d{4}[A-Z0-9]{18}"), # Jordan
        Validator("KW", 30, "KW\\d{2}[A-Z]{4}[A-Z0-9]{22}"), # Kuwait
        Validator("KZ", 20, "KZ\\d{5}[A-Z0-9]{13}"), # Kazakhstan
        Validator("LB", 28, "LB\\d{6}[A-Z0-9]{20}"), # Lebanon
        Validator("LC", 32, "LC\\d{2}[A-Z]{4}[A-Z0-9]{24}"), # Saint Lucia
        Validator("LI", 21, "LI\\d{7}[A-Z0-9]{12}"), # Liechtenstein
        Validator("LT", 20, "LT\\d{18}"), # Lithuania
        Validator("LU", 20, "LU\\d{5}[A-Z0-9]{13}"), # Luxembourg
        Validator("LV", 21, "LV\\d{2}[A-Z]{4}[A-Z0-9]{13}"), # Latvia
        Validator("MC", 27, "MC\\d{12}[A-Z0-9]{11}\\d{2}"), # Monaco
        Validator("MD", 24, "MD\\d{2}[A-Z0-9]{20}"), # Moldova
        Validator("ME", 22, "ME\\d{20}"), # Montenegro
        Validator("MK", 19, "MK\\d{5}[A-Z0-9]{10}\\d{2}"), # Macedonia
        Validator("MR", 27, "MR\\d{25}"), # Mauritania
        Validator("MT", 31, "MT\\d{2}[A-Z]{4}\\d{5}[A-Z0-9]{18}"), # Malta
        Validator("MU", 30, "MU\\d{2}[A-Z]{4}\\d{19}[A-Z]{3}"), # Mauritius
        Validator("NL", 18, "NL\\d{2}[A-Z]{4}\\d{10}"), # Netherlands (The)
        Validator("NO", 15, "NO\\d{13}"), # Norway
        Validator("PK", 24, "PK\\d{2}[A-Z]{4}[A-Z0-9]{16}"), # Pakistan
        Validator("PL", 28, "PL\\d{26}"), # Poland
        Validator("PS", 29, "PS\\d{2}[A-Z]{4}[A-Z0-9]{21}"), # Palestine, State of
        Validator("PT", 25, "PT\\d{23}"), # Portugal
        Validator("QA", 29, "QA\\d{2}[A-Z]{4}[A-Z0-9]{21}"), # Qatar
        Validator("RO", 24, "RO\\d{2}[A-Z]{4}[A-Z0-9]{16}"), # Romania
        Validator("RS", 22, "RS\\d{20}"), # Serbia
        Validator("SA", 24, "SA\\d{4}[A-Z0-9]{18}"), # Saudi Arabia
        Validator("SC", 31, "SC\\d{2}[A-Z]{4}\\d{20}[A-Z]{3}"), # Seychelles
        Validator("SE", 24, "SE\\d{22}"), # Sweden
        Validator("SI", 19, "SI\\d{17}"), # Slovenia
        Validator("SK", 24, "SK\\d{22}"), # Slovakia
        Validator("SM", 27, "SM\\d{2}[A-Z]{1}\\d{10}[A-Z0-9]{12}"), # San Marino
        Validator("ST", 25, "ST\\d{23}"), # Sao Tome and Principe
        Validator("SV", 28, "SV\\d{2}[A-Z]{4}\\d{20}"), # El Salvador
        Validator("TL", 23, "TL\\d{21}"), # Timor-Leste
        Validator("TN", 24, "TN\\d{22}"), # Tunisia
        Validator("TR", 26, "TR\\d{8}[A-Z0-9]{16}"), # Turkey
        Validator("UA", 29, "UA\\d{8}[A-Z0-9]{19}"), # Ukraine
        Validator("VA", 22, "VA\\d{20}"), # Vatican City State
        Validator("VG", 24, "VG\\d{2}[A-Z]{4}\\d{16}"), # Virgin Islands
        Validator("XK", 20, "XK\\d{18}"), # Kosovo
    ]

    __formatValidators: typing.Dict[str, Validator] = None

    @staticmethod
    def initialize_fields() -> None:
        IBANValidator.DEFAULT_IBAN_VALIDATOR: IBANValidator = (
            IBANValidator.IBANValidator1()
        )

    def setValidator1(self, countryCode: str, length: int, format_: str) -> Validator:
        if self == self.DEFAULT_IBAN_VALIDATOR:
            raise RuntimeError("The singleton validator cannot be modified")
        if length < 0:
            return self.__formatValidators.pop(countryCode, None)
        return self.setValidator0(Validator(countryCode, length, format_))

    def setValidator0(self, validator: Validator) -> Validator:
        if self == self.DEFAULT_IBAN_VALIDATOR:
            raise RuntimeError("The singleton validator cannot be modified")
        return self.__formatValidators.put(validator.countryCode, validator)

    def getValidator(self, code: str) -> Validator:

        if code is None or len(code) < 2:  # ensure we can extract the code
            return None

        key = code[0:2]

        return self.__formatValidators.get(key)

    def getDefaultValidators(self) -> typing.List[Validator]:
        return list(self.__DEFAULT_FORMATS)

    def hasValidator(self, code: str) -> bool:

        if code is None or len(code) < 2:  # ensure we can extract the code
            return False

        key = code[0:2]

        return self.__formatValidators.get(key) is not None

    def isValid(self, code: str) -> bool:

        formatValidator = self.getValidator(code)
        if (
            formatValidator is None
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
        m = {}
        for v in formatMap:
            m[v.countryCode] = v
        return m


IBANValidator.initialize_fields()
