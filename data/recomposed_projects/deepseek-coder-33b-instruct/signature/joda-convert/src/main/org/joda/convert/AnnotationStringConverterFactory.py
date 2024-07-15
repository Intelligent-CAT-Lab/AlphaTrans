from __future__ import annotations
import inspect
import re
import io
import typing
from typing import *
from src.main.org.joda.convert.ConstructorFromStringConverter import *
from src.main.org.joda.convert.FromString import *
from src.main.org.joda.convert.FromStringFactory import *
from src.main.org.joda.convert.MethodFromStringConverter import *
from src.main.org.joda.convert.ReflectionStringConverter import *
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.ToString import *
from src.main.org.joda.convert.TypedFromStringConverter import *


class AnnotationStringConverterFactory(StringConverterFactory):

    INSTANCE: AnnotationStringConverterFactory = None

    @staticmethod
    def initialize_fields() -> None:
        AnnotationStringConverterFactory.INSTANCE: AnnotationStringConverterFactory = (
            AnnotationStringConverterFactory()
        )

    def toString(self) -> str:
        return self.__class__.__name__

    def findConverter(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:
        return self.__findAnnotatedConverter(cls)

    def __eliminateEnumSubclass(
        self, cls: typing.Type[typing.Any]
    ) -> typing.Type[typing.Any]:
        sup = cls.__base__
        if sup is not None and sup.__base__ == Enum:
            return sup
        return cls

    def __findFromString(
        self, cls: typing.Type[typing.Any]
    ) -> typing.Union[inspect.Signature, typing.Callable]:

        methods = inspect.getmembers(cls, inspect.isfunction)
        matched = None
        for name, method in methods:
            if not method.__isabstractmethod__:
                from_string = getattr(method, "__FromString__", None)
                if from_string is not None:
                    if matched is not None:
                        raise RuntimeError(
                            "Two methods are annotated with @FromString: "
                            + cls.__name__
                        )
                    matched = method

        factory = getattr(cls, "__FromStringFactory__", None)
        if factory is not None:
            if matched is not None:
                raise RuntimeError(
                    "Class annotated with @FromString and @FromStringFactory: "
                    + cls.__name__
                )
            factory_methods = inspect.getmembers(factory.factory(), inspect.isfunction)
            for name, method in factory_methods:
                if not method.__isabstractmethod__:
                    if issubclass(cls, method.getReturnType):
                        from_string = getattr(method, "__FromString__", None)
                        if from_string is not None:
                            if matched is not None:
                                raise RuntimeError(
                                    "Two methods are annotated with @FromString on the factory:"
                                    + " "
                                    + factory.factory().__name__
                                )
                            matched = method
        return matched

    def __findFromStringMethod(
        self, cls: typing.Type[typing.Any], searchSuperclasses: bool
    ) -> TypedStringConverter[typing.Any]:

        loopCls = cls
        while loopCls is not None:
            fromString = self.__findFromString(loopCls)
            if fromString is not None:
                return MethodFromStringConverter(cls, fromString, loopCls)
            if not searchSuperclasses:
                break
            loopCls = loopCls.__base__

        matched = None
        if searchSuperclasses:
            for loopIfc in self.__eliminateEnumSubclass(cls).__bases__:
                fromString = self.__findFromString(loopIfc)
                if fromString is not None:
                    if matched is not None:
                        raise RuntimeError(
                            "Two different interfaces are annotated with "
                            "@FromString or @FromStringFactory: " + cls.__name__
                        )
                    matched = MethodFromStringConverter(cls, fromString, loopIfc)
        return matched

    def __findFromStringConstructor(
        self, cls: typing.Type[typing.Any]
    ) -> TypedStringConverter[typing.Any]:

        try:
            con = cls.__init__
        except AttributeError:
            return None

        from_string = getattr(con, "FromString", None)

        if from_string is None:
            return None

        return ConstructorFromStringConverter(cls, con)

    def __findToStringMethod(
        self, cls: typing.Type[typing.Any]
    ) -> typing.Union[inspect.Signature, typing.Callable]:

        matched = None
        loopCls = cls
        while loopCls != None and matched == None:
            methods = inspect.getmembers(loopCls, inspect.isfunction)
            for method in methods:
                if (
                    not method[1].__isabstractmethod__
                    and not method[1].__is_synthetic__
                ):
                    toString = getattr(method[1], "__ToString__", None)
                    if toString != None:
                        if matched != None:
                            raise RuntimeError(
                                "Two methods are annotated with @ToString: "
                                + cls.__name__
                            )
                        matched = method[1]
            loopCls = loopCls.__bases__[0] if len(loopCls.__bases__) > 0 else None
        if matched == None:
            for loopIfc in self.__eliminateEnumSubclass(cls).__bases__:
                methods = inspect.getmembers(loopIfc, inspect.isfunction)
                for method in methods:
                    if (
                        not method[1].__isabstractmethod__
                        and not method[1].__is_synthetic__
                    ):
                        toString = getattr(method[1], "__ToString__", None)
                        if toString != None:
                            if matched != None:
                                raise RuntimeError(
                                    "Two methods are annotated with @ToString on interfaces: "
                                    + cls.__name__
                                )
                            matched = method[1]
        return matched

    def __findAnnotatedFromStringConverter(
        self, cls: typing.Type[typing.Any]
    ) -> TypedStringConverter[typing.Any]:

        con = self.__findFromStringConstructor(cls)
        mth = self.__findFromStringMethod(cls, con == None)

        if con != None and mth != None:
            raise RuntimeError(
                "Both method and constructor are annotated with @FromString: "
                + cls.__name__
            )

        return con if con != None else mth

    def __findAnnotatedConverter(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:

        toString = self.__findToStringMethod(cls)
        if toString is None:
            return None

        fromString = self.__findAnnotatedFromStringConverter(cls)
        if fromString is None:
            raise RuntimeError(
                "Class annotated with @ToString but not with @FromString: "
                + cls.__name__
            )

        return ReflectionStringConverter(cls, toString, fromString)

    def __init__(self) -> None:
        pass

    def findFromStringConverter(
        self, cls: typing.Type[typing.Any]
    ) -> TypedStringConverter[typing.Any]:
        return self.__findAnnotatedFromStringConverter(cls)


AnnotationStringConverterFactory.initialize_fields()
