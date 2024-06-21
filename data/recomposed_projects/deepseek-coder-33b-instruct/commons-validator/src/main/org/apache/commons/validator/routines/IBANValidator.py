from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.validator.ValidatorResources import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.IBANCheckDigit import *


class Validator:

    lengthOfIBAN: int = None
    validator: RegexValidator = None
    countryCode: str = None

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

    DEFAULT_IBAN_VALIDATOR: IBANValidator = IBANValidator()
    __DEFAULT_FORMATS: typing.List[Validator] = (
        None  # LLM could not translate this field
    )
    __formatValidators: typing.Dict[str, Validator] = None

    def setValidator1(self, countryCode: str, length: int, format: str) -> Validator:

        if self == IBANValidator.DEFAULT_IBAN_VALIDATOR:
            raise RuntimeError("The singleton validator cannot be modified")

        if length < 0:
            return self.__formatValidators.pop(countryCode, None)

        return self.setValidator0(Validator(countryCode, length, format))

    def setValidator0(self, validator: Validator) -> Validator:

        if self == IBANValidator.DEFAULT_IBAN_VALIDATOR:
            raise RuntimeError("The singleton validator cannot be modified")

        self.__formatValidators[validator.countryCode] = validator
        return validator

    def getValidator(self, code: str) -> Validator:

        if code is None or len(code) < 2:  # ensure we can extract the code
            return None
        key = code[0:2]
        return self.__formatValidators.get(key)

    def getDefaultValidators(self) -> typing.List[Validator]:

        return self.__DEFAULT_FORMATS.copy()

    def hasValidator(self, code: str) -> bool:

        return self.getValidator(code) is not None

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

    def __createValidators(
        self, formatMap: typing.List[Validator]
    ) -> typing.Dict[str, Validator]:
        pass

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
