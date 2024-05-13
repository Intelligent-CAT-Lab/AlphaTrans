# Imports Begin
from src.main.org.apache.commons.fileupload.ProgressListener import *
import typing

# Imports End


class ProgressListenerTest:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    # Class Methods End

    pass


class ProgressListenerImpl(ProgressListener):

    # Class Fields Begin
    __expectedContentLength: int = None
    __expectedItems: int = None
    __bytesRead: int = None
    __items: int = None
    # Class Fields End

    # Class Methods Begin
    def update(self, pBytesRead: int, pContentLength: int, pItems: int) -> None:
        pass

    def checkFinished(self) -> None:
        pass

    def __init__(self, pContentLength: int, pItems: int) -> None:
        pass

    # Class Methods End
