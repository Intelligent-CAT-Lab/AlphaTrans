from __future__ import annotations
import io
import typing
from typing import *
from src.main.com.google.common.reflect.TypeToken import *
from src.main.org.joda.convert.StringConvert import *
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.TypeStringConverterFactory import *
from src.main.org.joda.convert.TypeTokenStringConverter import *
from src.main.org.joda.convert.TypedStringConverter import *


class TestGuavaTypeTokenStringConverter:

    def doTest(self, obj: typing.TypeVar("T", bound=typing.Any), str: str) -> None:

        test = TypeTokenStringConverter()
        assert TypeToken == test.getEffectiveType()
        assert str == test.convertToString(obj)
        assert obj == test.convertFromString(TypeToken, str)

        test2 = StringConvert.INSTANCE.findTypedConverterNoGenerics(TypeToken)
        assert TypeToken == test2.getEffectiveType()
        assert str == test2.convertToString(obj)
        assert obj == test2.convertFromString(TypeToken, str)

        test3 = TypeStringConverterFactory.INSTANCE
        converter3 = test3.findConverter(Type)
        assert Type == converter3.getEffectiveType()
        assert str == converter3.convertToString(obj.getType())
        assert obj.getType() == converter3.convertFromString(Type, str)

        test4 = StringConvert.INSTANCE.findTypedConverterNoGenerics(Type)
        assert Type == test4.getEffectiveType()
        assert str == test4.convertToString(obj.getType())
        assert obj.getType() == test4.convertFromString(Type, str)

        test5 = StringConvert.INSTANCE.findTypedConverterNoGenerics(ParameterizedType)
        assert ParameterizedType == test5.getEffectiveType()
        assert str == test5.convertToString(obj.getType())
        assert obj.getType() == test5.convertFromString(ParameterizedType, str)

    def test_twoParamComplexExtends(self) -> None:

        token = TypeToken[
            Dict[str, Dict[Union[int, Any], List[Union[int, float, complex, Any]]]]
        ]

        self.doTest(
            token,
            "java.util.Map<java.lang.String, java.util.Map<? super java.lang.Integer, ? extends"
            + " java.util.List<? extends java.lang.Number>>>",
        )

    def test_twoParamComplex(self) -> None:

        token = TypeToken.get(typing.Dict[str, typing.Dict[int, float]])
        self.doTest(
            token,
            "java.util.Map<java.lang.String, java.util.Map<java.lang.Integer, java.lang.Double>>",
        )

    def test_twoParamNestedExtends(self) -> None:

        token = TypeToken.get(typing.Dict[str, typing.List[typing.Any]])
        self.doTest(
            token,
            "java.util.Map<java.lang.String, ? extends java.util.List<? extends java.lang.Integer>>",
        )

    def test_twoParamNested(self) -> None:

        token = TypeToken.get(typing.Dict[str, typing.List[int]])
        self.doTest(
            token, "java.util.Map<java.lang.String, java.util.List<java.lang.Integer>>"
        )

    def test_twoParamsSuper(self) -> None:

        token = TypeToken.get(typing.Dict[typing.Any, typing.Any])
        self.doTest(
            token, "java.util.Map<? super java.lang.String, ? super java.lang.Integer>"
        )

    def test_twoParamsExtends(self) -> None:

        token = TypeToken.get(typing.Dict[typing.Any, typing.Any])
        self.doTest(
            token,
            "java.util.Map<? extends java.lang.CharSequence, ? extends java.lang.Number>",
        )

    def test_twoParams(self) -> None:

        token = TypeToken.of(typing.Dict[str, int])
        self.doTest(token, "java.util.Map<java.lang.String, java.lang.Integer>")

    def test_oneSuper(self) -> None:

        token = TypeToken.get(List[Union[int, Any]])
        self.doTest(token, "java.util.List<? super java.lang.Integer>")

    def test_oneExtends(self) -> None:

        token = TypeToken.get(List[Extends[Number]])
        self.doTest(token, "java.util.List<? extends java.lang.Number>")

    def test_oneArray(self) -> None:

        token = TypeToken.get(List[List[str]])
        test = TypeTokenStringConverter()
        asStr = test.convertToString(token)
        reverse1 = test.convertFromString(
            TypeToken, "java.util.List<java.lang.String[]>"
        )
        reverse2 = test.convertFromString(
            TypeToken, "java.util.List<[Ljava.lang.String;>"
        )
        assert reverse1 == reverse2
        expected = (
            "java.util.List<java.lang.String[]>"
            if asStr == "java.util.List<java.lang.String[]>"
            else "java.util.List<[Ljava.lang.String;>"
        )
        self.doTest(token, expected)

    def test_oneWild(self) -> None:

        token = TypeToken.get(List[Any])
        self.doTest(token, "java.util.List<?>")

    def test_oneParam(self) -> None:

        token = TypeToken.get(List[str])
        self.doTest(token, "java.util.List<java.lang.String>")

    def test_primitive_char(self) -> None:

        token = TypeToken.of(Character)
        self.doTest(token, "char")

    def test_primitive_int(self) -> None:

        token = TypeToken.of(int)
        self.doTest(token, "int")

    def test_simpleClass_rawList(self) -> None:

        token = TypeToken.of(List)
        self.doTest(token, "java.util.List")

    def test_simpleClass_Integer(self) -> None:

        token = TypeToken.of(int)
        self.doTest(token, "java.lang.Integer")

    def test_simpleClass_String(self) -> None:

        token = TypeToken.of(str)
        self.doTest(token, "java.lang.String")
