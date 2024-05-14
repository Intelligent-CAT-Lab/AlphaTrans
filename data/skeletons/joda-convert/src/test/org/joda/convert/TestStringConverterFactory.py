# Imports Begin
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.MockDistanceStringConverter import *
from src.main.org.joda.convert.TypedStringConverter import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.StringConvert import *
from src.main.org.joda.convert.DistanceMethodMethod import *
import typing

# Imports End


class TestStringConverterFactory:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def test_registerFactory_cannotChangeSingleton(self) -> None:
        pass

    def test_registerFactory_null(self) -> None:
        pass

    def test_registerFactory(self) -> None:
        pass

    def test_constructor_nullInArray(self) -> None:
        pass

    def test_constructor_null(self) -> None:
        pass

    def test_constructor(self) -> None:
        pass

    # Class Methods End


class Factory1(StringConverterFactory):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def findConverter(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:
        pass

    # Class Methods End
