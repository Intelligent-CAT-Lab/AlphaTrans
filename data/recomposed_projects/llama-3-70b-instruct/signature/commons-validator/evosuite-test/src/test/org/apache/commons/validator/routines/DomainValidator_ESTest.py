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
from src.main.org.apache.commons.validator.routines.DomainValidator import *

# from src.test.org.apache.commons.validator.routines.DomainValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class DomainValidator_ESTest(unittest.TestCase):

    def test65(self) -> None:

        domainValidator0 = DomainValidator.getInstance0()
        boolean0 = domainValidator0.isValid(
            "org.apache.commos.validator.routines.RegexValidator"
        )
        self.assertFalse(boolean0)

    def test64(self) -> None:

        domain_validator0 = DomainValidator.getInstance0()
        boolean0 = domain_validator0.isAllowLocal()
        self.assertFalse(boolean0)

    def test63(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_PLUS
        stringArray0 = [""] * 6
        domainValidator_Item0 = DomainValidator.Item(
            domainValidator_ArrayType0, stringArray0
        )
        list0 = [domainValidator_Item0, domainValidator_Item0, domainValidator_Item0]

        with pytest.raises(RuntimeError):
            DomainValidator.getInstance2(False, list0)

    def test62(self) -> None:

        domainValidator0 = DomainValidator.getInstance1(False)
        self.assertFalse(domainValidator0.isAllowLocal())

    def test61(self) -> None:

        domainValidator0 = DomainValidator.getInstance1(True)
        boolean0 = domainValidator0.isValid(".regexvalidator")
        self.assertTrue(domainValidator0.isAllowLocal())
        self.assertFalse(boolean0)

    def test60(self) -> None:

        linkedList0 = []
        domainValidator0 = DomainValidator(1618, linkedList0, False)
        boolean0 = domainValidator0.isValidGenericTld("bcg")
        self.assertTrue(boolean0)

    def test59(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_RO
        stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0)
        domainValidator_Item0 = Item(domainValidator_ArrayType0, stringArray0)
        domainValidator_ArrayType1 = DomainValidator.ArrayType.COUNTRY_CODE_MINUS
        domainValidator_Item1 = Item(domainValidator_ArrayType1, stringArray0)
        list0 = [
            domainValidator_Item0,
            domainValidator_Item1,
            domainValidator_Item1,
            domainValidator_Item1,
            domainValidator_Item1,
            domainValidator_Item1,
        ]
        domainValidator0 = DomainValidator(0, list0, True)
        self.assertTrue(domainValidator0.isAllowLocal())

    def test58(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.COUNTRY_CODE_RO
        stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0)

        domainValidator_ArrayType1 = DomainValidator.ArrayType.GENERIC_MINUS
        domainValidator_Item0 = Item(domainValidator_ArrayType1, stringArray0)

        list0 = [
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
        ]

        domainValidator0 = DomainValidator(0, list0, True)

        self.assertTrue(domainValidator0.isAllowLocal())

    def test57(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.COUNTRY_CODE_RO
        stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0)

        domainValidator_ArrayType1 = DomainValidator.ArrayType.LOCAL_MINUS
        domainValidator_Item0 = Item(domainValidator_ArrayType1, stringArray0)
        linkedList0 = [domainValidator_Item0]

        domainValidator0 = DomainValidator.getInstance2(False, linkedList0)
        stringArray1 = domainValidator0.getOverrides(domainValidator_ArrayType1)

        self.assertEqual(len(stringArray1), 307)
        self.assertFalse(domainValidator0.isAllowLocal())

    def test56(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_PLUS
        stringArray0 = []
        domainValidator_Item0 = Item(domainValidator_ArrayType0, stringArray0)
        linkedList0 = [domainValidator_Item0]
        domainValidator0 = DomainValidator(0, linkedList0, False)
        self.assertFalse(domainValidator0.isAllowLocal())

    def test55(self) -> None:

        domainValidator0 = DomainValidator.getInstance0()
        boolean0 = domainValidator0.isValid(None)
        self.assertFalse(boolean0)

    def test54(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_RO
        stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0)
        domainValidator_Item0 = Item(domainValidator_ArrayType0, stringArray0)
        list0 = [
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
        ]
        domainValidator0 = DomainValidator(0, list0, True)
        boolean0 = domainValidator0.isValid("lol")
        self.assertTrue(boolean0)

    def test53(self) -> None:

        domainValidator0 = DomainValidator.getInstance0()
        boolean0 = domainValidator0.isValid(".pk}")
        self.assertFalse(boolean0)

    def test52(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_RO
        stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0)
        domainValidator_Item0 = Item(domainValidator_ArrayType0, stringArray0)
        list0 = [
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
        ]
        domainValidator0 = DomainValidator(0, list0, True)
        boolean0 = domainValidator0.isValidDomainSyntax('..d>{"\!a`2k<ro[nuk')
        self.assertFalse(boolean0)
        self.assertTrue(domainValidator0.isAllowLocal())

    def test51(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_RO
        stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0)
        domainValidator_Item0 = Item(domainValidator_ArrayType0, stringArray0)
        list0 = [
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
        ]
        domainValidator0 = DomainValidator(0, list0, True)
        boolean0 = domainValidator0.isValidDomainSyntax(None)
        self.assertTrue(domainValidator0.isAllowLocal())
        self.assertFalse(boolean0)

    def test50(self) -> None:

        domainValidator0 = DomainValidator.getInstance0()
        boolean0 = domainValidator0.isValidDomainSyntax(
            "org.apache.commons.validator.routines.RegexValidator"
        )
        self.assertTrue(boolean0)

    def test49(self) -> None:

        domainValidator0 = DomainValidator.getInstance0()
        boolean0 = domainValidator0.isValidDomainSyntax("localdomain")
        self.assertTrue(boolean0)

    def test48(self) -> None:

        linkedList0 = []
        domainValidator0 = DomainValidator.getInstance2(True, linkedList0)
        boolean0 = domainValidator0.isValidTld("localdomain")
        self.assertTrue(boolean0)

    def test47(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_PLUS
        stringArray0 = ["::Hg"]
        domainValidator_Item0 = DomainValidator.Item(
            domainValidator_ArrayType0, stringArray0
        )
        list0 = [
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
        ]
        domainValidator0 = DomainValidator.getInstance2(False, list0)
        boolean0 = domainValidator0.isValidTld(":[Hg")
        self.assertFalse(domainValidator0.isAllowLocal())
        self.assertTrue(boolean0)

    def test46(self) -> None:

        linkedList0 = []
        domainValidator0 = DomainValidator.getInstance2(False, linkedList0)
        boolean0 = domainValidator0.isValidTld("cu")
        self.assertTrue(boolean0)
        self.assertFalse(domainValidator0.isAllowLocal())

    def test45(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_MINUS
        stringArray0 = ["toray"] * 7
        domainValidator_Item0 = DomainValidator.Item(
            domainValidator_ArrayType0, stringArray0
        )
        list0 = [domainValidator_Item0] * 9
        domainValidator0 = DomainValidator.getInstance2(False, list0)
        boolean0 = domainValidator0.isValidTld("toray")
        self.assertFalse(boolean0)
        self.assertFalse(domainValidator0.isAllowLocal())

    def test44(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.COUNTRY_CODE_PLUS
        stringArray0 = [
            "+`+?fs&ORu8pJBSA^",
            "+`+?fs&ORu8pJBSA^",
            "supplies",
            "+`+?fs&ORu8pJBSA^",
            "+`+?fs&ORu8pJBSA^",
            "JMwTb3D>du?Yk",
            "+`+?fs&ORu8pJBSA^",
        ]
        DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0)
        linkedList0 = []
        domainValidator0 = DomainValidator.getInstance2(True, linkedList0)
        boolean0 = domainValidator0.isValidCountryCodeTld("supplies")
        assert domainValidator0.isAllowLocal()
        assert boolean0

    def test43(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.COUNTRY_CODE_MINUS
        stringArray0 = ["PR"]
        domainValidator_Item0 = Item(domainValidator_ArrayType0, stringArray0)
        list0 = [
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
        ]
        domainValidator0 = DomainValidator.getInstance2(True, list0)
        boolean0 = domainValidator0.isValidTld("PR")
        self.assertFalse(boolean0)
        self.assertTrue(domainValidator0.isAllowLocal())

    def test42(self) -> None:

        domainValidator_ArrayType0 = ArrayType.LOCAL_PLUS
        stringArray0 = [";-]9dIQ(*H2'4CJ!"]
        domainValidator_Item0 = Item(domainValidator_ArrayType0, stringArray0)
        list0 = [domainValidator_Item0, domainValidator_Item0, domainValidator_Item0]
        domainValidator0 = DomainValidator.getInstance2(False, list0)
        boolean0 = domainValidator0.isValidLocalTld(";-]9dIQ(*H2'4CJ!")
        self.assertFalse(domainValidator0.isAllowLocal())
        self.assertTrue(boolean0)

    def test41(self) -> None:

        domain_validator0 = DomainValidator.getInstance0()
        boolean0 = domain_validator0.isValidCountryCodeTld(".}")
        self.assertFalse(boolean0)

    def test40(self) -> None:

        DomainValidator.getInstance0()
        domainValidator_ArrayType0 = DomainValidator.ArrayType.COUNTRY_CODE_PLUS
        stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0)

        try:
            DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Can only invoke this method before calling getInstance
            self.verifyException(
                "org.apache.commons.validator.routines.DomainValidator", e
            )

    def test39(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.COUNTRY_CODE_MINUS
        stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0)
        DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0)
        self.assertEqual(0, len(stringArray0))

    def test38(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_MINUS
        stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0)
        DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0)
        self.assertEqual(0, len(stringArray0))

    def test37(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_PLUS
        stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0)
        DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0)
        self.assertEqual(0, len(stringArray0))

    def test36(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_MINUS
        stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0)
        DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0)
        self.assertEqual(0, len(stringArray0))

    def test35(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_PLUS
        stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0)
        DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0)
        self.assertEqual(0, len(stringArray0))

    def test34(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.COUNTRY_CODE_RO
        stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0)

        with pytest.raises(ValueError):
            DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0)
            self.fail("Expecting exception: ValueError")

    def test33(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_RO
        stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0)

        with pytest.raises(ValueError):
            DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0)
            self.fail("Expecting exception: ValueError")

    def test32(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.INFRASTRUCTURE_RO
        stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0)

        with pytest.raises(ValueError):
            DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0)
            pytest.fail("Expecting exception: ValueError")

    def test31(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_RO
        stringArray0 = []

        try:
            DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException(
                "org.apache.commons.validator.routines.DomainValidator", e
            )

    def test30(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.COUNTRY_CODE_RO
        stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0)
        domainValidator_Item0 = Item(domainValidator_ArrayType0, stringArray0)
        list0 = [
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
        ]
        domainValidator0 = DomainValidator(0, list0, True)
        domainValidator_ArrayType1 = DomainValidator.ArrayType.LOCAL_MINUS
        domainValidator0.getOverrides(domainValidator_ArrayType1)
        self.assertTrue(domainValidator0.isAllowLocal())

    def test29(self) -> None:

        domain_validator0 = DomainValidator.getInstance0()
        domain_validator_ArrayType0 = DomainValidator.ArrayType.INFRASTRUCTURE_RO

        try:
            domain_validator0.getOverrides(domain_validator_ArrayType0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.apache.commons.validator.routines.DomainValidator", e)

    def test28(self) -> None:

        domainValidator0 = DomainValidator.getInstance0()

        # Undeclared exception handling in Python is done using try-except blocks
        try:
            domainValidator0.isValidCountryCodeTld(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # Python doesn't have a built-in verifyException method, but you can use assertions to check the exception type
            assert isinstance(e, TypeError), "Expecting exception: RuntimeError"

    def test27(self) -> None:

        domainValidator0 = DomainValidator.getInstance0()

        # Undeclared exception handling in Python is done using try-except blocks
        try:
            domainValidator0.isValidInfrastructureTld(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # Python doesn't have a built-in verifyException method, but you can use assertions to check the exception type
            assert isinstance(e, TypeError), "Expecting exception: RuntimeError"

    def test26(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_MINUS
        stringArray0 = [
            "accountant",
            "z< #tNhIw4*VE",
            "",
            "eat",
            'zYs,Sv:<5D"c',
            "",
            "",
            "",
            "z<*]jz?-(Eh",
        ]
        domainValidator_Item0 = Item(domainValidator_ArrayType0, stringArray0)
        list0 = [
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
        ]
        domainValidator0 = DomainValidator(0, list0, True)
        self.assertTrue(domainValidator0.isAllowLocal())

    def test25(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_RO
        stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0)

        domainValidator_ArrayType1 = DomainValidator.ArrayType.GENERIC_PLUS
        domainValidator_Item0 = Item(domainValidator_ArrayType1, stringArray0)

        list0 = [
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
        ]

        domainValidator0 = DomainValidator(0, list0, True)

        self.assertTrue(domainValidator0.isAllowLocal())

    def test24(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_RO
        stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0)
        domainValidator_Item0 = Item(domainValidator_ArrayType0, stringArray0)
        domainValidator_ArrayType1 = DomainValidator.ArrayType.COUNTRY_CODE_PLUS
        domainValidator_Item1 = Item(domainValidator_ArrayType1, stringArray0)
        list0 = [
            domainValidator_Item0,
            domainValidator_Item1,
            domainValidator_Item1,
            domainValidator_Item1,
            domainValidator_Item1,
            domainValidator_Item1,
        ]
        domainValidator0 = DomainValidator(0, list0, True)
        self.assertTrue(domainValidator0.isAllowLocal())

    def test23(self) -> None:

        linkedList0 = []
        domainValidator0 = DomainValidator.getInstance2(True, linkedList0)
        boolean0 = domainValidator0.isValidGenericTld("")
        self.assertTrue(domainValidator0.isAllowLocal())
        self.assertFalse(boolean0)

    def test22(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_PLUS
        stringArray0 = ["::Hg"]
        domainValidator_Item0 = DomainValidator.Item(
            domainValidator_ArrayType0, stringArray0
        )
        list0 = [
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
        ]
        domainValidator0 = DomainValidator.getInstance2(False, list0)
        boolean0 = domainValidator0.isValidGenericTld(":[Hg")
        self.assertFalse(domainValidator0.isAllowLocal())
        self.assertTrue(boolean0)

    def test21(self) -> None:

        domainValidator0 = DomainValidator.getInstance0()
        boolean0 = domainValidator0.isValidCountryCodeTld("cu")
        self.assertTrue(boolean0)

    def test20(self) -> None:

        domain_validator0 = DomainValidator.getInstance0()
        boolean0 = domain_validator0.isValidLocalTld("college")
        self.assertFalse(boolean0)

    def test19(self) -> None:

        domain_validator0 = None
        try:
            domain_validator0 = DomainValidator(0, None, False)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            pass

    def test18(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_RO
        stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0)
        domainValidator_Item0 = Item(domainValidator_ArrayType0, stringArray0)
        list0 = [
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
        ]
        domainValidator0 = DomainValidator(0, list0, True)

    def test17(self) -> None:

        with pytest.raises(RuntimeError):
            DomainValidator.getTLDEntries(None)

    def test16(self) -> None:

        domain_validator0 = DomainValidator.getInstance0()

        # Undeclared exception handling in Python is done using try-except blocks
        try:
            domain_validator0.isValidGenericTld(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # Python doesn't have a built-in function like verifyException in Java.
            # You can use assert to check if the exception is of the expected type.
            assert isinstance(e, TypeError), "Expecting exception: RuntimeError"

    def test15(self) -> None:

        domain_validator0 = DomainValidator.getInstance0()

        # Undeclared exception handling in Python is done using try-except blocks
        try:
            domain_validator0.isValidLocalTld(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # Python doesn't have a built-in verifyException method, but you can use assertions to check the exception type
            self.assertIsInstance(e, TypeError)

    def test14(self) -> None:

        domainValidator0 = DomainValidator.getInstance0()

        # Undeclared exception handling in Python is done using try-except blocks
        try:
            domainValidator0.isValidTld(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # Python doesn't have a built-in verifyException method, but you can use assertions to check the exception type
            assert isinstance(e, TypeError), "Expecting exception: RuntimeError"

    def test13(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_RO
        stringArray0 = [""]

        with self.assertRaises(RuntimeError):
            DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0)

    def test12(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_MINUS
        stringArray0 = [
            "_",
            "",
            "q+;OYL>?)j",
            "mSm$ SC~RD ",
            "org.apache.commons.validator.routines.RegexValidator",
        ]
        domainValidator_Item0 = Item(domainValidator_ArrayType0, stringArray0)
        list0 = [
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
        ]
        domainValidator0 = DomainValidator.getInstance2(True, list0)
        boolean0 = domainValidator0.isAllowLocal()
        self.assertTrue(boolean0)

    def test11(self) -> None:

        domainValidator0 = DomainValidator.getInstance0()
        boolean0 = domainValidator0.isValidInfrastructureTld("localdomain")
        self.assertFalse(boolean0)

    def test10(self) -> None:

        string0 = DomainValidator.unicodeToASCII("")
        self.assertEqual("", string0)

    def test09(self) -> None:

        string0 = DomainValidator.unicodeToASCII("`lVKf;<(]{u")
        self.assertEqual("`lVKf;<(]{u", string0)

    def test08(self) -> None:

        string0 = DomainValidator.unicodeToASCII(None)
        self.assertIsNone(string0)

    def test07(self) -> None:

        linkedList0 = []
        domainValidator0 = DomainValidator(-1, linkedList0, False)
        self.assertFalse(domainValidator0.isAllowLocal())

    def test06(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_MINUS
        stringArray0 = []
        domainValidator_Item0 = DomainValidator.Item(
            domainValidator_ArrayType0, stringArray0
        )
        list0 = [domainValidator_Item0, domainValidator_Item0]
        domainValidator0 = DomainValidator.getInstance2(False, list0)
        boolean0 = domainValidator0.isValidLocalTld(".localdomain")
        self.assertFalse(domainValidator0.isAllowLocal())
        self.assertTrue(boolean0)

    def test05(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_RO
        stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0)

        domainValidator_ArrayType1 = DomainValidator.ArrayType.COUNTRY_CODE_PLUS
        domainValidator_Item0 = Item(domainValidator_ArrayType1, stringArray0)

        list0 = [
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
        ]

        domainValidator0 = DomainValidator.getInstance2(True, list0)

        domainValidator_ArrayType2 = DomainValidator.ArrayType.COUNTRY_CODE_MINUS
        stringArray1 = domainValidator0.getOverrides(domainValidator_ArrayType2)

        self.assertEqual(0, len(stringArray1))
        self.assertTrue(domainValidator0.isAllowLocal())

    def test04(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.COUNTRY_CODE_MINUS
        stringArray0 = [""] * 5
        stringArray0[1] = '$=aAQp|Oni"=R'
        stringArray0[2] = "Ud|y8~I{"
        stringArray0[3] = "{3mr`<Dw#Dct&$"
        stringArray0[4] = "report"
        domainValidator_Item0 = Item(domainValidator_ArrayType0, stringArray0)
        list0 = [
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
        ]
        domainValidator0 = DomainValidator.getInstance2(True, list0)
        stringArray1 = domainValidator0.getOverrides(domainValidator_ArrayType0)
        self.assertTrue(domainValidator0.isAllowLocal())
        self.assertEqual(5, len(stringArray1))

    def test03(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_RO
        stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0)

        domainValidator_ArrayType1 = DomainValidator.ArrayType.COUNTRY_CODE_PLUS
        DomainValidator.updateTLDOverride(domainValidator_ArrayType1, stringArray0)

        linkedList0 = []
        domainValidator0 = DomainValidator.getInstance2(False, linkedList0)

        stringArray1 = domainValidator0.getOverrides(domainValidator_ArrayType1)

        self.assertFalse(domainValidator0.isAllowLocal())
        self.assertEqual(1201, len(stringArray1))

    def test02(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_MINUS
        stringArray0 = [
            "_",
            "",
            "q+;OYL>?)j",
            "mSm$ SC~RD ",
            "org.apache.commons.validator.routines.RegexValidator",
        ]
        domainValidator_Item0 = Item(domainValidator_ArrayType0, stringArray0)
        list0 = [
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
        ]
        domainValidator0 = DomainValidator.getInstance2(True, list0)
        stringArray1 = domainValidator0.getOverrides(domainValidator_ArrayType0)
        self.assertTrue(domainValidator0.isAllowLocal())
        self.assertEqual(5, len(stringArray1))

    def test01(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_PLUS
        stringArray0 = ["b<}Bc ,E(G)!"]
        stringArray0.append("Y%(,RtnG^pXYG/J(lN>")
        stringArray0.append('&b9L"Qb*+ 8q+pb')
        stringArray0.append("@9YN:P#T{EJ:")
        stringArray0.append(".africa")
        stringArray0.append("] is missing")
        stringArray0.append("hGjg0N-F:x+fo")
        stringArray0.append("-cy0hzf+g5`")
        domainValidator_Item0 = Item(domainValidator_ArrayType0, stringArray0)
        list0 = [domainValidator_Item0]
        domainValidator0 = DomainValidator.getInstance2(True, list0)
        stringArray1 = domainValidator0.getOverrides(domainValidator_ArrayType0)
        self.assertTrue(domainValidator0.isAllowLocal())
        self.assertEqual(8, len(stringArray1))

    def test00(self) -> None:

        domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_PLUS
        stringArray0 = ["{"]
        domainValidator_Item0 = DomainValidator.Item(
            domainValidator_ArrayType0, stringArray0
        )
        list0 = [
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
            domainValidator_Item0,
        ]
        domainValidator0 = DomainValidator.getInstance2(True, list0)
        stringArray1 = domainValidator0.getOverrides(domainValidator_ArrayType0)
        self.assertTrue(domainValidator0.isAllowLocal())
        self.assertEqual(1, len(stringArray1))
