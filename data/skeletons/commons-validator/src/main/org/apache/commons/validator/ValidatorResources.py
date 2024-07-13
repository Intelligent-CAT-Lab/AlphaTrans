from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.FormSet import *

# from src.main.org.apache.commons.logging.LogFactory import *
# from src.main.org.apache.commons.logging.Log import *
import logging
import typing
from typing import *
import io

# Imports End


class ValidatorResources:

    # Class Fields Begin
    _defaultFormSet: FormSet = None
    __ARGS_PATTERN: str = None
    __serialVersionUID: int = None
    __VALIDATOR_RULES: str = None
    __REGISTRATIONS: typing.List[typing.List[str]] = None
    __log: logging.Logger = None
    _defaultLocale: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def _buildKey(self, fs: FormSet) -> str:
        pass

    def __init__(self) -> None:
        pass

    def __getLog(self) -> logging.Logger:
        pass

    def __buildLocale(self, lang: str, country: str, variant: str) -> str:
        pass

    # Class Methods End
