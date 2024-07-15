from __future__ import annotations
import time
import locale
import re
import mock
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *

# from src.test.org.apache.commons.graph.model.DirectedMutableGraph_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class DirectedMutableGraph_ESTest(unittest.TestCase):

    def test12(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        clientInfoStatus0 = ClientInfoStatus.REASON_UNKNOWN

        try:
            directedMutableGraph0.getDegree(clientInfoStatus0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.model.DirectedMutableGraph", e)

    def test11(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        arrayDeque0 = ArrayDeque()

        try:
            directedMutableGraph0.decorateRemoveEdge(arrayDeque0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.model.DirectedMutableGraph", e)

    def test10(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        locale_Category0 = Locale.Category.FORMAT
        iterable0 = directedMutableGraph0.getOutbound(locale_Category0)
        self.assertIsNone(iterable0)

    def test09(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        clientInfoStatus0 = ClientInfoStatus.REASON_UNKNOWN
        directedMutableGraph0.decorateAddVertex(clientInfoStatus0)
        int0 = directedMutableGraph0.getDegree(clientInfoStatus0)
        self.assertEqual(0, int0)

    def test08(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        clientInfoStatus0 = ClientInfoStatus.REASON_UNKNOWN_PROPERTY
        iterable0 = directedMutableGraph0.getInbound(clientInfoStatus0)
        self.assertIsNone(iterable0)

    def test07(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        mockThrowable0 = MockThrowable()
        sQLNonTransientConnectionException0 = SQLNonTransientConnectionException(
            mockThrowable0
        )
        directedMutableGraph0.decorateRemoveVertex(sQLNonTransientConnectionException0)
        self.assertIsNone(sQLNonTransientConnectionException0.getSQLState())

    def test06(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        arrayDeque0 = ArrayDeque()

        # Undeclared exception in Java code, so we'll use a try-except block to catch the exception
        try:
            directedMutableGraph0.getInDegree(arrayDeque0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # no message in exception (getMessage() returned null)
            verifyException("org.apache.commons.graph.model.DirectedMutableGraph", e)

    def test05(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        arrayDeque0 = ArrayDeque()

        # Undeclared exception in Java, so we use try-except block to catch the exception
        try:
            directedMutableGraph0.getOutDegree(arrayDeque0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.model.DirectedMutableGraph", e)

    def test04(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        clientInfoStatus0 = ClientInfoStatus.REASON_UNKNOWN
        directedMutableGraph0.decorateAddVertex(clientInfoStatus0)
        directedMutableGraph0.decorateAddEdge(
            clientInfoStatus0, None, clientInfoStatus0
        )
        int0 = directedMutableGraph0.getDegree(clientInfoStatus0)
        self.assertEqual(2, int0)

    def test03(self) -> None:

        arrayDeque0 = ArrayDeque[SQLNonTransientConnectionException]()
        directedMutableGraph0 = DirectedMutableGraph[
            ArrayDeque[SQLNonTransientConnectionException], Object
        ]()
        directedMutableGraph0.decorateAddVertex(arrayDeque0)
        directedMutableGraph0.decorateAddEdge(arrayDeque0, arrayDeque0, arrayDeque0)
        int0 = directedMutableGraph0.getInDegree(arrayDeque0)
        self.assertEqual(1, int0)

    def test02(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[
            ArrayDeque[SQLNonTransientConnectionException], object
        ]()
        arrayDeque0 = ArrayDeque[SQLNonTransientConnectionException]()
        directedMutableGraph0.addVertex(arrayDeque0)
        int0 = directedMutableGraph0.getInDegree(arrayDeque0)
        self.assertEqual(0, int0)

    def test01(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[Locale.Category, Locale.Category]()
        locale_Category0 = Locale.Category.DISPLAY
        directedMutableGraph0.decorateAddVertex(locale_Category0)
        int0 = directedMutableGraph0.getOutDegree(locale_Category0)
        self.assertEqual(0, int0)

    def test00(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[
            ArrayDeque[SQLNonTransientConnectionException], object
        ]()
        arrayDeque0 = ArrayDeque[SQLNonTransientConnectionException]()
        directedMutableGraph0.decorateAddVertex(arrayDeque0)
        arrayDeque1 = ArrayDeque[SQLNonTransientConnectionException]()
        # Undeclared exception in Java code, so we'll use try-except block to catch the exception
        try:
            directedMutableGraph0.decorateAddEdge(arrayDeque1, None, arrayDeque0)
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            # no message in exception (getMessage() returned null)
            verifyException("org.apache.commons.graph.model.DirectedMutableGraph", e)
