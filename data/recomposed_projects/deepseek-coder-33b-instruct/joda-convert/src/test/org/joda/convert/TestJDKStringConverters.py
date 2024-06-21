from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.joda.convert.FromString import *
from src.main.org.joda.convert.JDKStringConverter import *
from src.main.org.joda.convert.RenameHandler import *
from src.test.org.joda.convert.Status import *
from src.main.org.joda.convert.StringConvert import *
from src.main.org.joda.convert.TypedStringConverter import *


class TestJDKStringConverters:

    def test_Enum_withRename(self) -> None:

        test = StringConvert.create().findTypedConverter(Status)
        assert test.convertToString(Status.VALID) == "VALID"
        assert test.convertToString(Status.INVALID) == "INVALID"
        assert test.convertFromString(Status, "VALID") == Status.VALID
        assert test.convertFromString(Status, "INVALID") == Status.INVALID
        try:
            test.convertFromString(Status, "OK")
            assert False
        except RuntimeError:
            pass
        RenameHandler.INSTANCE.renamedEnum("OK", Status.VALID)
        assert test.convertFromString(Status, "OK") == Status.VALID
        assert test.convertFromString(Status, "VALID") == Status.VALID
        assert test.convertFromString(Status, "INVALID") == Status.INVALID

    def test_Enum_invalidConstant(self) -> None:

        test = StringConvert.create().findTypedConverter(RoundingMode)
        try:
            test.convertFromString(RoundingMode, "RUBBISH")
        except Exception as e:
            print(f"Exception occurred: {e}")

    def test_Enum(self) -> None:

        test = StringConvert.create().findTypedConverter(RoundingMode)
        assert RoundingMode == test.getEffectiveType()
        assert "CEILING" == test.convertToString(RoundingMode.CEILING)
        assert RoundingMode.CEILING == test.convertFromString(RoundingMode, "CEILING")

    def test_Calendar_notGregorian(self) -> None:

        class Calendar:
            serialVersionUID = 1

            def roll(self, field: int, up: bool) -> None:
                pass

            def getMinimum(self, field: int) -> int:
                return 0

            def getMaximum(self, field: int) -> int:
                return 0

            def getLeastMaximum(self, field: int) -> int:
                return 0

            def getGreatestMinimum(self, field: int) -> int:
                return 0

            def computeTime(self) -> None:
                pass

            def computeFields(self) -> None:
                pass

            def add(self, field: int, amount: int) -> None:
                pass

        JDKStringConverter.CALENDAR.convertToString(Calendar())

    def test_Calendar_invalidFormat(self) -> None:

        JDKStringConverter.CALENDAR.convertFromString(
            GregorianCalendar, "2010-09-03XXX:34:05.000+02:00[Europe/London]"
        )

    def test_Calendar_invalidLength(self) -> None:

        # The Java code is calling a static method convertFromString on the JDKStringConverter class.
        # In Python, we can call this method directly on the class itself.
        # The method takes two parameters: the class to convert to and the string to convert from.
        # The class to convert to is GregorianCalendar.
        # The string to convert from is "2010-09-03".

        JDKStringConverter.convertFromString(GregorianCalendar, "2010-09-03")

    def test_Calendar(self) -> None:

        test = JDKStringConverter.CALENDAR
        cal = GregorianCalendar(TimeZone.getTimeZone("Europe/Paris"))
        cal.set(2010, 9 - 1, 3, 12, 34, 5)
        cal.set(Calendar.MILLISECOND, 0)
        self.doTest0(test, Calendar, cal, "2010-09-03T12:34:05.000+02:00[Europe/Paris]")

        cal2 = GregorianCalendar(TimeZone.getTimeZone("Europe/Paris"))
        cal2.set(2011, 1 - 1, 4, 12, 34, 5)
        cal2.set(Calendar.MILLISECOND, 0)
        self.doTest0(
            test, Calendar, cal2, "2011-01-04T12:34:05.000+01:00[Europe/Paris]"
        )

    def test_Date_invalidFormat(self) -> None:

        try:
            JDKStringConverter.DATE.convertFromString(
                Date, "2010-09-03XXX:34:05.000+02:00"
            )
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_Date_invalidLength(self) -> None:

        JDKStringConverter.DATE.convertFromString(Date, "2010-09-03")

    def test_Date(self) -> None:

        zone = dt.timezone.get_default()
        try:
            dt.timezone.set_default(dt.timezone(dt.timedelta(hours=2)))
            test = JDKStringConverter.DATE
            self.doTest0(
                test, dt.date, dt.date(2010, 9, 3), "2010-09-03T12:34:05.000+02:00"
            )
            self.doTest0(
                test, dt.date, dt.date(2011, 1, 4), "2011-01-04T12:34:05.000+01:00"
            )
        finally:
            dt.timezone.set_default(zone)

    def test_File(self) -> None:

        test = JDKStringConverter.FILE
        file = File("/path/to/file")
        self.doTest0(test, File, file, str(file))

    def test_InetAddress(self) -> None:

        test = JDKStringConverter.INET_ADDRESS
        self.doTest0(test, InetAddress, InetAddress.getByName("1.2.3.4"), "1.2.3.4")

        obj = InetAddress.getByName("2001:0db8:85a3:0000:0000:8a2e:0370:7334")
        str = test.convertToString(obj)
        assert (
            str == "2001:db8:85a3:0:0:8a2e:370:7334"
            or str == "2001:db8:85a3::8a2e:370:7334"
        )
        assert obj == test.convertFromString(InetAddress, str)
        assert obj == test.convertFromString(
            InetAddress, "2001:db8:85a3:0:0:8a2e:370:7334"
        )
        assert obj == test.convertFromString(
            InetAddress, "2001:db8:85a3::8a2e:370:7334"
        )

    def test_URI(self) -> None:

        test = JDKStringConverter.URI
        self.doTest0(
            test,
            URI,
            URI.create("http://localhost:8080/my/test"),
            "http://localhost:8080/my/test",
        )
        self.doTest0(test, URI, URI.create("/my/test"), "/my/test")
        self.doTest0(test, URI, URI.create("/my/../test"), "/my/../test")
        self.doTest0(test, URI, URI.create("urn:hello"), "urn:hello")

    def test_URL_invalidFormat(self) -> None:

        pass  # LLM could not translate this method

    def test_URL(self) -> None:

        test = JDKStringConverter.URL
        self.doTest0(
            test,
            URL,
            URL("http://localhost:8080/my/test"),
            "http://localhost:8080/my/test",
        )
        self.doTest0(test, URL, URL(None, "ftp:world"), "ftp:world")

    def test_UUID(self) -> None:

        test = JDKStringConverter.UUID
        uuid = uuid.uuid4()
        self.doTest0(test, uuid.UUID, uuid, str(uuid))

    def test_TimeZone(self) -> None:

        test = JDKStringConverter.TIME_ZONE
        self.doTest0(
            test, TimeZone, TimeZone.getTimeZone("Europe/London"), "Europe/London"
        )
        self.doTest0(
            test, TimeZone, TimeZone.getTimeZone("America/New_York"), "America/New_York"
        )

    def test_Currency(self) -> None:

        test = JDKStringConverter.CURRENCY
        self.doTest0(test, Currency, Currency.getInstance("GBP"), "GBP")
        self.doTest0(test, Currency, Currency.getInstance("USD"), "USD")

    def test_Package(self) -> None:

        test = JDKStringConverter.PACKAGE
        self.doTest0(test, Package, Package, "java.util")
        self.doTest0(test, Package, FromString, "org.joda.convert")

    def test_Class_withRename(self) -> None:

        try:
            JDKStringConverter.CLASS.convertFromString(Class, "org.foo.StringConvert")
            self.fail()
        except RuntimeError:
            pass

        RenameHandler.INSTANCE.renamedType("org.foo.StringConvert", StringConvert)

        self.assertEqual(
            StringConvert,
            JDKStringConverter.CLASS.convertFromString(Class, "org.foo.StringConvert"),
        )

    def test_Class_fail(self) -> None:

        JDKStringConverter.CLASS.convertFromString(Class, "RUBBISH")

    def test_Class_array(self) -> None:

        test = JDKStringConverter.CLASS
        self.doTest0(test, Class, bytearray, "[B")
        self.doTest0(
            test, Class, typing.List[FromString], "[Lorg.joda.convert.FromString;"
        )
        self.doTest0(
            test,
            Class,
            typing.List[typing.List[FromString]],
            "[[Lorg.joda.convert.FromString;",
        )

    def test_Class_primitive(self) -> None:

        test = JDKStringConverter.CLASS
        self.doTest0(test, Class, byte, "byte")
        self.doTest0(test, Class, short, "short")
        self.doTest0(test, Class, int, "int")
        self.doTest0(test, Class, long, "long")
        self.doTest0(test, Class, float, "float")
        self.doTest0(test, Class, double, "double")
        self.doTest0(test, Class, bool, "boolean")
        self.doTest0(test, Class, str, "char")
        self.doTest0(test, Class, None, "void")

    def test_Class(self) -> None:

        test = JDKStringConverter.CLASS
        self.doTest0(test, Class, Locale, "java.util.Locale")
        self.doTest0(test, Class, FromString, "org.joda.convert.FromString")

    def test_Locale(self) -> None:

        test = JDKStringConverter.LOCALE
        self.doTest0(test, Locale, Locale("en"), "en")
        self.doTest0(test, Locale, Locale("en", "GB"), "en_GB")
        self.doTest0(test, Locale, Locale("en", "GB", "VARIANT_B"), "en_GB_VARIANT_B")

    def test_AtomicBoolean_fail(self) -> None:

        JDKStringConverter.ATOMIC_BOOLEAN.convertFromString(AtomicBoolean, "RUBBISH")

    def test_AtomicBoolean_false(self) -> None:

        # Create an instance of JDKStringConverter
        test = JDKStringConverter.ATOMIC_BOOLEAN

        # Create an AtomicBoolean object with value False
        obj = AtomicBoolean(False)

        # Assert that the type of the object is AtomicBoolean
        assert test.getType() == AtomicBoolean

        # Assert that the string representation of the object is "false"
        assert test.convertToString(obj) == "false"

        # Convert the string "false" back to an AtomicBoolean object
        back = test.convertFromString(AtomicBoolean, "false")

        # Assert that the value of the AtomicBoolean object is False
        assert back.get() == False

    def test_AtomicBoolean_true(self) -> None:

        # Create an instance of JDKStringConverter
        test = JDKStringConverter.ATOMIC_BOOLEAN

        # Create an AtomicBoolean object with value True
        obj = AtomicBoolean(True)

        # Assert that the type of the object is AtomicBoolean
        assert isinstance(obj, AtomicBoolean)

        # Assert that the type returned by getType method is AtomicBoolean
        assert test.getType() == AtomicBoolean

        # Assert that the string representation of the object is "true"
        assert test.convertToString(obj) == "true"

        # Convert the string "true" back to AtomicBoolean
        back = test.convertFromString(AtomicBoolean, "true")

        # Assert that the type of the converted object is AtomicBoolean
        assert isinstance(back, AtomicBoolean)

        # Assert that the value of the converted object is True
        assert back.value == True

    def test_AtomicInteger(self) -> None:

        from java.util.concurrent.atomic import AtomicInteger

        test = JDKStringConverter.ATOMIC_INTEGER
        obj = AtomicInteger(12)
        assert AtomicInteger == test.getType()
        assert "12" == test.convertToString(obj)
        back = test.convertFromString(AtomicInteger, "12")
        assert 12 == back.get()

    def test_AtomicLong(self) -> None:

        from java.util.concurrent.atomic import AtomicLong

        test = JDKStringConverter.ATOMIC_LONG
        obj = AtomicLong(12)
        assert AtomicLong == test.getType()
        assert "12" == test.convertToString(obj)
        back = test.convertFromString(AtomicLong, "12")
        assert 12 == back.get()

    def test_BigDecimal(self) -> None:

        from decimal import Decimal

        test = JDKStringConverter.BIG_DECIMAL
        self.doTest0(test, Decimal, Decimal("12.23"), "12.23")

    def test_BigInteger(self) -> None:

        test = JDKStringConverter.BIG_INTEGER
        self.doTest0(test, BigInteger, BigInteger.valueOf(12), "12")

    def test_Float(self) -> None:

        test = JDKStringConverter.FLOAT
        self.doTest0(test, float, 12.2, "12.2")

    def test_Double(self) -> None:

        test = JDKStringConverter.DOUBLE
        self.doTest0(test, float, 12.4, "12.4")

    def test_Boolean_fail(self) -> None:

        JDKStringConverter.BOOLEAN.convertFromString(Boolean, "RUBBISH")

    def test_Boolean(self) -> None:

        test = JDKStringConverter.BOOLEAN
        self.doTest0(test, bool, True, "true")
        self.doTest0(test, bool, False, "false")

    def test_byteArray4(self) -> None:

        test = JDKStringConverter.BYTE_ARRAY
        array = bytearray([73, 97, 112, 77])
        str = "SWFwTQ=="
        assert test.getType() == bytearray
        assert test.convertToString(array) == str
        assert test.convertFromString(bytearray, str) == array

    def test_byteArray3(self) -> None:

        test = JDKStringConverter.BYTE_ARRAY
        array = bytearray([77])
        str = "TQ=="
        assert bytearray == test.getType()
        assert str == test.convertToString(array)
        assert array == test.convertFromString(bytearray, str)

    def test_byteArray2(self) -> None:

        test = JDKStringConverter.BYTE_ARRAY
        array = bytearray([77, 97])
        str = "TWE="
        assert bytearray == test.getType()
        assert str == test.convertToString(array)
        assert array == test.convertFromString(bytearray, str)

    def test_byteArray1(self) -> None:

        test = JDKStringConverter.BYTE_ARRAY
        array = bytearray([77, 97, 112])
        str = "TWFw"
        assert bytearray == test.getType()
        assert str == test.convertToString(array)
        assert array == test.convertFromString(bytearray, str)

    def test_Byte(self) -> None:

        test = JDKStringConverter.BYTE
        self.doTest0(test, Byte, Byte.valueOf((12).to_bytes(1, "big")), "12")

    def test_charArray(self) -> None:

        test = JDKStringConverter.CHAR_ARRAY
        array = ["M", "a", "p"]
        str = "Map"
        assert type(char) == test.getType()
        assert str == test.convertToString(array)
        assert array == list(test.convertFromString(char, str))

    def test_Character_fail(self) -> None:

        JDKStringConverter.CHARACTER.convertFromString(Character, "RUBBISH")

    def test_Character(self) -> None:

        test = JDKStringConverter.CHARACTER
        self.doTest0(test, Character, Character.valueOf("a"), "a")
        self.doTest0(test, Character, Character.valueOf("z"), "z")

    def test_Short(self) -> None:

        test = JDKStringConverter.SHORT
        self.doTest0(test, Short, Short.valueOf(12), "12")

    def test_Int(self) -> None:

        test = JDKStringConverter.INTEGER
        self.doTest0(test, int, 12, "12")

    def test_Long(self) -> None:

        test = JDKStringConverter.LONG
        self.doTest0(test, int, 12, "12")

    def test_CharSequence(self) -> None:

        test = JDKStringConverter.CHAR_SEQUENCE
        self.doTest0(test, CharSequence, "Hello", "Hello")
        self.doTest1(test, CharSequence, StringBuffer("Hello"), "Hello", "Hello")
        self.doTest1(test, CharSequence, StringBuilder("Hello"), "Hello", "Hello")

    def test_StringBuilder(self) -> None:

        test = JDKStringConverter.STRING_BUILDER
        obj = io.StringIO("Hello")
        assert isinstance(test.getType(), type)
        assert test.convertToString(obj) == "Hello"
        back = test.convertFromString(io.StringIO, "Hello")
        assert back.getvalue() == "Hello"

    def test_StringBuffer(self) -> None:

        test = JDKStringConverter.STRING_BUFFER
        obj = io.StringIO("Hello")
        assert isinstance(test.getType(), type(io.StringIO))
        assert test.convertToString(obj) == "Hello"
        back = test.convertFromString(io.StringIO, "Hello")
        assert back.getvalue() == "Hello"

    def test_String(self) -> None:

        test = JDKStringConverter.STRING
        self.doTest0(test, str, "Hello", "Hello")

    def doTest1(
        self,
        test: JDKStringConverter,
        cls: typing.Type[typing.Any],
        obj: typing.Any,
        str: str,
        objFromStr: typing.Any,
    ) -> None:

        assertEqual(cls, test.getType())
        assertEqual(str, test.convertToString(obj))
        assertEqual(objFromStr, test.convertFromString(cls, str))

    def doTest0(
        self,
        test: JDKStringConverter,
        cls: typing.Type[typing.Any],
        obj: typing.Any,
        str: str,
    ) -> None:

        self.doTest1(test, cls, obj, str, obj)
