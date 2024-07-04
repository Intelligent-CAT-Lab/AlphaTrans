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

    BAD_INIT: Atomic = Atomic(False)

    def test_matchUsingConfigFile(self) -> None:

        original_err = sys.stderr
        try:
            baos = io.BytesIO()
            ps = io.TextIOWrapper(baos, encoding="utf-8")
            sys.stderr = ps
            test = RenameHandler.create1(True)
            sys.stderr.flush()
            self.assertEqual(Status, test.lookupType("com.foo.Bar"))
            self.assertEqual(Status.VALID, test.lookupEnum(Status, "YES"))
            self.assertEqual(DistanceMethodMethod, test.lookupType("com.foo.Foo"))
            self.assertEqual(Status.INVALID, test.lookupEnum(Status, "NO"))
            logged = baos.getvalue().decode("utf-8")
            self.assertTrue(logged.startswith("ERROR: Invalid Renamed.ini: "))
            self.assertTrue("org.joda.convert.ClassDoesNotExist" in logged)
            self.assertTrue(
                "com.foo.convert.TestRenameHandlerBadInit" in test.getTypeRenames()
            )
            self.assertTrue(Status.STRING_CONVERTIBLE)
            self.assertFalse(BAD_INIT.get())

        finally:
            sys.stderr = original_err

    def test_locked(self) -> None:

        test = RenameHandler.create0()
        test.renamedType("com.foo.Bar", TestRenameHandler)
        test.lock()
        with pytest.raises(RuntimeError):
            test.renamedType("com.foo.Foo", TestRenameHandler)

    def test_renameBlockedType3(self) -> None:

        test = RenameHandler.create0()
        with pytest.raises(ValueError):
            test.renamedType("org.joda.foo.Bar", TestRenameHandler)

    def test_renameBlockedType2(self) -> None:

        test = RenameHandler.create0()
        with pytest.raises(ValueError):
            test.renamedType("javax.foo.Bar", TestRenameHandler)

    def test_renameBlockedType1(self) -> None:

        test = RenameHandler.create0()
        with pytest.raises(ValueError):
            test.renamedType("java.lang.String", TestRenameHandler)

    def test_noMatchType(self) -> None:

        test = RenameHandler.create0()

        with pytest.raises(ClassNotFoundException):
            test.lookupType("com.foo.Foo")

    def test_matchRenamedType(self) -> None:

        test = RenameHandler.create0()
        test.renamedType("com.foo.Bar", TestRenameHandler)
        renamed = test.lookupType("com.foo.Bar")
        self.assertEqual(TestRenameHandler, renamed)
