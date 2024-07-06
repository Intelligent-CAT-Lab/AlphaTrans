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
            that = typing.cast(GenericArrayType, obj)
            return Types.__equal(
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
        self.__componentType = JavaVersion.CURRENT.usedInGenericType0(componentType)


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
            and Types.__equal(self.getOwnerType(), that.getOwnerType())
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
        if (
            self.__ownerType is not None
            and JavaVersion.CURRENT.jdkTypeDuplicatesOwnerName()
        ):
            builder.write(JavaVersion.CURRENT.typeName(self.__ownerType) + ".")

        str_ = ""
        if self.__argumentsList is None:
            str_ = "null"
        else:
            for i in range(len(self.__argumentsList)):
                if i > 0:
                    str_ += ", "
                str_ += JavaVersion.CURRENT.typeName(self.__argumentsList[i])

        return builder.getvalue() + self.__rawType.__name__ + "<" + str_ + ">"

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

        Types.__checkNotNull(rawType)
        Types.__checkArgument0(
            len(typeArguments) == len(rawType.__dict__.get("__parameters__", []))
        )
        Types.__disallowPrimitiveType(typeArguments, "type parameter")
        self.__ownerType = ownerType
        self.__rawType = rawType
        self.__argumentsList = JavaVersion.CURRENT.usedInGenericType1(typeArguments)


class TypeVariableImpl:

    __bounds: typing.List[typing.Type] = None

    __name: str = ""

    __genericDeclaration: typing.Any = None

    def equals(self, obj: typing.Any) -> bool:

        if NativeTypeVariableEquals.NATIVE_TYPE_VARIABLE_ONLY:
            if (
                obj is not None
                and Proxy.isProxyClass(obj.__class__)
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

        Types.__disallowPrimitiveType(bounds, "bound for type variable")
        self.__genericDeclaration = Types.__checkNotNull(genericDeclaration)
        self.__name = Types.__checkNotNull(name)
        self.__bounds = list(bounds)


class TypeVariableInvocationHandler(typing.Callable):

    __typeVariableImpl: TypeVariableImpl[typing.Any] = None

    __typeVariableMethods: typing.Dict[
        str, typing.Union[inspect.Signature, typing.Callable]
    ] = None

    @staticmethod
    def run_static_init():

        # Create a new dictionary to store the methods
        builder = {}

        # Iterate over all methods in the TypeVariableImpl class
        for method in inspect.getmembers(TypeVariableImpl, inspect.isfunction):

            # If the method is declared in the TypeVariableImpl class
            if method[1].__qualname__.startswith(TypeVariableImpl.__name__):

                # Make the method accessible
                method[1].__globals__["__builtins__"]["_access_control_"] = True

                # Add the method to the dictionary
                builder[method[0]] = method[1]

        # Set the typeVariableMethods attribute to the dictionary
        TypeVariableInvocationHandler.__typeVariableMethods = builder

    def invoke(
        self,
        proxy: typing.Any,
        method: typing.Union[inspect.Signature, typing.Callable],
        args: typing.List[typing.Any],
    ) -> typing.Any:

        methodName: str = method.__name__
        typeVariableMethod: typing.Union[inspect.Signature, typing.Callable] = (
            self.__typeVariableMethods.get(methodName)
        )

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
            builder.write(JavaVersion.CURRENT.typeName(lowerBound))
        for upperBound in Types.__filterUpperBounds(self.__upperBounds):
            builder.write(" extends ")
            builder.write(JavaVersion.CURRENT.typeName(upperBound))
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
            if type is None or type in self.__visited:
                continue
            succeeded = False
            try:
                if isinstance(type, typing.TypeVar):
                    self.visitTypeVariable(type)
                elif isinstance(type, typing.Any):
                    self.visitWildcardType(type)
                elif isinstance(type, typing.Generic):
                    self.visitParameterizedType(type)
                elif isinstance(type, typing.Type):
                    self.visitClass(type)
                elif isinstance(type, typing.Union):
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

    NATIVE_TYPE_VARIABLE_ONLY: bool = None

    @staticmethod
    def initialize_fields() -> None:
        NativeTypeVariableEquals.NATIVE_TYPE_VARIABLE_ONLY: (
            bool
        ) = NativeTypeVariableEquals.class_.getTypeParameters()[
            0
        ] != newArtificialTypeVariable(
            NativeTypeVariableEquals, "X"
        )


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

        class LocalClass(Generic[T]):
            pass

        localClass = LocalClass[str]()
        subclass = type(localClass)
        parameterizedType = typing.get_type_hints(subclass)

        for behavior in ClassOwnership:
            if behavior.getOwnerType(LocalClass) == parameterizedType.get("T", None):
                return behavior

        raise AssertionError()

    def getOwnerType(self, rawType: typing.Type[typing.Any]) -> typing.Type[typing.Any]:

        if isinstance(self, ClassOwnership.LOCAL_CLASS_HAS_NO_OWNER):
            if rawType.isLocalClass():
                return None
            else:
                return rawType.getEnclosingClass()

        elif isinstance(self, ClassOwnership.OWNED_BY_ENCLOSING_CLASS):
            return rawType.getEnclosingClass()


class JavaVersion(ABC):

    CURRENT: JavaVersion = None

    JAVA9: JavaVersion = None

    JAVA7: JavaVersion = None

    JAVA6: JavaVersion = None
    JAVA6: JavaVersion = None
    JAVA8: JavaVersion = None

    @staticmethod
    def run_static_init():

        if issubclass(AnnotatedElement, TypeVariable):
            if "java.util.Map.java.util.Map" in str(
                TypeCapture[Map.Entry[str, int]].capture()
            ):
                JavaVersion.CURRENT = JavaVersion.JAVA8
            else:
                JavaVersion.CURRENT = JavaVersion.JAVA9
        elif isinstance(TypeCapture[int].capture(), type):
            JavaVersion.CURRENT = JavaVersion.JAVA7
        else:
            JavaVersion.CURRENT = JavaVersion.JAVA6

    @staticmethod
    def initialize_fields() -> None:
        JavaVersion.JAVA6: JavaVersion = type(
            "JAVA6",
            (JavaVersion,),
            {
                "newArrayType": lambda self, componentType: GenericArrayTypeImpl(
                    componentType
                ),
                "usedInGenericType0": lambda self, type: (
                    checkNotNull(type)
                    if type is not None and isinstance(type, Class) and type.isArray()
                    else type
                ),
            },
        )

        JavaVersion.JAVA6: JavaVersion = type(
            "JAVA6",
            (JavaVersion,),
            {
                "newArrayType": lambda self, componentType: GenericArrayTypeImpl(
                    componentType
                ),
                "usedInGenericType0": lambda self, type: (
                    checkNotNull(type)
                    if type is not None and isinstance(type, Class) and type.isArray()
                    else type
                ),
            },
        )

        JavaVersion.JAVA8: JavaVersion = type(
            "JAVA8",
            (JavaVersion,),
            {
                "newArrayType": lambda self, componentType: JAVA7.newArrayType(
                    componentType
                ),
                "usedInGenericType0": lambda self, type: JAVA7.usedInGenericType0(type),
                "typeName": lambda self, type: type.getTypeName(),
            },
        )

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

        if isinstance(type, type) and issubclass(type, object):
            return type.__name__
        else:
            return str(type)

    def usedInGenericType0(self, type: typing.Type) -> typing.Type:

        if type is not None and isinstance(type, type) and type.isArray():
            return GenericArrayTypeImpl(type.getComponentType())
        else:
            return checkNotNull(type)

    def newArrayType(self, componentType: typing.Type) -> typing.Type:

        if isinstance(componentType, type):
            return GenericArrayTypeImpl(componentType)
        else:
            raise TypeError("componentType must be a type")


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

        class ArrayClass:
            def __init__(self, componentType: typing.Type[typing.Any]):
                self.componentType = componentType

        return ArrayClass(componentType)

    @staticmethod
    def getComponentType(type: typing.Type) -> typing.Type:
        Types.__checkNotNull(type)
        result = AtomicReference[typing.Type]()
        TypeVisitor().visit(type)
        return result.get()

    @staticmethod
    def toString(type: typing.Type) -> str:
        return (
            type.__name__
            if isinstance(type, type) and issubclass(type, object)
            else str(type)
        )

    @staticmethod
    def supertypeOf(lowerBound: typing.Type) -> typing.Any:

        return WildcardTypeImpl([lowerBound], [object])

    @staticmethod
    def subtypeOf(upperBound: typing.Type) -> typing.Any:

        return WildcardTypeImpl([], [upperBound])

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
        Types.__checkNotNull(arguments)
        Types.checkArgument2(
            rawType.__dict__.get("__enclosing_class__") is not None,
            "Owner type for unenclosed %s",
            rawType,
        )
        return ParameterizedTypeImpl(ownerType, rawType, arguments)

    @staticmethod
    def newArrayType(componentType: typing.Type) -> typing.Type:

        if isinstance(componentType, WildcardTypeImpl):
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
        return JavaVersion.JAVA6.newArrayType(componentType)

    def __init__(self) -> None:
        pass

    @staticmethod
    def __equal(obj1: typing.Any, obj2: typing.Any) -> bool:
        return obj1 == obj2 or (obj1 is not None and obj1 == obj2)

    @staticmethod
    def __format(template: str, args: typing.List[typing.Any]) -> str:

        template = str(template)  # null -> "null"

        if args is None:
            args = [(None,)]

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
            raise RuntimeError()
        return reference

    @staticmethod
    def __disallowPrimitiveType(types: typing.List[typing.Type], usedAs: str) -> None:

        for type in types:
            if isinstance(type, type):
                cls = type
                Types.checkArgument2(
                    not cls.__dict__.get("__is_primitive__", False),
                    "Primitive type '%s' used as %s",
                    cls,
                    usedAs,
                )

    @staticmethod
    def __filterUpperBounds(
        bounds: typing.List[typing.Type],
    ) -> typing.List[typing.Type]:

        filtered: typing.List[typing.Type] = []
        for type in bounds:
            if not type == object:
                filtered.append(type)
        return filtered

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
                    if issubclass(componentType, (int, float, bool, str)):
                        return componentType
                return Types.subtypeOf(componentType)
        return None


TypeVariableInvocationHandler.run_static_init()

NativeTypeVariableEquals.initialize_fields()

ClassOwnership.initialize_fields()

JavaVersion.run_static_init()

JavaVersion.initialize_fields()
