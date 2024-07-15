from __future__ import annotations
import time
import re
import random
import sys
import os
import zlib
from io import StringIO
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

        b: io.StringIO = io.StringIO()

        tableFormat: str = f"T{len(self.__tables[0]).bit_length() - 9}_%d"
        startFormat: str = (
            "  private static final int " + tableFormat + "_start = %d*256;"
        )

        for j in range(len(self.__tables)):
            b.write(startFormat % (j, j))
            b.write("\n")

        b.write("  private static final int[] T = new int[] {")
        for s in self.toStrings(tableFormat):
            b.write("\n")
            b.write(s)
        b.seek(b.tell() - 2)
        b.write(" };\n")

        return b.getvalue()

    @staticmethod
    def main(args: typing.List[str]) -> None:

        if len(args) != 1:
            print("Usage: " + Table.__name__ + " <polynomial>")
            sys.exit(1)

        polynomial = int(args[0], 16)

        i = 8
        t = Table(i, 16, polynomial)
        s = t.toString()
        print(s)

        with open("table" + str(i) + ".txt", "w") as out:
            out.write(s)

    def __init__(self, nBits: int, nTables: int, polynomial: int) -> None:

        self.__tables = [[0] * (1 << nBits) for _ in range(nTables)]

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
                current[i] = (previous[i] >> 1) ^ first[previous[i] & mask]

    def toStrings(self, nameformat: str) -> typing.List[str]:

        s: typing.List[str] = [""] * len(self.__tables)

        for j in range(len(self.__tables)):
            t: typing.List[int] = self.__tables[j]
            b: io.StringIO = io.StringIO()
            b.write(f"    /* {nameformat} */".format(j))

            for i in range(0, len(t), 4):
                b.write("\n    ")
                for k in range(4):
                    b.write(f"0x{t[i+k]:08X}, ")

            s[j] = b.getvalue()

        return s


class BenchResult:

    mbps: float = 0.0

    value: int = 0

    def __init__(self, value: int, mbps: float) -> None:

        self.value = value
        self.mbps = mbps


