from __future__ import annotations
import time
import inspect
import re
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.joda.convert.RenameHandler import *

# from src.test.org.joda.convert.RenameHandler_ESTest_scaffolding import *


class RenameHandler_ESTest(unittest.TestCase):

    def test20(self) -> None:

        renameHandler0 = RenameHandler.create0()
        class0 = object

        try:
            renameHandler0.renamedType(None, class0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.assertEqual(str(e), "oldName must not be null")

    def test18(self) -> None:

        renameHandler0 = RenameHandler.create1(False)
        string0 = renameHandler0.toString()
        self.assertEqual("RenamedTypes{},RenamedEnumConstants{}", string0)

    def test17(self) -> None:

        renameHandler0 = RenameHandler.INSTANCE
        try:
            renameHandler0.renamedType("m", None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.assertEqual(str(e), "currentValue must not be null")

    def test16(self) -> None:

        renameHandler0 = RenameHandler.create1(True)
        class0 = object

        with pytest.raises(ValueError) as e:
            renameHandler0.renamedType("java.", class0)

        assert (
            str(e.value) == "oldName must not be a java.*, javax.* or org.joda.* type"
        )

    def test15(self) -> None:

        renameHandler0 = RenameHandler.create0()
        class0 = object

        try:
            renameHandler0.renamedType(
                "javax.org.joda.convert.AnnotationStringConverterFactory", class0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.assertEqual(
                str(e), "oldName must not be a java.*, javax.* or org.joda.* type"
            )

    def test14(self) -> None:

        renameHandler0 = RenameHandler.INSTANCE
        class0 = Proxy.Type

        with self.assertRaises(ValueError) as context:
            renameHandler0.renamedType("org.joda.convert.RenameHandler", class0)

        self.assertTrue(
            "oldName must not be a java.*, javax.* or org.joda.* type"
            in str(context.exception)
        )

    def test13(self) -> None:

        renameHandler0 = RenameHandler.create1(False)

        try:
            renameHandler0.lookupType(None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.joda.convert.RenameHandler", e)

    def test12(self) -> None:

        renameHandler0 = RenameHandler.create0()
        proxy_Type0 = Proxy.Type.SOCKS
        renameHandler0.renamedEnum("getAsInt", proxy_Type0)
        class0 = Proxy.Type
        proxy_Type1 = renameHandler0.lookupEnum(class0, "getAsInt")
        self.assertEqual(Proxy.Type.SOCKS, proxy_Type1)

    def test11(self) -> None:

        renameHandler0 = RenameHandler.create0()
        proxy_Type0 = Proxy.Type.SOCKS

        with self.assertRaises(ValueError) as context:
            renameHandler0.renamedEnum(None, proxy_Type0)

        self.assertTrue("oldName must not be null" in str(context.exception))

    def test10(self) -> None:

        renameHandler0 = RenameHandler.INSTANCE
        try:
            renameHandler0.renamedEnum("org.joda.`", None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.assertEqual(str(e), "currentValue must not be null")

    def test09(self) -> None:

        renameHandler0 = RenameHandler.create0()
        class0 = Proxy.Type

        try:
            renameHandler0.lookupEnum(class0, "$*_q")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("java.lang.Enum", e)

    def test08(self) -> None:

        renameHandler0 = RenameHandler.create0()

        with pytest.raises(ValueError) as e:
            renameHandler0.getEnumRenames(None)

        assert str(e.value) == "type must not be None"

    def test07(self) -> None:

        renameHandler0 = RenameHandler.INSTANCE

        with self.assertRaises(ValueError) as context:
            renameHandler0.lookupEnum(None, "name must")

        self.assertTrue("type must not be None" in str(context.exception))

    def test06(self) -> None:

        renameHandler0 = RenameHandler.create1(False)
        class0 = Proxy.Type

        with pytest.raises(ValueError):
            renameHandler0.lookupEnum(class0, None)
            self.fail("Expecting exception: ValueError")

        verifyException("org.joda.convert.RenameHandler", ValueError)

    def test05(self) -> None:

        renameHandler0 = RenameHandler.INSTANCE
        string0 = "^xA:b{bC$1"
        proxy_Type0 = Proxy.Type.DIRECT
        renameHandler0.renamedEnum(string0, proxy_Type0)
        RenameHandler.create0()
        renameHandler0.getEnumTypesWithRenames()
        renameHandler0.lock()
        try:
            renameHandler0.lookupType(string0)
            self.fail("Expecting exception: ClassNotFoundException")

        except ClassNotFoundException:
            pass

    def test04(self) -> None:

        renameHandler0 = RenameHandler.create0()
        class0 = Proxy.Type
        map0 = renameHandler0.getEnumRenames(class0)
        self.assertTrue(not map0)

    def test03(self) -> None:

        renameHandler0 = RenameHandler.INSTANCE
        proxy_Type0 = Proxy.Type.DIRECT
        renameHandler0.renamedEnum(">=J-O#E", proxy_Type0)

    def test02(self) -> None:

        renameHandler0 = RenameHandler.create0()
        renameHandler0.getTypeRenames()
        class0 = Proxy.Type
        renameHandler0.renamedType("name must not be null", class0)
        class1 = renameHandler0.lookupType("name must not be null")
        self.assertFalse(class1.isSynthetic())

    def test01(self) -> None:

        renameHandler0 = RenameHandler.create0()
        class0 = renameHandler0.lookupType("org.joda.convert.ReflectionStringConverter")
        self.assertFalse(class0.isPrimitive())

    def test00(self) -> None:

        renameHandler0 = RenameHandler.create0()
        class0 = renameHandler0.lookupType("char")
        self.assertFalse(inspect.isinterface(class0))
