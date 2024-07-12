from __future__ import annotations
import time
import re
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.Field import *
from src.main.org.apache.commons.validator.Form import *

# from src.test.org.apache.commons.validator.Form_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Form_ESTest(unittest.TestCase):

    def test14(self) -> None:
        form0 = Form()
        form0.getFields()
        assert not form0.isProcessed()

    def test13(self) -> None:
        form0 = Form()
        form0.getExtends()
        assert not form0.isProcessed()

    def test12(self) -> None:
        form0 = Form()
        form0.setName("Arg: name=")
        self.assertFalse(form0.isProcessed())

    def test11(self) -> None:
        form0 = Form()
        form0.setExtends("")
        boolean0 = form0.isExtending()
        self.assertTrue(boolean0)

    def test10(self) -> None:
        form0 = Form()
        form0.getName()
        assert not form0.isProcessed()

    def test09(self) -> None:
        form0 = Form()
        boolean0 = form0.isProcessed()
        self.assertFalse(boolean0)

    def test08(self) -> None:

        form0 = Form()
        linkedList0 = []
        form0.lFields = linkedList0
        field0 = Field()
        linkedList0.append(field0)
        form0.toString()
        self.assertFalse(form0.isProcessed())

    def test07(self) -> None:
        form0 = Form()
        boolean0 = form0.isExtending()
        self.assertFalse(boolean0)
        self.assertFalse(form0.isProcessed())

    def test06(self) -> None:

        form0 = Form()
        form0._lFields = None

        with pytest.raises(RuntimeError):
            form0.getFields()
            self.fail("Expecting exception: RuntimeError")

        try:
            self.verifyException("java.util.Collections$UnmodifiableCollection", e)
        except Exception as e:
            print(f"An error occurred: {e}")

    def test05(self) -> None:

        form0 = Form()
        form0._lFields = None

        with pytest.raises(RuntimeError):
            form0.toString()

        try:
            form0.toString()
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException("org.apache.commons.validator.Form", e)

    def test04(self) -> None:
        form0 = Form()
        form0.setExtends("")
        form0.getExtends()
        self.assertTrue(form0.isExtending())

    def test03(self) -> None:

        form0 = Form()
        form0._inherit = "h{IL5tqkx+D_z[)"
        string0 = form0.getExtends()
        self.assertFalse(form0.isProcessed())
        self.assertIsNotNone(string0)

    def test02(self) -> None:

        form0 = Form()
        form0._name = ""
        string0 = form0.getName()
        self.assertIsNotNone(string0)
        self.assertFalse(form0.isProcessed())

    def test01(self) -> None:

        form0 = Form()
        form0._name = "Arg: name="
        string0 = form0.getName()
        self.assertIsNotNone(string0)
        self.assertFalse(form0.isProcessed())

    def test00(self) -> None:

        form0 = Form()
        form0._name = "Arg: name="
        string0 = form0.toString()
        self.assertFalse(form0.isProcessed())
        self.assertEqual("Form: Arg: name=\n", string0)
