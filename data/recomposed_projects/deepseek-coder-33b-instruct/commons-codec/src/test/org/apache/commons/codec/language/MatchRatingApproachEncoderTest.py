from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.apache.commons.codec.StringEncoder import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.language.MatchRatingApproachEncoder import *


class MatchRatingApproachEncoderTest(unittest.TestCase):

    def _createStringEncoder(self) -> MatchRatingApproachEncoder:

        return MatchRatingApproachEncoder()

    def testCompare_Forenames_SEAN_PETE_NoMatchExpected(self) -> None:

        assert not self.getStringEncoder().isEncodeEquals("Sean", "Pete")

    def testCompare_Forenames_SEAN_JOHN_MatchExpected(self) -> None:

        # Assuming that the method isEncodeEquals is a static method in MatchRatingApproachEncoder class
        assert MatchRatingApproachEncoder.isEncodeEquals("Sean", "John")

    def testCompare_Surnames_MURPHY_LYNCH_NoMatchExpected(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method and assert that it returns False
        assert not encoder.isEncodeEquals("Murphy", "Lynch")

    def testCompare_SurnameCornerCase_Nulls_NoMatch(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with null values
        result = encoder.isEncodeEquals(None, None)

        # Assert that the result is False
        assert not result

    def testCompare_SurnamesCornerCase_MURPHY_NoSpace_NoMatch(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method and assert that it returns False
        assert not encoder.isEncodeEquals("Murphy", "")

    def testCompare_SurnamesCornerCase_MURPHY_Space_NoMatch(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method and assert that it returns False
        assert not encoder.isEncodeEquals("Murphy", " ")

    def testCompare_MCGOWAN_MCGEOGHEGAN_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals("McGowan", "Mc Geoghegan")

        # Assert that the result is True
        assert result == True

    def testCompare_PETERSON_PETERS_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals("Peterson", "Peters")

        # Assert that the result is True
        assert result == True

    def testCompare_Surname_PRZEMYSL_PSHEMESHIL_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals(" P rz e m y s l", " P sh e m e sh i l")

        # Assert that the result is True
        assert result == True

    def testCompare_Surname_ROSOCHOWACIEC_ROSOKHOVATSETS_SuccessfullyMatched(
        self,
    ) -> None:

        assert self.getStringEncoder().isEncodeEquals(
            "R o s o c h o w a c i e c", " R o s o k h o v a t s e t s"
        )

    def testCompare_Surname_SZLAMAWICZ_SHLAMOVITZ_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals("SZLAMAWICZ", "SHLAMOVITZ")

        # Assert that the result is True
        assert result == True

    def testCompare_Surname_LEWINSKY_LEVINSKI_SuccessfullyMatched(self) -> None:

        # Assuming that the method isEncodeEquals is a static method in MatchRatingApproachEncoder class
        assert MatchRatingApproachEncoder.isEncodeEquals("LEWINSKY", "LEVINSKI")

    def testCompare_Surname_LIPSHITZ_LIPPSZYC_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals("LIPSHITZ", "LIPPSZYC")

        # Assert that the result is True
        assert result == True

    def testCompare_Surname_MOSKOWITZ_MOSKOVITZ_SuccessfullyMatched(self) -> None:

        # Assuming that the MatchRatingApproachEncoder class has a method called isEncodeEquals
        # which takes two strings and returns a boolean indicating whether they are equal
        # after encoding.

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with the two strings
        result = encoder.isEncodeEquals("Moskowitz", "Moskovitz")

        # Assert that the result is True
        assert result == True

    def testCompare_Surname_AUERBACH_UHRBACH_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals("Auerbach", "Uhrbach")

        # Assert that the result is True
        assert result == True

    def testCompare_Surname_HAILEY_HALLEY_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals("Hailey", "Halley")

        # Assert that the result is True
        assert result == True

    def testCompare_Surname_COOPERFLYNN_SUPERLYN_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals("Cooper-Flynn", "Super-Lyn")

        # Assert that the result is True
        assert result == True

    def testCompare_LongSurnames_OMUIRCHEARTAIGH_OMIREADHAIGH_SuccessfulMatch(
        self,
    ) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals("o'muireadhaigh", "Ó 'Muircheartaigh ")

        # Assert that the result is True
        assert result == True

    def testCompare_LongSurnames_MORIARTY_OMUIRCHEARTAIGH_DoesNotSuccessfulMatch(
        self,
    ) -> None:

        # Assuming that the method isEncodeEquals is a static method in MatchRatingApproachEncoder class
        # If it's not, you need to create an instance of MatchRatingApproachEncoder
        # and call the method on that instance
        assert not MatchRatingApproachEncoder.isEncodeEquals(
            "Moriarty", "OMuircheartaigh"
        )

    def testCompare_Surname_OSULLIVAN_OSUILLEABHAIN_SuccessfulMatch(self) -> None:

        # Assuming that the method isEncodeEquals is a static method in MatchRatingApproachEncoder class
        # If it's not, you need to create an instance of MatchRatingApproachEncoder
        # and call the method on that instance
        assert MatchRatingApproachEncoder.isEncodeEquals(
            "O'Sullivan", "Ó ' S�illeabháin"
        )

    def testCompare_Forenames_UNA_OONAGH_ShouldSuccessfullyMatchButDoesNot(
        self,
    ) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals("Úna", "Oonagh")

        # Assert that the result is False
        assert not result

    def testCompare_KARL_ALESSANDRO_DoesNotMatch(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method and assert that it returns False
        assert not encoder.isEncodeEquals("Karl", "Alessandro")

    def testCompare_ZACH_ZAKARIA_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals("Zach", "Zacharia")

        # Assert that the result is True
        assert result == True

    def testCompareNameToSingleLetter_KARL_C_DoesNotMatch(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method and assert that it returns False
        assert not encoder.isEncodeEquals("Karl", "C")

    def testCompare_SmallInput_CARK_Kl_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals("Kl", "Karl")

        # Assert that the result is True
        assert result == True

    def testCompare_TOMASZ_TOM_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals("Tomasz", "tom")

        # Assert that the result is True
        assert result == True

    def testCompare_FRANCISZEK_FRANCES_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals("Franciszek", "Frances")

        # Assert that the result is True
        assert result == True

    def testCompare_SOPHIE_SOFIA_SuccessfullyMatched(self) -> None:

        # Instantiate MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call isEncodeEquals method
        result = encoder.isEncodeEquals("Sophie", "Sofia")

        # Assert that the result is True
        assert result == True

    def testCompare_OONA_OONAGH_SuccessfullyMatched(self) -> None:

        # Assuming MatchRatingApproachEncoder is a class in the same module
        # and isEncodeEquals is a method in MatchRatingApproachEncoder
        # If not, you need to import the class and method properly

        encoder = MatchRatingApproachEncoder()
        assert encoder.isEncodeEquals("Oona", "Oonagh")

    def testCompare_MICKY_MICHAEL_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals("Micky", "Michael")

        # Assert that the result is True
        assert result == True

    def testCompare_SAM_SAMUEL_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals("Sam", "Samuel")

        # Assert that the result is True
        assert result == True

    def testCompare_STEPHEN_STEFAN_SuccessfullyMatched(self) -> None:

        # Assuming that the MatchRatingApproachEncoder class has a method called isEncodeEquals
        # which takes two strings and returns a boolean indicating whether they are equal
        # after encoding.

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with "Stephen" and "Stefan" as arguments
        result = encoder.isEncodeEquals("Stephen", "Stefan")

        # Assert that the result is True
        assert result == True

    def testCompare_STEVEN_STEFAN_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals("Steven", "Stefan")

        # Assert that the result is True
        assert result == True

    def testCompare_STEPHEN_STEVEN_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals("Stephen", "Steven")

        # Assert that the result is True
        assert result == True

    def testCompare_COLM_COLIN_WithAccentsAndSymbolsAndSpaces_SuccessfullyMatched(
        self,
    ) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals("Cólm.   ", "C-olín")

        # Assert that the result is True
        assert result == True

    def testCompare_SEAN_SHAUN_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals("Séan", "Shaun")

        # Assert that the result is True
        assert result == True

    def testCompare_BRIAN_BRYAN_SuccessfullyMatched(self) -> None:

        # Assuming that the getStringEncoder() method is available in the MatchRatingApproachEncoder class
        # and it returns an instance of MatchRatingApproachEncoder
        encoder = self.getStringEncoder()

        # Assuming that the isEncodeEquals() method is available in the MatchRatingApproachEncoder class
        # and it returns a boolean indicating whether the two strings are equal
        assert encoder.isEncodeEquals("Brian", "Bryan")

    def testCompare_CATHERINE_KATHRYN_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals("Catherine", "Kathryn")

        # Assert that the result is True
        assert result == True

    def testCompare_ShortNames_AL_ED_WorksButNoMatch(self) -> None:

        # Assuming that the method isEncodeEquals is a static method in MatchRatingApproachEncoder class
        assert not MatchRatingApproachEncoder.isEncodeEquals("Al", "Ed")

    def testCompare_BURNS_BOURNE_SuccessfullyMatched(self) -> None:

        # Assuming that the method isEncodeEquals is a static method in MatchRatingApproachEncoder class
        assert MatchRatingApproachEncoder.isEncodeEquals("Burns", "Bourne")

    def testCompare_SMITH_SMYTH_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals("smith", "smyth")

        # Assert that the result is True
        assert result == True

    def testCompareNameSameNames_ReturnsFalseSuccessfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals("John", "John")

        # Assert that the result is True
        assert result == True

    def testCompareNameNullSpace_ReturnsFalseSuccessfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with null and " " as arguments
        result = encoder.isEncodeEquals(None, " ")

        # Assert that the result is False
        assert not result

    def testGetEncoding_One_Letter_to_Nothing(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the encode1 method and compare the result with the expected output
        assert encoder.encode1("E") == ""

    def testGetEncoding_Null_to_Nothing(self) -> None:

        # Assuming that MatchRatingApproachEncoder is a class in the same module
        # and it has a method encode1
        encoder = MatchRatingApproachEncoder()

        # Assuming that the encode1 method returns a string
        result = encoder.encode1(None)

        # Assuming that the assertEquals method is a method in the same module
        # and it compares two strings
        self.assertEquals("", result)

    def testGetEncoding_NoSpace_to_Nothing(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the encode1 method and compare the result with the expected value
        assert encoder.encode1("") == ""

    def testGetEncoding_Space_to_Nothing(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the encode1 method with a space character
        result = encoder.encode1(" ")

        # Assert that the result is an empty string
        assert result == ""

    def testGetEncoding_SMYTH_to_SMYTH(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the encode1 method
        result = encoder.encode1("Smyth")

        # Assert that the result is as expected
        assert result == "SMYTH"

    def testGetEncoding_SMITH_to_SMTH(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the encode1 method with "Smith" as argument
        result = encoder.encode1("Smith")

        # Assert that the result is "SMTH"
        assert result == "SMTH"

    def testGetEncoding_HARPER_HRPR(self) -> None:

        # Instantiate MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the encode1 method
        result = encoder.encode1("HARPER")

        # Assert the result
        assert result == "HRPR"

    def testisEncodeEqualsSecondNameJust1Letter_ReturnsFalse(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method and assert that it returns False
        assert not encoder.isEncodeEquals("test", "t")

    def testisEncodeEquals_CornerCase_FirstNameJust1Letter_ReturnsFalse(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method
        result = encoder.isEncodeEquals("t", "test")

        # Assert that the result is False
        assert not result

    def testisEncodeEquals_CornerCase_FirstNameNull_ReturnsFalse(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that the result of isEncodeEquals is False when the first argument is None
        assert not encoder.isEncodeEquals(None, "test")

    def testisEncodeEquals_CornerCase_SecondNameNull_ReturnsFalse(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with "test" and None as arguments
        result = encoder.isEncodeEquals("test", None)

        # Assert that the result is False
        assert not result

    def testisEncodeEquals_CornerCase_FirstNameJustSpace_ReturnsFalse(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with the space and "test" as arguments
        result = encoder.isEncodeEquals(" ", "test")

        # Assert that the result is False
        assert result == False

    def testisEncodeEquals_CornerCase_SecondNameJustSpace_ReturnsFalse(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method and assert that it returns False
        assert not encoder.isEncodeEquals("test", " ")

    def testisEncodeEquals_CornerCase_FirstNameNothing_ReturnsFalse(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method and assert that it returns False
        assert not encoder.isEncodeEquals("", "test")

    def testisEncodeEquals_CornerCase_SecondNameNothing_ReturnsFalse(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that the isEncodeEquals method returns False when the second argument is an empty string
        assert not encoder.isEncodeEquals("test", "")

    def testisVowel_SingleVowel_ReturnsTrue(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that the isVowel method returns True for the input "I"
        assert encoder.isVowel("I")

    def testcleanName_SuccessfullyClean(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the cleanName method
        result = encoder.cleanName("This-ís   a t.,es &t")

        # Assert that the result is as expected
        assert result == "THISISATEST"

    def testGetMinRating_13_Returns_1_Successfully(self) -> None:

        # Instantiate MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call getMinRating method
        result = encoder.getMinRating(13)

        # Assert the result
        self.assertEqual(1, result)

    def testgetMinRating_11_Returns_3_Successfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getMinRating method with 11 as argument
        result = encoder.getMinRating(11)

        # Assert that the result is 3
        assert result == 3

    def testgetMinRating_10_Returns3_Successfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getMinRating method with 10 as argument
        result = encoder.getMinRating(10)

        # Assert that the result is 3
        assert result == 3

    def testgetMinRating_8_Returns3_Successfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getMinRating method with 8 as argument
        result = encoder.getMinRating(8)

        # Assert that the result is 3
        assert result == 3

    def testgetMinRating_7_Returns4_Successfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getMinRating method with 7 as argument
        result = encoder.getMinRating(7)

        # Assert that the result is 4
        assert result == 4

    def testgetMinRating_6_Returns4_Successfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getMinRating method with 6 as argument
        result = encoder.getMinRating(6)

        # Assert that the result is 4
        assert result == 4

    def testgetMinRating_5_Returns4_Successfully2(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getMinRating method with 5 as argument
        result = encoder.getMinRating(5)

        # Assert that the result is 4
        assert result == 4

    def testgetMinRating_5_Returns4_Successfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getMinRating method with 5 as argument
        result = encoder.getMinRating(5)

        # Assert that the result is 4
        assert result == 4

    def testGetMinRating_2_Returns5_Successfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getMinRating method with 2 as argument
        result = encoder.getMinRating(2)

        # Assert that the result is 5
        assert result == 5

    def testGetMinRating_1_Returns5_Successfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getMinRating method with 1 as argument
        result = encoder.getMinRating(1)

        # Assert that the result is 5
        assert result == 5

    def testGetMinRating_7_Return4_Successfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getMinRating method with 7 as argument
        result = encoder.getMinRating(7)

        # Assert that the result is 4
        assert result == 4

    def testleftTorightThenRightToLeft_EINSTEIN_MICHAELA_Returns0(self) -> None:

        encoder = MatchRatingApproachEncoder()
        result = encoder.leftToRightThenRightToLeftProcessing("EINSTEIN", "MICHAELA")

        self.assertEqual(0, result)

    def testleftTorightThenRightToLeft_ALEXANDER_ALEXANDRA_Returns4(self) -> None:

        encoder = MatchRatingApproachEncoder()
        result = encoder.leftToRightThenRightToLeftProcessing("ALEXANDER", "ALEXANDRA")

        self.assertEqual(4, result)

    def testGetFirstLast3_PETE_Returns_PETE(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getFirst3Last3 method with "PETE" as argument
        result = encoder.getFirst3Last3("PETE")

        # Assert that the result is "PETE"
        assert result == "PETE"

    def testGetFirstLast3__ALEXANDER_Returns_Aleder(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getFirst3Last3 method
        result = encoder.getFirst3Last3("Alexzander")

        # Assert that the result is as expected
        assert result == "Aleder"

    def testRemoveVowel__DECLAN_Returns_DCLN(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the removeVowels method
        result = encoder.removeVowels("DECLAN")

        # Assert that the result is as expected
        assert result == "DCLN"

    def testRemoveVowel__AIDAN_Returns_ADN(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the removeVowels method
        result = encoder.removeVowels("AIDAN")

        # Assert that the result is "ADN"
        assert result == "ADN"

    def testRemoveVowel_ALESSANDRA_Returns_ALSSNDR(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the removeVowels method
        result = encoder.removeVowels("ALESSANDRA")

        # Assert that the result is as expected
        assert result == "ALSSNDR"

    def testIsVowel_SmallD_ReturnsFalse(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isVowel method with "d"
        result = encoder.isVowel("d")

        # Assert that the result is False
        assert not result

    def testIsVowel_CapitalA_ReturnsTrue(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isVowel method with "A"
        result = encoder.isVowel("A")

        # Assert that the result is True
        assert result == True

    def testRemoveDoubleDoubleVowel_BEETLE_NotRemoved(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the removeDoubleConsonants method
        result = encoder.removeDoubleConsonants("BEETLE")

        # Assert that the result is equal to "BEETLE"
        assert result == "BEETLE"

    def testRemoveDoubleConsonants_MISSISSIPPI_RemovedSuccessfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the removeDoubleConsonants method
        result = encoder.removeDoubleConsonants("MISSISSIPPI")

        # Assert that the result is as expected
        assert result == "MISISIPI"

    def testRemoveSingleDoubleConsonants_BUBLE_RemovedSuccessfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the removeDoubleConsonants method
        result = encoder.removeDoubleConsonants("BUBBLE")

        # Assert that the result is as expected
        assert result == "BUBLE"

    def testAccentRemoval_NullValue_ReturnNullSuccessfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that the result of removeAccents(None) is None
        assert encoder.removeAccents(None) is None

    def testAccentRemoval_NINO_NoChange(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the removeAccents method with an empty string
        result = encoder.removeAccents("")

        # Assert that the result is an empty string
        assert result == ""

    def testAccentRemovalNormalString_NoChange(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the removeAccents method
        result = encoder.removeAccents("Colorless green ideas sleep furiously")

        # Assert that the result is as expected
        assert result == "Colorless green ideas sleep furiously"

    def testAccentRemoval_ComprehensiveAccentMix_AllSuccessfullyRemoved(self) -> None:

        # Assuming that the removeAccents method is a static method in MatchRatingApproachEncoder class
        # If it's not, you need to create an instance of MatchRatingApproachEncoder
        # and call the method on that instance
        result = MatchRatingApproachEncoder.removeAccents(
            "È,É,Ê,Ë,Û,Ù,Ï,Î,�,Â,Ô,è,é,ê,ë,�,�,ï,î,à,â,ô,ç"
        )

        self.assertEqual("E,E,E,E,U,U,I,I,A,A,O,e,e,e,e,u,u,i,i,a,a,o,c", result)

    def testAccentRemoval_GerSpanFrenMix_SuccessfullyRemoved(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the removeAccents method
        result = encoder.removeAccents("äë��ßÄËÖÜñÑà")

        # Assert that the result is as expected
        self.assertEqual("aeoußAEOUnNa", result)

    def testAccentRemoval_MixedWithUnusualChars_SuccessfullyRemovedAndUnusualcharactersInvariant(
        self,
    ) -> None:

        # Assuming that the removeAccents method is a static method in MatchRatingApproachEncoder class
        # If it's not, you need to create an instance of MatchRatingApproachEncoder
        # and call the method on that instance
        result = MatchRatingApproachEncoder.removeAccents("�-e'í.,ó&�")

        # Assuming that the StringEncoderAbstractTest class has a method called assertEquals
        # If it's not, you need to import the appropriate class and method
        StringEncoderAbstractTest.assertEquals("A-e'i.,o&u", result)

    def testAccentRemoval_UpperandLower_SuccessfullyRemovedAndCaseInvariant(
        self,
    ) -> None:

        # Assuming that the removeAccents method is a static method in MatchRatingApproachEncoder class
        # If it's not, you need to create an instance of MatchRatingApproachEncoder
        # and call the method on that instance
        result = MatchRatingApproachEncoder.removeAccents("�eíÓuu")

        # Assuming that the StringEncoderAbstractTest class has a method called assertEquals
        # If it's not, you need to import the appropriate class and method
        StringEncoderAbstractTest.assertEquals("AeiOuu", result)

    def testAccentRemoval_WithSpaces_SuccessfullyRemovedAndSpacesInvariant(
        self,
    ) -> None:

        # Assuming that the removeAccents method is a static method in MatchRatingApproachEncoder class
        # If it's not, you need to create an instance of MatchRatingApproachEncoder
        # and call the method on that instance
        self.assertEqual(
            "ae io  u", MatchRatingApproachEncoder.removeAccents("áé íó  �")
        )

    def testAccentRemoval_AllLower_SuccessfullyRemoved(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the removeAccents method
        result = encoder.removeAccents("áéíó�")

        # Assert that the result is as expected
        assert result == "aeiou"
