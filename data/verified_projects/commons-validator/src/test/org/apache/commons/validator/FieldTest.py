from src.main.org.apache.commons.validator.Arg import *
from src.main.org.apache.commons.validator.Field import *
import unittest

class FieldTest(unittest.TestCase):

    def __init__(self, methodName='runTest') -> None:
        super().__init__(methodName)
        self._field = None

    @staticmethod
    def FieldTest1():
        return FieldTest()

    
    def setUp(self) -> None:
        self._field = Field()

    
    def tearDown(self) -> None:
        self._field = None

    
    def test_EmptyArgs(self) -> None:
        self.assertEqual(
            len(self._field.getArgs("required")),
            0,
            "Empty Args(1) "
        )

    
    def test_DefaultPositionImplied(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

        self.assertEqual(
            len(self._field.getArgs("required")),
            3,
            "testDefaultPositionImplied(1) "
        )
        self.assertEqual(
            self._field.getArg1("required", 0).getKey(),
            "default-position-0",
            "testDefaultPositionImplied(2) "
        )
        self.assertEqual(
            self._field.getArg1("required", 1).getKey(),
            "default-position-1",
            "testDefaultPositionImplied(3) "
        )
        self.assertEqual(
            self._field.getArg1("required", 2).getKey(),
            "default-position-2",
            "testDefaultPositionImplied(4) "
        )

   
    def test_DefaultUsingPositions(self) -> None:
        self._field.addArg(self.__createArg1("default-position-1", 1))
        self._field.addArg(self.__createArg1("default-position-0", 0))
        self._field.addArg(self.__createArg1("default-position-2", 2))

        self.assertEqual(
            len(self._field.getArgs("required")),
            3,
            "testDefaultUsingPositions(1) "
        )
        self.assertEqual(
            self._field.getArg1("required", 0).getKey(),
            "default-position-0",
            "testDefaultUsingPositions(2) "
        )
        self.assertEqual(
            self._field.getArg1("required", 1).getKey(),
            "default-position-1",
            "testDefaultUsingPositions(3) "
        )
        self.assertEqual(
            self._field.getArg1("required", 2).getKey(),
            "default-position-2",
            "testDefaultUsingPositions(4) "
        )

    
    def test_DefaultOnePosition(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg1("default-position-2", 2))
        self._field.addArg(self.__createArg0("default-position-3"))

        self.assertEqual(
            len(self._field.getArgs("required")),
            4,
            "testDefaultOnePosition(1) "
        )
        self.assertEqual(
            self._field.getArg1("required", 0).getKey(),
            "default-position-0",
            "testDefaultOnePosition(2) "
        )
        self.assertIsNone(
            self._field.getArg1("required", 1),
            "testDefaultOnePosition(3) "
        )
        self.assertEqual(
            self._field.getArg1("required", 2).getKey(),
            "default-position-2",
            "testDefaultOnePosition(4) "
        )
        self.assertEqual(
            self._field.getArg1("required", 3).getKey(),
            "default-position-3",
            "testDefaultOnePosition(5) "
        )

    
    def test_DefaultSomePositions(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg1("default-position-2", 2))
        self._field.addArg(self.__createArg0("default-position-3"))
        self._field.addArg(self.__createArg1("default-position-1", 1))

        self.assertEqual(
            len(self._field.getArgs("required")),
            4,
            "testDefaultSomePositions(1) "
        )
        self.assertEqual(
            self._field.getArg1("required", 0).getKey(),
            "default-position-0",
            "testDefaultSomePositions(2) "
        )
        self.assertEqual(
            self._field.getArg1("required", 1).getKey(),
            "default-position-1",
            "testDefaultSomePositions(3) "
        )
        self.assertEqual(
            self._field.getArg1("required", 2).getKey(),
            "default-position-2",
            "testDefaultSomePositions(4) "
        )
        self.assertEqual(
            self._field.getArg1("required", 3).getKey(),
            "default-position-3",
            "testDefaultSomePositions(5) "
        )

    
    def test_OverrideUsingPositionA(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))

        self.assertEqual(
            len(self._field.getArgs("required")),
            3,
            "testOverrideUsingPositionA(1) "
        )
        self.assertEqual(
            self._field.getArg1("required", 1).getKey(),
            "required-position-1",
            "testOverrideUsingPositionA(2) "
        )

        self.assertEqual(
            len(self._field.getArgs("mask")),
            3,
            "testOverrideUsingPositionA(3) "
        )
        self.assertEqual(
            self._field.getArg1("mask", 1).getKey(),
            "default-position-1",
            "testOverrideUsingPositionA(4) "
        )
        self.assertEqual(
            self._field.getArg0(1).getKey(),
            "default-position-1",
            "testOverrideUsingPositionA(5) "
        )

    
    def test_OverrideUsingPositionB(self) -> None:
        self._field.addArg(self.__createArg3("required-position-3", "required", 3))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

        self.assertEqual(
            len(self._field.getArgs("required")),
            4,
            "testOverrideUsingPositionB(1) "
        )
        self.assertEqual(
            self._field.getArg1("required", 0).getKey(),
            "default-position-0",
            "testOverrideUsingPositionB(2) "
        )
        self.assertEqual(
            self._field.getArg1("required", 1).getKey(),
            "required-position-1",
            "testOverrideUsingPositionB(3) "
        )
        self.assertEqual(
            self._field.getArg1("required", 2).getKey(),
            "default-position-2",
            "testOverrideUsingPositionB(4) "
        )
        self.assertEqual(
            self._field.getArg1("required", 3).getKey(),
            "required-position-3",
            "testOverrideUsingPositionB(5) "
        )

        self.assertEqual(
            len(self._field.getArgs("mask")),
            4,
            "testOverrideUsingPositionB(6) "
        )
        self.assertEqual(
            self._field.getArg1("mask", 0).getKey(),
            "default-position-0",
            "testOverrideUsingPositionB(6) "
        )
        self.assertEqual(
            self._field.getArg1("mask", 1).getKey(),
            "default-position-1",
            "testOverrideUsingPositionB(7) "
        )
        self.assertEqual(
            self._field.getArg1("mask", 2).getKey(),
            "default-position-2",
            "testOverrideUsingPositionB(8) "
        )
        self.assertIsNone(
            self._field.getArg1("mask", 3),
            "testOverrideUsingPositionB(9) "
        )

   
    def test_OverridePositionImplied(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg2("required-position-1", "required"))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-1", "mask"))

        self.assertEqual(
            len(self._field.getArgs("required")),
            3,
            "testOverridePositionImplied(1) "
        )
        self.assertEqual(
            self._field.getArg1("required", 0).getKey(),
            "default-position-0",
            "testOverridePositionImplied(2) "
        )
        self.assertEqual(
            self._field.getArg1("required", 1).getKey(),
            "required-position-1",
            "testOverridePositionImplied(3) "
        )
        self.assertEqual(
            self._field.getArg1("required", 2).getKey(),
            "required-position-2",
            "testOverridePositionImplied(4) "
        )

        self.assertEqual(
            len(self._field.getArgs("mask")),
            3,
            "testOverridePositionImplied(5) "
        )
        self.assertEqual(
            self._field.getArg1("mask", 0).getKey(),
            "default-position-0",
            "testOverridePositionImplied(6) "
        )
        self.assertEqual(
            self._field.getArg1("mask", 1).getKey(),
            "mask-position-1",
            "testOverridePositionImplied(7) "
        )
        self.assertIsNone(
            self._field.getArg1("mask", 2),
            "testOverridePositionImplied(8) "
        )
        self.assertEqual(
            self._field.getArg0(0).getKey(),
            "default-position-0",
            "testOverridePositionImplied(9) "
        )
        self.assertIsNone(
            self._field.getArg0(1),
            "testOverridePositionImplied(10) "
        )
        self.assertIsNone(
            self._field.getArg0(2),
            "testOverridePositionImplied(11) "
        )

    
    def test_OverrideSomePosition(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        self.assertEqual(
            len(self._field.getArgs("required")),
            4,
            "testOverrideSomePosition(1) "
        )
        self.assertEqual(
            self._field.getArg1("required", 0).getKey(),
            "default-position-0",
            "testOverrideSomePosition(2) "
        )
        self.assertEqual(
            self._field.getArg1("required", 1).getKey(),
            "required-position-1",
            "testOverrideSomePosition(3) "
        )
        self.assertEqual(
            self._field.getArg1("required", 2).getKey(),
            "required-position-2",
            "testOverrideSomePosition(4) "
        )
        self.assertIsNone(
            self._field.getArg1("required", 3),
            "testOverrideSomePosition(5) "
        )

        self.assertEqual(
            len(self._field.getArgs("mask")),
            4,
            "testOverrideSomePosition(6) "
        )
        self.assertEqual(
            self._field.getArg1("mask", 0).getKey(),
            "default-position-0",
            "testOverrideSomePosition(7) "
        )
        self.assertEqual(
            self._field.getArg1("mask", 1).getKey(),
            "default-position-1",
            "testOverrideSomePosition(8) "
        )
        self.assertEqual(
            self._field.getArg1("mask", 2).getKey(),
            "default-position-2",
            "testOverrideSomePosition(9) "
        )
        self.assertEqual(
            self._field.getArg1("mask", 3).getKey(),
            "mask-position-3",
            "testOverrideSomePosition(10) "
        )
        self.assertEqual(
            self._field.getArg0(0).getKey(),
            "default-position-0",
            "testOverrideSomePosition(11) "
        )
        self.assertEqual(
            self._field.getArg0(1).getKey(),
            "default-position-1",
            "testOverrideSomePosition(12) "
        )
        self.assertEqual(
            self._field.getArg0(2).getKey(),
            "default-position-2",
            "testOverrideSomePosition(13) "
        )
        self.assertIsNone(
            self._field.getArg0(3),
            "testOverrideSomePosition(14) "
        )

    
    def __createArg0(self, key) -> Arg:
        arg = Arg()
        arg.setKey(key)
        return arg

    
    def __createArg1(self, key, position) -> Arg:
        arg = self.__createArg0(key)
        arg.setPosition(position)
        return arg

    
    def __createArg2(self, key, name) -> Arg:
        arg = self.__createArg0(key)
        arg.setName(name)
        return arg

    
    def __createArg3(self, key, name, position) -> Arg:
        arg = self.__createArg2(key, name)
        arg.setPosition(position)
        return arg
