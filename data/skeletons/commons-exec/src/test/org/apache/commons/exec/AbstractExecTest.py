from __future__ import annotations

# Imports Begin
from src.test.org.apache.commons.exec.TestUtil import *
import io
import pathlib
from abc import ABC

# Imports End


class AbstractExecTest(ABC):

    # Class Fields Begin
    TEST_TIMEOUT: int = None
    WATCHDOG_TIMEOUT: int = None
    __OS_NAME: str = None
    __testDir: pathlib.Path = None
    # Class Fields End

    # Class Methods Begin
    def _testNotSupportedForCurrentOperatingSystem(self) -> str:
        pass

    def _testIsBrokenForCurrentOperatingSystem(self) -> str:
        pass

    def _resolveTestScript1(self, directoryName: str, baseName: str) -> pathlib.Path:
        pass

    def _resolveTestScript0(self, baseName: str) -> pathlib.Path:
        pass

    # Class Methods End
