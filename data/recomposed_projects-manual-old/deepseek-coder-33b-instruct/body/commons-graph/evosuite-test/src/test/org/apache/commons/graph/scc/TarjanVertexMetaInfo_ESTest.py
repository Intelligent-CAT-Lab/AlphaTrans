from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.scc.TarjanVertexMetaInfo import *

# from src.test.org.apache.commons.graph.scc.TarjanVertexMetaInfo_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class TarjanVertexMetaInfo_ESTest(unittest.TestCase):

    def test8(self) -> None:

        tarjanVertexMetaInfo0 = TarjanVertexMetaInfo()
        int0 = tarjanVertexMetaInfo0.getIndex()
        self.assertEqual(-1, int0)
        self.assertEqual(-1, tarjanVertexMetaInfo0.getLowLink())

    def test7(self) -> None:

        tarjanVertexMetaInfo0 = TarjanVertexMetaInfo()
        int0 = tarjanVertexMetaInfo0.getLowLink()
        self.assertEqual(-1, tarjanVertexMetaInfo0.getIndex())
        self.assertEqual(-1, int0)

    def test6(self) -> None:

        tarjanVertexMetaInfo0 = TarjanVertexMetaInfo()
        self.assertEqual(-1, tarjanVertexMetaInfo0.getLowLink())

        tarjanVertexMetaInfo0.setLowLink(0)
        int0 = tarjanVertexMetaInfo0.getLowLink()
        self.assertEqual(0, int0)

    def test5(self) -> None:

        tarjanVertexMetaInfo0 = TarjanVertexMetaInfo()
        self.assertEqual(-1, tarjanVertexMetaInfo0.getIndex())

        tarjanVertexMetaInfo0.setIndex(0)
        boolean0 = tarjanVertexMetaInfo0.hasUndefinedIndex()
        self.assertEqual(0, tarjanVertexMetaInfo0.getIndex())
        self.assertFalse(boolean0)

    def test4(self) -> None:

        tarjanVertexMetaInfo0 = TarjanVertexMetaInfo()
        boolean0 = tarjanVertexMetaInfo0.hasUndefinedIndex()
        self.assertTrue(boolean0)
        self.assertEqual(-1, tarjanVertexMetaInfo0.getLowLink())

    def test3(self) -> None:

        tarjanVertexMetaInfo0 = TarjanVertexMetaInfo()
        tarjanVertexMetaInfo0.setIndex(877)
        int0 = tarjanVertexMetaInfo0.getIndex()
        self.assertEqual(877, int0)

    def test2(self) -> None:

        tarjanVertexMetaInfo0 = TarjanVertexMetaInfo()
        self.assertTrue(tarjanVertexMetaInfo0.hasUndefinedIndex())

        tarjanVertexMetaInfo0.setIndex(0)
        int0 = tarjanVertexMetaInfo0.getIndex()
        self.assertEqual(0, int0)

    def test1(self) -> None:

        tarjanVertexMetaInfo0 = TarjanVertexMetaInfo()
        tarjanVertexMetaInfo0.setLowLink(2901)
        int0 = tarjanVertexMetaInfo0.getLowLink()
        self.assertEqual(2901, int0)

    def test0(self) -> None:

        tarjanVertexMetaInfo0 = TarjanVertexMetaInfo()
        tarjanVertexMetaInfo0.setIndex(-1184)
        boolean0 = tarjanVertexMetaInfo0.hasUndefinedIndex()
        self.assertEqual(-1184, tarjanVertexMetaInfo0.getIndex())
        self.assertFalse(boolean0)
