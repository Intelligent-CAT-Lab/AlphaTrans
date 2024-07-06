from __future__ import annotations
import re
import sys
import os
from io import BytesIO
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.test.org.joda.convert.DistanceMethodMethod import *
from src.main.org.joda.convert.RenameHandler import *
from src.test.org.joda.convert.Status import *


class TestRenameHandler(unittest.TestCase):

    BAD_INIT: bool = False

    def test_matchUsingConfigFile(self) -> None:
        originalErr = sys.stderr
        try:
            baos = io.BytesIO()
            ps = io.TextIOWrapper(baos, encoding="UTF-8")
            sys.stderr = ps
            test = RenameHandler.create1(True)
            sys.stderr.flush()
            self.assertEqual(Status, test.lookupType("com.foo.Bar"))
            self.assertEqual(Status.YES, test.lookupEnum(Status, "YES"))
            self.assertEqual(DistanceMethodMethod, test.lookupType("com.foo.Foo"))
            self.assertEqual(Status.INVALID, test.lookupEnum(Status, "NO"))
            logged = baos.getvalue().decode("UTF-8")
            self.assertTrue(logged.startswith("ERROR: Invalid Renamed.ini: "))
            self.assertTrue(logged.contains("org.joda.convert.ClassDoesNotExist"))
            self.assertTrue(
                test.getTypeRenames().containsKey(
                    "com.foo.convert.TestRenameHandlerBadInit"
                )
            )
            self.assertTrue(Status.STRING_CONVERTIBLE)
            self.assertFalse(BAD_INIT)

        finally:
            sys.stderr = originalErr

    def test_locked(self) -> None:

        pass  # LLM could not translate this method

    def test_renameBlockedType3(self) -> None:

        pass  # LLM could not translate this method

    def test_renameBlockedType2(self) -> None:

        pass  # LLM could not translate this method

    def test_renameBlockedType1(self) -> None:

        pass  # LLM could not translate this method

    def test_noMatchType(self) -> None:
        with self.assertRaises(ClassNotFoundException):
            test = RenameHandler.create0()
            test.lookupType("com.foo.Foo")

    def test_matchRenamedType(self) -> None:
        test: RenameHandler = RenameHandler.create0()
        test.renamedType("com.foo.Bar", TestRenameHandler)
        renamed: typing.Type[typing.Any] = test.lookupType("com.foo.Bar")
        self.assertEqual(TestRenameHandler, renamed)
