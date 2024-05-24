from __future__ import annotations

# Imports Begin
from src.main.org.joda.convert.TypeCapture import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class GenericArrayTypeImpl:

    # Class Fields Begin
    __componentType: typing.Type = None
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def equals(self, obj: typing.Any) -> bool:
        pass

    def hashCode(self) -> int:
        pass

    def toString(self) -> str:
        pass

    def getGenericComponentType(self) -> typing.Type:
        pass

    def __init__(self, componentType: typing.Type) -> None:
        pass

    # Class Methods End


class ParameterizedTypeImpl(typing.Generic[typing.TypeVar("T")]):

    # Class Fields Begin
    __ownerType: typing.Type = None
    __argumentsList: typing.List[typing.Type] = None
    __rawType: typing.Type[typing.Any] = None
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def equals(self, other: typing.Any) -> bool:
        pass

    def hashCode(self) -> int:
        pass

    def toString(self) -> str:
        pass

    def getOwnerType(self) -> typing.Type:
        pass

    def getRawType(self) -> typing.Type:
        pass

    def getActualTypeArguments(self) -> typing.List[typing.Type]:
        pass

    def __init__(
        self,
        ownerType: typing.Type,
        rawType: typing.Type[typing.Any],
        typeArguments: typing.List[typing.Type],
    ) -> None:
        pass

    # Class Methods End


class TypeVariableImpl:

    # Class Fields Begin
    __genericDeclaration: typing.Any = None
    __name: str = None
    __bounds: typing.List[typing.Type] = None
    # Class Fields End

    # Class Methods Begin
    def equals(self, obj: typing.Any) -> bool:
        pass

    def hashCode(self) -> int:
        pass

    def toString(self) -> str:
        pass

    def getName(self) -> str:
        pass

    def getGenericDeclaration(self) -> typing.Any:
        pass

    def __init__(
        self,
        genericDeclaration: typing.Any,
        name: str,
        bounds: typing.List[typing.Type],
    ) -> None:
        pass

    # Class Methods End


