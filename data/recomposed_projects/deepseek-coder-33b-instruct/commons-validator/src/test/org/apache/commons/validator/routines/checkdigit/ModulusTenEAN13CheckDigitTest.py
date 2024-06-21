from src.main.org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit import *
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import AbstractCheckDigitTest


class ModulusTenEAN13CheckDigitTest(AbstractCheckDigitTest):

    @classmethod
    def setUpClass(cls):
        pass

    
    def __init__(self, methodName='runTest') -> None:
        super().__init__(methodName)

    
    def setUp(self) -> None:
        try:
            super().setUp()
            self._routine = ModulusTenCheckDigit\
                .ModulusTenCheckDigit1([1, 3], True)
            self._valid = [
                "9780072129519",
                "9780764558313",
                "4025515373438",
                "0095673400332"
            ]
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")