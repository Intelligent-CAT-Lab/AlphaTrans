# Imports Begin
from src.main.org.apache.commons.graph.utils.TestRunner import *
import typing

# Imports End


class MultiThreadedTestRunner:

    # Class Fields Begin
    __th: typing.List[threading.Thread] = None
    __exceptions: typing.List[BaseException] = None
    # Class Fields End

    # Class Methods Begin
    def runRunnables(self) -> None:
        pass

    def addException(self, e: BaseException) -> None:
        pass

    def __init__(self, runnables: typing.List[TestRunner]) -> None:
        pass

    # Class Methods End
