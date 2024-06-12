from src.main.org.apache.commons.validator.routines.DateValidator import *
from src.test.org.apache.commons.validator.routines.AbstractCalendarValidatorTest import AbstractCalendarValidatorTest
from src.main.org.apache.commons.validator.routines.AbstractCalendarValidator import *
import os
from datetime import datetime
from locale import LC_TIME, setlocale
from zoneinfo import ZoneInfo

class DateValidatorTest(AbstractCalendarValidatorTest):

    def __init__(self, methodName='runTest') -> None:
        super().__init__(methodName)
        self.__dateValidator = None

    
    def setUp(self) -> None:
        try:
            super().setUp()
            super().setUpValidator(
                DateValidator.DateValidator1()
            )
            self.__dateValidator = DateValidator.DateValidator1()
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")

    
    def test_LocaleProviders(self) -> None:
        localeProviders = os.getenv('java.locale.providers')
        if localeProviders is not None:
            self.assertTrue(
                localeProviders.startswith('COMPAT'),
                "java.locale.providers must start with COMPAT"
            )
        txt = "3/20/15 10:59:00 PM"
        dateformat = datetime\
            .strptime(txt,'%m/%d/%y %I:%M:%S %p')\
            .replace(tzinfo=ZoneInfo('GMT'))
        date = dateformat
        self.assertIsNotNone(
            date,
            "Date should not be None"
        )

    
    def test_DateValidatorMethods(self) -> None:
        setlocale(LC_TIME, 'en_US.UTF-8')
        locale = 'de_DE.UTF-8'
        pattern = "yyyy-MM-dd"
        patternVal = "2005-12-31"
        germanVal = "31 Dez 2005"
        germanPattern = "dd MMM yyyy"
        localeVal = "31.12.2005"
        defaultVal = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0)

        self.assertEqual(
            DateValidator.getInstance().validate0(defaultVal),
            expected,
            "validate(A) default"
        )
        self.assertEqual(
            DateValidator.getInstance().validate4(localeVal, locale),
            expected,
            "validate(A) locale"
        )
        self.assertEqual(
            DateValidator.getInstance().validate2(patternVal, pattern),
            expected,
            "validate(A) pattern"
        )
        self.assertEqual(
            DateValidator.getInstance().validate6(germanVal, germanPattern, locale),
            expected,
            "validate(A) both"
        )

        self.assertTrue(
            DateValidator.getInstance().isValid0(defaultVal), 
            "isValid(A) default"
        )
        self.assertTrue(
            DateValidator.getInstance().isValid2(localeVal, locale),
            "isValid(A) locale"
        )
        self.assertTrue(
            DateValidator.getInstance().isValid1(patternVal, pattern),
            "isValid(A) pattern"
        )
        self.assertTrue(
            DateValidator.getInstance().isValid3(germanVal, germanPattern, locale),
            "isValid(A) both"
        )

        self.assertIsNone(
            DateValidator.getInstance().validate0(XXXX),
            "validate(B) default"
        )
        self.assertIsNone(
            DateValidator.getInstance().validate4(XXXX, locale),
            "validate(B) locale"
        )
        self.assertIsNone(
            DateValidator.getInstance().validate2(XXXX, pattern),
            "validate(B) pattern"
        )
        self.assertIsNone(
            DateValidator.getInstance().validate6('31 Dec 2005', germanPattern, locale),
            "validate(B) both"
        )

        self.assertFalse(
            DateValidator.getInstance().isValid0(XXXX),
            "isValid(B) default"
        )
        self.assertFalse(
            DateValidator.getInstance().isValid2(XXXX, locale),
            "isValid(B) locale"
        )
        self.assertFalse(
            DateValidator.getInstance().isValid1(XXXX, pattern),
            "isValid(B) pattern"
        )
        self.assertFalse(
            DateValidator.getInstance().isValid3('31 Dec 2005', germanPattern, locale),
            "isValid(B) both"
        )

        now = datetime.now()
        if now.astimezone(AbstractCalendarValidatorTest\
            ._EET).utcoffset() == now\
            .astimezone().utcoffset():
            zone = AbstractCalendarValidatorTest._EST
        else:
            zone = AbstractCalendarValidatorTest._EET
        expectedZone = self._createCalendar(zone, 20051231, 0)
        self.assertNotEqual(
            expected,
            expectedZone,
            "default/zone same " + str(zone)
        )

        self.assertEqual(
            DateValidator.getInstance().validate1(defaultVal, zone),
            expectedZone,
            "validate(C) default"
        )
        self.assertEqual(
            DateValidator.getInstance().validate5(localeVal, locale, zone),
            expectedZone,
            "validate(C) locale"
        )
        self.assertEqual(
            DateValidator.getInstance().validate3(patternVal, pattern, zone),
            expectedZone,
            "validate(C) pattern"
        )
        self.assertEqual(
            DateValidator.getInstance().validate7(germanVal, germanPattern, locale, zone),
            expectedZone,
            "validate(C) both"
        )

    
    def test_Compare(self) -> None:
        sameTime = 124522
        testDate = 20050823
        diffHour = self._createDate(AbstractCalendarValidatorTest._GMT, testDate, 115922)

        value = self._createDate(AbstractCalendarValidatorTest._GMT, testDate, sameTime)
        date20050824 = self._createDate(
            AbstractCalendarValidatorTest._GMT,
            20050824,
            sameTime
        )
        date20050822 = self._createDate(
            AbstractCalendarValidatorTest._GMT,
            20050822,
            sameTime
        )

        date20050830 = self._createDate(
            AbstractCalendarValidatorTest._GMT,
            20050830,
            sameTime
        )
        date20050816 = self._createDate(
            AbstractCalendarValidatorTest._GMT,
            20050816,
            sameTime
        )

        date20050901 = self._createDate(
            AbstractCalendarValidatorTest._GMT,
            20050901,
            sameTime
        )
        date20050801 = self._createDate(
            AbstractCalendarValidatorTest._GMT,
            20050801,
            sameTime
        )
        date20050731 = self._createDate(
            AbstractCalendarValidatorTest._GMT,
            20050731,
            sameTime
        )

        date20051101 = self._createDate(
            AbstractCalendarValidatorTest._GMT,
            20051101,
            sameTime
        )
        date20051001 = self._createDate(
            AbstractCalendarValidatorTest._GMT,
            20051001,
            sameTime
        )
        date20050701 = self._createDate(
            AbstractCalendarValidatorTest._GMT,
            20050701,
            sameTime
        )
        date20050630 = self._createDate(
            AbstractCalendarValidatorTest._GMT,
            20050630,
            sameTime
        )
        date20050110 = self._createDate(
            AbstractCalendarValidatorTest._GMT,
            20050110,
            sameTime
        )

        date20060101 = self._createDate(
            AbstractCalendarValidatorTest._GMT,
            20060101,
            sameTime
        )
        date20050101 = self._createDate(
            AbstractCalendarValidatorTest._GMT,
            20050101,
            sameTime
        )
        date20041231 = self._createDate(
            AbstractCalendarValidatorTest._GMT,
            20041231,
            sameTime
        )

        self.assertEqual(
            self.__dateValidator.compareDates(
                value,
                date20050824,
                AbstractCalendarValidatorTest._GMT
            ),
            -1,
            "date LT"
        )
        self.assertEqual(
            self.__dateValidator.compareDates(
                value,
                diffHour,
                AbstractCalendarValidatorTest._GMT
            ),
            0,
            "date EQ"
        )
        self.assertEqual(
            self.__dateValidator.compareDates(
                value,
                date20050822,
                AbstractCalendarValidatorTest._GMT
            ),
            1,
            "date GT"
        )

        self.assertEqual(
            self.__dateValidator.compareWeeks(
                value,
                date20050830,
                AbstractCalendarValidatorTest._GMT
            ),
            -1,
            "week LT"
        )
        self.assertEqual(
            self.__dateValidator.compareWeeks(
                value,
                date20050824,
                AbstractCalendarValidatorTest._GMT
            ),
            0,
            "week =1"
        )
        self.assertEqual(
            self.__dateValidator.compareWeeks(
                value,
                date20050822,
                AbstractCalendarValidatorTest._GMT
            ),
            0,
            "week =2"
        )
        self.assertEqual(
            self.__dateValidator.compareWeeks(
                value,
                date20050822,
                AbstractCalendarValidatorTest._GMT
            ),
            0,
            "week =3"
        )
        self.assertEqual(
            self.__dateValidator.compareWeeks(
                value,
                date20050816,
                AbstractCalendarValidatorTest._GMT
            ),
            1,
            "week GT"
        )

        self.assertEqual(
            self.__dateValidator.compareMonths(
                value,
                date20050901,
                AbstractCalendarValidatorTest._GMT
            ),
            -1,
            "mnth LT"
        )
        self.assertEqual(
            self.__dateValidator.compareMonths(
                value,
                date20050830,
                AbstractCalendarValidatorTest._GMT
            ),
            0,
            "mnth =1"
        )
        self.assertEqual(
            self.__dateValidator.compareMonths(
                value,
                date20050801,
                AbstractCalendarValidatorTest._GMT
            ),
            0,
            "mnth =2"
        )
        self.assertEqual(
            self.__dateValidator.compareMonths(
                value,
                date20050816,
                AbstractCalendarValidatorTest._GMT
            ),
            0,
            "mnth =3"
        )
        self.assertEqual(
            self.__dateValidator.compareMonths(
                value,
                date20050731,
                AbstractCalendarValidatorTest._GMT
            ),
            1,
            "mnth GT"
        )

        self.assertEqual(
            self.__dateValidator.compareQuarters0(
                value,
                date20051101,
                AbstractCalendarValidatorTest._GMT
            ),
            -1,
            "qtrA <1"
        )
        self.assertEqual(
            self.__dateValidator.compareQuarters0(
                value,
                date20051001,
                AbstractCalendarValidatorTest._GMT
            ),
            -1,
            "qtrA <2"
        )
        self.assertEqual(
            self.__dateValidator.compareQuarters0(
                value,
                date20050901,
                AbstractCalendarValidatorTest._GMT
            ),
            0,
            "qtrA =1"
        )
        self.assertEqual(
            self.__dateValidator.compareQuarters0(
                value,
                date20050701,
                AbstractCalendarValidatorTest._GMT
            ),
            0,
            "qtrA =2"
        )
        self.assertEqual(
            self.__dateValidator.compareQuarters0(
                value,
                date20050731,
                AbstractCalendarValidatorTest._GMT
            ),
            0,
            "qtrA =3"
        )
        self.assertEqual(
            self.__dateValidator.compareQuarters0(
                value,
                date20050630,
                AbstractCalendarValidatorTest._GMT
            ),
            1,
            "qtrA GT"
        )

        self.assertEqual(
            self.__dateValidator.compareQuarters1(
                value,
                date20051101,
                AbstractCalendarValidatorTest._GMT, 2
            ),
            -1,
            "qtrB LT"
        )
        self.assertEqual(
            self.__dateValidator.compareQuarters1(
                value,
                date20051001,
                AbstractCalendarValidatorTest._GMT, 2
            ),
            0,
            "qtrB =1"
        )
        self.assertEqual(
            self.__dateValidator.compareQuarters1(
                value,
                date20050901,
                AbstractCalendarValidatorTest._GMT, 2
            ),
            0,
            "qtrB =2"
        )
        self.assertEqual(
            self.__dateValidator.compareQuarters1(
                value,
                date20050701,
                AbstractCalendarValidatorTest._GMT, 2
            ),
            1,
            "qtrB =3"
        )
        self.assertEqual(
            self.__dateValidator.compareQuarters1(
                value,
                date20050731,
                AbstractCalendarValidatorTest._GMT, 2
            ),
            1,
            "qtrB =4"
        )
        self.assertEqual(
            self.__dateValidator.compareQuarters1(
                value,
                date20050630,
                AbstractCalendarValidatorTest._GMT, 2
            ),
            1,
            "qtrB GT"
        )
        self.assertEqual(
            self.__dateValidator.compareQuarters1(
                value,
                date20050110,
                AbstractCalendarValidatorTest._GMT, 2
            ),
            1,
            "qtrB prev"
        )

        self.assertEqual(
            self.__dateValidator.compareYears(
                value,
                date20060101,
                AbstractCalendarValidatorTest._GMT
            ),
            -1,
            "year LT"
        )
        self.assertEqual(
            self.__dateValidator.compareYears(
                value,
                date20050101,
                AbstractCalendarValidatorTest._GMT
            ),
            0,
            "year EQ"
        )
        self.assertEqual(
            self.__dateValidator.compareYears(
                value,
                date20041231,
                AbstractCalendarValidatorTest._GMT
            ),
            1,
            "year GT"
        )

        sameDayTwoAm = self._createDate(AbstractCalendarValidatorTest._GMT, testDate, 20000)
        self.assertEqual(
            self.__dateValidator.compareDates(
                value,
                date20050824,
                AbstractCalendarValidatorTest._EST
            ),
            -1,
            "date LT"
        )
        self.assertEqual(
            self.__dateValidator.compareDates(
                value,
                diffHour,
                AbstractCalendarValidatorTest._EST
            ),
            0,
            "date EQ"
        )
        self.assertEqual(
            self.__dateValidator.compareDates(
                value,
                sameDayTwoAm,
                AbstractCalendarValidatorTest._EST
            ),
            1,
            "date EQ"
        )
        self.assertEqual(
            self.__dateValidator.compareDates(
                value,
                date20050822,
                AbstractCalendarValidatorTest._EST
            ),
            1,
            "date GT"
        )
