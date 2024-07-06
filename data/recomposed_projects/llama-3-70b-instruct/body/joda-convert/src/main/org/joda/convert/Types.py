from __future__ import annotations
import inspect
import re
import os
from io import StringIO
from abc import ABC
import io
import typing
from typing import *
from src.main.org.joda.convert.TypeCapture import *


class GenericArrayTypeImpl:

    __serialVersionUID: int = 0
    __componentType: typing.Type = None

    def equals(self, obj: typing.Any) -> bool:
        if isinstance(obj, GenericArrayType):
            that: GenericArrayType = obj
            return Types.__equal(
                self.getGenericComponentType(), that.getGenericComponentType()
            )
        return False

    def hashCode(self) -> int:
        return self.__componentType.hashCode()

    def toString(self) -> str:
        return Types.toString(self.__componentType) + "[]"

    def getGenericComponentType(self) -> typing.Type:
        return self.__componentType

    def __init__(self, componentType: typing.Type) -> None:
        self.__componentType = JavaVersion.CURRENT.usedInGenericType0(componentType)


class ParameterizedTypeImpl(typing.Generic[typing.TypeVar("T")]):

    __serialVersionUID: int = 0
    __rawType: typing.Type[typing.Any] = None

    __argumentsList: typing.List[typing.Type] = None

    __ownerType: typing.Type = None

    def equals(self, other: typing.Any) -> bool:
        if not isinstance(other, ParameterizedType):
            return False
        that: ParameterizedType = other
        return (
            self.getRawType().equals(that.getRawType())
            and Types.__equal(self.getOwnerType(), that.getOwnerType())
            and Arrays.equals(
                self.getActualTypeArguments(), that.getActualTypeArguments()
            )
        )

    def hashCode(self) -> int:
        return (
            (0 if self.__ownerType == None else self.__ownerType.hashCode())
            ^ self.__argumentsList.hashCode()
            ^ self.__rawType.hashCode()
        )

    def toString(self) -> str:
        builder = io.StringIO()
        if (
            self.__ownerType != None
            and JavaVersion.CURRENT.jdkTypeDuplicatesOwnerName()
        ):
            builder.write(JavaVersion.CURRENT.typeName(self.__ownerType))
            builder.write(".")
        str = ""
        if self.__argumentsList == None:
            str = "null"
        else:
            for i in range(0, len(self.__argumentsList)):
                if i > 0:
                    str += ", "
                str += JavaVersion.CURRENT.typeName(self.__argumentsList[i])
        return (
            builder.write(self.__rawType.getName())
            .write("<")
            .write(str)
            .write(">")
            .toString()
        )

    def getOwnerType(self) -> typing.Type:
        return self.__ownerType

    def getRawType(self) -> typing.Type:
        return self.__rawType

    def getActualTypeArguments(self) -> typing.List[typing.Type]:
        return Types.__toArray(self.__argumentsList)

    def __init__(
        self,
        ownerType: typing.Type,
        rawType: typing.Type[typing.Any],
        typeArguments: typing.List[typing.Type],
    ) -> None:
        Types.checkNotNull(rawType)
        Types.checkArgument0(typeArguments.length == rawType.getTypeParameters().length)
        Types.disallowPrimitiveType(typeArguments, "type parameter")
        self.__ownerType = ownerType
        self.__rawType = rawType
        self.__argumentsList = JavaVersion.CURRENT.usedInGenericType1(typeArguments)


class TypeVariableImpl:

    __bounds: typing.List[typing.Type] = None

    __name: str = ""

    __genericDeclaration: typing.Any = None

    def equals(self, obj: typing.Any) -> bool:

        pass  # LLM could not translate this method

    def hashCode(self) -> int:
        return self.__genericDeclaration.hashCode() ^ self.__name.hashCode()

    def toString(self) -> str:
        return self.__name

    def getName(self) -> str:
        return self.__name

    def getGenericDeclaration(self) -> typing.Any:
        return self.__genericDeclaration

    def __init__(
        self,
        genericDeclaration: typing.Any,
        name: str,
        bounds: typing.List[typing.Type],
    ) -> None:

        pass  # LLM could not translate this method


