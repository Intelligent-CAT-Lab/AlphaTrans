from __future__ import annotations

# Imports Begin
from src.test.org.apache.commons.exec.TestUtil import *
from src.main.org.apache.commons.exec.PumpStreamHandler import *
from src.main.org.apache.commons.exec.OS import *
from src.main.org.apache.commons.exec.ExecuteWatchdog import *
from src.main.org.apache.commons.exec.ExecuteStreamHandler import *
from src.main.org.apache.commons.exec.DefaultExecutor import *
from src.main.org.apache.commons.exec.CommandLine import *
import unittest
import io
import pathlib

# Imports End


class Exec62Test(unittest.TestCase):

    # Class Fields Begin
    __outputFile: Path = None
    # Class Fields End

    # Class Methods Begin
    def testMe(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    def __execute(self, scriptName: str) -> None:
        pass

    # Class Methods End
