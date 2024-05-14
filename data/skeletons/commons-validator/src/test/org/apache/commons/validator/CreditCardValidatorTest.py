# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
from src.main.org.apache.commons.validator.routines.CreditCardValidator import *
from src.main.org.apache.commons.validator.routines.CodeValidator import *
from src.main.org.apache.commons.validator.CreditCardValidator import *
import typing

# Imports End


class CreditCardValidatorTest(TestCase):

    # Class Fields Begin
    __VALID_VISA: str = None
    __VALID_SHORT_VISA: str = None
    __VALID_AMEX: str = None
    __VALID_MASTERCARD: str = None
    __VALID_DISCOVER: str = None
    __VALID_DINERS: str = None
    # Class Fields End

    # Class Methods Begin
    def testAddAllowedCardType(self) -> None:
        pass

    def testIsValid(self) -> None:
        pass

    def __init__(self, name: str) -> None:
        pass

    # Class Methods End


class DinersClub(CreditCardType):

    # Class Fields Begin
    __PREFIX: str = None
    # Class Fields End

    # Class Methods Begin
    def matches(self, card: str) -> bool:
        pass

    # Class Methods End
