import pytest

from src.main.org.apache.commons.validator.util.Flags import *
import unittest

class FlagsTest(unittest.TestCase):

    __LONG_FLAG = 1

    __LONG_FLAG_2 = 2
    __INT_FLAG = 4

    def __init__(self, methodName='runTest') -> None:
        super().__init__(methodName)
    

    @pytest.mark.test
    def testHashCode(self) -> None:
        f = Flags(1, 45)
        self.assertEqual(f.hashCode(), 45)
    

    @pytest.mark.test
    def testGetFlags(self) -> None:
        f = Flags(1, 45)
        self.assertEquals(f.getFlags(), 45)
    

    @pytest.mark.test
    def testIsOnOff(self) -> None:
        f = Flags(0, 0)
        f.turnOn(FlagsTest.__LONG_FLAG)
        f.turnOn(FlagsTest.__INT_FLAG)
        self.assertTrue(f.isOn(FlagsTest.__LONG_FLAG))
        self.assertTrue(not f.isOff(FlagsTest.__LONG_FLAG))

        self.assertTrue(f.isOn(FlagsTest.__INT_FLAG))
        self.assertTrue(not f.isOff(FlagsTest.__INT_FLAG))

        self.assertTrue(f.isOff(FlagsTest.__LONG_FLAG_2))
    

    @pytest.mark.test
    def testTurnOnOff(self) -> None:
        pass

    
    @pytest.mark.test
    def testTurnOff(self) -> None:
        pass


    @pytest.mark.test
    def testTurnOffAll(self) -> None:
        f = Flags(1, 98432)
        f.turnOffAll()
        self.assertEqual(0, f.getFlags())

    
    @pytest.mark.test
    def testClear(self) -> None:
        f = Flags(1, 98432)
        f.clear()
        self.assertEqual(0, f.getFlags())
    

    @pytest.mark.test
    def testTurnOnAll(self) -> None:
        f = Flags(0, 0)
        f.turnOnAll()
        self.assertEqual(~0, f.getFlags())
    

    @pytest.mark.test
    def testIsOn_isFalseWhenNotAllFlagsInArgumentAreOn(self) -> None:
        first = Flags(1, 1)
        firstAndSecond = 3

        self.assertFalse(first.isOn(firstAndSecond))
    

    @pytest.mark.test
    def testIsOn_isTrueWhenHighOrderBitIsSetAndQueried(self) -> None:
        allOn = Flags(1, ~0)
        highOrderBit = 0x8000000000000000

        self.assertTrue(allOn.isOn(highOrderBit))
    

    @pytest.mark.test
    def testClone(self) -> None:
        pass
    

    @pytest.mark.test
    def testEqualsObject(self) -> None:
        pass


    @pytest.mark.test
    def testToString(self) -> None:
        f = Flags(0, 0)
        s = f.toString()
        self.assertEqual(64, len(s))

        f.turnOn(FlagsTest.__INT_FLAG)
        s = f.toString()
        self.assertEqual(64, len(s))

        self.assertEqual(
            "0000000000000000000000000000000000000000000000000000000000000100",
            s
        )
