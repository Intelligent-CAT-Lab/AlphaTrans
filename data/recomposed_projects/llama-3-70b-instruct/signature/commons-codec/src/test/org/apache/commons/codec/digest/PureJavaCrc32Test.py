from __future__ import annotations
import re
import random
import os
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.digest.PureJavaCrc32 import *


class Table:

    __tables: typing.List[typing.List[int]] = None

    def toString(self) -> str:
        b = StringBuilder()
        tableFormat = (
            String.format(
                "T%d_", Integer.numberOfTrailingZeros(self.__tables[0].length)
            )
            + "%d"
        )
        startFormat = "  private static final int " + tableFormat + "_start = %d*256;"
        for j in range(0, self.__tables.length):
            b.append(String.format(startFormat, j, j))
            b.append("\n")
        b.append("  private static final int[] T = new int[] {")
        for s in self.toStrings(tableFormat):
            b.append("\n")
            b.append(s)
        b.setCharAt(b.length() - 2, "\n")
        b.append(" };\n")
        return b.toString()

    @staticmethod
    def main(args: typing.List[str]) -> None:

        pass  # LLM could not translate this method

    def __init__(self, nBits: int, nTables: int, polynomial: int) -> None:
        self.__tables = [[0 for _ in range(1 << nBits)] for _ in range(nTables)]
        first = self.__tables[0]
        for i in range(len(first)):
            crc = i
            for _ in range(nBits):
                if (crc & 1) == 1:
                    crc >>= 1
                    crc ^= polynomial
                else:
                    crc >>= 1
            first[i] = crc
        mask = len(first) - 1
        for j in range(1, len(self.__tables)):
            previous = self.__tables[j - 1]
            current = self.__tables[j]
            for i in range(len(current)):
                current[i] = (previous[i] >> nBits) ^ first[previous[i] & mask]

    def toStrings(self, nameformat: str) -> typing.List[str]:
        s: typing.List[str] = [None] * len(self.__tables)
        for j in range(len(self.__tables)):
            t: typing.List[int] = self.__tables[j]
            b: StringBuilder = StringBuilder()
            b.append(String.format("    /* " + nameformat + " */", j))
            i: int = 0
            while i < len(t):
                b.append("\n    ")
                for k in range(4):
                    b.append(String.format("0x%08X, ", t[i]))
                    i += 1
            s[j] = b.toString()
        return s


class BenchResult:

    mbps: float = 0.0

    value: int = 0

    def __init__(self, value: int, mbps: float) -> None:
        self.value = value
        self.mbps = mbps


