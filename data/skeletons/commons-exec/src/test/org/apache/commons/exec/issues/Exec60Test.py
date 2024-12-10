from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.exec.Executor import *
from src.main.org.apache.commons.exec.ExecuteWatchdog import *
from src.main.org.apache.commons.exec.ExecuteException import *
from src.main.org.apache.commons.exec.DefaultExecutor import *
from src.main.org.apache.commons.exec.CommandLine import *
from src.test.org.apache.commons.exec.AbstractExecTest import *
import unittest
import io
import pathlib

# Imports End


class Exec60Test(AbstractExecTest, unittest.TestCase):

    # Class Fields Begin
    __exec: Executor = None
    __pingScript: pathlib.Path = None
    # Class Fields End

    # Class Methods Begin
    def testExec_60(self) -> None:
        pass

    # Class Methods End
