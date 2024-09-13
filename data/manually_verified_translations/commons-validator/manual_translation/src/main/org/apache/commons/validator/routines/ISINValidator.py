from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.validator.routines.CodeValidator import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISINCheckDigit import *


class ISINValidator:

    __checkCountryCode: bool = False

    __SPECIALS: typing.List[str] = ["EZ", "XS"]

    __CCODES: typing.List[str] = ['AW', 'AF', 'AO', 'AI', 'AX', 'AL',
        'AD', 'AE', 'AR', 'AM', 'AS', 'AQ', 'TF', 'AG', 'AU', 'AT', 'AZ', 'BI', 'BE',
        'BJ', 'BQ', 'BF', 'BD', 'BG', 'BH', 'BS', 'BA', 'BL', 'BY', 'BZ', 'BM', 'BO',
        'BR', 'BB', 'BN', 'BT', 'BV', 'BW', 'CF', 'CA', 'CC', 'CH', 'CL', 'CN', 'CI',
        'CM', 'CD', 'CG', 'CK', 'CO', 'KM', 'CV', 'CR', 'CU', 'CW', 'CX', 'KY', 'CY',
        'CZ', 'DE', 'DJ', 'DM', 'DK', 'DO', 'DZ', 'EC', 'EG', 'ER', 'EH', 'ES', 'EE',
        'ET', 'FI', 'FJ', 'FK', 'FR', 'FO', 'FM', 'GA', 'GB', 'GE', 'GG', 'GH', 'GI',
        'GN', 'GP', 'GM', 'GW', 'GQ', 'GR', 'GD', 'GL', 'GT', 'GF', 'GU', 'GY', 'HK',
        'HM', 'HN', 'HR', 'HT', 'HU', 'ID', 'IM', 'IN', 'IO', 'IE', 'IR', 'IQ', 'IS',
        'IL', 'IT', 'JM', 'JE', 'JO', 'JP', 'KZ', 'KE', 'KG', 'KH', 'KI', 'KN', 'KR',
        'KW', 'LA', 'LB', 'LR', 'LY', 'LC', 'LI', 'LK', 'LS', 'LT', 'LU', 'LV', 'MO',
        'MF', 'MA', 'MC', 'MD', 'MG', 'MV', 'MX', 'MH', 'MK', 'ML', 'MT', 'MM', 'ME',
        'MN', 'MP', 'MZ', 'MR', 'MS', 'MQ', 'MU', 'MW', 'MY', 'YT', 'NA', 'NC', 'NE',
        'NF', 'NG', 'NI', 'NU', 'NL', 'NO', 'NP', 'NR', 'NZ', 'OM', 'PK', 'PA', 'PN',
        'PE', 'PH', 'PW', 'PG', 'PL', 'PR', 'KP', 'PT', 'PY', 'PS', 'PF', 'QA', 'RE',
        'RO', 'RU', 'RW', 'SA', 'SD', 'SN', 'SG', 'GS', 'SH', 'SJ', 'SB', 'SL', 'SV',
        'SM', 'SO', 'PM', 'RS', 'SS', 'ST', 'SR', 'SK', 'SI', 'SE', 'SZ', 'SX', 'SC',
        'SY', 'TC', 'TD', 'TG', 'TH', 'TJ', 'TK', 'TM', 'TL', 'TO', 'TT', 'TN', 'TR',
        'TV', 'TW', 'TZ', 'UG', 'UA', 'UM', 'UY', 'US', 'UZ', 'VA', 'VC', 'VE', 'VG',
        'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'ZA', 'ZM', 'ZW']

    __ISIN_VALIDATOR_TRUE: ISINValidator = None
    __ISIN_VALIDATOR_FALSE: ISINValidator = None
    __ISIN_REGEX: str = "([A-Z]{2}[A-Z0-9]{9}[0-9])"
    __VALIDATOR = CodeValidator.CodeValidator4(__ISIN_REGEX, 12, ISINCheckDigit.ISIN_CHECK_DIGIT)
    __serialVersionUID: int = -5964391439144260936

    def run_static_init():
        ISINValidator.__SPECIALS.sort()
        ISINValidator.__CCODES.sort()

    @staticmethod
    def initialize_fields() -> None:
        ISINValidator.__ISIN_VALIDATOR_TRUE: ISINValidator = ISINValidator(True)

        ISINValidator.__ISIN_VALIDATOR_FALSE: ISINValidator = ISINValidator(False)

    def validate(self, code: str) -> typing.Any:

        validate = self.__VALIDATOR.validate(code)
        if validate is not None and self.__checkCountryCode:
            return self.__checkCode(code[:2]) and validate
        return validate

    def isValid(self, code: str) -> bool:

        valid = self.__VALIDATOR.isValid(code)
        if valid and self.__checkCountryCode:
            return self.__checkCode(code[:2])
        return valid

    @staticmethod
    def getInstance(checkCountryCode: bool) -> ISINValidator:
        return (
            ISINValidator.__ISIN_VALIDATOR_TRUE
            if checkCountryCode
            else ISINValidator.__ISIN_VALIDATOR_FALSE
        )

    def __checkCode(self, code: str) -> bool:
        return code in self.__CCODES or code in self.__SPECIALS

    def __init__(self, checkCountryCode: bool) -> None:
        self.__checkCountryCode = checkCountryCode


ISINValidator.run_static_init()

ISINValidator.initialize_fields()
