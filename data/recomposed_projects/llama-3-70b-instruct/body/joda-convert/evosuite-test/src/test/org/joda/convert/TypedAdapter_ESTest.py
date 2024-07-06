from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import typing
from typing import *
import unittest

# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.TypeTokenStringConverter import *
from src.main.org.joda.convert.TypedAdapter import *

# from src.test.org.joda.convert.TypedAdapter_ESTest_scaffolding import *
from src.main.org.joda.convert.TypedStringConverter import *


class TypedAdapter_ESTest(unittest.TestCase):

    def test0(self) -> None:

        class0 = TypeTokenStringConverter
        typedStringConverter0 = TypedAdapter.adapt(class0, None)
        typedStringConverter1 = TypedAdapter.adapt(class0, typedStringConverter0)
        self.assertIs(typedStringConverter1, typedStringConverter0)