class PerformanceTest:

    CRCS: typing.List[typing.Type[typing.Any]] = []

    zip: typing.Type[typing.Any] = PureJavaCrc32
    BYTES_PER_SIZE: int = 32 * 1024 * 1024 * 4
    MAX_LEN: int = 32 * 1024 * 1024

    @staticmethod
    def run_static_init():
        PerformanceTest.CRCS.append(PerformanceTest.zip)
        PerformanceTest.CRCS.append(PureJavaCrc32)

    @staticmethod
    def main(args: typing.List[str]) -> None:

        PerformanceTest.__printSystemProperties(sys.stdout)
        PerformanceTest.__doBench0(PerformanceTest.CRCS, sys.stdout)

    @staticmethod
    def __printSystemProperties(out: typing.IO) -> None:

        names = [
            "java.version",
            "java.runtime.name",
            "java.runtime.version",
            "java.vm.version",
            "java.vm.vendor",
            "java.vm.name",
            "java.vm.specification.version",
            "java.specification.version",
            "os.arch",
            "os.name",
            "os.version",
        ]
        p = os.environ
        for n in names:
            out.write(f"{n} = {p.get(n)}\n")

    @staticmethod
    def __doBench2(
        clazz: typing.Type[typing.Any],
        numThreads: int,
        bytes: typing.List[int],
        size: int,
    ) -> BenchResult:

        threads = [None] * numThreads
        results = [None] * len(threads)

        trials = PerformanceTest.BYTES_PER_SIZE // size
        mbProcessed = trials * size / 1024.0 / 1024.0
        ctor = clazz.__init__

        for i in range(len(threads)):
            index = i

            class Thread:
                crc = ctor()

                def run(self):
                    st = time.time_ns()
                    self.crc.reset()
                    for trialIndex in range(trials):
                        self.crc.update(bytes, 0, size)
                    et = time.time_ns()
                    secondsElapsed = (et - st) / 1000000000.0
                    results[index] = BenchResult(
                        self.crc.getValue(), mbProcessed / secondsElapsed
                    )

            threads[i] = Thread()

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        expected = results[0].value
        sum = results[0].mbps
        for i in range(1, len(results)):
            if results[i].value != expected:
                raise AssertionError(clazz.__name__ + " results not matched.")
            sum += results[i].mbps
        return BenchResult(expected, sum / len(results))

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
        for i in range(len(crcs)):
            c = crcs[i]
            out.write("|")
            PerformanceTest.__printCell(c.__name__, 8, out)
            for j in range(i):
                PerformanceTest.__printCell(diffStr, len(diffStr), out)
        out.write("\n")

        for numThreads in range(1, 17):
            out.write("|")
            PerformanceTest.__printCell(str(size), len(numBytesStr), out)
            PerformanceTest.__printCell(str(numThreads), len(numThreadsStr), out)

            expected = None
            previous = []
            for c in crcs:
                gc.collect()

                result = PerformanceTest.__doBench2(c, numThreads, bytes, size)
                PerformanceTest.__printCell(
                    f"{result.mbps:9.1f}", len(c.__name__) + 1, out
                )

                if c == PerformanceTest.zip:
                    expected = result
                elif expected is None:
                    raise RuntimeError(
                        f"The first class is {c.__name__} but not {PerformanceTest.zip.__name__}"
                    )
                elif result.value != expected.value:
                    raise RuntimeError(f"{c.__name__} has bugs.")

                for p in previous:
                    diff = (result.mbps - p.mbps) / p.mbps * 100
                    PerformanceTest.__printCell(f"{diff:5.1f}%", len(diffStr), out)
                previous.append(result)
            out.write("\n")

    @staticmethod
    def __doBench0(crcs: typing.List[typing.Type[typing.Any]], out: typing.IO) -> None:

        bytes = [0] * PerformanceTest.MAX_LEN
        Random().nextBytes(bytes)

        out.write("\nPerformance Table (The unit is MB/sec; #T = #Theads)\n")

        for c in crcs:
            PerformanceTest.__doBench2(c, 1, bytes, 2)
            PerformanceTest.__doBench2(c, 1, bytes, 2101)

        for size in range(32, PerformanceTest.MAX_LEN + 1, 2):
            PerformanceTest.__doBench1(crcs, bytes, size, out)

    @staticmethod
    def __printCell(s: str, width: int, out: typing.IO) -> None:
        w = len(s) if len(s) > width else width
        out.write(f" %{w}s |")


class PureJavaCrc32Test(unittest.TestCase):

    __ours: PureJavaCrc32 = PureJavaCrc32()
    __theirs: typing.Any = zlib.crc32(b"")

    def testCorrectness(self) -> None:

        self.__checkSame()

        self.__theirs.update(104)
        self.__ours.update1(104)
        self.__checkSame()

        self.__checkOnBytes([40, 60, 97, -70], False)

        self.__checkOnBytes("hello world!".encode("utf-8"), False)

        random1 = random.Random()
        random2 = random.Random()
        for i in range(10000):
            randomBytes = bytearray(random1.randint(0, 2048))
            random2.randbytes(randomBytes)
            self.__checkOnBytes(randomBytes, False)

    def __checkSame(self) -> None:

        # Assuming that PureJavaCrc32 has a method getValue()
        assert self.__theirs.getValue() == self.__ours.getValue()

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
                + hex(self.__theirs.getValue())[2:]
                + "\nours:\t"
                + hex(self.__ours.getValue())[2:]
            )

        self.__theirs.reset()
        self.__ours.reset()

        self.__ours.update0(bytes, 0, len(bytes))
        self.__theirs.update(bytes, 0, len(bytes))
        if print:
            print(
                "theirs:\t"
                + hex(self.__theirs.getValue())[2:]
                + "\nours:\t"
                + hex(self.__ours.getValue())[2:]
            )

        self.__checkSame()

        if len(bytes) >= 10:
            self.__ours.update0(bytes, 5, 5)
            self.__theirs.update(bytes, 5, 5)
            self.__checkSame()


PerformanceTest.run_static_init()
