from __future__ import annotations
import time
import inspect
import re
import os
import io
import typing
from typing import *
from src.main.org.joda.convert.AnnotationStringConverterFactory import *
from src.main.org.joda.convert.ConstructorFromStringConverter import *
from src.main.org.joda.convert.EnumStringConverterFactory import *
from src.main.org.joda.convert.FromStringConverter import *
from src.main.org.joda.convert.JDKStringConverter import *
from src.main.org.joda.convert.MethodFromStringConverter import *
from src.main.org.joda.convert.ReflectionStringConverter import *
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.ToStringConverter import *
from src.main.org.joda.convert.TypeStringConverterFactory import *
from src.main.org.joda.convert.TypedAdapter import *
from src.main.org.joda.convert.TypedFromStringConverter import *
from src.main.org.joda.convert.TypedStringConverter import *
from src.main.org.joda.convert.factory.BooleanArrayStringConverterFactory import *
from src.main.org.joda.convert.factory.BooleanObjectArrayStringConverterFactory import *
from src.main.org.joda.convert.factory.ByteObjectArrayStringConverterFactory import *
from src.main.org.joda.convert.factory.CharObjectArrayStringConverterFactory import *
from src.main.org.joda.convert.factory.NumericArrayStringConverterFactory import *
from src.main.org.joda.convert.factory.NumericObjectArrayStringConverterFactory import *


