# Imports Begin
from src.main.org.joda.convert.Status import *
from src.main.org.joda.convert.RenameHandler import *
from src.main.org.joda.convert.DistanceMethodMethod import *
import unittest
import sys
import os
import typing
from typing import *
import io

# Imports End


class TestRenameHandler(unittest.TestCase):

    # Class Fields Begin
    BAD_INIT: bool = False
    # Class Fields End

    # Class Methods Begin
    def test_matchUsingConfigFile(self) -> None:

        original_err = sys.stderr
        try:
            baos = io.BytesIO()
            ps = PrintStream(baos, False, "UTF-8")
            sys.stderr = ps
            test = RenameHandler.create1(True)
            sys.stderr.flush()
            self.assertEqual(Status, test.lookupType("com.foo.Bar"))
            self.assertEqual(Status.VALID, test.lookupEnum(Status, "YES"))
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
            self.assertFalse(self.BAD_INIT.get())
        finally:
            sys.stderr = original_err

    def test_locked(self) -> None:

        pass  # LLM could not translate method body

    def test_renameBlockedType3(self) -> None:

        test = RenameHandler.create0()
        test.renamedType("org.joda.foo.Bar", TestRenameHandler)

    def test_renameBlockedType2(self) -> None:

        test = RenameHandler.create0()
        test.renamedType("javax.foo.Bar", TestRenameHandler)

    def test_renameBlockedType1(self) -> None:

        pass  # LLM could not translate method body

    def test_noMatchType(self) -> None:

        test = RenameHandler.create0()
        test.lookupType("com.foo.Foo")

    def test_matchRenamedType(self) -> None:

        test = RenameHandler.create0()
        test.renamedType("com.foo.Bar", TestRenameHandler)
        renamed = test.lookupType("com.foo.Bar")
        self.assertEqual(TestRenameHandler, renamed)

    # Class Methods End
