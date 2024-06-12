import unittest
import logging
import pickle
from io import BytesIO
from abc import ABC
from typing import List

class AbstractCheckDigitTest(unittest.TestCase, ABC):

    __POSSIBLE_CHECK_DIGITS =\
        "0123456789 ABCDEFHIJKLMNOPQRSTUVWXYZ\tabcdefghijklmnopqrstuvwxyz!@£$%^&*()_+"

    
    @classmethod
    def setUpClass(cls):
        if cls == AbstractCheckDigitTest:
            "Tests shall only be executed on child classes with concrete implementations."
            raise unittest.SkipTest("Skip tests in the abstract base class.")

    
    def __init__(self, methodName='runTest') -> None:
        self.setUpClass()
        super().__init__(methodName)
        self._log = logging.getLogger(__name__)
        self._checkDigitLth = 1
        self._routine = None
        self._valid = []
        self._invalid = ["12345678A"]
        self._zeroSum = "0000000000"
        self._missingMessage = "Code is missing"
    

    def setUp(
        self,
        routine = None,
        valid = [],
        invalid = ["12345678A"],
        zeroSum = "0000000000",
        missingMessage = "Code is missing"
        ) -> None:
        self._routine = routine
        self._valid = valid
        self._invalid = invalid
        self._zeroSum = zeroSum
        self._missingMessage = missingMessage

    
    def tearDown(self) -> None:
        try:
            super().tearDown()
            self._valid = None
            self._routine = None
        except Exception as e:
            self.fail(f"An exception occurred when cleaning up the test: {e}")

    
    def test_IsValidTrue(self) -> None:
        if self._log.isEnabledFor(logging.DEBUG):
            self._log.debug(f"test_IsValidTrue() for {self._routine.__class__.__name__}")

        for i in range(len(self._valid)):
            if self._log.isEnabledFor(logging.DEBUG):
                self._log.debug(f"   {i} Testing Valid Code=[{self._valid[i]}]")
            self.assertTrue(self._routine.isValid(self._valid[i]), f"valid[{i}]: {self._valid[i]}")

    
    def test_IsValidFalse(self) -> None:
        if self._log.isEnabledFor(logging.DEBUG):
            self._log.debug(f"test_IsValidFalse() for {self._routine.__class__.__name__}")

        for i in range(len(self._invalid)):
            if self._log.isEnabledFor(logging.DEBUG):
                self._log.debug(f"   {i} Testing Invalid Code=[{self._invalid[i]}]")
            self.assertFalse(self._routine.isValid(self._invalid[i]), f"invalid[{i}]: {self._invalid[i]}")

        invalidCheckDigits = self._createInvalidCodes(self._valid)
        for i in range(len(invalidCheckDigits)):
            if self._log.isEnabledFor(logging.DEBUG):
                self._log.debug(f"   {i} Testing Invalid Check Digit, Code=[{invalidCheckDigits[i]}]")
            self.assertFalse(self._routine.isValid(invalidCheckDigits[i]), f"invalid check digit[{i}]: {invalidCheckDigits[i]}")

    
    def test_CalculateValid(self) -> None:
        if self._log.isEnabledFor(logging.DEBUG):
            self._log.debug(f"test_CalculateValid() for {self._routine.__class__.__name__}")

        for i in range(len(self._valid)):
            code = self._removeCheckDigit(self._valid[i])
            expected = self._checkDigit(self._valid[i])
            try:
                if self._log.isEnabledFor(logging.DEBUG):
                    self._log.debug(f"   {i} Testing Valid Check Digit, Code=[{code}] expected=[{expected}]")
                self.assertEqual(expected, self._routine.calculate(code), f"valid[{i}]: {self._valid[i]}")
            except Exception as e:
                self.fail(f"valid[{i}]={self._valid[i]} threw {e}")

    
    def test_CalculateInvalid(self) -> None:
        if self._log.isEnabledFor(logging.DEBUG):
            self._log.debug(f"test_CalculateInvalid() for {self._routine.__class__.__name__}")

        for i in range(len(self._invalid)):
            try:
                if self._log.isEnabledFor(logging.DEBUG):
                    self._log.debug(f"   {i} Testing Invalid Check Digit, Code=[{self._invalid[i]}]")
                expected = self._checkDigit(self._invalid[i])
                actual = self._routine.calculate(self._removeCheckDigit(self._invalid[i]))
                if expected == actual:
                    self.fail(f"Expected mismatch for {self._invalid[i]} expected {expected} actual {actual}")
            except CheckDigitException as e:
                self.assertTrue(e.getMessage().startswith("Invalid "), f"Invalid Character[{i}]={e.getMessage()}")

    
    def test_MissingCode(self) -> None:
        self.assertFalse(self._routine.isValid(None), "isValid() Null")

        self.assertFalse(self._routine.isValid(""), "isValid() Zero Length")
        
        self.assertFalse(self._routine.isValid("9"), "isValid() Length 1")

        try:
            self._routine.calculate(None)
            self.fail("calculate() Null - expected exception")
        except Exception as e:
            self.assertEqual(self._missingMessage, str(e), "calculate() Null")

        try:
            self._routine.calculate("")
            self.fail("calculate() Zero Length - expected exception")
        except Exception as e:
            self.assertEqual(self._missingMessage, str(e), "calculate() Zero Length")

    
    def test_ZeroSum(self) -> None:
        self.assertFalse(self._routine.isValid(self._zeroSum), "isValid() Zero Sum")

        try:
            self._routine.calculate(self._zeroSum)
            self.fail("Zero Sum - expected exception")
        except Exception as e:
            self.assertEqual("Invalid code, sum is zero", str(e), "isValid() Zero Sum")

    
    def test_Serialization(self) -> None:
        baos = BytesIO()
        try:
            pickle.dump(self._routine, baos)
        except Exception as e:
            self.fail(f"{self._routine.__class__.__name__} error during serialization: {e}")

        result = None
        try:
            bais = BytesIO(baos.getvalue())
            result = pickle.load(bais)
        except Exception as e:
            self.fail(f"{self._routine.__class__.__name__} error during deserialization: {e}")
        
        self.assertIsNotNone(result)

    
    def _createInvalidCodes(self, codes: List[str]) -> List[str]:
        invalidCodes = []

        for fullCode in codes:
            code = self._removeCheckDigit(fullCode)
            check = self._checkDigit(fullCode)
            for char in self.__POSSIBLE_CHECK_DIGITS:
                if char != check:
                    invalidCodes.append(code + char)

        return invalidCodes

    
    def _removeCheckDigit(self, code: str) -> str:
        if code is None or len(code) <= self._checkDigitLth:
            return None
        return code[:len(code) - self._checkDigitLth]

    
    def _checkDigit(self, code: str) -> str:
        if code is None or len(code) <= self._checkDigitLth:
            return ""
        return code[len(code) - self._checkDigitLth:]
