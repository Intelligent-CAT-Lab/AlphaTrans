from __future__ import annotations

# Imports Begin
import io

# Imports End


class Timer:

    # Class Fields Begin
    __startNano: int = None
    __duration: int = None
    # Class Fields End

    # Class Methods Begin
    def getDuration(self) -> int:
        pass

    def end(self) -> int:
        pass

    def start(self) -> None:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End


class PerformanceLogger:

    # Class Fields Begin
    compressionTimer: Timer = None
    decompressionTimer: Timer = None
    __originalSize: int = None
    __compressedSize: int = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def __getMiS(size: int, nanoTime: int) -> float:
        pass

    def getDecompressSpeed(self) -> float:
        pass

    def getCompressSpeed(self) -> float:
        pass

    def getBitPerInt(self) -> float:
        pass

    def getCompressedSize(self) -> int:
        pass

    def getOriginalSize(self) -> int:
        pass

    def addCompressedSize(self, value: int) -> int:
        pass

    def addOriginalSize(self, value: int) -> int:
        pass

    # Class Methods End
