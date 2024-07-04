from __future__ import annotations
import re
import os
import numbers
import unittest
import pytest
import io
import unittest


class CustomValidatorResourcesTest(unittest.TestCase):

    def _tearDown(self) -> None:
        pass

    def _setUp(self) -> None:
        pass

    def testCustomResources(self) -> None:
        in_stream = None
        try:
            in_stream = open("TestNumber-config.xml", "r")
        except Exception as e:
            self.fail("Error loading resources: " + str(e))
        finally:
            try:
                if in_stream is not None:
                    in_stream.close()
            except Exception:
                pass

    def __init__(self, name: str) -> None:
        super().__init__(name)
