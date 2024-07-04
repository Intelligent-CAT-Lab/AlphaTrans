from __future__ import annotations
import time
import copy
import re
import os
import datetime
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.impl.AbandonedConfig import *

# from src.test.org.apache.commons.pool2.impl.AbandonedConfig_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class AbandonedConfig_ESTest(unittest.TestCase):

    def test24(self) -> None:
        abandonedConfig0 = AbandonedConfig(0, None)
        abandonedConfig0.setRemoveAbandonedTimeout1(-1098)
        self.assertTrue(abandonedConfig0.getRequireFullStackTrace())

    def test23(self) -> None:
        abandonedConfig0 = AbandonedConfig(23, None)
        abandonedConfig0.getRemoveAbandonedTimeout()
        self.assertTrue(abandonedConfig0.getRequireFullStackTrace())

    def test22(self) -> None:

        abandonedConfig0 = AbandonedConfig(23, None)
        abandonedConfig0.toString()
        self.assertTrue(abandonedConfig0.getRequireFullStackTrace())

    def test21(self) -> None:
        abandonedConfig0 = AbandonedConfig.copy(None)
        self.assertIsNone(abandonedConfig0)

    def test20(self) -> None:
        abandonedConfig0 = AbandonedConfig(-2737, None)
        abandonedConfig0.getRemoveAbandonedOnMaintenance()
        self.assertTrue(abandonedConfig0.getRequireFullStackTrace())

    def test19(self) -> None:
        abandonedConfig0 = AbandonedConfig(631, None)
        abandonedConfig0.getLogAbandoned()
        self.assertTrue(abandonedConfig0.getRequireFullStackTrace())

    def test18(self) -> None:
        abandonedConfig0 = AbandonedConfig(1, None)
        abandonedConfig0.getRemoveAbandonedOnBorrow()
        self.assertTrue(abandonedConfig0.getRequireFullStackTrace())

    def test17(self) -> None:
        abandonedConfig0 = AbandonedConfig(1762, None)
        abandonedConfig0.getUseUsageTracking()
        self.assertTrue(abandonedConfig0.getRequireFullStackTrace())

    def test16(self) -> None:
        abandonedConfig0 = AbandonedConfig(252, None)
        boolean0 = abandonedConfig0.getRequireFullStackTrace()
        self.assertTrue(boolean0)

    def test15(self) -> None:
        abandonedConfig0 = AbandonedConfig(-2737, None)
        duration0 = abandonedConfig0.getRemoveAbandonedTimeoutDuration()
        abandonedConfig0.setRemoveAbandonedTimeout0(duration0)
        self.assertTrue(abandonedConfig0.getRequireFullStackTrace())

    def test14(self) -> None:
        abandonedConfig0 = AbandonedConfig(-1, None)
        printWriter0 = abandonedConfig0.getLogWriter()
        abandonedConfig0.setLogWriter(printWriter0)
        self.assertTrue(abandonedConfig0.getRequireFullStackTrace())

    def test13(self) -> None:
        abandonedConfig0 = None
        try:
            abandonedConfig0 = AbandonedConfig(0, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.apache.commons.pool2.impl.AbandonedConfig", e)

    def test12(self) -> None:
        abandonedConfig0 = AbandonedConfig(631, None)
        abandonedConfig0.setLogAbandoned(True)
        abandonedConfig1 = AbandonedConfig.copy(abandonedConfig0)
        self.assertTrue(abandonedConfig0.getLogAbandoned())
        self.assertTrue(abandonedConfig1.getRequireFullStackTrace())

    def test11(self) -> None:
        abandonedConfig0 = AbandonedConfig(631, None)
        abandonedConfig0.setRemoveAbandonedOnBorrow(True)
        abandonedConfig1 = AbandonedConfig.copy(abandonedConfig0)
        self.assertTrue(abandonedConfig0.getRemoveAbandonedOnBorrow())
        self.assertFalse(abandonedConfig1.getRemoveAbandonedOnMaintenance())

    def test10(self) -> None:
        abandonedConfig0 = AbandonedConfig(137, None)
        abandonedConfig0.setRemoveAbandonedOnMaintenance(True)
        AbandonedConfig.copy(abandonedConfig0)
        self.assertTrue(abandonedConfig0.getRemoveAbandonedOnMaintenance())
        self.assertTrue(abandonedConfig0.getRequireFullStackTrace())

    def test09(self) -> None:
        abandonedConfig0 = AbandonedConfig(774, None)
        self.assertTrue(abandonedConfig0.getRequireFullStackTrace())

        abandonedConfig0.setRequireFullStackTrace(False)
        abandonedConfig1 = AbandonedConfig.copy(abandonedConfig0)
        self.assertFalse(abandonedConfig0.getRequireFullStackTrace())
        self.assertFalse(abandonedConfig1.getRemoveAbandonedOnMaintenance())

    def test08(self) -> None:
        abandonedConfig0 = AbandonedConfig(2567, None)
        abandonedConfig0.setUseUsageTracking(True)
        abandonedConfig1 = AbandonedConfig.copy(abandonedConfig0)
        self.assertTrue(abandonedConfig0.getUseUsageTracking())
        self.assertFalse(abandonedConfig1.getRemoveAbandonedOnMaintenance())

    def test07(self) -> None:
        abandonedConfig0 = AbandonedConfig(631, None)
        abandonedConfig0.setLogAbandoned(True)
        boolean0 = abandonedConfig0.getLogAbandoned()
        self.assertTrue(boolean0)

    def test06(self) -> None:
        abandonedConfig0 = AbandonedConfig(23, None)
        abandonedConfig0.setLogWriter(None)
        abandonedConfig0.getLogWriter()
        self.assertTrue(abandonedConfig0.getRequireFullStackTrace())

    def test05(self) -> None:
        abandonedConfig0 = AbandonedConfig(1, None)
        abandonedConfig0.setRemoveAbandonedOnBorrow(True)
        boolean0 = abandonedConfig0.getRemoveAbandonedOnBorrow()
        self.assertTrue(boolean0)

    def test04(self) -> None:
        abandonedConfig0 = AbandonedConfig(137, None)
        abandonedConfig0.setRemoveAbandonedOnMaintenance(True)
        boolean0 = abandonedConfig0.getRemoveAbandonedOnMaintenance()
        self.assertTrue(boolean0)

    def test03(self) -> None:
        abandonedConfig0 = AbandonedConfig(-2312, None)
        duration0 = datetime.timedelta(microseconds=-2312)
        abandonedConfig0.setRemoveAbandonedTimeout0(duration0)
        abandonedConfig0.getRemoveAbandonedTimeout()
        self.assertTrue(abandonedConfig0.getRequireFullStackTrace())

    def test02(self) -> None:
        abandonedConfig0 = AbandonedConfig(137, None)
        duration0 = datetime.timedelta(milliseconds=137)
        abandonedConfig0.setRemoveAbandonedTimeout0(duration0)
        abandonedConfig0.getRemoveAbandonedTimeout()
        self.assertTrue(abandonedConfig0.getRequireFullStackTrace())

    def test01(self) -> None:
        abandonedConfig0 = AbandonedConfig(0, None)
        self.assertTrue(abandonedConfig0.getRequireFullStackTrace())

        abandonedConfig0.setRequireFullStackTrace(False)
        boolean0 = abandonedConfig0.getRequireFullStackTrace()
        self.assertFalse(boolean0)

    def test00(self) -> None:
        abandonedConfig0 = AbandonedConfig(1762, None)
        abandonedConfig0.setUseUsageTracking(True)
        boolean0 = abandonedConfig0.getUseUsageTracking()
        self.assertTrue(boolean0)
