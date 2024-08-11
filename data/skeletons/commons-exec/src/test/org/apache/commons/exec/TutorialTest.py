from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.exec.ExecuteException import *
from src.main.org.apache.commons.exec.DefaultExecuteResultHandler import *
from src.test.org.apache.commons.exec.TestUtil import *
from src.main.org.apache.commons.exec.Executor import *
from src.main.org.apache.commons.exec.ExecuteWatchdog import *
from src.main.org.apache.commons.exec.ExecuteResultHandler import *
from src.main.org.apache.commons.exec.DefaultExecutor import *
from src.main.org.apache.commons.exec.CommandLine import *
import unittest
import os
import datetime
import io
import pathlib

# Imports End


class PrintResultHandler(DefaultExecuteResultHandler):

    # Class Fields Begin
    __watchdog: ExecuteWatchdog = None
    # Class Fields End

    # Class Methods Begin
    def onProcessFailed(self, e: ExecuteException) -> None:
        pass

    def onProcessComplete(self, exitValue: int) -> None:
        pass

    def __init__(
        self, constructorId: int, exitValue: int, watchdog: ExecuteWatchdog
    ) -> None:
        pass

    # Class Methods End


class TutorialTest(unittest.TestCase):

    # Class Fields Begin
    __testDir: pathlib.Path = None
    __acroRd32Script: pathlib.Path = None
    # Class Fields End

    # Class Methods Begin
    def testTutorialExample_test2_decomposed(self) -> None:
        pass

    def testTutorialExample_test1_decomposed(self) -> None:
        pass

    def testTutorialExample_test0_decomposed(self) -> None:
        pass

    def print_(
        self,
        file: pathlib.Path,
        printJobTimeout: datetime.timedelta,
        printInBackground: bool,
    ) -> PrintResultHandler:
        pass

    # Class Methods End
