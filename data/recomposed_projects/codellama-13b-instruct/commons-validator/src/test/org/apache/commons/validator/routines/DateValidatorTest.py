# Imports Begin
from src.main.org.apache.commons.validator.routines.DateValidator import *
from src.main.org.apache.commons.validator.routines.AbstractCalendarValidatorTest import *
from src.main.org.apache.commons.validator.routines.AbstractCalendarValidator import *
import unittest
import os

# Imports End


class DateValidatorTest(unittest.TestCase, AbstractCalendarValidatorTest):

    # Class Fields Begin
    __dateValidator: DateValidator = None
    # Class Fields End

    # Class Methods Begin
    def _setUp(self) -> None:

        super().setUp()
        self.__dateValidator = DateValidator.DateValidator1()
        self.validator = self.__dateValidator

    def testCompare(self) -> None:

        pass  # LLM could not translate method body

    def testDateValidatorMethods(self) -> None:

        Locale.setDefault(Locale.US)
        locale = Locale.GERMAN
        pattern = "yyyy-MM-dd"
        patternVal = "2005-12-31"
        germanVal = "31 Dez 2005"
        germanPattern = "dd MMM yyyy"
        localeVal = "31.12.2005"
        defaultVal = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()
        self.assertEqual(
            "validate(A) default",
            expected,
            DateValidator.getInstance().validate0(defaultVal),
        )
        self.assertEqual(
            "validate(A) locale ",
            expected,
            DateValidator.getInstance().validate4(localeVal, locale),
        )
        self.assertEqual(
            "validate(A) pattern",
            expected,
            DateValidator.getInstance().validate2(patternVal, pattern),
        )
        self.assertEqual(
            "validate(A) both",
            expected,
            DateValidator.getInstance().validate6(
                germanVal, germanPattern, Locale.GERMAN
            ),
        )
        self.assertTrue(
            "isValid(A) default", DateValidator.getInstance().isValid0(defaultVal)
        )
        self.assertTrue(
            "isValid(A) locale ",
            DateValidator.getInstance().isValid2(localeVal, locale),
        )
        self.assertTrue(
            "isValid(A) pattern",
            DateValidator.getInstance().isValid1(patternVal, pattern),
        )
        self.assertTrue(
            "isValid(A) both",
            DateValidator.getInstance().isValid3(
                germanVal, germanPattern, Locale.GERMAN
            ),
        )
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX))
        assertNull(
            "validate(B) locale ", DateValidator.getInstance().validate4(XXXX, locale)
        )
        assertNull(
            "validate(B) pattern", DateValidator.getInstance().validate2(XXXX, pattern)
        )
        assertNull(
            "validate(B) both",
            DateValidator.getInstance().validate6(
                "31 Dec 2005", germanPattern, Locale.GERMAN
            ),
        )
        self.assertFalse(
            "isValid(B) default", DateValidator.getInstance().isValid0(XXXX)
        )

    def testLocaleProviders(self) -> None:

        locale_providers = os.environ.get("java.locale.providers")
        if locale_providers is not None:
            assert locale_providers.startswith("COMPAT")
        txt = "3/20/15 10:59:00 PM"
        date_format = DateFormat.getDateTimeInstance(
            DateFormat.SHORT, DateFormat.MEDIUM, Locale.US
        )
        date_format.setTimeZone(TimeZone.getTimeZone("GMT"))
        date = date_format.parse(txt)
        assert date is not None

    def __init__(self, name: str) -> None:

        super().__init__(name)

    # Class Methods End