class TypeVariableInvocationHandler(typing.Callable):

    # Class Fields Begin
    __typeVariableMethods: typing.Dict[
        str, typing.Union[inspect.Signature, typing.Callable]
    ] = None
    __typeVariableImpl: TypeVariableImpl[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def invoke(
        self,
        proxy: typing.Any,
        method: typing.Union[inspect.Signature, typing.Callable],
        args: typing.List[typing.Any],
    ) -> typing.Any:
        pass

    def __init__(self, typeVariableImpl: TypeVariableImpl[typing.Any]) -> None:
        pass

    # Class Methods End


class WildcardTypeImpl:

    # Class Fields Begin
    __lowerBounds: typing.List[typing.Type] = None
    __upperBounds: typing.List[typing.Type] = None
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def hashCode(self) -> int:
        pass

    def equals(self, obj: typing.Any) -> bool:
        pass

    def getUpperBounds(self) -> typing.List[typing.Type]:
        pass

    def getLowerBounds(self) -> typing.List[typing.Type]:
        pass

    def __init__(
        self,
        lowerBounds: typing.List[typing.Type],
        upperBounds: typing.List[typing.Type],
    ) -> None:
        pass

    # Class Methods End


class TypeVisitor(ABC):

    # Class Fields Begin
    __visited: typing.Set[typing.Type] = None
    # Class Fields End

    # Class Methods Begin
    def visit(self, types: typing.List[typing.Type]) -> None:
        pass

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
        pass

    def visitClass(self, t: typing.Type[typing.Any]) -> None:
        pass

    # Class Methods End


class ClassOwnership:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    # Class Methods End

    pass


class JavaVersion:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def jdkTypeDuplicatesOwnerName(self) -> bool:
        pass

    # Class Methods End


class NativeTypeVariableEquals:

    # Class Fields Begin
    NATIVE_TYPE_VARIABLE_ONLY: bool = None
    # Class Fields End

    # Class Methods Begin
    # Class Methods End


class LocalClass:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    # Class Methods End

    pass


class LocalClass:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    # Class Methods End

    pass


class TypeVisitor:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def visitClass(self, t: typing.Type[typing.Any]) -> None:
        pass

    def visitGenericArrayType(
        self,
        t: typing.Union[
            typing.List[typing.TypeVar("T", bound=typing.Any)], array.array
        ],
    ) -> None:
        pass

    def visitWildcardType(self, t: typing.Any) -> None:
        pass

    def visitTypeVariable(self, t: typing.TypeVar("T", bound=typing.Any)) -> None:
        pass

    # Class Methods End


class TypeCapture:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    # Class Methods End

    pass


class TypeCapture:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    # Class Methods End

    pass


class ClassOwnership(ABC):

    # Class Fields Begin
    OWNED_BY_ENCLOSING_CLASS: ClassOwnership = None
    LOCAL_CLASS_HAS_NO_OWNER: ClassOwnership = None
    JVM_BEHAVIOR: ClassOwnership = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def __detectJvmBehavior() -> ClassOwnership:
        pass

    def getOwnerType(self, rawType: typing.Type[typing.Any]) -> typing.Type[typing.Any]:
        pass

    # Class Methods End


class JavaVersion(ABC):

    # Class Fields Begin
    JAVA6: JavaVersion = None
    JAVA7: JavaVersion = None
    JAVA8: JavaVersion = None
    JAVA9: JavaVersion = None
    CURRENT: JavaVersion = None
    # Class Fields End

    # Class Methods Begin
    def usedInGenericType1(
        self, types: typing.List[typing.Type]
    ) -> typing.List[typing.Type]:
        pass

    def jdkTypeDuplicatesOwnerName(self) -> bool:
        pass

    def typeName(self, type: typing.Type) -> str:
        pass

    def usedInGenericType0(self, type: typing.Type) -> typing.Type:
        pass

    def newArrayType(self, componentType: typing.Type) -> typing.Type:
        pass

    # Class Methods End


class Types:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def checkArgument2(
        expression: bool,
        errorMessageTemplate: str,
        errorMessageArgs: typing.List[typing.Any],
    ) -> None:
        pass

    @staticmethod
    def getArrayClass(
        componentType: typing.Type[typing.Any],
    ) -> typing.Type[typing.Any]:
        pass

    @staticmethod
    def getComponentType(type: typing.Type) -> typing.Type:
        pass

    @staticmethod
    def toString(type: typing.Type) -> str:
        pass

    @staticmethod
    def supertypeOf(lowerBound: typing.Type) -> typing.Any:
        pass

    @staticmethod
    def subtypeOf(upperBound: typing.Type) -> typing.Any:
        pass

    @staticmethod
    def newArtificialTypeVariable(
        declaration: typing.Any, name: str, bounds: typing.List[typing.Type]
    ) -> typing.TypeVar("D", bound=typing.Any):
        pass

    @staticmethod
    def newParameterizedType(
        rawType: typing.Type[typing.Any], arguments: typing.List[typing.Type]
    ) -> typing.Generic[typing.TypeVar("T")]:
        pass

    @staticmethod
    def newParameterizedTypeWithOwner(
        ownerType: typing.Type,
        rawType: typing.Type[typing.Any],
        arguments: typing.List[typing.Type],
    ) -> typing.Generic[typing.TypeVar("T")]:
        pass

    @staticmethod
    def newArrayType(componentType: typing.Type) -> typing.Type:
        pass

    def __init__(self) -> None:
        pass

    @staticmethod
    def __equal(obj1: typing.Any, obj2: typing.Any) -> bool:
        pass

    @staticmethod
    def __format(template: str, args: typing.List[typing.Any]) -> str:
        pass

    @staticmethod
    def __checkArgument1(expression: bool, errorMessage: typing.Any) -> None:
        pass

    @staticmethod
    def __checkArgument0(expression: bool) -> None:
        pass

    @staticmethod
    def __checkNotNull(reference: typing.Any) -> typing.Any:
        pass

    @staticmethod
    def __disallowPrimitiveType(types: typing.List[typing.Type], usedAs: str) -> None:
        pass

    @staticmethod
    def __filterUpperBounds(
        bounds: typing.List[typing.Type],
    ) -> typing.List[typing.Type]:
        pass

    @staticmethod
    def __toArray(types: typing.Collection[typing.Type]) -> typing.List[typing.Type]:
        pass

    @staticmethod
    def __newProxy(
        interfaceType: typing.Type[typing.Any], handler: typing.Callable
    ) -> typing.Any:
        pass

    @staticmethod
    def __newTypeVariableImpl(
        genericDeclaration: typing.Any, name: str, bounds: typing.List[typing.Type]
    ) -> typing.TypeVar("D", bound=typing.Any):
        pass

    @staticmethod
    def __subtypeOfComponentType(bounds: typing.List[typing.Type]) -> typing.Type:
        pass

    # Class Methods End
