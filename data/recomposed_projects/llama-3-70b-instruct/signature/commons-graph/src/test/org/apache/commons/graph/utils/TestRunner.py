from __future__ import annotations
import re
import unittest
import pytest
from abc import ABC
import io
import typing
from typing import *
from src.test.org.apache.commons.graph.utils.MultiThreadedTestRunner import *


class TestRunner(typing.Callable, ABC):

    __runner: MultiThreadedTestRunner = None

    def setTestRunner(self, runner: MultiThreadedTestRunner) -> None:
        self.__runner = runner

    def run(self) -> None:

        pass  # LLM could not translate this method

    def runTest(self) -> None:
        pass
