from __future__ import annotations
import io
import enum
import typing
from typing import *
from src.test.org.joda.convert.AltCharSequence import *
from src.main.org.joda.convert.ConstructorFromStringConverter import *
from src.test.org.joda.convert.DistanceFromStringConstructorInvalidParameter import *
from src.test.org.joda.convert.DistanceFromStringConstructorInvalidParameterCount import *
from src.test.org.joda.convert.DistanceFromStringException import *
from src.test.org.joda.convert.DistanceFromStringInvalidParameter import *
from src.test.org.joda.convert.DistanceFromStringInvalidParameterCount import *
from src.test.org.joda.convert.DistanceFromStringInvalidReturnType import *
from src.test.org.joda.convert.DistanceFromStringNoToString import *
from src.test.org.joda.convert.DistanceMethodAndConstructorAnnotations import *
from src.test.org.joda.convert.DistanceMethodMethod import *
from src.test.org.joda.convert.DistanceMethodMethodCharSequence import *
from src.test.org.joda.convert.DistanceNoAnnotations import *
from src.test.org.joda.convert.DistanceNoAnnotationsCharSequence import *
from src.test.org.joda.convert.DistanceToStringException import *
from src.test.org.joda.convert.DistanceToStringInvalidParameters import *
from src.test.org.joda.convert.DistanceToStringInvalidReturnType import *
from src.test.org.joda.convert.DistanceToStringNoFromString import *
from src.test.org.joda.convert.DistanceTwoFromStringMethodAnnotations import *
from src.test.org.joda.convert.DistanceTwoToStringAnnotations import *
from src.test.org.joda.convert.DistanceWithFactory import *
from src.main.org.joda.convert.FromStringConverter import *
from src.test.org.joda.convert.HasCodeImpl import *
from src.main.org.joda.convert.JDKStringConverter import *
from src.main.org.joda.convert.MethodFromStringConverter import *
from src.test.org.joda.convert.MockDistanceStringConverter import *
from src.test.org.joda.convert.MockIntegerStringConverter import *
from src.main.org.joda.convert.ReflectionStringConverter import *
from src.main.org.joda.convert.StringConvert import *
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.test.org.joda.convert.SubMethodConstructor import *
from src.test.org.joda.convert.SubMethodMethod import *
from src.test.org.joda.convert.SuperFactorySub import *
from src.test.org.joda.convert.SuperFactorySuper import *
from src.main.org.joda.convert.ToStringConverter import *
from src.main.org.joda.convert.TypedFromStringConverter import *
from src.main.org.joda.convert.TypedStringConverter import *
from src.test.org.joda.convert.Validity import *
from src.test.org.joda.convert.ValidityCheck import *
from src.test.org.joda.convert.ValidityStringConverter import *
from src.test.org.joda.convert.test1.Test1Class import *
from src.test.org.joda.convert.test2.Test2Class import *
from src.test.org.joda.convert.test2.Test2Interface import *
from src.test.org.joda.convert.test3.Test3Class import *
from src.test.org.joda.convert.test3.Test3SuperClass import *
from src.test.org.joda.convert.test4.Test4Class import *
from src.test.org.joda.convert.test4.Test4Interface import *