class TypeVariableInvocationHandler(typing.Callable):

    __typeVariableImpl: TypeVariableImpl[typing.Any] = None

    __typeVariableMethods: typing.Dict[
        str, typing.Union[inspect.Signature, typing.Callable]
    ] = None

    @staticmethod
    def run_static_init():
        builder = {}
        for method in TypeVariableImpl.__class__.getMethods():
            if method.getDeclaringClass().equals(TypeVariableImpl.__class__):
                try:
                    method.setAccessible(True)
                except AccessControlException as e:
                    pass
                builder[method.getName()] = method
        TypeVariableInvocationHandler.__typeVariableMethods = builder

    def invoke(
        self,
        proxy: typing.Any,
        method: typing.Union[inspect.Signature, typing.Callable],
        args: typing.List[typing.Any],
    ) -> typing.Any:
        methodName = method.getName()
        typeVariableMethod = typeVariableMethods.get(methodName)
        if typeVariableMethod == None:
            raise NotImplementedError(methodName)
        else:
            try:
                return typeVariableMethod.invoke(typeVariableImpl, args)
            except InvocationTargetException as e:
                raise e.getCause()

    def __init__(self, typeVariableImpl: TypeVariableImpl[typing.Any]) -> None:
        self.__typeVariableImpl = typeVariableImpl


class WildcardTypeImpl:

    __serialVersionUID: int = 0
    __upperBounds: typing.List[typing.Type] = None

    __lowerBounds: typing.List[typing.Type] = None

    def toString(self) -> str:
        builder = StringBuilder("?")
        for lowerBound in self.__lowerBounds:
            builder.append(" super ").append(JavaVersion.CURRENT.typeName(lowerBound))
        for upperBound in filterUpperBounds(self.__upperBounds):
            builder.append(" extends ").append(JavaVersion.CURRENT.typeName(upperBound))
        return builder.toString()

    def hashCode(self) -> int:
        return self.__lowerBounds.hashCode() ^ self.__upperBounds.hashCode()

    def equals(self, obj: typing.Any) -> bool:
        if isinstance(obj, WildcardType):
            that: WildcardType = obj
            return self.lowerBounds == list(
                that.getLowerBounds()
            ) and self.upperBounds == list(that.getUpperBounds())
        return False

    def getUpperBounds(self) -> typing.List[typing.Type]:
        return Types.__toArray(self.__upperBounds)

    def getLowerBounds(self) -> typing.List[typing.Type]:
        return Types.__toArray(self.__lowerBounds)

    def __init__(
        self,
        lowerBounds: typing.List[typing.Type],
        upperBounds: typing.List[typing.Type],
    ) -> None:
        Types.__disallowPrimitiveType(lowerBounds, "lower bound for wildcard")
        Types.__disallowPrimitiveType(upperBounds, "upper bound for wildcard")
        self.__lowerBounds = JavaVersion.CURRENT.usedInGenericType1(lowerBounds)
        self.__upperBounds = JavaVersion.CURRENT.usedInGenericType1(upperBounds)


class TypeVisitor(ABC):

    __visited: typing.Set[typing.Type] = set()

    def visit(self, types: typing.List[typing.Type]) -> None:
        for type in types:
            if type is None or not self.__visited.add(type):
                continue
            succeeded = False
            try:
                if isinstance(type, TypeVariable):
                    self.visitTypeVariable(type)
                elif isinstance(type, WildcardType):
                    self.visitWildcardType(type)
                elif isinstance(type, ParameterizedType):
                    self.visitParameterizedType(type)
                elif isinstance(type, Class):
                    self.visitClass(type)
                elif isinstance(type, GenericArrayType):
                    self.visitGenericArrayType(type)
                else:
                    raise AssertionError("Unknown type: " + type)
                succeeded = True
            finally:
                if not succeeded:
                    self.__visited.remove(type)

    def visitWildcardType(self, t: typing.Any) -> None:
        pass

    def visitTypeVariable(self, t: typing.TypeVar("T", bound=typing.Any)) -> None:
        pass

    def visitParameterizedType(self, t: typing.Generic[typing.TypeVar("T")]) -> None:
        pass

    def visitGenericArrayType(
        self,
        t: typing.Union[
            typing.List[typing.TypeVar("T", bound=typing.Any)], array.array
        ],
    ) -> None:
        self.visit(t.getGenericComponentType())

    def visitClass(self, t: typing.Type[typing.Any]) -> None:
        self.visit(t)


