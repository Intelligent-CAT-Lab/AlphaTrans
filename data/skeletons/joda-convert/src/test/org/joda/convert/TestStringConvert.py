# Imports Begin
from src.main.org.joda.convert.test4.Test4Interface import *
from src.main.org.joda.convert.test4.Test4Class import *
from src.main.org.joda.convert.test3.Test3SuperClass import *
from src.main.org.joda.convert.test3.Test3Class import *
from src.main.org.joda.convert.test2.Test2Interface import *
from src.main.org.joda.convert.test2.Test2Class import *
from src.main.org.joda.convert.test1.Test1Class import *
from src.main.org.joda.convert.ValidityStringConverter import *
from src.main.org.joda.convert.ValidityCheck import *
from src.main.org.joda.convert.Validity import *
from src.main.org.joda.convert.TypedStringConverter import *
from src.main.org.joda.convert.TypedFromStringConverter import *
from src.main.org.joda.convert.ToStringConverter import *
from src.main.org.joda.convert.SuperFactorySuper import *
from src.main.org.joda.convert.SuperFactorySub import *
from src.main.org.joda.convert.SubMethodMethod import *
from src.main.org.joda.convert.SubMethodConstructor import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.StringConvert import *
from src.main.org.joda.convert.ReflectionStringConverter import *
from src.main.org.joda.convert.MockIntegerStringConverter import *
from src.main.org.joda.convert.MockDistanceStringConverter import *
from src.main.org.joda.convert.MethodFromStringConverter import *
from src.main.org.joda.convert.JDKStringConverter import *
from src.main.org.joda.convert.HasCodeImpl import *
from src.main.org.joda.convert.FromStringConverter import *
from src.main.org.joda.convert.DistanceWithFactory import *
from src.main.org.joda.convert.DistanceTwoToStringAnnotations import *
from src.main.org.joda.convert.DistanceTwoFromStringMethodAnnotations import *
from src.main.org.joda.convert.DistanceToStringNoFromString import *
from src.main.org.joda.convert.DistanceToStringInvalidReturnType import *
from src.main.org.joda.convert.DistanceToStringInvalidParameters import *
from src.main.org.joda.convert.DistanceToStringException import *
from src.main.org.joda.convert.DistanceNoAnnotationsCharSequence import *
from src.main.org.joda.convert.DistanceNoAnnotations import *
from src.main.org.joda.convert.DistanceMethodMethodCharSequence import *
from src.main.org.joda.convert.DistanceMethodMethod import *
from src.main.org.joda.convert.DistanceMethodAndConstructorAnnotations import *
from src.main.org.joda.convert.DistanceFromStringNoToString import *
from src.main.org.joda.convert.DistanceFromStringInvalidReturnType import *
from src.main.org.joda.convert.DistanceFromStringInvalidParameterCount import *
from src.main.org.joda.convert.DistanceFromStringInvalidParameter import *
from src.main.org.joda.convert.DistanceFromStringException import *
from src.main.org.joda.convert.DistanceFromStringConstructorInvalidParameterCount import *
from src.main.org.joda.convert.DistanceFromStringConstructorInvalidParameter import *
from src.main.org.joda.convert.ConstructorFromStringConverter import *
from src.main.org.joda.convert.AltCharSequence import *
import typing

# Imports End