class TestStringConvert:

    def test_convert_toString(self) -> None:

        # Create an instance of StringConvert
        string_convert = StringConvert()

        # Call the toString method and compare the result
        self.assertEqual("StringConvert", string_convert.toString())

    def ttest_registerMethodConstructor_cannotChangeSingleton(self) -> None:

        StringConvert.INSTANCE.registerMethodConstructor(
            DistanceNoAnnotationsCharSequence, "toString"
        )

    def test_registerMethodConstructor_noSuchConstructor(self) -> None:

        test = StringConvert.StringConvert1()
        test.registerMethodConstructor(enum.Enum, "toString")

    def test_registerMethodConstructor_nullToString(self) -> None:

        test = StringConvert.StringConvert1()
        test.registerMethodConstructor(DistanceNoAnnotations, None)

    def test_registerMethodConstructor_nullClass(self) -> None:

        test = StringConvert.StringConvert1()
        test.registerMethodConstructor(None, "toString")

    def test_registerMethods_classAlreadyRegistered(self) -> None:

        test = StringConvert.StringConvert1()
        test.registerMethods(DistanceNoAnnotations, "toString", "parse")
        test.registerMethods(DistanceNoAnnotations, "toString", "parse")

    def ttest_registerMethods_cannotChangeSingleton(self) -> None:

        StringConvert.INSTANCE.registerMethods(
            DistanceNoAnnotationsCharSequence, "toString", "parse"
        )

    def test_registerMethods_noSuchFromStringMethod(self) -> None:

        test = StringConvert.StringConvert1()
        test.registerMethods(DistanceNoAnnotations, "toString", "rubbishName")

    def test_registerMethods_invalidToStringMethod(self) -> None:

        test = StringConvert.StringConvert1()
        test.registerMethods(Thread, "currentThread", "toString")

    def test_registerMethods_noSuchToStringMethod(self) -> None:

        test = StringConvert.StringConvert1()
        test.registerMethods(DistanceNoAnnotations, "rubbishName", "parse")

    def test_registerMethods_nullFromString(self) -> None:

        test = StringConvert.StringConvert1()
        test.registerMethods(DistanceNoAnnotations, "toString", None)

    def test_registerMethods_nullToString(self) -> None:

        test = StringConvert.StringConvert1()
        test.registerMethods(DistanceNoAnnotations, None, "parse")

    def test_registerMethods_nullClass(self) -> None:

        test = StringConvert.StringConvert1()
        test.registerMethods(None, "toString", "parse")

    def test_registerMethodsCharSequence(self) -> None:

        test = StringConvert.StringConvert1()
        test.registerMethods(DistanceNoAnnotationsCharSequence, "toString", "parse")
        d = DistanceNoAnnotationsCharSequence(1, None, 25)
        assert "Distance[25m]" == test.convertToString0(d)
        assert (
            d.amount
            == test.convertFromString(DistanceNoAnnotationsCharSequence, "25m").amount
        )
        conv = test.findConverter(DistanceNoAnnotationsCharSequence)
        self.__assertFromStringConverter(conv, MethodFromStringConverter)
        assert conv == test.findConverter(DistanceNoAnnotationsCharSequence)

    def test_registerMethods(self) -> None:

        test = StringConvert.StringConvert1()
        test.registerMethods(DistanceNoAnnotations, "toString", "parse")
        d = DistanceNoAnnotations(1, None, 25)
        assert test.convertToString0(d) == "Distance[25m]"
        assert d.amount == test.convertFromString(DistanceNoAnnotations, "25m").amount
        conv = test.findConverter(DistanceNoAnnotations)
        self.__assertFromStringConverter(conv, MethodFromStringConverter)
        assert conv == test.findConverter(DistanceNoAnnotations)

    def test_registerFactory_cannotChangeSingleton(self) -> None:

        StringConvert.INSTANCE.register1(
            DistanceNoAnnotations,
            DISTANCE_TO_STRING_CONVERTER,
            DISTANCE_FROM_STRING_CONVERTER,
        )

    def test_register_FunctionalInterfaces_nullFromString(self) -> None:

        test = StringConvert.StringConvert1()
        test.register1(DistanceNoAnnotations, DISTANCE_TO_STRING_CONVERTER, None)

    def test_register_FunctionalInterfaces_nullToString(self) -> None:

        test = StringConvert.StringConvert1()
        test.register1(DistanceNoAnnotations, None, DISTANCE_FROM_STRING_CONVERTER)

    def test_register_FunctionalInterfaces_nullClass(self) -> None:

        test = StringConvert.StringConvert1()
        test.register1(
            None, DISTANCE_TO_STRING_CONVERTER, DISTANCE_FROM_STRING_CONVERTER
        )

    def test_register_FunctionalInterfaces(self) -> None:

        test = StringConvert.StringConvert1()
        test.register1(
            DistanceNoAnnotations,
            DISTANCE_TO_STRING_CONVERTER,
            DISTANCE_FROM_STRING_CONVERTER,
        )
        d = DistanceNoAnnotations(1, None, 25)
        assert "Distance[25m]" == test.convertToString0(d)
        assert d.amount == test.convertFromString(DistanceNoAnnotations, "25m").amount
        conv = test.findConverter(DistanceNoAnnotations)
        assert "$" in conv.__class__.__name__
        assert conv is test.findConverter(DistanceNoAnnotations)

    def test_register_classAlreadyRegistered(self) -> None:

        StringConvert.StringConvert1().register0(
            int, MockIntegerStringConverter.INSTANCE
        )

    def test_register_notOnShared(self) -> None:

        StringConvert.register0(Integer, MockIntegerStringConverter.INSTANCE)

    def test_register_converterNotNull(self) -> None:

        StringConvert.INSTANCE.register0(Integer, None)

    def test_register_classNotNull(self) -> None:

        StringConvert.INSTANCE.register0(None, MockIntegerStringConverter.INSTANCE)

    def test_convert_Enum_overrideDefaultWithConverter(self) -> None:

        test = StringConvert.StringConvert1()
        test.register0(Validity, ValidityStringConverter.INSTANCE)
        assert "VALID" == test.convertToString1(Validity, Validity.VALID)
        assert "INVALID" == test.convertToString1(Validity, Validity.INVALID)
        assert Validity.VALID == test.convertFromString(Validity, "VALID")
        assert Validity.INVALID == test.convertFromString(Validity, "INVALID")
        assert Validity.VALID == test.convertFromString(Validity, "OK")

    def test_convert_annotatedTwoFromStringMethod(self) -> None:

        test = StringConvert.StringConvert1()
        test.findConverter(DistanceTwoFromStringMethodAnnotations)

    def test_convert_annotatedFromStringNoToString(self) -> None:

        test = StringConvert.StringConvert1()
        test.findConverter(DistanceFromStringNoToString)

    def test_convert_annotatedToStringNoFromString(self) -> None:

        test = StringConvert.StringConvert1()
        test.findConverter(DistanceToStringNoFromString)

    def test_convert_annotatedFromStringConstructorInvalidParameterCount(self) -> None:

        test = StringConvert.StringConvert1()
        test.findConverter(DistanceFromStringConstructorInvalidParameterCount)

    def test_convert_annotatedFromStringConstructorInvalidParameter(self) -> None:

        test = StringConvert.StringConvert1()
        test.findConverter(DistanceFromStringConstructorInvalidParameter)

    def test_convert_annotatedFromStringInvalidParameterCount(self) -> None:

        test = StringConvert.StringConvert1()
        test.findConverter(DistanceFromStringInvalidParameterCount)

    def test_convert_annotatedFromStringInvalidParameter(self) -> None:

        test = StringConvert.StringConvert1()
        test.findConverter(DistanceFromStringInvalidParameter)

    def test_convert_annotatedFromStringInvalidReturnType(self) -> None:

        test = StringConvert.StringConvert1()
        test.findConverter(DistanceFromStringInvalidReturnType)

    def test_convert_annotatedToStringInvalidParameters(self) -> None:

        test = StringConvert.StringConvert1()
        test.findConverter(DistanceToStringInvalidParameters)

    def test_convert_annotatedToStringInvalidReturnType(self) -> None:

        test = StringConvert.StringConvert1()
        test.findConverter(DistanceToStringInvalidReturnType)

    def test_convert_annotatedTwoToString(self) -> None:

        test = StringConvert.StringConvert1()
        test.findConverter(DistanceTwoToStringAnnotations)

    def test_convert_annotatedMethodAndConstructor(self) -> None:

        test = StringConvert.StringConvert1()
        test.findConverter(DistanceMethodAndConstructorAnnotations)

    def test_convert_annotationNoMethods(self) -> None:

        test = StringConvert.StringConvert1()
        test.findConverter(DistanceNoAnnotations)

    def test_convert_annotation_FromStringFactoryClashingMethods_fromInterface(
        self,
    ) -> None:

        test = StringConvert.StringConvert1()
        test.findConverter(Test4Interface)

    def test_convert_annotation_FromStringFactoryClashingMethods_fromClass(
        self,
    ) -> None:

        test = StringConvert.StringConvert1()
        test.findConverter(Test4Class)

    def test_convert_annotation_ToStringFromStringOnSuperClassBeatsInterface(
        self,
    ) -> None:

        test = StringConvert.StringConvert1()
        d = Test3Class(25)
        self.assertEqual("25g", test.convertToString0(d))
        self.assertEqual(d.amount, test.convertFromString(Test3Class, "25g").amount)
        conv = test.findTypedConverter(Test3Class)
        self.__assertFromStringConverter(conv, MethodFromStringConverter)
        self.assertIs(conv, test.findConverter(Test3Class))
        self.assertEqual(Test3SuperClass, conv.getEffectiveType())
        self.assertTrue(conv.toString().startswith("RefectionStringConverter"))

    def test_convert_annotation_FactoryAndToStringOnInterface_usingInterface(
        self,
    ) -> None:

        test = StringConvert.StringConvert1()
        d = Test2Class(25)
        self.assertEqual("25g", test.convertToString0(d))
        self.assertEqual("25g", test.convertFromString(Test2Interface, "25g").print())
        conv = test.findTypedConverter(Test2Interface)
        self.__assertFromStringConverter(conv, MethodFromStringConverter)
        self.assertEqual(Test2Interface, conv.getEffectiveType())
        self.assertIs(conv, test.findConverter(Test2Interface))
        self.assertTrue(conv.toString().startswith("RefectionStringConverter"))

    def test_convert_annotation_FactoryAndToStringOnInterface(self) -> None:

        test = StringConvert.StringConvert1()
        d = Test2Class(25)
        self.assertEqual("25g", test.convertToString0(d))
        self.assertEqual(d.amount, test.convertFromString(Test2Class, "25g").amount)
        conv = test.findTypedConverter(Test2Class)
        self.__assertFromStringConverter(conv, MethodFromStringConverter)
        self.assertEqual(Test2Interface, conv.getEffectiveType())
        self.assertIs(conv, test.findConverter(Test2Class))
        self.assertTrue(conv.toString().startswith("RefectionStringConverter"))

    def test_convert_annotation_ToStringOnInterface(self) -> None:

        test = StringConvert.StringConvert1()
        d = Test1Class(25)
        self.assertEqual("25g", test.convertToString0(d))
        self.assertEqual(d.amount, test.convertFromString(Test1Class, "25g").amount)
        conv = test.findTypedConverter(Test1Class)
        self.__assertFromStringConverter(conv, MethodFromStringConverter)
        self.assertEqual(Test1Class, conv.getEffectiveType())
        self.assertIs(conv, test.findConverter(Test1Class))
        self.assertTrue(conv.toString().startswith("RefectionStringConverter"))

    def test_convert_annotationFactoryMethod(self) -> None:

        test = StringConvert.StringConvert1()
        d = DistanceWithFactory(25)
        self.assertEqual("25m", test.convertToString0(d))
        self.assertEqual(
            d.amount, test.convertFromString(DistanceWithFactory, "25m").amount
        )
        conv = test.findTypedConverter(DistanceWithFactory)
        self.__assertFromStringConverter(conv, MethodFromStringConverter)
        self.assertEqual(DistanceWithFactory, conv.getEffectiveType())
        self.assertIs(conv, test.findConverter(DistanceWithFactory))
        self.assertTrue(conv.toString().startswith("RefectionStringConverter"))

    def test_convert_annotationFromStringInvokeException(self) -> None:

        test = StringConvert.StringConvert1()
        conv = test.findConverter(DistanceFromStringException)
        try:
            conv.convertFromString(DistanceFromStringException, "25m")
            self.fail()
        except RuntimeError as ex:
            self.assertEqual(ParseException, type(ex.__cause__))

    def test_convert_annotationToStringInvokeException(self) -> None:

        test = StringConvert.StringConvert1()
        d = DistanceToStringException(25)
        conv = test.findConverter(DistanceToStringException)
        try:
            conv.convertToString(d)
            self.fail()
        except RuntimeError as ex:
            self.assertEqual(ParseException, type(ex.__cause__))

    def test_convert_annotationSuperFactorySubViaSub2(self) -> None:

        test = StringConvert.StringConvert1()
        test.convertFromString(SuperFactorySub, "25m")

    def test_convert_annotationSuperFactorySubViaSub1(self) -> None:

        test = StringConvert.StringConvert1()
        d = SuperFactorySub(25)
        assert test.convertToString0(d) == "25m"

    def test_convert_annotationSuperFactorySubViaSuper(self) -> None:

        test = StringConvert.StringConvert1()
        d = SuperFactorySub(8)
        assert test.convertToString0(d) == "8m"
        fromStr = test.convertFromString(SuperFactorySuper, "8m")
        assert d.amount == fromStr.amount
        assert isinstance(fromStr, SuperFactorySub)
        conv = test.findTypedConverter(SuperFactorySub)
        self.__assertFromStringConverter(conv, MethodFromStringConverter)
        assert SuperFactorySuper == conv.getEffectiveType()
        assert conv == test.findConverter(SuperFactorySub)

    def __assertFromStringConverter(
        self, conv: StringConverter[typing.Any], expectedType: typing.Type[typing.Any]
    ) -> None:
        pass

    def test_convert_annotationSuperFactorySuper(self) -> None:

        test = StringConvert.StringConvert1()
        d = SuperFactorySuper(25)
        self.assertEqual("25m", test.convertToString0(d))
        self.assertEqual(
            d.amount, test.convertFromString(SuperFactorySuper, "25m").amount
        )
        conv = test.findTypedConverter(SuperFactorySuper)
        self.__assertFromStringConverter(conv, MethodFromStringConverter)
        self.assertEqual(SuperFactorySuper, conv.getEffectiveType())
        self.assertIs(conv, test.findConverter(SuperFactorySuper))

    def test_convert_annotationSubMethodConstructor(self) -> None:

        test = StringConvert.StringConvert1()
        d = SubMethodConstructor("25m")
        self.assertEqual("25m", test.convertToString0(d))
        self.assertEqual(
            d.amount, test.convertFromString(SubMethodConstructor, "25m").amount
        )
        conv = test.findTypedConverter(SubMethodConstructor)
        self.__assertFromStringConverter(conv, ConstructorFromStringConverter)
        self.assertEqual(SubMethodConstructor, conv.getEffectiveType())
        self.assertIs(conv, test.findConverter(SubMethodConstructor))

    def test_convert_annotationSubMethodMethod(self) -> None:

        test = StringConvert.StringConvert1()
        d = SubMethodMethod(25)
        self.assertEqual("25m", test.convertToString0(d))
        self.assertEqual(
            d.amount, test.convertFromString(SubMethodMethod, "25m").amount
        )
        conv = test.findTypedConverter(SubMethodMethod)
        self.__assertFromStringConverter(conv, MethodFromStringConverter)
        self.assertEqual(SubMethodMethod, conv.getEffectiveType())
        self.assertIs(conv, test.findConverter(SubMethodMethod))

    def test_convert_annotationMethodBridgeMethod(self) -> None:

        test = StringConvert.StringConvert1()
        d = HasCodeImpl("CODE")
        self.assertEqual("CODE", test.convertToString0(d))
        self.assertEqual(d.code, test.convertFromString(HasCodeImpl, "CODE").code)
        conv = test.findTypedConverter(HasCodeImpl)
        self.__assertFromStringConverter(conv, ConstructorFromStringConverter)
        self.assertIs(conv, test.findConverter(HasCodeImpl))
        self.assertEqual(HasCodeImpl, conv.getEffectiveType())
        self.assertEqual(True, conv.toString().startswith("RefectionStringConverter"))

    def test_convert_annotationMethodMethodCharSequence(self) -> None:

        test = StringConvert.StringConvert1()
        d = DistanceMethodMethodCharSequence(25)
        assert test.convertToString0(d) == "25m"
        assert (
            d.amount
            == test.convertFromString(DistanceMethodMethodCharSequence, "25m").amount
        )
        conv = test.findTypedConverter(DistanceMethodMethodCharSequence)
        self.__assertFromStringConverter(conv, MethodFromStringConverter)
        assert conv == test.findConverter(DistanceMethodMethodCharSequence)
        assert DistanceMethodMethodCharSequence == conv.getEffectiveType()
        assert conv.toString().startswith("RefectionStringConverter")

    def test_convert_annotationMethodMethod(self) -> None:

        test = StringConvert.StringConvert1()
        d = DistanceMethodMethod(25)
        self.assertEqual("25m", test.convertToString0(d))
        self.assertEqual(
            d.amount, test.convertFromString(DistanceMethodMethod, "25m").amount
        )
        conv = test.findTypedConverter(DistanceMethodMethod)
        self.__assertFromStringConverter(conv, MethodFromStringConverter)
        self.assertIs(conv, test.findConverter(DistanceMethodMethod))
        self.assertEqual(DistanceMethodMethod, conv.getEffectiveType())
        self.assertTrue(conv.toString().startswith("RefectionStringConverter"))

    def test_findConverterNoGenerics_Object(self) -> None:

        StringConvert.INSTANCE.findConverterNoGenerics(Object)

    def test_findConverterNoGenerics_null(self) -> None:

        StringConvert.INSTANCE.findConverterNoGenerics(None)

    def test_findConverterNoGenerics(self) -> None:

        cls = int
        conv = StringConvert.INSTANCE.findConverterNoGenerics(cls)
        self.assertEqual(12, conv.convertFromString(cls, "12"))
        self.assertEqual("12", conv.convertToString(12))

    def test_findConverter_Object(self) -> None:

        StringConvert.INSTANCE.findConverter(Object)

    def test_findConverter_null(self) -> None:

        StringConvert.INSTANCE.findConverter(None)

    def test_findConverter(self) -> None:

        cls = int
        conv = StringConvert.INSTANCE.findConverter(cls)
        assert conv.convertFromString(cls, "12") == int(12)
        assert conv.convertToString(12) == "12"

    def test_convertFromString_nullClass(self) -> None:

        assert StringConvert.INSTANCE.convertFromString(None, "6") is None

    def test_convertFromString_null(self) -> None:

        assert StringConvert.INSTANCE.convertFromString(Integer, None) is None

    def test_convertFromString_inheritNotSearchedFor(self) -> None:

        StringConvert.INSTANCE.convertFromString(AltCharSequence, "A")

    def test_convertFromString_inherit(self) -> None:

        from src.main.org.joda.convert.RoundingMode import RoundingMode
        from src.main.org.joda.convert.StringConvert import StringConvert

        self.assertEqual(
            RoundingMode.CEILING,
            StringConvert.INSTANCE.convertFromString(RoundingMode, "CEILING"),
        )

    def test_convertFromString_enumSubclass(self) -> None:

        self.assertEqual(
            ValidityCheck.VALID,
            StringConvert.INSTANCE.convertFromString(ValidityCheck, "VALID"),
        )

    def test_convertFromString_primitiveBoolean(self) -> None:

        self.assertEqual(True, StringConvert.INSTANCE.convertFromString(bool, "true"))

    def test_convertFromString_primitiveInt(self) -> None:

        self.assertEqual(6, StringConvert.INSTANCE.convertFromString(int, "6"))

    def test_convertFromString(self) -> None:

        from src.main.org.joda.convert.StringConvert import StringConvert

        assert Integer.valueOf(6) == StringConvert.INSTANCE.convertFromString(
            Integer, "6"
        )

    def test_convertToString_withType_nullClass(self) -> None:

        from src.main.org.joda.convert.StringConvert import StringConvert

        assert StringConvert.INSTANCE.convertToString1(None, "6") is None

    def test_convertToString_withType_null(self) -> None:

        # Assuming StringConvert is a class and convertToString1 is a method in that class
        # Also assuming that the method convertToString1 takes two parameters: a class and an object
        # If this is not the case, you will need to adjust the method call accordingly

        self.assertEqual(None, StringConvert.convertToString1(Integer, None))

    def test_convertToString_withType_inherit1(self) -> None:

        from java.math import RoundingMode
        from src.main.org.joda.convert.StringConvert import StringConvert

        self.assertEqual(
            "CEILING",
            StringConvert.INSTANCE.convertToString1(RoundingMode, RoundingMode.CEILING),
        )

    def test_convertToString_withType_primitive2(self) -> None:

        i = 6
        self.assertEqual("6", StringConvert.INSTANCE.convertToString1(int, i))

    def test_convertToString_withType_primitive1(self) -> None:

        i = 6
        self.assertEqual("6", StringConvert.INSTANCE.convertToString1(Integer, i))

    def test_convertToString_withType_noGenerics(self) -> None:

        i = 6
        cls = int
        self.assertEqual("6", StringConvert.INSTANCE.convertToString1(cls, i))

    def test_convertToString_withType(self) -> None:

        i = 6
        self.assertEqual("6", StringConvert.INSTANCE.convertToString1(int, i))

    def test_convertToString_null(self) -> None:

        from src.main.org.joda.convert.StringConvert import StringConvert

        assert StringConvert.INSTANCE.convertToString0(None) is None

    def test_convertToString_inherit(self) -> None:

        from src.main.org.joda.convert.RoundingMode import RoundingMode
        from src.main.org.joda.convert.StringConvert import StringConvert

        self.assertEqual(
            "CEILING", StringConvert.INSTANCE.convertToString0(RoundingMode.CEILING)
        )

    def test_convertToString_primitive(self) -> None:

        i = 6
        self.assertEqual("6", StringConvert.INSTANCE.convertToString0(i))

    def test_convertToString(self) -> None:

        i = 6
        self.assertEqual("6", StringConvert.INSTANCE.convertToString0(i))

    def test_isConvertible(self) -> None:

        assert StringConvert.INSTANCE.isConvertible(int)
        assert StringConvert.INSTANCE.isConvertible(str)
        assert not StringConvert.INSTANCE.isConvertible(object)

    def test_constructor_false(self) -> None:

        test = StringConvert(False)
        conv = test.findConverter(int)
        self.assertEqual(None, conv)

    def test_constructor_true(self) -> None:

        test = StringConvert(True)
        conv = test.findConverter(int)
        assert isinstance(conv, JDKStringConverter)

    def test_constructor(self) -> None:

        test = StringConvert.StringConvert1()
        conv = test.findTypedConverter(int)
        assert isinstance(conv, JDKStringConverter)
        assert conv.getEffectiveType() == int

    def test_register_distance(self) -> None:

        test = StringConvert.StringConvert1()
        test.register0(DistanceMethodMethod, MockDistanceStringConverter.INSTANCE)
        assert (
            test.findConverter(DistanceMethodMethod)
            == MockDistanceStringConverter.INSTANCE
        )

    def __assertFromStringConverter(
        self, conv: StringConverter[typing.Any], expectedType: typing.Type[typing.Any]
    ) -> None:

        assert isinstance(
            conv, ReflectionStringConverter
        ), "conv is not an instance of ReflectionStringConverter"
        obj = conv.fromString
        assert isinstance(
            obj, expectedType
        ), f"Expected type {expectedType}, but got {type(obj)}"
