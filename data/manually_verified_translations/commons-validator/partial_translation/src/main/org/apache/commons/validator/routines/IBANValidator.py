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
    __DEFAULT_FORMATS: typing.List[Validator] = (
        None  # LLM could not translate this field
    )

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
