from __future__ import annotations
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
            that = typing.cast(GenericArrayType, obj)
            return self.__equal(
                self.getGenericComponentType(), that.getGenericComponentType()
            )
        return False

    def hashCode(self) -> int:

        return hash(self.__componentType)

    def toString(self) -> str:

        return Types.toString(self.__componentType) + "[]"

    def getGenericComponentType(self) -> typing.Type:

        return self.__componentType

    def __init__(self, componentType: typing.Type) -> None:

        self.__componentType = self.usedInGenericType0(componentType)


class ParameterizedTypeImpl(typing.Generic[typing.TypeVar("T")]):

    __serialVersionUID: int = 0
    __rawType: typing.Type[typing.Any] = None
    __argumentsList: typing.List[typing.Type] = None
    __ownerType: typing.Type = None

    def equals(self, other: typing.Any) -> bool:

        if not isinstance(other, ParameterizedType):
            return False
        that = typing.cast(ParameterizedType, other)
        return (
            self.getRawType() == that.getRawType()
            and self.__equal(self.getOwnerType(), that.getOwnerType())
            and self.getActualTypeArguments() == that.getActualTypeArguments()
        )

    def hashCode(self) -> int:

        return (
            (0 if self.__ownerType is None else hash(self.__ownerType))
            ^ hash(tuple(self.__argumentsList))
            ^ hash(self.__rawType)
        )

    def toString(self) -> str:

        builder = io.StringIO()
        if self.__ownerType is not None and self.jdkTypeDuplicatesOwnerName():
            builder.write(self.typeName(self.__ownerType) + ".")

        str_val = ""
        if self.__argumentsList is None:
            str_val = "null"
        else:
            for i in range(len(self.__argumentsList)):
                if i > 0:
                    str_val += ", "
                str_val += self.typeName(self.__argumentsList[i])

        return builder.getvalue() + self.__rawType.getName() + "<" + str_val + ">"

    def getOwnerType(self) -> typing.Type:

        return self.__ownerType

    def getRawType(self) -> typing.Type:

        return self.__rawType

    def getActualTypeArguments(self) -> typing.List[typing.Type]:

        return self.__toArray(self.__argumentsList)

    def __init__(
        self,
        ownerType: typing.Type,
        rawType: typing.Type[typing.Any],
        typeArguments: typing.List[typing.Type],
    ) -> None:

        self.__checkNotNull(rawType)
        self.__checkArgument0(len(typeArguments) == len(rawType.__parameters__))
        self.__disallowPrimitiveType(typeArguments, "type parameter")
        self.__ownerType = ownerType
        self.__rawType = rawType
        self.__argumentsList = self.usedInGenericType1(typeArguments)


class TypeVariableImpl:

    __bounds: typing.List[typing.Type] = None
    __name: str = None
    __genericDeclaration: typing.Any = None

    def equals(self, obj: typing.Any) -> bool:

        if NativeTypeVariableEquals.NATIVE_TYPE_VARIABLE_ONLY:
            if (
                obj is not None
                and Proxy.isProxyClass(type(obj))
                and Proxy.getInvocationHandler(obj) is not None
                and isinstance(
                    Proxy.getInvocationHandler(obj), TypeVariableInvocationHandler
                )
            ):
                typeVariableInvocationHandler = Proxy.getInvocationHandler(obj)
                that = typeVariableInvocationHandler.typeVariableImpl
                return (
                    self.__name == that.getName()
                    and self.__genericDeclaration == that.getGenericDeclaration()
                    and self.__bounds == that.bounds
                )
            return False
        else:
            if isinstance(obj, TypeVariable):
                that = obj
                return (
                    self.__name == that.getName()
                    and self.__genericDeclaration == that.getGenericDeclaration()
                )
            return False

    def hashCode(self) -> int:

        return hash(self.__genericDeclaration) ^ hash(self.__name)

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

        self.__disallowPrimitiveType(bounds, "bound for type variable")
        self.__genericDeclaration = self.__checkNotNull(genericDeclaration)
        self.__name = self.__checkNotNull(name)
        self.__bounds = list(bounds)


