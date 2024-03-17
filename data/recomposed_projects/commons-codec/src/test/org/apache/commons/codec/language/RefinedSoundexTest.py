# Imports Begin
from src.main.org.apache.commons.codec.language.RefinedSoundex import *
from src.main.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *
import unittest
# Imports End

class RefinedSoundexTest(unittest.TestCase, StringEncoderAbstractTest<RefinedSoundex>):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testNewInstance3(self) -> None:

            self.assertEqual(
                    "D6043",
                    RefinedSoundex(0, RefinedSoundex.US_ENGLISH_MAPPING_STRING, None).soundex("dogs"))

    def testNewInstance2(self) -> None:

            self.assertEqual(
                "D6043",
                RefinedSoundex(1, None, RefinedSoundex.US_ENGLISH_MAPPING_STRING.toCharArray()).soundex("dogs")
            )

    def testNewInstance(self) -> None:

            self.assertEqual("D6043", self.soundex("dogs"))

    def testGetMappingCodeNonLetter(self) -> None:

            code = self.getStringEncoder().getMappingCode('#')
            assert code == 0, "Code does not equals zero"

    def testEncode(self) -> None:

            assert self.getStringEncoder().encode1("testing") == "T6036084"
            assert self.getStringEncoder().encode1("TESTING") == "T6036084"
            assert self.getStringEncoder().encode1("The") == "T60"
            assert self.getStringEncoder().encode1("quick") == "Q503"
            assert self.getStringEncoder().encode1("brown") == "B1908"
            assert self.getStringEncoder().encode1("fox") == "F205"
            assert self.getStringEncoder().encode1("jumped") == "J408106"
            assert self.getStringEncoder().encode1("over") == "O0209"
            assert self.getStringEncoder().encode1("the") == "T60"
            assert self.getStringEncoder().encode1("lazy") == "L7050"
            assert self.getStringEncoder().encode1("dogs") == "D6043"
            assert RefinedSoundex.US_ENGLISH.encode1("dogs") == "D6043"

    def testDifference(self) -> None:

            self.assertEqual(0, self.getStringEncoder().difference(None, None))
            self.assertEqual(0, self.getStringEncoder().difference("", ""))
            self.assertEqual(0, self.getStringEncoder().difference(" ", " "))
            self.assertEqual(6, self.getStringEncoder().difference("Smith", "Smythe"))
            self.assertEqual(3, self.getStringEncoder().difference("Ann", "Andrew"))
            self.assertEqual(1, self.getStringEncoder().difference("Margaret", "Andrew"))
            self.assertEqual(1, self.getStringEncoder().difference("Janet", "Margaret"))
            self.assertEqual(5, self.getStringEncoder().difference("Green", "Greene"))
            self.assertEqual(1, self.getStringEncoder().difference("Blotchet-Halls", "Greene"))
            self.assertEqual(6, self.getStringEncoder().difference("Smith", "Smythe"))
            self.assertEqual(8, self.getStringEncoder().difference("Smithers", "Smythers"))
            self.assertEqual(5, self.getStringEncoder().difference("Anothers", "Brothers"))

    def _createStringEncoder(self) -> RefinedSoundex:

            return RefinedSoundex(2, None, None)

    # Class Methods End