class TestStringConvert:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def test_convert_toString(self) -> None:
        pass

    def ttest_registerMethodConstructor_cannotChangeSingleton(self) -> None:
        pass

    def test_registerMethodConstructor_noSuchConstructor(self) -> None:
        pass

    def test_registerMethodConstructor_nullToString(self) -> None:
        pass

    def test_registerMethodConstructor_nullClass(self) -> None:
        pass

    def test_registerMethods_classAlreadyRegistered(self) -> None:
        pass

    def ttest_registerMethods_cannotChangeSingleton(self) -> None:
        pass

    def test_registerMethods_noSuchFromStringMethod(self) -> None:
        pass

    def test_registerMethods_invalidToStringMethod(self) -> None:
        pass

    def test_registerMethods_noSuchToStringMethod(self) -> None:
        pass

    def test_registerMethods_nullFromString(self) -> None:
        pass

    def test_registerMethods_nullToString(self) -> None:
        pass

    def test_registerMethods_nullClass(self) -> None:
        pass

    def test_registerMethodsCharSequence(self) -> None:
        pass

    def test_registerMethods(self) -> None:
        pass

    def test_registerFactory_cannotChangeSingleton(self) -> None:
        pass

    def test_register_FunctionalInterfaces_nullFromString(self) -> None:
        pass

    def test_register_FunctionalInterfaces_nullToString(self) -> None:
        pass

    def test_register_FunctionalInterfaces_nullClass(self) -> None:
        pass

    def test_register_FunctionalInterfaces(self) -> None:
        pass

    def test_register_classAlreadyRegistered(self) -> None:
        pass

    def test_register_notOnShared(self) -> None:
        pass

    def test_register_converterNotNull(self) -> None:
        pass

    def test_register_classNotNull(self) -> None:
        pass

    def test_convert_Enum_overrideDefaultWithConverter(self) -> None:
        pass

    def test_convert_annotatedTwoFromStringMethod(self) -> None:
        pass

    def test_convert_annotatedFromStringNoToString(self) -> None:
        pass

    def test_convert_annotatedToStringNoFromString(self) -> None:
        pass

    def test_convert_annotatedFromStringConstructorInvalidParameterCount(self) -> None:
        pass

    def test_convert_annotatedFromStringConstructorInvalidParameter(self) -> None:
        pass

    def test_convert_annotatedFromStringInvalidParameterCount(self) -> None:
        pass

    def test_convert_annotatedFromStringInvalidParameter(self) -> None:
        pass

    def test_convert_annotatedFromStringInvalidReturnType(self) -> None:
        pass

    def test_convert_annotatedToStringInvalidParameters(self) -> None:
        pass

    def test_convert_annotatedToStringInvalidReturnType(self) -> None:
        pass

    def test_convert_annotatedTwoToString(self) -> None:
        pass

    def test_convert_annotatedMethodAndConstructor(self) -> None:
        pass

    def test_convert_annotationNoMethods(self) -> None:
        pass

    def test_convert_annotation_FromStringFactoryClashingMethods_fromInterface(
        self,
    ) -> None:
        pass

    def test_convert_annotation_FromStringFactoryClashingMethods_fromClass(
        self,
    ) -> None:
        pass

    def test_convert_annotation_ToStringFromStringOnSuperClassBeatsInterface(
        self,
    ) -> None:
        pass

    def test_convert_annotation_FactoryAndToStringOnInterface_usingInterface(
        self,
    ) -> None:
        pass

    def test_convert_annotation_FactoryAndToStringOnInterface(self) -> None:
        pass

    def test_convert_annotation_ToStringOnInterface(self) -> None:
        pass

    def test_convert_annotationFactoryMethod(self) -> None:
        pass

    def test_convert_annotationFromStringInvokeException(self) -> None:
        pass

    def test_convert_annotationToStringInvokeException(self) -> None:
        pass

    def test_convert_annotationSuperFactorySubViaSub2(self) -> None:
        pass

    def test_convert_annotationSuperFactorySubViaSub1(self) -> None:
        pass

    def test_convert_annotationSuperFactorySubViaSuper(self) -> None:
        pass

    def test_convert_annotationSuperFactorySuper(self) -> None:
        pass

    def test_convert_annotationSubMethodConstructor(self) -> None:
        pass

    def test_convert_annotationSubMethodMethod(self) -> None:
        pass

    def test_convert_annotationMethodBridgeMethod(self) -> None:
        pass

    def test_convert_annotationMethodMethodCharSequence(self) -> None:
        pass

    def test_convert_annotationMethodMethod(self) -> None:
        pass

    def test_findConverterNoGenerics_Object(self) -> None:
        pass

    def test_findConverterNoGenerics_null(self) -> None:
        pass

    def test_findConverterNoGenerics(self) -> None:
        pass

    def test_findConverter_Object(self) -> None:
        pass

    def test_findConverter_null(self) -> None:
        pass

    def test_findConverter(self) -> None:
        pass

    def test_convertFromString_nullClass(self) -> None:
        pass

    def test_convertFromString_null(self) -> None:
        pass

    def test_convertFromString_inheritNotSearchedFor(self) -> None:
        pass

    def test_convertFromString_inherit(self) -> None:
        pass

    def test_convertFromString_enumSubclass(self) -> None:
        pass

    def test_convertFromString_primitiveBoolean(self) -> None:
        pass

    def test_convertFromString_primitiveInt(self) -> None:
        pass

    def test_convertFromString(self) -> None:
        pass

    def test_convertToString_withType_nullClass(self) -> None:
        pass

    def test_convertToString_withType_null(self) -> None:
        pass

    def test_convertToString_withType_inherit1(self) -> None:
        pass

    def test_convertToString_withType_primitive2(self) -> None:
        pass

    def test_convertToString_withType_primitive1(self) -> None:
        pass

    def test_convertToString_withType_noGenerics(self) -> None:
        pass

    def test_convertToString_withType(self) -> None:
        pass

    def test_convertToString_null(self) -> None:
        pass

    def test_convertToString_inherit(self) -> None:
        pass

    def test_convertToString_primitive(self) -> None:
        pass

    def test_convertToString(self) -> None:
        pass

    def test_isConvertible(self) -> None:
        pass

    def test_constructor_false(self) -> None:
        pass

    def test_constructor_true(self) -> None:
        pass

    def test_constructor(self) -> None:
        pass

    def test_register_distance(self) -> None:
        pass

    def __assertFromStringConverter(
        self, conv: StringConverter[typing.Any], expectedType: typing.Type[typing.Any]
    ) -> None:
        pass

    # Class Methods End


class ToStringConverter:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def convertToString(self, object: DistanceNoAnnotations) -> str:
        pass

    # Class Methods End


class FromStringConverter:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def convertFromString(
        self, cls: typing.Type[DistanceNoAnnotations], str: str
    ) -> DistanceNoAnnotations:
        pass

    # Class Methods End