class NativeTypeVariableEquals:

    NATIVE_TYPE_VARIABLE_ONLY: bool = False


class LocalClass:

    pass


class ClassOwnership(ABC):

    JVM_BEHAVIOR: ClassOwnership = None
    LOCAL_CLASS_HAS_NO_OWNER: ClassOwnership = None

    OWNED_BY_ENCLOSING_CLASS: ClassOwnership = None

    @staticmethod
    def initialize_fields() -> None:
        ClassOwnership.JVM_BEHAVIOR: ClassOwnership = (
            ClassOwnership.__detectJvmBehavior()
        )

    @staticmethod
    def __detectJvmBehavior() -> ClassOwnership:
        localClass = LocalClass[str]()  # CSIGNORE
        subclass = localClass.__class__
        parameterizedType = typing.cast(typing.Type[typing.Any], subclass.__bases__[0])
        for behavior in ClassOwnership.__subclasses__():
            if behavior().getOwnerType(LocalClass) == parameterizedType.__class__:
                return behavior()
        raise AssertionError()

    def getOwnerType(self, rawType: typing.Type[typing.Any]) -> typing.Type[typing.Any]:
        return rawType.getEnclosingClass()


class JavaVersion(ABC):

    CURRENT: JavaVersion = None

    JAVA9: JavaVersion = None

    JAVA8: JavaVersion = None
    JAVA7: JavaVersion = None

    JAVA6: JavaVersion = None

    @staticmethod
    def initialize_fields() -> None:
        JavaVersion.JAVA8: JavaVersion = JavaVersion()

        JavaVersion.JAVA6: JavaVersion = JavaVersion()

    def usedInGenericType1(
        self, types: typing.List[typing.Type]
    ) -> typing.List[typing.Type]:
        builder: typing.List[typing.Type] = []
        for type in types:
            builder.append(self.usedInGenericType0(type))
        return builder

    def jdkTypeDuplicatesOwnerName(self) -> bool:
        return True

    def typeName(self, type: typing.Type) -> str:
        return Types.toString(type)

    def usedInGenericType0(self, type: typing.Type) -> typing.Type:
        return type

    def newArrayType(self, componentType: typing.Type) -> typing.Type:
        return Array[componentType]


