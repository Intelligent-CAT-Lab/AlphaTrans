from __future__ import annotations

# Imports Begin
from src.test.org.apache.commons.exec.TestUtil import *
from src.main.org.apache.commons.exec.PumpStreamHandler import *
from src.main.org.apache.commons.exec.OS import *
from src.main.org.apache.commons.exec.ExecuteWatchdog import *
from src.main.org.apache.commons.exec.ExecuteStreamHandler import *
from src.main.org.apache.commons.exec.ExecuteException import *
from src.main.org.apache.commons.exec.DefaultExecutor import *
from src.main.org.apache.commons.exec.CommandLine import *
import unittest
import io
import pathlib

# Imports End


class Exec41Test(unittest.TestCase):

    # Class Fields Begin
    __testDir: pathlib.Path = None
    __pingScript: pathlib.Path = None
    # Class Fields End

    # Class Methods Begin
    def testExec41WithStreams(self) -> None:
        pass

    def testExec41WithoutStreams(self) -> None:
        pass

    # Class Methods End
