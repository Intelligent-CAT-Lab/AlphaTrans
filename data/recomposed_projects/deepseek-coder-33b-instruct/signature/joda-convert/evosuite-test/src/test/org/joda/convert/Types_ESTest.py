from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import typing
from typing import *
import unittest

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.joda.convert.Types import *

# from src.test.org.joda.convert.Types_ESTest_scaffolding import *


class Types_ESTest(unittest.TestCase):

    def test36(self) -> None:

        typeArray0 = []
        class0 = Method
        parameterizedType0 = Types.newParameterizedType(class0, typeArray0)
        wildcardType0 = Types.subtypeOf(parameterizedType0)
        type0 = Types.getComponentType(wildcardType0)
        self.assertIsNone(type0)

    def test35(self) -> None:

        class0 = Method
        class1 = Types.getArrayClass(class0)
        wildcardType0 = Types.subtypeOf(class1)
        typeArray0 = [class1, wildcardType0, class1]
        types_WildcardTypeImpl0 = WildcardTypeImpl(typeArray0, typeArray0)

        try:
            Types.newArrayType(types_WildcardTypeImpl0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.joda.convert.Types", e)

    def test34(self) -> None:

        typeArray0 = []
        class0 = Method
        parameterizedType0 = Types.newParameterizedType(class0, typeArray0)
        wildcardType0 = Types.subtypeOf(parameterizedType0)
        type0 = Types.newArrayType(wildcardType0)
        assert not type0 == wildcardType0

    def test33(self) -> None:

        typeArray0 = []
        class0 = Method
        parameterizedType0 = Types.newParameterizedType(class0, typeArray0)
        type0 = Types.newArrayType(parameterizedType0)
        Types.getComponentType(type0)

    def test32(self) -> None:

        typeArray0 = []
        class0 = Method
        parameterizedType0 = Types.newParameterizedType(class0, typeArray0)
        type0 = Types.newArrayType(parameterizedType0)
        typeArray1 = [None] * 5
        typeArray1[0] = type0
        typeArray1[1] = class0
        typeArray1[2] = class0
        typeArray1[3] = parameterizedType0
        typeArray1[4] = parameterizedType0
        types_WildcardTypeImpl0 = WildcardTypeImpl(typeArray0, typeArray1)
        types_WildcardTypeImpl0.getTypeName()

    def test31(self) -> None:
        types_JavaVersion0 = JavaVersion.JAVA8
        types_JavaVersion0.jdkTypeDuplicatesOwnerName()

    def test30(self) -> None:

        types_JavaVersion0 = JavaVersion.JAVA7
        class0 = Method
        class1 = Types.getArrayClass(class0)
        types_JavaVersion0.typeName(class1)

    def test29(self) -> None:

        types_NativeTypeVariableEquals0 = Types.NativeTypeVariableEquals[Method]()

    def test28(self) -> None:

        typeArray0 = []
        class0 = Method
        class1 = Types.getArrayClass(class0)
        parameterizedType0 = Types.newParameterizedType(class0, typeArray0)
        wildcardType0 = Types.subtypeOf(parameterizedType0)
        typeArray1 = [None] * 5
        typeArray1[0] = wildcardType0
        typeArray1[1] = wildcardType0
        typeArray1[2] = wildcardType0
        typeArray1[3] = class1
        typeArray1[4] = class0
        types_WildcardTypeImpl0 = WildcardTypeImpl(typeArray0, typeArray1)
        Types.getComponentType(types_WildcardTypeImpl0)

    def test27(self) -> None:

        typeArray0 = []
        typeArray1 = [None] * 3
        class0 = Method
        parameterizedType0 = Types.newParameterizedType(class0, typeArray0)
        wildcardType0 = Types.supertypeOf(parameterizedType0)
        typeArray1[1] = wildcardType0
        Types.newArrayType(typeArray1[1])

    def test26(self) -> None:

        typeArray0 = []
        types_WildcardTypeImpl0 = WildcardTypeImpl(typeArray0, typeArray0)

        try:
            Types.newArrayType(types_WildcardTypeImpl0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.joda.convert.Types", e)

    def test25(self) -> None:

        typeArray0 = []
        class0 = Method
        parameterizedType0 = Types.newParameterizedType(class0, typeArray0)

        try:
            Types.newParameterizedTypeWithOwner(parameterizedType0, class0, typeArray0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.joda.convert.Types", e)

    def test24(self) -> None:

        typeArray0 = []
        class0 = Method
        Types.newParameterizedTypeWithOwner(None, class0, typeArray0)

    def test23(self) -> None:

        typeArray0 = [None] * 39

        try:
            Types.newArtificialTypeVariable(
                None, "org.joda.convert.TypeCapture", typeArray0
            )
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.convert.Types", e)

    def test22(self) -> None:

        class0 = Method
        class1 = Types.getArrayClass(class0)
        wildcardType0 = Types.subtypeOf(class1)
        wildcardType1 = Types.subtypeOf(wildcardType0)
        Types.getComponentType(wildcardType1)

    def test21(self) -> None:

        class0 = Method
        typeArray0 = [None] * 6

        try:
            Types.newParameterizedType(class0, typeArray0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.joda.convert.Types", e)

    def test20(self) -> None:

        typeArray0 = []
        class0 = Method
        parameterizedType0 = Types.newParameterizedType(class0, typeArray0)
        types_WildcardTypeImpl0 = typing.cast(
            WildcardTypeImpl, Types.supertypeOf(parameterizedType0)
        )
        object0 = object()
        types_WildcardTypeImpl0.equals(object0)

    def test19(self) -> None:

        typeArray0 = []
        types_WildcardTypeImpl0 = WildcardTypeImpl(typeArray0, typeArray0)
        types_WildcardTypeImpl0.equals(types_WildcardTypeImpl0)

    def test18(self) -> None:

        class0 = Method
        class1 = Types.getArrayClass(class0)
        wildcardType0 = Types.subtypeOf(class1)
        types_JavaVersion0 = JavaVersion.JAVA6
        typeArray0 = [None] * 3
        typeArray0[0] = wildcardType0
        typeArray0[1] = wildcardType0
        typeArray0[2] = class0
        types_JavaVersion0.usedInGenericType1(typeArray0)

    def test17(self) -> None:

        class0 = Method
        class1 = Types.getArrayClass(class0)
        type0 = Types.newArrayType(class1)
        types_JavaVersion0 = Types.JavaVersion.JAVA6
        typeArray0 = [None] * 2
        typeArray0[0] = type0
        try:
            types_JavaVersion0.usedInGenericType1(typeArray0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.convert.Types", e)

    def test16(self) -> None:

        try:
            Types.checkArgument2(False, "org.joda.convert.Types", None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.joda.convert.Types", e)

    def test15(self) -> None:

        with self.assertRaises(RuntimeError):
            Types.getArrayClass(None)

    def test14(self) -> None:
        try:
            Types.getComponentType(None)
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException("org.joda.convert.Types", e)

    def test13(self) -> None:

        try:
            Types.newArrayType(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.convert.Types", e)

    def test12(self) -> None:

        try:
            Types.newArtificialTypeVariable(None, "q{YJe$dI$", None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.convert.Types", e)

    def test11(self) -> None:

        class0 = Method
        try:
            Types.newParameterizedType(class0, None)
            self.fail("Expecting exception: RuntimeError")

        except TypeError as e:
            self.verifyException("org.joda.convert.Types$ParameterizedTypeImpl", e)

    def test10(self) -> None:

        class0 = Method
        try:
            Types.newParameterizedTypeWithOwner(class0, class0, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.convert.Types", e)

    def test09(self) -> None:

        class0 = Method
        try:
            Types.newParameterizedTypeWithOwner(None, class0, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.convert.Types$ParameterizedTypeImpl", e)

    def test08(self) -> None:

        with pytest.raises(RuntimeError):
            Types.subtypeOf(None)

    def test07(self) -> None:

        with pytest.raises(RuntimeError):
            Types.supertypeOf(None)

    def test06(self) -> None:

        with pytest.raises(RuntimeError):
            Types.toString(None)

    def test05(self) -> None:
        class0 = Method
        Types.toString(type(class0))

    def test04(self) -> None:

        class0 = Method
        class1 = Types.getArrayClass(class0)
        typeArray0 = [None] * 8
        typeArray0[0] = typeArray0[1] = typeArray0[4] = class1
        typeArray0[2] = typeArray0[3] = typeArray0[5] = typeArray0[6] = typeArray0[
            7
        ] = class0
        types_WildcardTypeImpl0 = WildcardTypeImpl(typeArray0, typeArray0)
        types_WildcardTypeImpl0.getLowerBounds()

    def test03(self) -> None:

        typeArray0 = []
        types_WildcardTypeImpl0 = WildcardTypeImpl(typeArray0, typeArray0)
        types_WildcardTypeImpl0.getUpperBounds()

    def test02(self) -> None:

        class0 = Method
        types_WildcardTypeImpl0 = Types.supertypeOf(class0)
        types_WildcardTypeImpl0.toString()

    def test01(self) -> None:

        typeArray0 = [None] * 2
        self.assertTrue(Types.checkArgument2(True, "v#*", typeArray0))

    def test00(self) -> None:

        objectArray0 = [None] * 8

        try:
            Types.checkArgument2(False, "%s isn't parameterized", objectArray0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.joda.convert.Types", e)