class StringConvert:

    INSTANCE: StringConvert = None
    LOG: bool = False

    __fromStrings: typing.Dict[
        typing.Type[typing.Any], FromStringConverter[typing.Any]
    ] = {}
    __registered: typing.Dict[
        typing.Type[typing.Any], TypedStringConverter[typing.Any]
    ] = {}
    __factories: typing.List[StringConverterFactory] = []
    __CACHED_NULL: TypedStringConverter[typing.Any] = None

    @staticmethod
    def run_static_init():

        log = None
        try:
            log = os.getenv("org.joda.convert.debug")
        except Exception:
            pass
        StringConvert.LOG = log == "true"

    @staticmethod
    def initialize_fields() -> None:
        StringConvert.INSTANCE: StringConvert = StringConvert.StringConvert1()

        StringConvert.__CACHED_NULL: TypedStringConverter[
            typing.Any
        ] = TypedStringConverter[typing.Any](
            convertToString=lambda object: None,
            convertFromString=lambda cls, str: None,
            getEffectiveType=lambda: None,
        )

    def toString(self) -> str:
        return self.__class__.__name__

    def findFromStringConverter(
        self, cls: typing.Type[typing.Any]
    ) -> FromStringConverter[typing.Any]:

        converter = self.__findConverterQuiet(cls)

        if converter is None:
            fromStringConverter = typing.cast(
                FromStringConverter[typing.Any], self.__fromStrings.get(cls)
            )

            if fromStringConverter is None:
                raise Exception("No registered converter found: " + str(cls))

            return fromStringConverter

        return converter

    def findTypedConverterNoGenerics(
        self, cls: typing.Type[typing.Any]
    ) -> TypedStringConverter[typing.Any]:

        conv = typing.cast(
            TypedStringConverter[typing.Any], self.__findConverterQuiet(cls)
        )
        if conv is None:
            raise RuntimeError("No registered converter found: " + cls.__name__)
        return conv

    def __lookupConverter(
        self, cls: typing.Type[typing.Any]
    ) -> TypedStringConverter[typing.Any]:

        for factory in self.__factories:
            factoryConv = typing.cast(
                StringConverter[typing.Any], factory.findConverter(cls)
            )
            if factoryConv is not None:
                return TypedAdapter.adapt(cls, factoryConv)
        return None

    def __findConverterQuiet(
        self, cls: typing.Type[typing.Any]
    ) -> TypedStringConverter[typing.Any]:

        if cls is None:
            raise ValueError("Class must not be null")

        conv = self.__registered.get(cls)

        if conv == self.__CACHED_NULL:
            return None

        if conv is None:
            try:
                conv = self.__lookupConverter(cls)
            except RuntimeError as ex:
                self.__registered.putIfAbsent(cls, self.__CACHED_NULL)
                raise ex

            if conv is None:
                self.__registered.putIfAbsent(cls, self.__CACHED_NULL)
                fromString = (
                    AnnotationStringConverterFactory.INSTANCE.findFromStringConverter(
                        cls
                    )
                )
                if fromString is not None:
                    self.__fromStrings.put(cls, fromString)
                return None

            self.__registered.putIfAbsent(cls, conv)

        return conv

    @staticmethod
    def loadType(fullName: str) -> typing.Type[typing.Any]:

        try:
            loader = Thread.currentThread().getContextClassLoader()
            if loader is not None and not fullName.startswith("["):
                return loader.loadClass(fullName)
            else:
                return Class.forName(fullName)
        except (ClassNotFoundException, ModuleNotFoundError) as ex:
            return StringConvert.__loadPrimitiveType(fullName, ex)

    def registerMethodConstructor(
        self, cls: typing.Type[typing.Any], toStringMethodName: str
    ) -> None:

        if cls is None:
            raise ValueError("Class must not be null")
        if toStringMethodName is None:
            raise ValueError("Method name must not be null")
        if self == StringConvert.INSTANCE:
            raise ValueError("Global singleton cannot be extended")

        toString = self.__findToStringMethod(cls, toStringMethodName)
        fromString = self.__findFromStringConstructorByType(cls)
        fromStringConverter = ConstructorFromStringConverter(cls, fromString)
        converter = ReflectionStringConverter(cls, toString, fromStringConverter)
        self.__registered[cls] = converter

    def registerMethods(
        self,
        cls: typing.Type[typing.Any],
        toStringMethodName: str,
        fromStringMethodName: str,
    ) -> None:

        if cls is None:
            raise ValueError("Class must not be null")
        if toStringMethodName is None or fromStringMethodName is None:
            raise ValueError("Method names must not be null")
        if self == StringConvert.INSTANCE:
            raise ValueError("Global singleton cannot be extended")

        toString = self.__findToStringMethod(cls, toStringMethodName)
        fromString = self.__findFromStringMethod(cls, fromStringMethodName)

        fromStringConverter = MethodFromStringConverter(cls, fromString, cls)
        converter = ReflectionStringConverter(cls, toString, fromStringConverter)

        self.__registered[cls] = converter

    def register1(
        self,
        cls: typing.Type[typing.Any],
        toString: ToStringConverter[typing.Any],
        fromString: FromStringConverter[typing.Any],
    ) -> None:

        if fromString is None or toString is None:
            raise ValueError("Converters must not be None")

        self.register0(
            cls,
            TypedStringConverter(
                lambda object: toString.convertToString(object),
                lambda cls, str: fromString.convertFromString(cls, str),
                lambda: cls,
            ),
        )

    def register0(
        self, cls: typing.Type[typing.Any], converter: StringConverter[typing.Any]
    ) -> None:

        if cls is None:
            raise ValueError("Class must not be null")
        if converter is None:
            raise ValueError("StringConverter must not be null")
        if self == StringConvert.INSTANCE:
            raise RuntimeError("Global singleton cannot be extended")
        self.__registered[cls] = TypedAdapter.adapt(cls, converter)

    def registerFactory(self, factory: StringConverterFactory) -> None:

        if factory is None:
            raise ValueError("Factory must not be null")
        if self == StringConvert.INSTANCE:
            raise ValueError("Global singleton cannot be extended")
        self.__factories.insert(0, factory)

    def findTypedConverter(
        self, cls: typing.Type[typing.Any]
    ) -> TypedStringConverter[typing.Any]:

        conv = self.__findConverterQuiet(cls)
        if conv is None:
            raise RuntimeError("No registered converter found: " + str(cls))
        return conv

    def findConverterNoGenerics(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:
        return self.findTypedConverterNoGenerics(cls)

    def findConverter(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:
        return self.findTypedConverter(cls)

    def isConvertible(self, cls: typing.Type[typing.Any]) -> bool:
        try:
            return cls is not None and self.__findConverterQuiet(cls) is not None
        except RuntimeError:
            return False

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:

        if str is None:
            return None

        conv = self.findFromStringConverter(cls)

        return conv.convertFromString(cls, str)

    def convertToString1(self, cls: typing.Type[typing.Any], object: typing.Any) -> str:

        if object is None:
            return None

        conv = self.findConverterNoGenerics(cls)
        return conv.convertToString(object)

    def convertToString0(self, object: typing.Any) -> str:

        if object is None:
            return None

        cls = type(object)
        conv = self.findConverterNoGenerics(cls)

        return conv.convertToString(object)

    @staticmethod
    def StringConvert1() -> StringConvert:
        return StringConvert(True, [])

    def __init__(
        self, includeJdkConverters: bool, factories: typing.List[StringConverterFactory]
    ) -> None:

        if factories is None:
            raise ValueError("StringConverterFactory array must not be null")
        for i in range(len(factories)):
            if factories[i] is None:
                raise ValueError(
                    "StringConverterFactory array must not contain a null element"
                )

        if includeJdkConverters:
            for conv in JDKStringConverter:
                self.__registered[conv.getType()] = conv
            self.__registered[bool] = JDKStringConverter.BOOLEAN
            self.__registered[int] = JDKStringConverter.INTEGER
            self.__registered[float] = JDKStringConverter.FLOAT
            self.__registered[complex] = JDKStringConverter.DOUBLE
            self.__registered[str] = JDKStringConverter.STRING
            self.__tryRegisterGuava()
            self.__tryRegisterJava8Optionals()
            self.__tryRegisterTimeZone()
            self.__tryRegisterJava8()
            self.__tryRegisterThreeTenBackport()
            self.__tryRegisterThreeTenOld()

        if len(factories) > 0:
            self.__factories.extend(factories)
        self.__factories.append(AnnotationStringConverterFactory.INSTANCE)
        if includeJdkConverters:
            self.__factories.append(EnumStringConverterFactory.INSTANCE)
            self.__factories.append(TypeStringConverterFactory.INSTANCE)

    @staticmethod
    def create() -> StringConvert:
        return StringConvert(
            True,
            NumericArrayStringConverterFactory.INSTANCE,
            NumericObjectArrayStringConverterFactory.INSTANCE,
            CharObjectArrayStringConverterFactory.INSTANCE,
            ByteObjectArrayStringConverterFactory.INSTANCE,
            BooleanArrayStringConverterFactory.INSTANCE,
            BooleanObjectArrayStringConverterFactory.INSTANCE,
        )

    @staticmethod
    def __loadPrimitiveType(
        fullName: str, ex: typing.Union[ModuleNotFoundError, ImportError]
    ) -> typing.Type[typing.Any]:

        if fullName == "int":
            return int
        elif fullName == "long":
            return long
        elif fullName == "double":
            return float
        elif fullName == "boolean":
            return bool
        elif fullName == "short":
            return short
        elif fullName == "byte":
            return byte
        elif fullName == "char":
            return char
        elif fullName == "float":
            return float
        elif fullName == "void":
            return None
        else:
            raise ex

    def __findFromStringConstructorByType(
        self, cls: typing.Type[typing.Any]
    ) -> typing.Callable[..., typing.Any]:

        pass  # LLM could not translate this method

    def __findFromStringMethod(
        self, cls: typing.Type[typing.Any], methodName: str
    ) -> typing.Union[inspect.Signature, typing.Callable]:

        try:
            m = getattr(cls, methodName)
        except AttributeError:
            raise ValueError("Method not found")

        if not isinstance(m, staticmethod):
            raise ValueError("Method must be static: " + methodName)

        return m

    def __findToStringMethod(
        self, cls: typing.Type[typing.Any], methodName: str
    ) -> typing.Union[inspect.Signature, typing.Callable]:

        try:
            m = getattr(cls, methodName)
        except AttributeError as ex:
            raise ValueError(ex)

        if inspect.ismethod(m):
            if inspect.isfunction(m):
                return m
            else:
                raise ValueError("Method must not be static: " + methodName)
        else:
            raise ValueError("Method must not be static: " + methodName)

    def __tryRegister(self, className: str, fromStringMethodName: str) -> None:

        cls = self.loadType(className)
        self.registerMethods(cls, "toString", fromStringMethodName)

    def __tryRegisterThreeTenOld(self) -> None:

        try:
            self.__tryRegister("javax.time.Instant", "parse")
            self.__tryRegister("javax.time.Duration", "parse")
            self.__tryRegister("javax.time.calendar.LocalDate", "parse")
            self.__tryRegister("javax.time.calendar.LocalTime", "parse")
            self.__tryRegister("javax.time.calendar.LocalDateTime", "parse")
            self.__tryRegister("javax.time.calendar.OffsetDate", "parse")
            self.__tryRegister("javax.time.calendar.OffsetTime", "parse")
            self.__tryRegister("javax.time.calendar.OffsetDateTime", "parse")
            self.__tryRegister("javax.time.calendar.ZonedDateTime", "parse")
            self.__tryRegister("javax.time.calendar.Year", "parse")
            self.__tryRegister("javax.time.calendar.YearMonth", "parse")
            self.__tryRegister("javax.time.calendar.MonthDay", "parse")
            self.__tryRegister("javax.time.calendar.Period", "parse")
            self.__tryRegister("javax.time.calendar.ZoneOffset", "of")
            self.__tryRegister("javax.time.calendar.ZoneId", "of")
            self.__tryRegister("javax.time.calendar.TimeZone", "of")

        except Exception as ex:
            if self.LOG:
                print("tryRegisterThreeTenOld: " + str(ex))

    def __tryRegisterThreeTenBackport(self) -> None:

        try:
            self.__tryRegister("org.threeten.bp.Instant", "parse")
            self.__tryRegister("org.threeten.bp.Duration", "parse")
            self.__tryRegister("org.threeten.bp.LocalDate", "parse")
            self.__tryRegister("org.threeten.bp.LocalTime", "parse")
            self.__tryRegister("org.threeten.bp.LocalDateTime", "parse")
            self.__tryRegister("org.threeten.bp.OffsetTime", "parse")
            self.__tryRegister("org.threeten.bp.OffsetDateTime", "parse")
            self.__tryRegister("org.threeten.bp.ZonedDateTime", "parse")
            self.__tryRegister("org.threeten.bp.Year", "parse")
            self.__tryRegister("org.threeten.bp.YearMonth", "parse")
            self.__tryRegister("org.threeten.bp.MonthDay", "parse")
            self.__tryRegister("org.threeten.bp.Period", "parse")
            self.__tryRegister("org.threeten.bp.ZoneOffset", "of")
            self.__tryRegister("org.threeten.bp.ZoneId", "of")
            self.__tryRegister("org.threeten.bp.ZoneRegion", "of")

        except Exception as ex:
            if self.LOG:
                print("tryRegisterThreeTenBackport: " + str(ex))

    def __tryRegisterJava8(self) -> None:

        try:
            self.__tryRegister("java.time.Instant", "parse")
            self.__tryRegister("java.time.Duration", "parse")
            self.__tryRegister("java.time.LocalDate", "parse")
            self.__tryRegister("java.time.LocalTime", "parse")
            self.__tryRegister("java.time.LocalDateTime", "parse")
            self.__tryRegister("java.time.OffsetTime", "parse")
            self.__tryRegister("java.time.OffsetDateTime", "parse")
            self.__tryRegister("java.time.ZonedDateTime", "parse")
            self.__tryRegister("java.time.Year", "parse")
            self.__tryRegister("java.time.YearMonth", "parse")
            self.__tryRegister("java.time.MonthDay", "parse")
            self.__tryRegister("java.time.Period", "parse")
            self.__tryRegister("java.time.ZoneOffset", "of")
            self.__tryRegister("java.time.ZoneId", "of")
            self.__tryRegister("java.time.ZoneRegion", "of")

        except Exception as ex:
            if self.LOG:
                print("tryRegisterJava8: " + str(ex))

    def __tryRegisterTimeZone(self) -> None:

        try:
            self.__registered[SimpleTimeZone] = JDKStringConverter.TIME_ZONE

        except Exception as ex:
            if self.LOG:
                print("tryRegisterTimeZone1: " + str(ex))

        try:
            zone = TimeZone.getDefault()
            self.__registered[zone.__class__] = JDKStringConverter.TIME_ZONE

        except Exception as ex:
            if self.LOG:
                print("tryRegisterTimeZone2: " + str(ex))

        try:
            zone = TimeZone.getTimeZone("Europe/London")
            self.__registered[zone.__class__] = JDKStringConverter.TIME_ZONE

        except Exception as ex:
            if self.LOG:
                print("tryRegisterTimeZone3: " + str(ex))

    def __tryRegisterJava8Optionals(self) -> None:

        try:
            cls1 = self.loadType("java.util.OptionalInt")
            conv1 = cls1.getDeclaredConstructor().newInstance()
            self.__registered[conv1.getEffectiveType()] = conv1

            cls2 = self.loadType("org.joda.convert.OptionalLongStringConverter")
            conv2 = cls2.getDeclaredConstructor().newInstance()
            self.__registered[conv2.getEffectiveType()] = conv2

            cls3 = self.loadType("org.joda.convert.OptionalDoubleStringConverter")
            conv3 = cls3.getDeclaredConstructor().newInstance()
            self.__registered[conv3.getEffectiveType()] = conv3

        except Exception as ex:
            if self.LOG:
                print("tryRegisterOptionals: " + str(ex))

    def __tryRegisterGuava(self) -> None:

        try:
            moduleClass = type(object).__class__.getMethod("getModule").getReturnType()
            convertModule = (
                type(object).__class__.getMethod("getModule").invoke(StringConvert)
            )
            layer = convertModule.getClass().getMethod("getLayer").invoke(convertModule)
            if layer is not None:
                optGuava = (
                    layer.getClass()
                    .getMethod("findModule", str)
                    .invoke(layer, "com.google.common")
                )
                found = optGuava.getClass().getMethod("isPresent").invoke(optGuava)
                if found:
                    guavaModule = optGuava.getClass().getMethod("get").invoke(optGuava)
                    moduleClass.getMethod("addReads", moduleClass).invoke(
                        convertModule, guavaModule
                    )

        except Exception as ex:
            if self.LOG:
                print("tryRegisterGuava1: " + str(ex))

        try:
            self.loadType("com.google.common.reflect.TypeToken")
            cls = self.loadType("org.joda.convert.TypeTokenStringConverter")
            conv = cls.getDeclaredConstructor().newInstance()
            self.__registered[conv.getEffectiveType()] = conv

        except Exception as ex:
            if self.LOG:
                print("tryRegisterGuava2: " + str(ex))


StringConvert.run_static_init()

StringConvert.initialize_fields()
