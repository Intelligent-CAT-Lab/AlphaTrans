from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.CalendarValidator import *
from src.test.org.apache.commons.validator.routines.AbstractCalendarValidatorTest import *
from src.main.org.apache.commons.validator.routines.AbstractCalendarValidator import *
import datetime
import typing
from typing import *
import io

# Imports End


class AbstractCalendarValidator:

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:
        pass

    # Class Methods End


class CalendarValidatorTest(AbstractCalendarValidatorTest):

    # Class Fields Begin
    __DATE_2005_11_23: int = None
    __TIME_12_03_45: int = None
    __calValidator: CalendarValidator = None
    # Class Fields End

    # Class Methods Begin
    def testFormat(self) -> None:
        pass

    def _setUp(self) -> None:
        pass

    def testAdjustToTimeZone(self) -> None:
        pass

    def testDateTimeStyle(self) -> None:
        pass

    def testCompare(self) -> None:
        pass

    def testCalendarValidatorMethods(self) -> None:
        pass

    def __init__(self, name: str) -> None:
        pass

    # Class Methods End