class PerformanceTest:

    CRCS: typing.List[typing.Type[typing.Any]] = []

    zip: typing.Type[typing.Any] = CRC32
    MAX_LEN: int = 32 * 1024 * 1024
    BYTES_PER_SIZE: int = MAX_LEN * 4

    @staticmethod
    def run_static_init():
        PerformanceTest.CRCS.append(PerformanceTest.zip)
        PerformanceTest.CRCS.append(PureJavaCrc32)

    @staticmethod
    def main(args: typing.List[str]) -> None:
        PerformanceTest.__printSystemProperties(System.out)
        PerformanceTest.__doBench0(PerformanceTest.CRCS, System.out)

    @staticmethod
    def __printSystemProperties(out: typing.IO) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def __doBench2(
        clazz: typing.Type[typing.Any],
        numThreads: int,
        bytes: typing.List[int],
        size: int,
    ) -> BenchResult:

        pass  # LLM could not translate this method

    @staticmethod
    def __doBench1(
        crcs: typing.List[typing.Type[typing.Any]],
        bytes: typing.List[int],
        size: int,
        out: typing.IO,
    ) -> None:
        numBytesStr = " #Bytes "
        numThreadsStr = "#T"
        diffStr = "% diff"

        out.write("|")
        PerformanceTest.__printCell(numBytesStr, 0, out)
        PerformanceTest.__printCell(numThreadsStr, 0, out)
        for i in range(0, len(crcs)):
            c = crcs[i]
            out.write("|")
            PerformanceTest.__printCell(c.__name__, 8, out)
            for j in range(0, i):
                PerformanceTest.__printCell(diffStr, len(diffStr), out)
        out.write("\n")

        for numThreads in range(1, 17, 2):
            out.write("|")
            PerformanceTest.__printCell(str(size), len(numBytesStr), out)
            PerformanceTest.__printCell(str(numThreads), len(numThreadsStr), out)

            expected = None
            previous = []
            for c in crcs:
                System.gc()

                result = PerformanceTest.__doBench2(c, numThreads, bytes, size)
                PerformanceTest.__printCell(
                    str.format("%9.1f", result.mbps), len(c.__name__) + 1, out
                )

                if c == PerformanceTest.zip:
                    expected = result
                elif expected is None:
                    raise Exception(
                        "The first class is "
                        + c.__name__
                        + " but not "
                        + PerformanceTest.zip.__name__
                    )
                elif result.value != expected.value:
                    raise Exception(c + " has bugs!")

                for p in previous:
                    diff = (result.mbps - p.mbps) / p.mbps * 100
                    PerformanceTest.__printCell(
                        str.format("%5.1f%%", diff), len(diffStr), out
                    )
                previous.append(result)
            out.write("\n")

    @staticmethod
    def __doBench0(crcs: typing.List[typing.Type[typing.Any]], out: typing.IO) -> None:
        bytes: typing.List[int] = [0] * PerformanceTest.MAX_LEN
        random: Random = Random()
        random.nextBytes(bytes)

        out.write("\nPerformance Table (The unit is MB/sec; #T = #Theads)\n")

        for c in crcs:
            PerformanceTest.__doBench2(c, 1, bytes, 2)
            PerformanceTest.__doBench2(c, 1, bytes, 2101)

        for size in range(32, PerformanceTest.MAX_LEN + 1, 1 << 1):
            PerformanceTest.__doBench1(crcs, bytes, size, out)

    @staticmethod
    def __printCell(s: str, width: int, out: typing.IO) -> None:
        w = len(s) if len(s) > width else width
        out.write(" %{}s |".format(w) % s)


class PureJavaCrc32Test(unittest.TestCase):

    ours: PureJavaCrc32 = PureJavaCrc32()
    theirs: CRC32 = CRC32()

    def testCorrectness(self) -> None:
        self.__checkSame()

        self.__theirs.update(104)
        self.__ours.update1(104)
        self.__checkSame()

        self.__checkOnBytes([40, 60, 97, -70], False)

        self.__checkOnBytes("hello world!".encode("utf-8"), False)

        random1 = Random()
        random2 = Random()
        for i in range(10000):
            randomBytes = [0] * random1.nextInt(2048)
            random2.nextBytes(randomBytes)
            self.__checkOnBytes(randomBytes, False)

    def __checkSame(self) -> None:
        self.assertEqual(self.__theirs.getValue(), self.__ours.getValue())

    def __checkOnBytes(self, bytes: typing.List[int], print: bool) -> None:
        self.__theirs.reset()
        self.__ours.reset()
        self.__checkSame()

        for b in bytes:
            self.__ours.update1(b)
            self.__theirs.update(b)
            self.__checkSame()

        if print:
            print(
                "theirs:\t"
                + hex(self.__theirs.getValue())
                + "\nours:\t"
                + hex(self.__ours.getValue())
            )

        self.__theirs.reset()
        self.__ours.reset()

        self.__ours.update0(bytes, 0, len(bytes))
        self.__theirs.update(bytes, 0, len(bytes))
        if print:
            print(
                "theirs:\t"
                + hex(self.__theirs.getValue())
                + "\nours:\t"
                + hex(self.__ours.getValue())
            )

        self.__checkSame()

        if len(bytes) >= 10:
            self.__ours.update0(bytes, 5, 5)
            self.__theirs.update(bytes, 5, 5)
            self.__checkSame()


PerformanceTest.run_static_init()
