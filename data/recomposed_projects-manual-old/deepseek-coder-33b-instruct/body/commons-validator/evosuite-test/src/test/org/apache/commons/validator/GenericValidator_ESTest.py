from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.GenericValidator import *

# from src.test.org.apache.commons.validator.GenericValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class GenericValidator_ESTest(unittest.TestCase):

    def test87(self) -> None:
        boolean0 = GenericValidator.isCreditCard("5g~@j rdLbg(")
        self.assertFalse(boolean0)

    def test86(self) -> None:
        boolean0 = GenericValidator.isDate0(":p1^X$(rtiVc/-'8", None)
        self.assertFalse(boolean0)

    def test85(self) -> None:
        boolean0 = GenericValidator.isEmail(None)
        self.assertFalse(boolean0)

    def test84(self) -> None:
        boolean0 = GenericValidator.isDate1("6", "6", True)
        self.assertTrue(boolean0)

    def test83(self) -> None:

        generic_validator0 = GenericValidator()

    def test82(self) -> None:

        boolean0 = GenericValidator.isUrl(":p1^X$(rtiVc/-'8")
        self.assertFalse(boolean0)

    def test81(self) -> None:
        boolean0 = GenericValidator.isBlankOrNull(None)
        self.assertTrue(boolean0)

    def test80(self) -> None:
        boolean0 = GenericValidator.isBlankOrNull("OD_3ktO$TiX2kvoXDu")
        self.assertFalse(boolean0)

    def test79(self) -> None:
        boolean0 = GenericValidator.isBlankOrNull("")
        self.assertTrue(boolean0)

    def test78(self) -> None:

        boolean0 = GenericValidator.matchRegexp(None, None)
        self.assertFalse(boolean0)

    def test77(self) -> None:

        boolean0 = GenericValidator.matchRegexp("6", "6")
        self.assertTrue(boolean0)

    def test76(self) -> None:

        boolean0 = GenericValidator.matchRegexp("", "")
        self.assertFalse(boolean0)

    def test75(self) -> None:
        boolean0 = GenericValidator.isInRange0(50, 52, 50)
        self.assertFalse(boolean0)

    def test74(self) -> None:
        boolean0 = GenericValidator.isInRange0(0, 0, 1)
        self.assertTrue(boolean0)

    def test73(self) -> None:
        boolean0 = GenericValidator.isInRange0(1, 1, 0)
        self.assertFalse(boolean0)

    def test72(self) -> None:
        boolean0 = GenericValidator.isInRange1((-3098), 1451, 1451)
        self.assertFalse(boolean0)

    def test71(self) -> None:
        boolean0 = GenericValidator.isInRange1(4, 4, 4)
        self.assertTrue(boolean0)

    def test70(self) -> None:
        boolean0 = GenericValidator.isInRange2((-1109), 1.0, (-3995.326))
        self.assertFalse(boolean0)

    def test69(self) -> None:
        boolean0 = GenericValidator.isInRange2(1407, 0.0, 0.0)
        self.assertFalse(boolean0)

    def test68(self) -> None:
        boolean0 = GenericValidator.isInRange3(464, 707, 0)
        self.assertFalse(boolean0)

    def test67(self) -> None:
        boolean0 = GenericValidator.isInRange3(0, 0, 1173)
        self.assertTrue(boolean0)

    def test66(self) -> None:
        boolean0 = GenericValidator.isInRange3(1173, 1173, 417)
        self.assertFalse(boolean0)

    def test65(self) -> None:
        boolean0 = GenericValidator.isInRange4(0, 0, 1103)
        self.assertFalse(boolean0)

    def test64(self) -> None:
        boolean0 = GenericValidator.isInRange4(608, 0, 0)
        self.assertFalse(boolean0)

    def test63(self) -> None:
        boolean0 = GenericValidator.isInRange4((-1510), (-4340), 1)
        self.assertTrue(boolean0)

    def test62(self) -> None:
        boolean0 = GenericValidator.isInRange5((-1.0), 0, 0)
        self.assertFalse(boolean0)

    def test61(self) -> None:
        boolean0 = GenericValidator.isInRange5(1819.8485, -846.1781808, -846.1781808)
        self.assertFalse(boolean0)

    def test60(self) -> None:
        boolean0 = GenericValidator.maxLength0(":p1^X$(rtiVc/-'8", -1)
        self.assertFalse(boolean0)

    def test59(self) -> None:
        boolean0 = GenericValidator.maxLength0("", 0)
        self.assertTrue(boolean0)

    def test58(self) -> None:

        boolean0 = GenericValidator.maxLength1(
            "org.apache.commons.validator.GenericValidator", 453, 453
        )
        self.assertTrue(boolean0)

    def test57(self) -> None:
        boolean0 = GenericValidator.minLength0("X&Z\u0000us^PTsBI2tLt]", 1151)
        self.assertFalse(boolean0)

    def test56(self) -> None:
        boolean0 = GenericValidator.minLength0("IyNzKSe", 1)
        self.assertTrue(boolean0)

    def test55(self) -> None:

        boolean0 = GenericValidator.minLength1("X&Z\u0000us^PTsBI2tLt]", 439, 439)
        self.assertFalse(boolean0)

    def test54(self) -> None:

        boolean0 = GenericValidator.minLength1("kerryproperties", -4479, -4479)
        self.assertTrue(boolean0)

    def test53(self) -> None:
        boolean0 = GenericValidator.minValue0(901, 1119)
        self.assertFalse(boolean0)

    def test52(self) -> None:
        boolean0 = GenericValidator.minValue0(1351, (-1))
        self.assertTrue(boolean0)

    def test51(self) -> None:
        boolean0 = GenericValidator.minValue1((-2598), 0)
        self.assertFalse(boolean0)

    def test50(self) -> None:
        boolean0 = GenericValidator.minValue1(1, 0)
        self.assertTrue(boolean0)

    def test49(self) -> None:
        boolean0 = GenericValidator.minValue2(1.0, 618)
        self.assertFalse(boolean0)

    def test48(self) -> None:
        boolean0 = GenericValidator.minValue2(314.023783, -1.0)
        self.assertTrue(boolean0)

    def test47(self) -> None:
        boolean0 = GenericValidator.minValue3((-1.0), 1108.2054)
        self.assertFalse(boolean0)

    def test46(self) -> None:
        boolean0 = GenericValidator.minValue3(1819.8485, 0)
        self.assertTrue(boolean0)

    def test45(self) -> None:
        boolean0 = GenericValidator.maxValue0(760, 28)
        self.assertFalse(boolean0)

    def test44(self) -> None:
        boolean0 = GenericValidator.maxValue0((-2126), (-1569))
        self.assertTrue(boolean0)

    def test43(self) -> None:
        boolean0 = GenericValidator.maxValue1((-1), (-500))
        self.assertFalse(boolean0)

    def test42(self) -> None:
        boolean0 = GenericValidator.maxValue1((-443), 0)
        self.assertTrue(boolean0)

    def test41(self) -> None:
        boolean0 = GenericValidator.maxValue2(618, (-1.0))
        self.assertFalse(boolean0)

    def test40(self) -> None:
        boolean0 = GenericValidator.maxValue2(0, 0)
        self.assertTrue(boolean0)

    def test39(self) -> None:
        boolean0 = GenericValidator.maxValue3(4278.329, 0.0)
        self.assertFalse(boolean0)

    def test38(self) -> None:
        boolean0 = GenericValidator.maxValue3(1819.8485, 1819.8485)
        self.assertTrue(boolean0)

    def test36(self) -> None:

        # Undeclared exception
        try:
            GenericValidator.isDate1("xhMFx6{=~kOMgCQ", "xhMFx6{=~kOMgCQ", True)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Illegal pattern character 'x'
            self.verifyException("java.text.SimpleDateFormat", e)

    def test30(self) -> None:

        try:
            GenericValidator.matchRegexp(':Uy";hY-YJd', ':Uy";hY-YJd')
        except ValueError:
            pass

    def test29(self) -> None:

        try:
            GenericValidator.matchRegexp("m07f@qS(x=f=/l", "m07f@qS(x=f=/l")
            self.fail("Expecting exception: PatternSyntaxException")

        except re.error as e:
            # Unclosed group near index 15
            # m07f@qS(x=f=/l
            #
            self.assertRegex(str(e), r"unclosed group")

    def test28(self) -> None:

        with pytest.raises(RuntimeError):
            GenericValidator.maxLength0(None, -526)

    def test27(self) -> None:

        try:
            GenericValidator.maxLength1(None, -1, -1)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e), RuntimeError)

    def test26(self) -> None:

        with pytest.raises(RuntimeError):
            GenericValidator.minLength0(None, 4638)

    def test25(self) -> None:

        try:
            GenericValidator.minLength1(None, 4638, 4638)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e), RuntimeError)

    def test24(self) -> None:
        boolean0 = GenericValidator.isDate1("_gj~f:WG_", "", True)
        self.assertFalse(boolean0)

    def test23(self) -> None:
        boolean0 = GenericValidator.isInRange0((-1), (-80), (-1))
        self.assertTrue(boolean0)

    def test22(self) -> None:
        boolean0 = GenericValidator.isInRange1(201, 4, 4)
        self.assertFalse(boolean0)

    def test21(self) -> None:
        boolean0 = GenericValidator.isInRange1(short(-98), short(-98), 676)
        self.assertTrue(boolean0)

    def test20(self) -> None:
        boolean0 = GenericValidator.isInRange2((-1269.3605), (-1269.3605), (-1269.3605))
        self.assertTrue(boolean0)

    def test19(self) -> None:
        boolean0 = GenericValidator.isInRange2(0.0, 0.0, 660.781)
        self.assertTrue(boolean0)

    def test18(self) -> None:
        boolean0 = GenericValidator.isInRange3(869, 0, 0)
        self.assertFalse(boolean0)

    def test17(self) -> None:
        boolean0 = GenericValidator.isInRange3(3052, 3052, 3052)
        self.assertTrue(boolean0)

    def test16(self) -> None:
        boolean0 = GenericValidator.isInRange4(0, 0, 0)
        self.assertTrue(boolean0)

    def test15(self) -> None:
        boolean0 = GenericValidator.isInRange5(1819.8485, 1819.8485, 1819.8485)
        self.assertTrue(boolean0)

    def test14(self) -> None:
        boolean0 = GenericValidator.isInRange5((-1.0), (-562.6511325711), 0)
        self.assertTrue(boolean0)

    def test13(self) -> None:
        boolean0 = GenericValidator.maxLength0("L^vv>?<NjY", 1407)
        self.assertTrue(boolean0)

    def test12(self) -> None:

        boolean0 = GenericValidator.maxLength1("5g~@j rdLbg(", 0, 3067)
        self.assertFalse(boolean0)

    def test11(self) -> None:

        boolean0 = GenericValidator.maxLength1("", 0, 0)
        self.assertTrue(boolean0)

    def test10(self) -> None:
        boolean0 = GenericValidator.minLength0("7", 1)
        self.assertTrue(boolean0)

    def test09(self) -> None:

        boolean0 = GenericValidator.minLength1("YzH6", 56, 901)
        self.assertFalse(boolean0)

    def test08(self) -> None:

        boolean0 = GenericValidator.minLength1("", 0, 0)
        self.assertTrue(boolean0)

    def test07(self) -> None:
        boolean0 = GenericValidator.minValue0(439, 439)
        self.assertTrue(boolean0)

    def test06(self) -> None:
        boolean0 = GenericValidator.minValue1(4, 4)
        self.assertTrue(boolean0)

    def test05(self) -> None:
        boolean0 = GenericValidator.minValue2((-3130.8232), (-3130.8232))
        self.assertTrue(boolean0)

    def test04(self) -> None:
        boolean0 = GenericValidator.minValue3((-43.566), (-43.566))
        self.assertTrue(boolean0)

    def test03(self) -> None:
        boolean0 = GenericValidator.maxValue0(0, 0)
        self.assertTrue(boolean0)

    def test02(self) -> None:
        boolean0 = GenericValidator.maxValue1(618, 618)
        self.assertTrue(boolean0)

    def test01(self) -> None:
        boolean0 = GenericValidator.maxValue2(0.0, 2024.657723147502)
        self.assertTrue(boolean0)

    def test00(self) -> None:
        boolean0 = GenericValidator.maxValue3(0, 2533.4265)
        self.assertTrue(boolean0)
