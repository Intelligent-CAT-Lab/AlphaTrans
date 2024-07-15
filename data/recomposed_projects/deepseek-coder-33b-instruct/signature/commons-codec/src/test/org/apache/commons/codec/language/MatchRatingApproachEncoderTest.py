from __future__ import annotations
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.StringEncoder import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.language.MatchRatingApproachEncoder import *


class MatchRatingApproachEncoderTest(unittest.TestCase):

    def _createStringEncoder(self) -> MatchRatingApproachEncoder:
        return MatchRatingApproachEncoder()

    def testCompare_Forenames_SEAN_PETE_NoMatchExpected(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method and assert that it returns False for "Sean" and "Pete"
        self.assertFalse(encoder.isEncodeEquals("Sean", "Pete"))

    def testCompare_Forenames_SEAN_JOHN_MatchExpected(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with "Sean" and "John" as arguments
        result = encoder.isEncodeEquals("Sean", "John")

        # Assert that the result is True
        self.assertTrue(result)

    def testCompare_Surnames_MURPHY_LYNCH_NoMatchExpected(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use assertFalse to check if the encoded names "Murphy" and "Lynch" are not equal
        self.assertFalse(encoder.isEncodeEquals("Murphy", "Lynch"))

    def testCompare_SurnameCornerCase_Nulls_NoMatch(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that the isEncodeEquals method returns False when both inputs are None
        self.assertFalse(encoder.isEncodeEquals(None, None))

    def testCompare_SurnamesCornerCase_MURPHY_NoSpace_NoMatch(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that the isEncodeEquals method returns False when comparing "Murphy" with an empty string
        self.assertFalse(encoder.isEncodeEquals("Murphy", ""))

    def testCompare_SurnamesCornerCase_MURPHY_Space_NoMatch(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that the isEncodeEquals method returns False when comparing "Murphy" and " "
        self.assertFalse(encoder.isEncodeEquals("Murphy", " "))

    def testCompare_MCGOWAN_MCGEOGHEGAN_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method to compare "McGowan" and "Mc Geoghegan"
        self.assertTrue(encoder.isEncodeEquals("McGowan", "Mc Geoghegan"))

    def testCompare_PETERSON_PETERS_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method to compare "Peterson" and "Peters"
        self.assertTrue(encoder.isEncodeEquals("Peterson", "Peters"))

    def testCompare_Surname_PRZEMYSL_PSHEMESHIL_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method and assert that it returns True
        self.assertTrue(encoder.isEncodeEquals(" P rz e m y s l", " P sh e m e sh i l"))

    def testCompare_Surname_ROSOCHOWACIEC_ROSOKHOVATSETS_SuccessfullyMatched(
        self,
    ) -> None:

        self.assertTrue(
            self.getStringEncoder().isEncodeEquals(
                "R o s o c h o w a c i e c", " R o s o k h o v a t s e t s"
            )
        )

    def testCompare_Surname_SZLAMAWICZ_SHLAMOVITZ_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method to compare "SZLAMAWICZ" and "SHLAMOVITZ"
        result = encoder.isEncodeEquals("SZLAMAWICZ", "SHLAMOVITZ")

        # Assert that the result is True
        self.assertTrue(result)

    def testCompare_Surname_LEWINSKY_LEVINSKI_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method to compare "LEWINSKY" and "LEVINSKI"
        result = encoder.isEncodeEquals("LEWINSKY", "LEVINSKI")

        # Assert that the result is True
        self.assertTrue(result)

    def testCompare_Surname_LIPSHITZ_LIPPSZYC_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method to compare "LIPSHITZ" and "LIPPSZYC"
        result = encoder.isEncodeEquals("LIPSHITZ", "LIPPSZYC")

        # Assert that the result is True
        self.assertTrue(result)

    def testCompare_Surname_MOSKOWITZ_MOSKOVITZ_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method to compare "Moskowitz" and "Moskovitz"
        self.assertTrue(encoder.isEncodeEquals("Moskowitz", "Moskovitz"))

    def testCompare_Surname_AUERBACH_UHRBACH_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method to compare "Auerbach" and "Uhrbach"
        self.assertTrue(encoder.isEncodeEquals("Auerbach", "Uhrbach"))

    def testCompare_Surname_HAILEY_HALLEY_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method to compare "Hailey" and "Halley"
        self.assertTrue(encoder.isEncodeEquals("Hailey", "Halley"))

    def testCompare_Surname_COOPERFLYNN_SUPERLYN_SuccessfullyMatched(self) -> None:

        self.assertTrue(
            self.getStringEncoder().isEncodeEquals("Cooper-Flynn", "Super-Lyn")
        )

    def testCompare_LongSurnames_OMUIRCHEARTAIGH_OMIREADHAIGH_SuccessfulMatch(
        self,
    ) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method and assert that it returns True
        self.assertTrue(encoder.isEncodeEquals("o'muireadhaigh", "Ó 'Muircheartaigh "))

    def testCompare_LongSurnames_MORIARTY_OMUIRCHEARTAIGH_DoesNotSuccessfulMatch(
        self,
    ) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use assertFalse to check if the encoded versions of "Moriarty" and "OMuircheartaigh" are not equal
        self.assertFalse(encoder.isEncodeEquals("Moriarty", "OMuircheartaigh"))

    def testCompare_Surname_OSULLIVAN_OSUILLEABHAIN_SuccessfulMatch(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method to compare the two names
        result = encoder.isEncodeEquals("O'Sullivan", "Ó ' S�illeabháin")

        # Assert that the result is True
        self.assertTrue(result)

    def testCompare_Forenames_UNA_OONAGH_ShouldSuccessfullyMatchButDoesNot(
        self,
    ) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use assertFalse to check if the encoded versions of "Úna" and "Oonagh" are not equal
        self.assertFalse(encoder.isEncodeEquals("Úna", "Oonagh"))

    def testCompare_KARL_ALESSANDRO_DoesNotMatch(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use assertFalse to check if the encoded versions of "Karl" and "Alessandro" are not equal
        self.assertFalse(encoder.isEncodeEquals("Karl", "Alessandro"))

    def testCompare_ZACH_ZAKARIA_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method to compare "Zach" and "Zacharia"
        self.assertTrue(encoder.isEncodeEquals("Zach", "Zacharia"))

    def testCompareNameToSingleLetter_KARL_C_DoesNotMatch(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method and assert that it returns False
        self.assertFalse(encoder.isEncodeEquals("Karl", "C"))

    def testCompare_SmallInput_CARK_Kl_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method and assert that it returns True
        self.assertTrue(encoder.isEncodeEquals("Kl", "Karl"))

    def testCompare_TOMASZ_TOM_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method and assert that it returns True
        self.assertTrue(encoder.isEncodeEquals("Tomasz", "tom"))

    def testCompare_FRANCISZEK_FRANCES_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method to compare "Franciszek" and "Frances"
        self.assertTrue(encoder.isEncodeEquals("Franciszek", "Frances"))

    def testCompare_SOPHIE_SOFIA_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method to compare "Sophie" and "Sofia"
        self.assertTrue(encoder.isEncodeEquals("Sophie", "Sofia"))

    def testCompare_OONA_OONAGH_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method to compare "Oona" and "Oonagh"
        self.assertTrue(encoder.isEncodeEquals("Oona", "Oonagh"))

    def testCompare_MICKY_MICHAEL_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method to compare "Micky" and "Michael"
        result = encoder.isEncodeEquals("Micky", "Michael")

        # Assert that the result is True
        self.assertTrue(result)

    def testCompare_SAM_SAMUEL_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method to compare "Sam" and "Samuel"
        result = encoder.isEncodeEquals("Sam", "Samuel")

        # Assert that the result is True
        self.assertTrue(result)

    def testCompare_STEPHEN_STEFAN_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method to compare "Stephen" and "Stefan"
        self.assertTrue(encoder.isEncodeEquals("Stephen", "Stefan"))

    def testCompare_STEVEN_STEFAN_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method to compare "Steven" and "Stefan"
        self.assertTrue(encoder.isEncodeEquals("Steven", "Stefan"))

    def testCompare_STEPHEN_STEVEN_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method to compare "Stephen" and "Steven"
        self.assertTrue(encoder.isEncodeEquals("Stephen", "Steven"))

    def testCompare_COLM_COLIN_WithAccentsAndSymbolsAndSpaces_SuccessfullyMatched(
        self,
    ) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method and assert that it returns True
        self.assertTrue(encoder.isEncodeEquals("Cólm.   ", "C-olín"))

    def testCompare_SEAN_SHAUN_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method to compare "Séan" and "Shaun"
        self.assertTrue(encoder.isEncodeEquals("Séan", "Shaun"))

    def testCompare_BRIAN_BRYAN_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method to compare "Brian" and "Bryan"
        self.assertTrue(encoder.isEncodeEquals("Brian", "Bryan"))

    def testCompare_CATHERINE_KATHRYN_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method to compare "Catherine" and "Kathryn"
        self.assertTrue(encoder.isEncodeEquals("Catherine", "Kathryn"))

    def testCompare_ShortNames_AL_ED_WorksButNoMatch(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use assertFalse to check if the encoded versions of "Al" and "Ed" are not equal
        self.assertFalse(encoder.isEncodeEquals("Al", "Ed"))

    def testCompare_BURNS_BOURNE_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("Burns", "Bourne"))

    def testCompare_SMITH_SMYTH_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Use the isEncodeEquals method to compare "smith" and "smyth"
        self.assertTrue(encoder.isEncodeEquals("smith", "smyth"))

    def testCompareNameSameNames_ReturnsFalseSuccessfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with the same name
        result = encoder.isEncodeEquals("John", "John")

        # Assert that the result is True
        self.assertTrue(result)

    def testCompareNameNullSpace_ReturnsFalseSuccessfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that the result of isEncodeEquals with null and space is False
        self.assertFalse(encoder.isEncodeEquals(None, " "))

    def testGetEncoding_One_Letter_to_Nothing(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the encode1 method with "E" as input
        result = encoder.encode1("E")

        # Assert that the result is an empty string
        self.assertEqual("", result)

    def testGetEncoding_Null_to_Nothing(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that the encoding of null is an empty string
        self.assertEqual("", encoder.encode1(None))

    def testGetEncoding_NoSpace_to_Nothing(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the encode1 method with an empty string
        result = encoder.encode1("")

        # Assert that the result is an empty string
        self.assertEqual("", result)

    def testGetEncoding_Space_to_Nothing(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that encoding a space returns an empty string
        self.assertEqual("", encoder.encode1(" "))

    def testGetEncoding_SMYTH_to_SMYTH(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the encode1 method with "Smyth" as input
        result = encoder.encode1("Smyth")

        # Assert that the result is "SMYTH"
        self.assertEqual("SMYTH", result)

    def testGetEncoding_SMITH_to_SMTH(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the encode1 method with "Smith" as input
        result = encoder.encode1("Smith")

        # Assert that the result is "SMTH"
        self.assertEqual("SMTH", result)

    def testGetEncoding_HARPER_HRPR(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the encode1 method with "HARPER" as input
        result = encoder.encode1("HARPER")

        # Assert that the result is "HRPR"
        self.assertEqual("HRPR", result)

    def testisEncodeEqualsSecondNameJust1Letter_ReturnsFalse(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with two strings
        result = encoder.isEncodeEquals("test", "t")

        # Assert that the result is False
        self.assertFalse(result)

    def testisEncodeEquals_CornerCase_FirstNameJust1Letter_ReturnsFalse(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with the given parameters
        result = encoder.isEncodeEquals("t", "test")

        # Assert that the result is False
        self.assertFalse(result)

    def testisEncodeEquals_CornerCase_FirstNameNull_ReturnsFalse(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that the isEncodeEquals method returns False when the first name is None
        self.assertFalse(encoder.isEncodeEquals(None, "test"))

    def testisEncodeEquals_CornerCase_SecondNameNull_ReturnsFalse(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that the isEncodeEquals method returns False when the second name is None
        self.assertFalse(encoder.isEncodeEquals("test", None))

    def testisEncodeEquals_CornerCase_FirstNameJustSpace_ReturnsFalse(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with a space and a string
        result = encoder.isEncodeEquals(" ", "test")

        # Assert that the result is False
        self.assertFalse(result)

    def testisEncodeEquals_CornerCase_SecondNameJustSpace_ReturnsFalse(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with "test" and " " as arguments
        result = encoder.isEncodeEquals("test", " ")

        # Assert that the result is False
        self.assertFalse(result)

    def testisEncodeEquals_CornerCase_FirstNameNothing_ReturnsFalse(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that the isEncodeEquals method returns False when the first name is an empty string
        self.assertFalse(encoder.isEncodeEquals("", "test"))

    def testisEncodeEquals_CornerCase_SecondNameNothing_ReturnsFalse(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that the isEncodeEquals method returns False when the second name is an empty string
        self.assertFalse(encoder.isEncodeEquals("test", ""))

    def testisVowel_SingleVowel_ReturnsTrue(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that the letter "I" is a vowel
        self.assertTrue(encoder.isVowel("I"))

    def testcleanName_SuccessfullyClean(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the cleanName method with a test string
        cleaned_name = encoder.cleanName("This-ís   a t.,es &t")

        # Assert that the result is as expected
        self.assertEqual(cleaned_name, "THISISATEST")

    def testGetMinRating_13_Returns_1_Successfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getMinRating method with 13 as argument
        result = encoder.getMinRating(13)

        # Assert that the result is 1
        self.assertEqual(1, result)

    def testgetMinRating_11_Returns_3_Successfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getMinRating method with 11 as argument
        result = encoder.getMinRating(11)

        # Assert that the result is 3
        self.assertEqual(result, 3)

    def testgetMinRating_10_Returns3_Successfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getMinRating method with 10 as argument
        result = encoder.getMinRating(10)

        # Assert that the result is 3
        self.assertEqual(3, result)

    def testgetMinRating_8_Returns3_Successfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getMinRating method with 8 as argument
        result = encoder.getMinRating(8)

        # Assert that the result is 3
        self.assertEqual(3, result)

    def testgetMinRating_7_Returns4_Successfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getMinRating method with 7 as argument
        result = encoder.getMinRating(7)

        # Assert that the result is 4
        self.assertEqual(4, result)

    def testgetMinRating_6_Returns4_Successfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getMinRating method with 6 as argument
        result = encoder.getMinRating(6)

        # Assert that the result is 4
        self.assertEqual(4, result)

    def testgetMinRating_5_Returns4_Successfully2(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that the result of getMinRating(5) is 4
        self.assertEqual(4, encoder.getMinRating(5))

    def testgetMinRating_5_Returns4_Successfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getMinRating method with 5 as argument
        result = encoder.getMinRating(5)

        # Assert that the result is 4
        self.assertEqual(4, result)

    def testGetMinRating_2_Returns5_Successfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getMinRating method with 2 as argument
        result = encoder.getMinRating(2)

        # Assert that the result is 5
        self.assertEqual(5, result)

    def testGetMinRating_1_Returns5_Successfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getMinRating method with 1 as argument
        result = encoder.getMinRating(1)

        # Assert that the result is 5
        self.assertEqual(5, result)

    def testGetMinRating_7_Return4_Successfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getMinRating method with 7 as argument
        result = encoder.getMinRating(7)

        # Assert that the result is 4
        self.assertEqual(4, result)

    def testleftTorightThenRightToLeft_EINSTEIN_MICHAELA_Returns0(self) -> None:

        self.assertEqual(
            0,
            self.getStringEncoder().leftToRightThenRightToLeftProcessing(
                "EINSTEIN", "MICHAELA"
            ),
        )

    def testleftTorightThenRightToLeft_ALEXANDER_ALEXANDRA_Returns4(self) -> None:

        self.assertEqual(
            4,
            self.getStringEncoder().leftToRightThenRightToLeftProcessing(
                "ALEXANDER", "ALEXANDRA"
            ),
        )

    def testGetFirstLast3_PETE_Returns_PETE(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getFirst3Last3 method with "PETE" as the argument
        result = encoder.getFirst3Last3("PETE")

        # Assert that the result is "PETE"
        self.assertEqual("PETE", result)

    def testGetFirstLast3__ALEXANDER_Returns_Aleder(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getFirst3Last3 method with "Alexzander" as input
        result = encoder.getFirst3Last3("Alexzander")

        # Assert that the result is "Aleder"
        self.assertEqual("Aleder", result)

    def testRemoveVowel__DECLAN_Returns_DCLN(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the removeVowels method with "DECLAN" as input
        result = encoder.removeVowels("DECLAN")

        # Assert that the result is "DCLN"
        self.assertEqual("DCLN", result)

    def testRemoveVowel__AIDAN_Returns_ADN(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the removeVowels method with "AIDAN" as input
        result = encoder.removeVowels("AIDAN")

        # Assert that the result is "ADN"
        self.assertEqual("ADN", result)

    def testRemoveVowel_ALESSANDRA_Returns_ALSSNDR(self) -> None:

        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        name = "ALESSANDRA"
        result = "".join([char for char in name if char not in vowels])
        self.assertEqual("ALSSNDR", result)

    def testIsVowel_SmallD_ReturnsFalse(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that the letter "d" is not a vowel
        self.assertFalse(encoder.isVowel("d"))

    def testIsVowel_CapitalA_ReturnsTrue(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that 'A' is a vowel
        self.assertTrue(encoder.isVowel("A"))

    def testRemoveDoubleDoubleVowel_BEETLE_NotRemoved(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the removeDoubleConsonants method with "BEETLE" as input
        result = encoder.removeDoubleConsonants("BEETLE")

        # Assert that the result is "BEETLE"
        self.assertEqual("BEETLE", result)

    def testRemoveDoubleConsonants_MISSISSIPPI_RemovedSuccessfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the removeDoubleConsonants method
        result = encoder.removeDoubleConsonants("MISSISSIPPI")

        # Assert that the result is as expected
        self.assertEqual("MISISIPI", result)

    def testRemoveSingleDoubleConsonants_BUBLE_RemovedSuccessfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the removeDoubleConsonants method
        result = encoder.removeDoubleConsonants("BUBBLE")

        # Assert that the result is as expected
        self.assertEqual("BUBLE", result)

    def testAccentRemoval_NullValue_ReturnNullSuccessfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that the removeAccents method returns None when given None
        self.assertIsNone(encoder.removeAccents(None))

    def testAccentRemoval_NINO_NoChange(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the removeAccents method with an empty string
        result = encoder.removeAccents("")

        # Assert that the result is an empty string
        self.assertEqual("", result)

    def testAccentRemovalNormalString_NoChange(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Define the expected and actual strings
        expected = "Colorless green ideas sleep furiously"
        actual = encoder.removeAccents("Colorless green ideas sleep furiously")

        # Use the unittest.TestCase.assertEqual method to compare the expected and actual strings
        self.assertEqual(expected, actual)

    def testAccentRemoval_ComprehensiveAccentMix_AllSuccessfullyRemoved(self) -> None:

        self.assertEqual(
            "E,E,E,E,U,U,I,I,A,A,O,e,e,e,e,u,u,i,i,a,a,o,c",
            self.getStringEncoder().removeAccents(
                "È,É,Ê,Ë,Û,Ù,Ï,Î,�,Â,Ô,è,é,ê,ë,�,�,ï,î,à,â,ô,ç"
            ),
        )

    def testAccentRemoval_GerSpanFrenMix_SuccessfullyRemoved(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the removeAccents method with the input string
        result = encoder.removeAccents("äë��ßÄËÖÜñÑà")

        # Assert that the result is as expected
        self.assertEqual("aeoußAEOUnNa", result)

    def testAccentRemoval_MixedWithUnusualChars_SuccessfullyRemovedAndUnusualcharactersInvariant(
        self,
    ) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Define the accented word
        accented_word = "�-e'í.,ó&�"

        # Call the removeAccents method
        result = encoder.removeAccents(accented_word)

        # Assert that the result is as expected
        self.assertEqual("A-e'i.,o&u", result)

    def testAccentRemoval_UpperandLower_SuccessfullyRemovedAndCaseInvariant(
        self,
    ) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the removeAccents method with the accented word
        result = encoder.removeAccents("�eíÓuu")

        # Check if the result is as expected
        self.assertEqual("AeiOuu", result)

    def testAccentRemoval_WithSpaces_SuccessfullyRemovedAndSpacesInvariant(
        self,
    ) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the removeAccents method with the accented word
        result = encoder.removeAccents("áé íó  �")

        # Assert that the result is as expected
        self.assertEqual("ae io  u", result)

    def testAccentRemoval_AllLower_SuccessfullyRemoved(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the removeAccents method with the accented word
        result = encoder.removeAccents("áéíó�")

        # Assert that the result is as expected
        self.assertEqual("aeiou", result)
