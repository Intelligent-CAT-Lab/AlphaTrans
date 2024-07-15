from __future__ import annotations
import time
import inspect
import re
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
            log = System.getProperty("org.joda.convert.debug")
        except PermissionError as ex:
            pass
        LOG = "true".equalsIgnoreCase(log)

    @staticmethod
    def initialize_fields() -> None:
        StringConvert.INSTANCE: StringConvert = StringConvert.StringConvert1()

        StringConvert.__CACHED_NULL: TypedStringConverter[typing.Any] = (
            TypedStringConverter[typing.Any]()
        )

    def toString(self) -> str:
        return self.__class__.__name__

    def findFromStringConverter(
        self, cls: typing.Type[typing.Any]
    ) -> FromStringConverter[typing.Any]:
        converter: TypedStringConverter[typing.Any] = self.__findConverterQuiet(cls)
        if converter is None:
            fromStringConverter: FromStringConverter[typing.Any] = (
                self.__fromStrings.get(cls)
            )
            if fromStringConverter is None:
                raise RuntimeError("No registered converter found: " + cls)
            return fromStringConverter
        return converter

    def findTypedConverterNoGenerics(
        self, cls: typing.Type[typing.Any]
    ) -> TypedStringConverter[typing.Any]:
        conv: TypedStringConverter[typing.Any] = self.__findConverterQuiet(cls)
        if conv is None:
            raise RuntimeError("No registered converter found: " + str(cls))
        return conv

    def __lookupConverter(
        self, cls: typing.Type[typing.Any]
    ) -> TypedStringConverter[typing.Any]:

        pass  # LLM could not translate this method

    def __findConverterQuiet(
        self, cls: typing.Type[typing.Any]
    ) -> TypedStringConverter[typing.Any]:
        if cls is None:
            raise ValueError("Class must not be null")
        conv: TypedStringConverter[typing.Any] = self.__registered.get(cls)
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
                fromString: TypedFromStringConverter[typing.Any] = (
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

        pass  # LLM could not translate this method

    def registerMethodConstructor(
        self, cls: typing.Type[typing.Any], toStringMethodName: str
    ) -> None:
        if cls is None:
            raise ValueError("Class must not be null")
        if toStringMethodName is None:
            raise ValueError("Method name must not be null")
        if self is StringConvert.INSTANCE:
            raise RuntimeError("Global singleton cannot be extended")
        toString: typing.Union[inspect.Signature, typing.Callable] = (
            self.__findToStringMethod(cls, toStringMethodName)
        )
        fromString: typing.Callable[..., typing.Any] = (
            self.__findFromStringConstructorByType(cls)
        )
        fromStringConverter: TypedFromStringConverter[typing.Any] = (
            ConstructorFromStringConverter[typing.Any](cls, fromString)
        )
        converter: ReflectionStringConverter[typing.Any] = ReflectionStringConverter[
            typing.Any
        ](cls, toString, fromStringConverter)
        self.__registered.putIfAbsent(cls, converter)

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
            raise RuntimeError("Global singleton cannot be extended")
        toString = self.__findToStringMethod(cls, toStringMethodName)
        fromString = self.__findFromStringMethod(cls, fromStringMethodName)
        fromStringConverter = MethodFromStringConverter(cls, fromString, cls)
        converter = ReflectionStringConverter(cls, toString, fromStringConverter)
        self.__registered.putIfAbsent(cls, converter)

    def register1(
        self,
        cls: typing.Type[typing.Any],
        toString: ToStringConverter[typing.Any],
        fromString: FromStringConverter[typing.Any],
    ) -> None:

        pass  # LLM could not translate this method

    def register0(
        self, cls: typing.Type[typing.Any], converter: StringConverter[typing.Any]
    ) -> None:
        if cls is None:
            raise ValueError("Class must not be null")
        if converter is None:
            raise ValueError("StringConverter must not be null")
        if self is StringConvert.INSTANCE:
            raise RuntimeError("Global singleton cannot be extended")
        self.__registered[cls] = TypedAdapter.adapt(cls, converter)

    def registerFactory(self, factory: StringConverterFactory) -> None:
        if factory is None:
            raise ValueError("Factory must not be null")
        if self == INSTANCE:
            raise RuntimeError("Global singleton cannot be extended")
        self.__factories.insert(0, factory)

    def findTypedConverter(
        self, cls: typing.Type[typing.Any]
    ) -> TypedStringConverter[typing.Any]:
        conv: TypedStringConverter[typing.Any] = self.__findConverterQuiet(cls)
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

        pass  # LLM could not translate this method

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:
        if str is None:
            return None
        conv: FromStringConverter[typing.Any] = self.findFromStringConverter(cls)
        return conv.convertFromString(cls, str)

    def convertToString1(self, cls: typing.Type[typing.Any], object: typing.Any) -> str:
        if object is None:
            return None
        conv: StringConverter[typing.Any] = self.findConverterNoGenerics(cls)
        return conv.convertToString(object)

    def convertToString0(self, object: typing.Any) -> str:
        if object is None:
            return None
        cls = object.__class__
        conv = self.findConverterNoGenerics(cls)
        return conv.convertToString(object)

    @staticmethod
    def StringConvert1() -> StringConvert:
        return StringConvert(True)

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
            for conv in JDKStringConverter.values():
                self.__registered[conv.getType()] = conv
            self.__registered[bool] = JDKStringConverter.BOOLEAN
            self.__registered[byte] = JDKStringConverter.BYTE
            self.__registered[short] = JDKStringConverter.SHORT
            self.__registered[int] = JDKStringConverter.INTEGER
            self.__registered[long] = JDKStringConverter.LONG
            self.__registered[float] = JDKStringConverter.FLOAT
            self.__registered[double] = JDKStringConverter.DOUBLE
            self.__registered[chr] = JDKStringConverter.CHARACTER
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

        pass  # LLM could not translate this method

    def __findFromStringConstructorByType(
        self, cls: typing.Type[typing.Any]
    ) -> typing.Callable[..., typing.Any]:

        pass  # LLM could not translate this method

    def __findFromStringMethod(
        self, cls: typing.Type[typing.Any], methodName: str
    ) -> typing.Union[inspect.Signature, typing.Callable]:

        pass  # LLM could not translate this method

    def __findToStringMethod(
        self, cls: typing.Type[typing.Any], methodName: str
    ) -> typing.Union[inspect.Signature, typing.Callable]:
        m = cls.getMethod(methodName)
        if Modifier.isStatic(m.getModifiers()):
            raise ValueError("Method must not be static: " + methodName)
        return m

    def __tryRegister(self, className: str, fromStringMethodName: str) -> None:
        cls = self.loadType(className)
        self.registerMethods(cls, "toString", fromStringMethodName)

    def __tryRegisterThreeTenOld(self) -> None:

        pass  # LLM could not translate this method

    def __tryRegisterThreeTenBackport(self) -> None:

        pass  # LLM could not translate this method

    def __tryRegisterJava8(self) -> None:

        pass  # LLM could not translate this method

    def __tryRegisterTimeZone(self) -> None:

        pass  # LLM could not translate this method

    def __tryRegisterJava8Optionals(self) -> None:

        pass  # LLM could not translate this method

    def __tryRegisterGuava(self) -> None:
        try:
            moduleClass = type(type).getMethod("getModule").getReturnType()
            convertModule = type(type).getMethod("getModule").invoke(StringConvert)
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
            if StringConvert.LOG:
                System.err.println("tryRegisterGuava1: " + ex)
        try:
            self.loadType("com.google.common.reflect.TypeToken")
            cls = self.loadType("org.joda.convert.TypeTokenStringConverter")
            conv = cls.getDeclaredConstructor().newInstance()
            self.__registered[conv.getEffectiveType()] = conv
        except Exception as ex:
            if StringConvert.LOG:
                System.err.println("tryRegisterGuava2: " + ex)


StringConvert.run_static_init()

StringConvert.initialize_fields()
