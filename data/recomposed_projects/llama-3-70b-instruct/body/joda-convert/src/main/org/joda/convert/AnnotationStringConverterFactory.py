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
        return self.__findAnnotatedConverter(cls)  # capture generics

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
        methods = cls.__dict__.values()
        matched = None
        for method in methods:
            if not method.__name__ == "__init__" and not method.__name__ == "__new__":
                if hasattr(method, "__annotations__"):
                    if "FromString" in method.__annotations__:
                        if matched is not None:
                            raise RuntimeError(
                                "Two methods are annotated with @FromString: "
                                + cls.__name__
                            )
                        matched = method
                if hasattr(cls, "__annotations__"):
                    if "FromStringFactory" in cls.__annotations__:
                        if matched is not None:
                            raise RuntimeError(
                                "Class annotated with @FromString and @FromStringFactory: "
                                + cls.__name__
                            )
                        factory_methods = cls.__annotations__[
                            "FromStringFactory"
                        ].factory.__dict__.values()
                        for method in factory_methods:
                            if (
                                not method.__name__ == "__init__"
                                and not method.__name__ == "__new__"
                            ):
                                if cls in method.__annotations__:
                                    if hasattr(method, "__annotations__"):
                                        if "FromString" in method.__annotations__:
                                            if matched is not None:
                                                raise RuntimeError(
                                                    "Two methods are annotated with @FromString on the factory:"
                                                    + " "
                                                    + cls.__annotations__[
                                                        "FromStringFactory"
                                                    ].factory.__name__
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
            if searchSuperclasses == False:
                break
            loopCls = loopCls.__base__
        matched = None
        if searchSuperclasses:
            for loopIfc in self.__eliminateEnumSubclass(cls).__dict__.values():
                fromString = self.__findFromString(loopIfc)
                if fromString is not None:
                    if matched is not None:
                        raise RuntimeError(
                            "Two different interfaces are annotated with "
                            + "@FromString or @FromStringFactory: "
                            + cls.__name__
                        )
                    matched = MethodFromStringConverter(cls, fromString, loopIfc)
        return matched

    def __findFromStringConstructor(
        self, cls: typing.Type[typing.Any]
    ) -> TypedStringConverter[typing.Any]:

        pass  # LLM could not translate this method

    def __findToStringMethod(
        self, cls: typing.Type[typing.Any]
    ) -> typing.Union[inspect.Signature, typing.Callable]:
        matched = None
        loopCls = cls
        while loopCls is not None and matched is None:
            methods = loopCls.__dict__.values()
            for method in methods:
                if (
                    not method.__name__ == "__init__"
                    and not method.__name__ == "__new__"
                ):
                    toString = method.__annotations__.get("return")
                    if toString is not None:
                        if matched is not None:
                            raise RuntimeError(
                                "Two methods are annotated with @ToString: "
                                + cls.__name__
                            )
                        matched = method
            loopCls = loopCls.__base__
        if matched is None:
            for loopIfc in self.__eliminateEnumSubclass(cls).__bases__:
                methods = loopIfc.__dict__.values()
                for method in methods:
                    if (
                        not method.__name__ == "__init__"
                        and not method.__name__ == "__new__"
                    ):
                        toString = method.__annotations__.get("return")
                        if toString is not None:
                            if matched is not None:
                                raise RuntimeError(
                                    "Two methods are annotated with @ToString on interfaces: "
                                    + cls.__name__
                                )
                            matched = method
        return matched

    def __findAnnotatedFromStringConverter(
        self, cls: typing.Type[typing.Any]
    ) -> TypedStringConverter[typing.Any]:
        con = self.__findFromStringConstructor(cls)
        mth = self.__findFromStringMethod(
            cls, con is None
        )  # optionally checks superclasses
        if con is not None and mth is not None:
            raise RuntimeError(
                "Both method and constructor are annotated with @FromString: "
                + cls.__name__
            )
        return con if con is not None else mth

    def __findAnnotatedConverter(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:
        toString = self.__findToStringMethod(cls)  # checks superclasses
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
