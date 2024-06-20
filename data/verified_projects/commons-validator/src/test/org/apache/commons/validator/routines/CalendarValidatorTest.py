import pytest

from src.main.org.apache.commons.validator.routines.AbstractCalendarValidator import *
from src.main.org.apache.commons.validator.routines.CalendarValidator import *
from src.test.org.apache.commons.validator.routines.AbstractCalendarValidatorTest import AbstractCalendarValidatorTest

from locale import setlocale, getlocale, LC_TIME
from datetime import datetime
from zoneinfo import ZoneInfo

class CalendarValidatorTest(AbstractCalendarValidatorTest):

    __DATE_2005_11_23 = 20051123
    __TIME_12_03_45 = 120345
    
    __test__ = True
    
    __calValidator = None

    
    def setUp(self) -> None:
        try:
            super().setUp()
            self.__calValidator = CalendarValidator.CalendarValidator1()
            self._validator = self.__calValidator
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")
    

    @pytest.mark.test
    def testCalendarValidatorMethods(self) -> None:
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
            expected,
            CalendarValidator.getInstance().validate0(defaultVal),
            "validate(A) default"
        )
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate4(localeVal, locale),
            "validate(A) locale"
        )
        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate2(patternVal, pattern),
            "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            CalendarValidator.getInstance()\
                .validate6(germanVal, germanPattern, 'de_DE.UTF-8'),
            "validate(A) both"
        )
        
        self.assertTrue(
            CalendarValidator.getInstance().isValid0(defaultVal),
            "isValid(A) default"
        )
        self.assertTrue(
            CalendarValidator.getInstance().isValid2(localeVal, locale),
            "isValid(A) locale"
        )
        self.assertTrue(
            CalendarValidator.getInstance().isValid1(patternVal, pattern),
            "isValid(A) pattern"
        )
        self.assertTrue(
            CalendarValidator.getInstance()\
                .isValid3(germanVal, germanPattern, 'de_DE.UTF-8'),
            "isValid(A) both"
        )
        
        self.assertIsNone(
            CalendarValidator.getInstance().validate0(XXXX),
            "validate(B) default"
        )
        self.assertIsNone(
            CalendarValidator.getInstance().validate4(XXXX, locale),
            "validate(B) locale"
        )
        self.assertIsNone(
            CalendarValidator.getInstance().validate2(XXXX, pattern),
            "validate(B) pattern"
        )
        self.assertIsNone(
            CalendarValidator.getInstance()\
                .validate6("31 Dec 2005", germanPattern, 'de_DE.UTF-8'),
            "validate(B) both"
        )
        
        self.assertFalse(
            CalendarValidator.getInstance().isValid0(XXXX),
            "isValid(B) default"
        )
        self.assertFalse(
            CalendarValidator.getInstance().isValid2(XXXX, locale),
            "isValid(B) locale"
        )
        self.assertFalse(
            CalendarValidator.getInstance().isValid1(XXXX, pattern),
            "isValid(B) pattern"
        )
        self.assertFalse(
            CalendarValidator.getInstance()\
                .isValid3("31 Dec 2005", germanPattern, 'de_DE.UTF-8'),
            "isValid(B) both"
        )

        defaultZone = ZoneInfo("UTC")
        defaultOffset = datetime.now(defaultZone).utcoffset().total_seconds()
        eetOffset = datetime.now(AbstractCalendarValidatorTest._EET)\
            .utcoffset().total_seconds()

        if defaultOffset == eetOffset:
            zone = AbstractCalendarValidatorTest._EST
        else:
            zone = AbstractCalendarValidatorTest._EET

        expectedZone = self.__createCalendar(zone, 20051231, 0)
        expected = datetime(2005, 12, 31, tzinfo=defaultZone)

        self.assertFalse(
            expected.timestamp() == expectedZone.timestamp(),
            "default/EET same"
        )

        self.assertEqual(
            expectedZone,
            CalendarValidator.getInstance().validate1(defaultVal, zone),
            "validate(C) default"
        )
        self.assertEqual(
            expectedZone,
            CalendarValidator.getInstance().validate5(localeVal, locale, zone),
            "validate(C) locale "
        )
        self.assertEqual(
            expectedZone,
            CalendarValidator.getInstance().validate3(patternVal, pattern, zone),
            "validate(C) pattern"   
        )
        self.assertEqual(
            expectedZone,
            CalendarValidator.getInstance()\
                .validate7(germanVal, germanPattern, 'de_DE.UTF-8', zone),
            "validate(C) both"
        )

    
    @pytest.mark.test
    def testCompare(self) -> None:
        sameTime = 124522
        testDate = 20050823
        diffHour = self._createCalendar(AbstractCalendarValidatorTest._GMT, testDate, 115922)
        diffMin = self._createCalendar(AbstractCalendarValidatorTest._GMT, testDate, 124422)
        diffSec = self._createCalendar(AbstractCalendarValidatorTest._GMT, testDate, 124521)
        
        value = self._createCalendar(AbstractCalendarValidatorTest._GMT, testDate, sameTime)
        cal20050824 = self._createCalendar(
            AbstractCalendarValidatorTest._GMT,
            20050824,
            sameTime
        )
        cal20050822 = self._createCalendar(
            AbstractCalendarValidatorTest._GMT,
            20050822,
            sameTime
        )
        
        cal20050830 = self._createCalendar(
            AbstractCalendarValidatorTest._GMT,
            20050830,
            sameTime
        )
        cal20050816 = self._createCalendar(
            AbstractCalendarValidatorTest._GMT,
            20050816,
            sameTime
        )
        
        cal20050901 = self._createCalendar(
            AbstractCalendarValidatorTest._GMT,
            20050901,
            sameTime
        )
        cal20050801 = self._createCalendar(
            AbstractCalendarValidatorTest._GMT,
            20050801,
            sameTime
        )
        cal20050731 = self._createCalendar(
            AbstractCalendarValidatorTest._GMT,
            20050731,
            sameTime
        )
        
        cal20051101 = self._createCalendar(
            AbstractCalendarValidatorTest._GMT,
            20051101,
            sameTime
        )
        cal20051001 = self._createCalendar(
            AbstractCalendarValidatorTest._GMT,
            20051001,
            sameTime
        )
        cal20050701 = self._createCalendar(
            AbstractCalendarValidatorTest._GMT,
            20050701,
            sameTime
        )
        cal20050630 = self._createCalendar(
            AbstractCalendarValidatorTest._GMT,
            20050630,
            sameTime
        )
        
        cal20060101 = self._createCalendar(
            AbstractCalendarValidatorTest._GMT,
            20060101,
            sameTime
        )
        cal20050101 = self._createCalendar(
            AbstractCalendarValidatorTest._GMT,
            20050101,
            sameTime
        )
        cal20041231 = self._createCalendar(
            AbstractCalendarValidatorTest._GMT,
            20041231,
            sameTime
        )
        
        self.assertEqual(
            1,
            self.__calValidator.compare(value, diffHour, Calendar.HOUR_OF_DAY),
            "hour GT"
        )
        self.assertEqual(
            0,
            self.__calValidator.compare(value, diffMin, Calendar.HOUR_OF_DAY),
            "hour EQ"
        )
        self.assertEqual(
            1, self.__calValidator.compare(value, diffMin, Calendar.MINUTE),
            "mins GT"
        )
        self.assertEqual(
            0,
            self.__calValidator.compare(value, diffSec,Calendar.MINUTE),
            "mins EQ"
        )
        self.assertEqual(
            1,
            self.__calValidator.compare(value, diffSec, Calendar.SECOND),
            "secs GT"
        )
        
        self.assertEqual(-1, self.__calValidator.compareDates(value, cal20050824), "date LT")
        self.assertEqual(0, self.__calValidator.compareDates(value, diffHour), "date EQ")
        self.assertEqual(
            0,
            self.__calValidator.compare(value, diffHour, Calendar.DAY_OF_YEAR),
            "date(B)"
        )
        self.assertEqual(1, self.__calValidator.compareDates(value, cal20050822), "date GT")
        
        self.assertEqual(-1, self.__calValidator.compareWeeks(value, cal20050830), "week LT")
        self.assertEqual(0, self.__calValidator.compareWeeks(value, cal20050824), "week =1")
        self.assertEqual(0, self.__calValidator.compareWeeks(value, cal20050822), "week =2")
        self.assertEqual(
            0,
            self.__calValidator.compare(value, cal20050822, Calendar.WEEK_OF_MONTH),
            "week =3"
        )
        self.assertEqual(
            0,
            self.__calValidator.compareWeeks(value, cal20050822),
            "week =4"
        )
        self.assertEqual(1, self.__calValidator.compareWeeks(value, cal20050816), "week GT")
        
        self.assertEqual(-1, self.__calValidator.compareMonths(value, cal20050901), "mnth LT")
        self.assertEqual(0, self.__calValidator.compareMonths(value, cal20050830), "mnth =1")
        self.assertEqual(0, self.__calValidator.compareMonths(value, cal20050801), "mnth =2")
        self.assertEqual(0, self.__calValidator.compareMonths(value, cal20050816), "mnth =3")
        self.assertEqual(1, self.__calValidator.compareMonths(value, cal20050731), "mnth GT")
        
        self.assertEqual(
            -1,
            self.__calValidator.compareQuarters0(value, cal20051101),
            "qtrA <1"
        )
        self.assertEqual(
            -1,
            self.__calValidator.compareQuarters0(value, cal20051001),
            "qtrA <2"
        )
        self.assertEqual(
            0,
            self.__calValidator.compareQuarters0(value, cal20050901),
            "qtrA =1"
        )
        self.assertEqual(
            0,
            self.__calValidator.compareQuarters0(value, cal20050701),
            "qtrA =2"
        )
        self.assertEqual(
            0,
            self.__calValidator.compareQuarters0(value, cal20050731),
            "qtrA =3"
        )
        self.assertEqual(
            1,
            self.__calValidator.compareQuarters0(value, cal20050630),
            "qtrA GT"
        )
        
        self.assertEqual(
            -1,
            self.__calValidator.compareQuarters1(value, cal20051101, 2),
            "qtrB LT"
        )
        self.assertEqual(
            0,
            self.__calValidator.compareQuarters1(value, cal20051001, 2),
            "qtrB =1"
        )
        self.assertEqual(
            0,
            self.__calValidator.compareQuarters1(value, cal20050901, 2),
            "qtrB =2"
        )
        self.assertEqual(
            1,
            self.__calValidator.compareQuarters1(value, cal20050701, 2),
            "qtrB =3"
        )
        self.assertEqual(
            1,
            self.__calValidator.compareQuarters1(value, cal20050731, 2),
            "qtrB =4"
        )
        self.assertEqual(
            1,
            self.__calValidator.compareQuarters1(value, cal20050630, 2),
            "qtrB GT"
        )
        
        self.assertEqual(-1, self.__calValidator.compareYears(value, cal20060101), "year LT")
        self.assertEqual(0, self.__calValidator.compareYears(value, cal20050101), "year EQ")
        self.assertEqual(1, self.__calValidator.compareYears(value, cal20041231), "year GT")
        
        try:
            self.__calValidator.compare(value, value, -1)
            self.fail("Invalid Compare field - expected IllegalArgumentException to be thrown")
        except ValueError as e:
            self.assertEqual(
                str(e),
                "Invalid field: -1",
                "Invalid Compare field - expected IllegalArgumentException to be thrown"
            )


    @pytest.mark.test
    def testDateTimeStyle(self) -> None:
        origDefault = getlocale(LC_TIME)
        setlocale(LC_TIME, 'en_GB.UTF-8')
        
        dateTimeValidator = CalendarValidatorForTestingDateTimeStyle(
            True,
            DateFormat.SHORT,
            DateFormat.SHORT
        )

        self.assertTrue(
            dateTimeValidator.isValid0("31/12/05 14:23"),
            "validate(A) default"
        )
        self.assertTrue(
            dateTimeValidator.isValid2("12/31/05 2:23 PM", 'en_US.UTF-8'),
            "validate(A) locale "
        )

        setlocale(LC_TIME, origDefault)
    
    @pytest.mark.test
    def testFormat(self) -> None:
        origDefault = getlocale(LC_TIME)
        setlocale(LC_TIME, 'en_GB.UTF-8')

        cal20050101 = self._createCalendar(AbstractCalendarValidatorTest._GMT, 20051231, 11500)
        self.assertIsNone(
            self.__calValidator.format0(None),
            "null"
        )
        self.assertEqual(
            "31/12/05",
            self.__calValidator.format0(cal20050101),
            "default"
        )
        self.assertEqual(
            "12/31/05",
            self.__calValidator.format2(cal20050101, 'en_US.UTF-8'),
            "locale"
        )
        self.assertEqual(
            "2005-12-31 01:15",
            self.__calValidator.format1(cal20050101, "yyyy-MM-dd HH:mm"),
            "patternA"
        )
        self.assertEqual(
            "2005-12-31 GMT",
            self.__calValidator.format1(cal20050101, "yyyy-MM-dd z"),
            "patternB"
        )
        self.assertEqual(
            "31 Dez 2005",
            self.__calValidator.format3(cal20050101, "dd MMM yyyy", 'de_DE.UTF-8'),
            "both"
        )

        self.assertEqual(
            "30/12/05",
            self.__calValidator.format0(cal20050101, AbstractCalendarValidatorTest._EST),
            "EST default"
        )
        self.assertEqual(
            "12/30/05",
            self.__calValidator.format2(
                cal20050101,
                'en_US.UTF-8',
                AbstractCalendarValidatorTest._EST
            ),
            "EST locale"
        )
        self.assertEqual(
            "2005-12-30 20:15",
            self.__calValidator.format1(
                cal20050101,
                "yyyy-MM-dd HH:mm",
                AbstractCalendarValidatorTest._EST
            ),
            "EST patternA"
        )
        self.assertEqual(
            "2005-12-30 EST",
            self.__calValidator.format1(
                cal20050101,
                "yyyy-MM-dd z",
                AbstractCalendarValidatorTest._EST
            ),
            "EST patternB"
        )
        self.assertEqual(
            "30 Dez 2005",
            self.__calValidator.format4(
                cal20050101,
                "dd MMM yyyy",
                'de_DE.UTF-8',
                AbstractCalendarValidatorTest._EST
            ),
            "EST both"
        )

        setlocale(LC_TIME, origDefault)
    

    @pytest.mark.test
    def testAdjustToTimeZone(self) -> None:
        calEST = self._createCalendar(
            AbstractCalendarValidatorTest._EST,
            CalendarValidatorTest.__DATE_2005_11_23,
            CalendarValidatorTest.__TIME_12_03_45
        )
        dateEST = calEST

        calGMT = self._createCalendar(
            AbstractCalendarValidatorTest._GMT,
            CalendarValidatorTest.__DATE_2005_11_23,
            CalendarValidatorTest.__TIME_12_03_45
        )
        dateGMT = calGMT

        calCET = self._createCalendar(
            AbstractCalendarValidatorTest._EET,
            CalendarValidatorTest.__DATE_2005_11_23,
            CalendarValidatorTest.__TIME_12_03_45
        )
        dateCET = calCET

        self.assertFalse(
            dateGMT.timestamp() == dateCET.timestamp(),
            "Check GMT != CET"
        )
        self.assertFalse(
            dateGMT.timestamp() == dateEST.timestamp(),
            "Check GMT != EST"
        )
        self.assertFalse(
            dateCET.timestamp() == dateEST.timestamp(),
            "Check CET != EST"
        )

        CalendarValidator.adjustToTimeZone(calEST, AbstractCalendarValidatorTest._GMT)
        self.assertEqual(
            dateGMT,
            calEST,
            "EST to GMT"
        )
        self.assertFalse(
            dateEST == calEST,
            "Check EST = GMT"
        )
        CalendarValidator.adjustToTimeZone(calEST, AbstractCalendarValidatorTest._EST)
        self.assertEqual(
            dateEST,
            calEST,
            "back to EST"
        )
        self.assertFalse(
            dateGMT == calEST,
            "Check EST != GMT"
        )

        CalendarValidator.adjustToTimeZone(calCET, AbstractCalendarValidatorTest._GMT)
        self.assertEqual(
            dateGMT,
            calCET,
            "CET to GMT"
        )
        self.assertFalse(
            dateCET == calCET,
            "Check CET = GMT"
        )
        CalendarValidator.adjustToTimeZone(calCET, AbstractCalendarValidatorTest._EET)
        self.assertEqual(
            dateCET,
            calCET,
            "back to CET"
        )
        self.assertFalse(
            dateGMT == calCET,
            "Check CET != GMT"
        )

        calUTC = self._createCalendar(
            AbstractCalendarValidatorTest._UTC,
            CalendarValidatorTest.__DATE_2005_11_23,
            CalendarValidatorTest.__TIME_12_03_45
        )
        self.assertTrue(
            AbstractCalendarValidatorTest._GMT\
                .utcoffset(None) == AbstractCalendarValidatorTest\
                ._UTC.utcoffset(None),
            "SAME: UTC = GMT"
        )
        self.assertEqual(
            calUTC,
            calGMT,
            "SAME: Check time (A)"
        )
        self.assertFalse(
            AbstractCalendarValidatorTest._GMT == calUTC.tzinfo,
            "SAME: Check GMT(A)"
        )
        self.assertTrue(
            AbstractCalendarValidatorTest._UTC == calUTC.tzinfo,
            "SAME: Check UTC(A)"
        )
        CalendarValidator.adjustToTimeZone(calUTC, AbstractCalendarValidatorTest._GMT)
        self.assertEqual(
            calUTC,
            calGMT,
            "SAME: Check time (B)"
        )
        self.assertTrue(
            AbstractCalendarValidatorTest._GMT == calUTC.tzinfo,
            "SAME: Check GMT(B)"
        )
        self.assertFalse(
            AbstractCalendarValidatorTest._UTC == calUTC.tzinfo,
            "SAME: Check UTC(B)"
        )


class Calendar:
    HOUR_OF_DAY = 11
    MINUTE = 12
    SECOND = 13
    DAY_OF_YEAR = 6
    WEEK_OF_MONTH = 4


class DateFormat:
    SHORT = 3


class CalendarValidatorForTestingDateTimeStyle(AbstractCalendarValidator):
    def __init__(self, strict, dateStyle, timeStyle):
        super().__init__(strict, dateStyle, timeStyle)
        self.__serialVersionUID = 1

    def processParsedValue(self, value, formatter):
        return value
