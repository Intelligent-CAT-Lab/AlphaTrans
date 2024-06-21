from __future__ import annotations
import sys
import io
import typing
from typing import *
from src.test.org.joda.convert.DistanceMethodMethod import *
from src.main.org.joda.convert.RenameHandler import *
from src.test.org.joda.convert.Status import *


class TestRenameHandler:

    BAD_INIT: bool = None  # LLM could not translate this field

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
                test.getTypeRenames().get("com.foo.convert.TestRenameHandlerBadInit")
                is not None
            )
            self.assertTrue(Status.STRING_CONVERTIBLE)
            self.assertFalse(TestRenameHandler.BAD_INIT)

        finally:
            sys.stderr = original_err

    def test_locked(self) -> None:

        test = RenameHandler.create0()
        test.renamedType("com.foo.Bar", TestRenameHandler)
        test.lock()
        test.renamedType("com.foo.Foo", TestRenameHandler)

    def test_renameBlockedType3(self) -> None:

        test = RenameHandler.create0()
        test.renamedType("org.joda.foo.Bar", TestRenameHandler)

    def test_renameBlockedType2(self) -> None:

        test = RenameHandler.create0()
        test.renamedType("javax.foo.Bar", TestRenameHandler)

    def test_renameBlockedType1(self) -> None:

        test = RenameHandler.create0()
        test.renamedType("java.lang.String", TestRenameHandler)

    def test_noMatchType(self) -> None:

        # Calling the static method create0 from RenameHandler class
        test = RenameHandler.create0()

        # Calling the method lookupType from RenameHandler class
        test.lookupType("com.foo.Foo")

    def test_matchRenamedType(self) -> None:

        # Calling the static method create0 from RenameHandler class
        test = RenameHandler.create0()

        # Calling the method renamedType from RenameHandler class
        test.renamedType("com.foo.Bar", TestRenameHandler)

        # Calling the method lookupType from RenameHandler class
        renamed = test.lookupType("com.foo.Bar")

        # Checking if the returned class is the same as TestRenameHandler
        assert renamed == TestRenameHandler
