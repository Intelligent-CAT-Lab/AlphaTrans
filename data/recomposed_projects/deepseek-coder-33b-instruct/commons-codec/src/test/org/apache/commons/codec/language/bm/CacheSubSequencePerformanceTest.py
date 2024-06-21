from __future__ import annotations
import re
import unittest
import pytest
import io


class CacheSubSequencePerformanceTest(unittest.TestCase):

    def test0(self) -> None:

        times = 10000000
        print("Test with String : ", end="")
        self.__test1("Angelo", times)
        print("Test with StringBuilder : ", end="")
        self.__test1(StringBuilder("Angelo"), times)
        print("Test with cached String : ", end="")
        self.__test1(self.__cacheSubSequence("Angelo"), times)
        print("Test with cached StringBuilder : ", end="")
        self.__test1(self.__cacheSubSequence(StringBuilder("Angelo")), times)

    def __cacheSubSequence(self, cached: str) -> str:

        class CacheCharSequence(io.StringIO):
            def __init__(self, cached: str):
                super().__init__(cached)
                self.cache = [
                    [None for _ in range(len(cached))] for _ in range(len(cached))
                ]

            def subSequence(self, start: int, end: int) -> str:
                if start == end:
                    return ""
                res = self.cache[start][end - 1]
                if res is None:
                    res = cached[start:end]
                    self.cache[start][end - 1] = res
                return res

        return CacheCharSequence(cached)

    def __test2(self, input: str) -> None:

        for i in range(len(input)):
            for j in range(i, len(input) + 1):
                input[i:j]

    def __test1(self, input: str, times: int) -> None:

        begin_time_millis = int(round(time.time() * 1000))
        for i in range(times):
            self.__test2(input)
        print(str(int(round(time.time() * 1000)) - begin_time_millis) + " millis")