class TypeVariableInvocationHandler(typing.Callable):

    __typeVariableImpl: TypeVariableImpl[typing.Any] = None
    __typeVariableMethods: typing.Dict[
        str, typing.Union[inspect.Signature, typing.Callable]
    ] = None

    def invoke(
        self,
        proxy: typing.Any,
        method: typing.Union[inspect.Signature, typing.Callable],
        args: typing.List[typing.Any],
    ) -> typing.Any:

        methodName = method.__name__
        typeVariableMethod = self.__typeVariableMethods.get(methodName)

        if typeVariableMethod is None:
            raise NotImplementedError(methodName)
        else:
            try:
                return typeVariableMethod(self.__typeVariableImpl, *args)
            except Exception as e:
                raise e.__cause__

    def __init__(self, typeVariableImpl: TypeVariableImpl[typing.Any]) -> None:

        self.__typeVariableImpl = typeVariableImpl


class WildcardTypeImpl:

    __serialVersionUID: int = 0
    __upperBounds: typing.List[typing.Type] = None
    __lowerBounds: typing.List[typing.Type] = None

    def toString(self) -> str:

        builder = io.StringIO()
        builder.write("?")

        for lowerBound in self.__lowerBounds:
            builder.write(" super ")
            builder.write(self.typeName(lowerBound))

        for upperBound in self.__filterUpperBounds(self.__upperBounds):
            builder.write(" extends ")
            builder.write(self.typeName(upperBound))

        return builder.getvalue()

    def hashCode(self) -> int:

        return hash(tuple(self.__lowerBounds)) ^ hash(tuple(self.__upperBounds))

    def equals(self, obj: typing.Any) -> bool:

        if isinstance(obj, WildcardType):
            that = typing.cast(WildcardType, obj)
            return self.__lowerBounds == list(
                that.getLowerBounds()
            ) and self.__upperBounds == list(that.getUpperBounds())
        return False

    def getUpperBounds(self) -> typing.List[typing.Type]:

        return self.__upperBounds

    def getLowerBounds(self) -> typing.List[typing.Type]:

        return self.__lowerBounds

    def __init__(
        self,
        lowerBounds: typing.List[typing.Type],
        upperBounds: typing.List[typing.Type],
    ) -> None:

        self.__disallowPrimitiveType(lowerBounds, "lower bound for wildcard")
        self.__disallowPrimitiveType(upperBounds, "upper bound for wildcard")
        self.__lowerBounds = self.usedInGenericType1(lowerBounds)
        self.__upperBounds = self.usedInGenericType1(upperBounds)


class TypeVisitor(ABC):

    __visited: typing.Set[typing.Type] = set()

    def visit(self, types: typing.List[typing.Type]) -> None:

        for type in types:
            if type is None or type in self.__visited:
                continue
            self.__visited.add(type)
            succeeded = False
            try:
                if isinstance(type, typing.TypeVar):
                    self.visitTypeVariable(type)
                elif isinstance(type, typing.Generic):
                    self.visitParameterizedType(type)
                elif isinstance(type, typing.Type):
                    self.visitClass(type)
                elif isinstance(type, typing.List):
                    self.visitGenericArrayType(type)
                else:
                    raise AssertionError("Unknown type: " + str(type))
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

        pass

    def visitClass(self, t: typing.Type[typing.Any]) -> None:

        pass


class NativeTypeVariableEquals:

    NATIVE_TYPE_VARIABLE_ONLY: bool = NativeTypeVariableEquals.__dict__[
        "__orig_bases__"
    ][0].__args__[0] != typing.TypeVar("X")


class LocalClass:

    pass


class ClassOwnership(ABC):

    JVM_BEHAVIOR: ClassOwnership = detectJvmBehavior()
    LOCAL_CLASS_HAS_NO_OWNER: ClassOwnership = None
    OWNED_BY_ENCLOSING_CLASS: ClassOwnership = None

    @staticmethod
    def __detectJvmBehavior() -> ClassOwnership:

        class LocalClass(Generic[T]):
            pass

        localClass = LocalClass[str]()
        subclass = type(localClass)
        parameterizedType = typing.get_args(subclass.__orig_bases__[0])[0]

        for behavior in ClassOwnership:
            if behavior.getOwnerType(LocalClass) == parameterizedType.__origin__:
                return behavior

        raise AssertionError()

    def getOwnerType(self, rawType: typing.Type[typing.Any]) -> typing.Type[typing.Any]:

        pass


