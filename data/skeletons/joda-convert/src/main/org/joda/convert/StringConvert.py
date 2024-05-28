from __future__ import annotations

# Imports Begin
from src.main.org.joda.convert.factory.NumericObjectArrayStringConverterFactory import *
from src.main.org.joda.convert.factory.NumericArrayStringConverterFactory import *
from src.main.org.joda.convert.factory.CharObjectArrayStringConverterFactory import *
from src.main.org.joda.convert.factory.ByteObjectArrayStringConverterFactory import *
from src.main.org.joda.convert.factory.BooleanObjectArrayStringConverterFactory import *
from src.main.org.joda.convert.factory.BooleanArrayStringConverterFactory import *
from src.main.org.joda.convert.TypedStringConverter import *
from src.main.org.joda.convert.TypedFromStringConverter import *
from src.main.org.joda.convert.TypedAdapter import *
from src.main.org.joda.convert.TypeStringConverterFactory import *
from src.main.org.joda.convert.ToStringConverter import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.ReflectionStringConverter import *
from src.main.org.joda.convert.MethodFromStringConverter import *
from src.main.org.joda.convert.JDKStringConverter import *
from src.main.org.joda.convert.FromStringConverter import *
from src.main.org.joda.convert.EnumStringConverterFactory import *
from src.main.org.joda.convert.ConstructorFromStringConverter import *
from src.main.org.joda.convert.AnnotationStringConverterFactory import *
import typing
from typing import *
import io

# Imports End


class TypedStringConverter:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getEffectiveType(self) -> typing.Type[typing.Any]:
        pass

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:
        pass

    def convertToString(self, object: typing.Any) -> str:
        pass

    # Class Methods End


class TypedStringConverter:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getEffectiveType(self) -> typing.Type[typing.Any]:
        pass

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:
        pass

    def convertToString(self, object: typing.Any) -> str:
        pass

    # Class Methods End


class StringConvert:

    # Class Fields Begin
    LOG: bool = None
    __CACHED_NULL: TypedStringConverter[typing.Any] = None
    INSTANCE: StringConvert = None
    __factories: typing.List[StringConverterFactory] = None
    __registered: typing.Dict[
        typing.Type[typing.Any], TypedStringConverter[typing.Any]
    ] = None
    __fromStrings: typing.Dict[
        typing.Type[typing.Any], FromStringConverter[typing.Any]
    ] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def findFromStringConverter(
        self, cls: typing.Type[typing.Any]
    ) -> FromStringConverter[typing.Any]:
        pass

    def findTypedConverterNoGenerics(
        self, cls: typing.Type[typing.Any]
    ) -> TypedStringConverter[typing.Any]:
        pass

    def __lookupConverter(
        self, cls: typing.Type[typing.Any]
    ) -> TypedStringConverter[typing.Any]:
        pass

    def __findConverterQuiet(
        self, cls: typing.Type[typing.Any]
    ) -> TypedStringConverter[typing.Any]:
        pass

    @staticmethod
    def loadType(fullName: str) -> typing.Type[typing.Any]:
        pass

    def registerMethodConstructor(
        self, cls: typing.Type[typing.Any], toStringMethodName: str
    ) -> None:
        pass

    def registerMethods(
        self,
        cls: typing.Type[typing.Any],
        toStringMethodName: str,
        fromStringMethodName: str,
    ) -> None:
        pass

    def register1(
        self,
        cls: typing.Type[typing.Any],
        toString: ToStringConverter[typing.Any],
        fromString: FromStringConverter[typing.Any],
    ) -> None:
        pass

    def register0(
        self, cls: typing.Type[typing.Any], converter: StringConverter[typing.Any]
    ) -> None:
        pass

    def registerFactory(self, factory: StringConverterFactory) -> None:
        pass

    def findTypedConverter(
        self, cls: typing.Type[typing.Any]
    ) -> TypedStringConverter[typing.Any]:
        pass

    def findConverterNoGenerics(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:
        pass

    def findConverter(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:
        pass

    def isConvertible(self, cls: typing.Type[typing.Any]) -> bool:
        pass

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:
        pass

    def convertToString1(self, cls: typing.Type[typing.Any], object: typing.Any) -> str:
        pass

    def convertToString0(self, object: typing.Any) -> str:
        pass

    @staticmethod
    def StringConvert1() -> StringConvert:
        pass

    def __init__(
        self, includeJdkConverters: bool, factories: typing.List[StringConverterFactory]
    ) -> None:
        pass

    @staticmethod
    def create() -> StringConvert:
        pass

    @staticmethod
    def __loadPrimitiveType(
        fullName: str, ex: typing.Union[ModuleNotFoundError, ImportError]
    ) -> typing.Type[typing.Any]:
        pass

    def __findFromStringConstructorByType(
        self, cls: typing.Type[typing.Any]
    ) -> typing.Callable[..., typing.Any]:
        pass

    def __findFromStringMethod(
        self, cls: typing.Type[typing.Any], methodName: str
    ) -> typing.Union[inspect.Signature, typing.Callable]:
        pass

    def __findToStringMethod(
        self, cls: typing.Type[typing.Any], methodName: str
    ) -> typing.Union[inspect.Signature, typing.Callable]:
        pass

    def __tryRegister(self, className: str, fromStringMethodName: str) -> None:
        pass

    def __tryRegisterThreeTenOld(self) -> None:
        pass

    def __tryRegisterThreeTenBackport(self) -> None:
        pass

    def __tryRegisterJava8(self) -> None:
        pass

    def __tryRegisterTimeZone(self) -> None:
        pass

    def __tryRegisterJava8Optionals(self) -> None:
        pass

    def __tryRegisterGuava(self) -> None:
        pass

    # Class Methods End