class Types:

    @staticmethod
    def checkArgument2(
        expression: bool,
        errorMessageTemplate: str,
        errorMessageArgs: typing.List[typing.Any],
    ) -> None:
        if not expression:
            raise ValueError(Types.__format(errorMessageTemplate, errorMessageArgs))

    @staticmethod
    def getArrayClass(
        componentType: typing.Type[typing.Any],
    ) -> typing.Type[typing.Any]:
        return Array.newInstance(componentType, 0).getClass()

    @staticmethod
    def getComponentType(type: typing.Type) -> typing.Type:

        pass  # LLM could not translate this method

    @staticmethod
    def toString(type: typing.Type) -> str:

        pass  # LLM could not translate this method

    @staticmethod
    def supertypeOf(lowerBound: typing.Type) -> typing.Any:
        return WildcardTypeImpl([lowerBound], [Object])

    @staticmethod
    def subtypeOf(upperBound: typing.Type) -> typing.Any:
        return WildcardTypeImpl([], [upperBound])

    @staticmethod
    def newArtificialTypeVariable(
        declaration: typing.Any, name: str, bounds: typing.List[typing.Type]
    ) -> typing.TypeVar("D", bound=typing.Any):
        return Types.__newTypeVariableImpl(
            declaration, name, (bounds if len(bounds) != 0 else [typing.Any])
        )

    @staticmethod
    def newParameterizedType(
        rawType: typing.Type[typing.Any], arguments: typing.List[typing.Type]
    ) -> typing.Generic[typing.TypeVar("T")]:
        return ParameterizedTypeImpl(
            ClassOwnership.JVM_BEHAVIOR.getOwnerType(rawType), rawType, arguments
        )

    @staticmethod
    def newParameterizedTypeWithOwner(
        ownerType: typing.Type,
        rawType: typing.Type[typing.Any],
        arguments: typing.List[typing.Type],
    ) -> typing.Generic[typing.TypeVar("T")]:
        if ownerType is None:
            return Types.newParameterizedType(rawType, arguments)
        Types.checkNotNull(arguments)
        Types.checkArgument2(
            rawType.getEnclosingClass() is not None,
            "Owner type for unenclosed %s",
            rawType,
        )
        return ParameterizedTypeImpl(ownerType, rawType, arguments)

    @staticmethod
    def newArrayType(componentType: typing.Type) -> typing.Type:
        if isinstance(componentType, WildcardType):
            wildcard: WildcardType = componentType
            lowerBounds: typing.List[typing.Type] = wildcard.getLowerBounds()
            Types.__checkArgument1(
                len(lowerBounds) <= 1,
                "Wildcard cannot have more than one lower bounds.",
            )
            if len(lowerBounds) == 1:
                return Types.supertypeOf(Types.newArrayType(lowerBounds[0]))
            else:
                upperBounds: typing.List[typing.Type] = wildcard.getUpperBounds()
                Types.__checkArgument1(
                    len(upperBounds) == 1, "Wildcard should have only one upper bound."
                )
                return Types.subtypeOf(Types.newArrayType(upperBounds[0]))
        return JavaVersion.CURRENT.newArrayType(componentType)

    def __init__(self) -> None:
        pass

    @staticmethod
    def __equal(obj1: typing.Any, obj2: typing.Any) -> bool:
        return obj1 == obj2 or (obj1 != None and obj1.equals(obj2))

    @staticmethod
    def __format(template: str, args: typing.List[typing.Any]) -> str:
        template = str(template)  # null -> "null"

        args = args if args is not None else ["(Object[])null"]

        builder = io.StringIO()
        template_start = 0
        i = 0
        while i < len(args):
            placeholder_start = template.find("%s", template_start)
            if placeholder_start == -1:
                break
            builder.write(template[template_start:placeholder_start])
            builder.write(str(args[i]))
            i += 1
            template_start = placeholder_start + 2
        builder.write(template[template_start:])

        if i < len(args):
            builder.write(" [")
            builder.write(str(args[i]))
            i += 1
            while i < len(args):
                builder.write(", ")
                builder.write(str(args[i]))
                i += 1
            builder.write("]")

        return builder.getvalue()

    @staticmethod
    def __checkArgument1(expression: bool, errorMessage: typing.Any) -> None:
        if not expression:
            raise ValueError(str(errorMessage))

    @staticmethod
    def __checkArgument0(expression: bool) -> None:
        if not expression:
            raise ValueError()

    @staticmethod
    def __checkNotNull(reference: typing.Any) -> typing.Any:

        pass  # LLM could not translate this method

    @staticmethod
    def __disallowPrimitiveType(types: typing.List[typing.Type], usedAs: str) -> None:
        for type in types:
            if isinstance(type, Class):
                cls = type
                Types.checkArgument2(
                    not cls.isPrimitive(), "Primitive type '%s' used as %s", cls, usedAs
                )

    @staticmethod
    def __filterUpperBounds(
        bounds: typing.List[typing.Type],
    ) -> typing.List[typing.Type]:

        pass  # LLM could not translate this method

    @staticmethod
    def __toArray(types: typing.Collection[typing.Type]) -> typing.List[typing.Type]:
        return list(types)

    @staticmethod
    def __newProxy(
        interfaceType: typing.Type[typing.Any], handler: typing.Callable
    ) -> typing.Any:
        Types.__checkNotNull(handler)
        Types.checkArgument2(
            interfaceType.isInterface(), "%s is not an interface", interfaceType
        )
        object = Proxy.newProxyInstance(
            interfaceType.getClassLoader(), [interfaceType], handler
        )
        return interfaceType.cast(object)

    @staticmethod
    def __newTypeVariableImpl(
        genericDeclaration: typing.Any, name: str, bounds: typing.List[typing.Type]
    ) -> typing.TypeVar("D", bound=typing.Any):
        typeVariableImpl = TypeVariableImpl[typing.Any](
            genericDeclaration, name, bounds
        )
        typeVariable = Types.__newProxy(
            TypeVariable, TypeVariableInvocationHandler(typeVariableImpl)
        )
        return typeVariable

    @staticmethod
    def __subtypeOfComponentType(bounds: typing.List[typing.Type]) -> typing.Type:

        pass  # LLM could not translate this method


TypeVariableInvocationHandler.run_static_init()

ClassOwnership.initialize_fields()

JavaVersion.initialize_fields()

JavaVersion.run_static_init()