class JavaVersion(ABC):

    CURRENT: JavaVersion = None
    JAVA9: JavaVersion = None

    JAVA8: JavaVersion = type(
        "JAVA8",
        (JavaVersion,),
        {
            "newArrayType": lambda self, componentType: self.JAVA7.newArrayType(
                componentType
            ),
            "usedInGenericType0": lambda self, type: self.JAVA7.usedInGenericType0(
                type
            ),
            "typeName": lambda self, type: self.getTypeName(type),
            "getTypeName": lambda self, type: self.invokeGetTypeName(type),
        },
    )
    JAVA7: JavaVersion = None

    JAVA6: JavaVersion = JavaVersion()

    def usedInGenericType1(
        self, types: typing.List[typing.Type]
    ) -> typing.List[typing.Type]:

        builder = []
        for type in types:
            builder.append(self.usedInGenericType0(type))
        return builder

    def jdkTypeDuplicatesOwnerName(self) -> bool:

        return True

    def typeName(self, type: typing.Type) -> str:

        return self.toString(type)

    def usedInGenericType0(self, type: typing.Type) -> typing.Type:

        pass

    def newArrayType(self, componentType: typing.Type) -> typing.Type:

        class ArrayType(typing.Generic[componentType]):
            pass

        return ArrayType


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
    def __format(template: str, args: typing.List[typing.Any]) -> str:
        return template.format(*args)

    @staticmethod
    def getArrayClass(
        componentType: typing.Type[typing.Any],
    ) -> typing.Type[typing.Any]:

        class ArrayClass(ABC):
            pass

        class ArrayClass(ArrayClass, componentType):
            pass

        return ArrayClass

    @staticmethod
    def getComponentType(type: typing.Type) -> typing.Type:

        class TypeVisitor:
            def __init__(self):
                self.result = None

            def visitTypeVariable(self, t: typing.TypeVar) -> None:
                self.result = Types.subtypeOfComponentType(t.__bound__)

            def visitWildcardType(self, t: typing.Type) -> None:
                self.result = Types.subtypeOfComponentType(t.__constraints__)

            def visitGenericArrayType(self, t: typing.Type) -> None:
                self.result = t.__args__[0]

            def visitClass(self, t: typing.Type) -> None:
                self.result = t.__component_type__

        TypeVisitor.__checkNotNull(type)
        visitor = TypeVisitor()
        visitor.visit(type)
        return visitor.result

    @staticmethod
    def toString(type: typing.Type) -> str:

        if isinstance(type, type(ABC)):
            return type.__name__
        else:
            return type.toString()

    @staticmethod
    def supertypeOf(lowerBound: typing.Type) -> typing.Any:

        class WildcardTypeImpl(typing.Generic[T], typing.Protocol):
            def __init__(
                self,
                lowerBounds: typing.List[typing.Type],
                upperBounds: typing.List[typing.Type],
            ) -> None:
                self.lowerBounds = lowerBounds
                self.upperBounds = upperBounds

        return WildcardTypeImpl([lowerBound], [object])

    @staticmethod
    def subtypeOf(upperBound: typing.Type) -> typing.Any:

        class WildcardTypeImpl(typing.Generic[T], typing.Protocol):
            def __init__(
                self,
                lowerBounds: typing.List[typing.Type],
                upperBounds: typing.List[typing.Type],
            ) -> None:
                self.lowerBounds = lowerBounds
                self.upperBounds = upperBounds

        return WildcardTypeImpl(list(), [upperBound])

    @staticmethod
    def newArtificialTypeVariable(
        declaration: typing.Any, name: str, bounds: typing.List[typing.Type]
    ) -> typing.TypeVar("D", bound=typing.Any):

        if len(bounds) == 0:
            bounds = [object]

        return Types.__newTypeVariableImpl(declaration, name, bounds)

    @staticmethod
    def newParameterizedType(
        rawType: typing.Type[typing.Any], arguments: typing.List[typing.Type]
    ) -> typing.Generic[typing.TypeVar("T")]:

        class ParameterizedTypeImpl(Types):
            def __init__(
                self,
                ownerType: typing.Type,
                rawType: typing.Type[typing.Any],
                typeArguments: typing.List[typing.Type],
            ) -> None:
                self.ownerType = ownerType
                self.rawType = rawType
                self.typeArguments = typeArguments

        return ParameterizedTypeImpl(Types.getOwnerType(rawType), rawType, arguments)

    @staticmethod
    def newParameterizedTypeWithOwner(
        ownerType: typing.Type,
        rawType: typing.Type[typing.Any],
        arguments: typing.List[typing.Type],
    ) -> typing.Generic[typing.TypeVar("T")]:

        if ownerType is None:
            return Types.newParameterizedType(rawType, arguments)

        Types.__checkNotNull(arguments)
        Types.checkArgument2(
            rawType.getEnclosingClass() is not None,
            "Owner type for unenclosed %s",
            rawType,
        )

        return Types(ownerType, rawType, arguments)

    @staticmethod
    def newArrayType(componentType: typing.Type) -> typing.Type:

        if isinstance(componentType, WildcardType):
            wildcard = componentType
            lowerBounds = wildcard.getLowerBounds()
            Types.__checkArgument1(
                len(lowerBounds) <= 1,
                "Wildcard cannot have more than one lower bounds.",
            )
            if len(lowerBounds) == 1:
                return Types.supertypeOf(Types.newArrayType(lowerBounds[0]))
            else:
                upperBounds = wildcard.getUpperBounds()
                Types.__checkArgument1(
                    len(upperBounds) == 1, "Wildcard should have only one upper bound."
                )
                return Types.subtypeOf(Types.newArrayType(upperBounds[0]))
        return JavaVersion.CURRENT.newArrayType(componentType)

    def __init__(self) -> None:

        pass

    @staticmethod
    def __equal(obj1: typing.Any, obj2: typing.Any) -> bool:

        return obj1 == obj2 or (obj1 is not None and obj1.equals(obj2))

    @staticmethod
    def __format(template: str, args: typing.List[typing.Any]) -> str:

        if args is None:
            args = ["(Object[])null"]

        builder = io.StringIO()
        template_start = 0
        i = 0
        while i < len(args):
            placeholder_start = template.find("%s", template_start)
            if placeholder_start == -1:
                break
            builder.write(template[template_start:placeholder_start])
            builder.write(str(args[i]))
            template_start = placeholder_start + 2
            i += 1

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

        if reference is None:
            raise NullPointerException()
        return reference

    @staticmethod
    def __disallowPrimitiveType(types: typing.List[typing.Type], usedAs: str) -> None:

        for type in types:
            if isinstance(type, type):
                cls = type
                if cls.__name__ in [
                    "bool",
                    "int",
                    "float",
                    "complex",
                    "str",
                    "bytes",
                    "bytearray",
                    "memoryview",
                    "range",
                    "tuple",
                    "frozenset",
                ]:
                    Types.checkArgument2(
                        False,
                        "Primitive type '%s' used as %s" % (cls.__name__, usedAs),
                        [],
                    )

    @staticmethod
    def __filterUpperBounds(
        bounds: typing.List[typing.Type],
    ) -> typing.List[typing.Type]:

        filtered = []
        for type in bounds:
            if type != object:
                filtered.append(type)
        return filtered

    @staticmethod
    def __toArray(types: typing.Collection[typing.Type]) -> typing.List[typing.Type]:

        return list(types)

    @staticmethod
    def __newProxy(
        interfaceType: typing.Type[typing.Any], handler: typing.Callable
    ) -> typing.Any:

        # Check if handler is not None
        if handler is None:
            raise ValueError("handler must not be None")

        # Check if interfaceType is an interface
        if not inspect.isclass(interfaceType) or not issubclass(interfaceType, ABC):
            raise ValueError(f"{interfaceType} is not an interface")

        # Create a new proxy instance
        object = Proxy.newProxyInstance(
            interfaceType.__class__.__class_loader__, [interfaceType], handler
        )

        # Cast the object to the interface type
        return interfaceType.cast(object)

    @staticmethod
    def __newTypeVariableImpl(
        genericDeclaration: typing.Any, name: str, bounds: typing.List[typing.Type]
    ) -> typing.TypeVar("D", bound=typing.Any):

        class TypeVariableImpl(typing.Generic[D], ABC):
            def __init__(
                self, genericDeclaration: D, name: str, bounds: typing.List[typing.Type]
            ):
                self.genericDeclaration = genericDeclaration
                self.name = name
                self.bounds = bounds

        class TypeVariableInvocationHandler(ABC):
            def __init__(self, typeVariableImpl: TypeVariableImpl[D]):
                self.typeVariableImpl = typeVariableImpl

        typeVariableImpl = TypeVariableImpl(genericDeclaration, name, bounds)
        typeVariable = Types.__newProxy(
            TypeVariable, TypeVariableInvocationHandler(typeVariableImpl)
        )
        return typeVariable

    @staticmethod
    def __subtypeOfComponentType(bounds: typing.List[typing.Type]) -> typing.Type:

        for bound in bounds:
            componentType = Types.getComponentType(bound)
            if componentType is not None:
                if isinstance(componentType, type):
                    componentClass = componentType
                    if componentClass in (int, float, bool, str):
                        return componentClass
                return Types.subtypeOf(componentType)
        return None
