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

        # Instantiate the MatchRatingApproachEncoder class
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with "Sean" and "Pete" as arguments
        result = encoder.isEncodeEquals("Sean", "Pete")

        # Assert that the result is False
        self.assertFalse(result)

    def testCompare_Forenames_SEAN_JOHN_MatchExpected(self) -> None:

        match_rating_approach_encoder = MatchRatingApproachEncoder()
        assert match_rating_approach_encoder.isEncodeEquals("Sean", "John")

    def testCompare_Surnames_MURPHY_LYNCH_NoMatchExpected(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that the isEncodeEquals method returns False for "Murphy" and "Lynch"
        self.assertFalse(encoder.isEncodeEquals("Murphy", "Lynch"))

    def testCompare_SurnameCornerCase_Nulls_NoMatch(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that isEncodeEquals returns False when both arguments are None
        self.assertFalse(encoder.isEncodeEquals(None, None))

    def testCompare_SurnamesCornerCase_MURPHY_NoSpace_NoMatch(self) -> None:

        encoder = MatchRatingApproachEncoder()
        assert not encoder.isEncodeEquals("Murphy", "")

    def testCompare_SurnamesCornerCase_MURPHY_Space_NoMatch(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that the isEncodeEquals method returns False when comparing "Murphy" and " "
        self.assertFalse(encoder.isEncodeEquals("Murphy", " "))

    def testCompare_MCGOWAN_MCGEOGHEGAN_SuccessfullyMatched(self) -> None:

        assert self.getStringEncoder().isEncodeEquals("McGowan", "Mc Geoghegan")

    def testCompare_PETERSON_PETERS_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with "Peterson" and "Peters"
        result = encoder.isEncodeEquals("Peterson", "Peters")

        # Assert that the result is True
        self.assertTrue(result)

    def testCompare_Surname_PRZEMYSL_PSHEMESHIL_SuccessfullyMatched(self) -> None:

        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals(" P rz e m y s l", " P sh e m e sh i l"))

    def testCompare_Surname_ROSOCHOWACIEC_ROSOKHOVATSETS_SuccessfullyMatched(
        self,
    ) -> None:

        encoder = MatchRatingApproachEncoder()
        assert encoder.isEncodeEquals(
            "R o s o c h o w a c i e c", " R o s o k h o v a t s e t s"
        )

    def testCompare_Surname_SZLAMAWICZ_SHLAMOVITZ_SuccessfullyMatched(self) -> None:

        encoder = MatchRatingApproachEncoder()
        assert encoder.isEncodeEquals("SZLAMAWICZ", "SHLAMOVITZ")

    def testCompare_Surname_LEWINSKY_LEVINSKI_SuccessfullyMatched(self) -> None:

        encoder = MatchRatingApproachEncoder()
        assert encoder.isEncodeEquals("LEWINSKY", "LEVINSKI")

    def testCompare_Surname_LIPSHITZ_LIPPSZYC_SuccessfullyMatched(self) -> None:

        encoder = MatchRatingApproachEncoder()
        assert encoder.isEncodeEquals("LIPSHITZ", "LIPPSZYC")

    def testCompare_Surname_MOSKOWITZ_MOSKOVITZ_SuccessfullyMatched(self) -> None:

        encoder = MatchRatingApproachEncoder()
        assert encoder.isEncodeEquals("Moskowitz", "Moskovitz")

    def testCompare_Surname_AUERBACH_UHRBACH_SuccessfullyMatched(self) -> None:

        encoder = MatchRatingApproachEncoder()
        assert encoder.isEncodeEquals("Auerbach", "Uhrbach")

    def testCompare_Surname_HAILEY_HALLEY_SuccessfullyMatched(self) -> None:

        encoder = MatchRatingApproachEncoder()
        assert encoder.isEncodeEquals("Hailey", "Halley")

    def testCompare_Surname_COOPERFLYNN_SUPERLYN_SuccessfullyMatched(self) -> None:

        encoder = MatchRatingApproachEncoder()
        assert encoder.isEncodeEquals("Cooper-Flynn", "Super-Lyn")

    def testCompare_LongSurnames_OMUIRCHEARTAIGH_OMIREADHAIGH_SuccessfulMatch(
        self,
    ) -> None:

        encoder = MatchRatingApproachEncoder()
        assert encoder.isEncodeEquals("o'muireadhaigh", "Ó 'Muircheartaigh ")

    def testCompare_LongSurnames_MORIARTY_OMUIRCHEARTAIGH_DoesNotSuccessfulMatch(
        self,
    ) -> None:

        match_rating_approach_encoder = MatchRatingApproachEncoder()
        assert not match_rating_approach_encoder.isEncodeEquals(
            "Moriarty", "OMuircheartaigh"
        )

    def testCompare_Surname_OSULLIVAN_OSUILLEABHAIN_SuccessfulMatch(self) -> None:

        encoder = MatchRatingApproachEncoder()
        assert encoder.isEncodeEquals("O'Sullivan", "Ó ' S�illeabháin")

    def testCompare_Forenames_UNA_OONAGH_ShouldSuccessfullyMatchButDoesNot(
        self,
    ) -> None:

        encoder = MatchRatingApproachEncoder()
        assert not encoder.isEncodeEquals("Úna", "Oonagh")

    def testCompare_KARL_ALESSANDRO_DoesNotMatch(self) -> None:

        string_encoder = MatchRatingApproachEncoder()
        self.assertFalse(string_encoder.isEncodeEquals("Karl", "Alessandro"))

    def testCompare_ZACH_ZAKARIA_SuccessfullyMatched(self) -> None:

        # Instantiate MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with "Zach" and "Zacharia"
        result = encoder.isEncodeEquals("Zach", "Zacharia")

        # Assert that the result is True
        self.assertTrue(result)

    def testCompareNameToSingleLetter_KARL_C_DoesNotMatch(self) -> None:

        # Instantiate the MatchRatingApproachEncoder class
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with "Karl" and "C" as arguments
        result = encoder.isEncodeEquals("Karl", "C")

        # Assert that the result is False
        self.assertFalse(result)

    def testCompare_SmallInput_CARK_Kl_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with the given names
        result = encoder.isEncodeEquals("Kl", "Karl")

        # Assert that the result is True
        self.assertTrue(result)

    def testCompare_TOMASZ_TOM_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with "Tomasz" and "tom"
        result = encoder.isEncodeEquals("Tomasz", "tom")

        # Assert that the result is True
        self.assertTrue(result)

    def testCompare_FRANCISZEK_FRANCES_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with "Franciszek" and "Frances"
        result = encoder.isEncodeEquals("Franciszek", "Frances")

        # Assert that the result is True
        self.assertTrue(result)

    def testCompare_SOPHIE_SOFIA_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with "Sophie" and "Sofia"
        result = encoder.isEncodeEquals("Sophie", "Sofia")

        # Assert that the result is True
        self.assertTrue(result)

    def testCompare_OONA_OONAGH_SuccessfullyMatched(self) -> None:

        string_encoder = StringEncoder()
        self.assertTrue(string_encoder.isEncodeEquals("Oona", "Oonagh"))

    def testCompare_MICKY_MICHAEL_SuccessfullyMatched(self) -> None:

        # Instantiate MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with "Micky" and "Michael"
        result = encoder.isEncodeEquals("Micky", "Michael")

        # Assert that the result is True
        self.assertTrue(result)

    def testCompare_SAM_SAMUEL_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("Sam", "Samuel"))

    def testCompare_STEPHEN_STEFAN_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("Stephen", "Stefan"))

    def testCompare_STEVEN_STEFAN_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with "Steven" and "Stefan"
        result = encoder.isEncodeEquals("Steven", "Stefan")

        # Assert that the result is True
        self.assertTrue(result)

    def testCompare_STEPHEN_STEVEN_SuccessfullyMatched(self) -> None:

        encoder = MatchRatingApproachEncoder()
        assert encoder.isEncodeEquals("Stephen", "Steven")

    def testCompare_COLM_COLIN_WithAccentsAndSymbolsAndSpaces_SuccessfullyMatched(
        self,
    ) -> None:

        assert self.getStringEncoder().isEncodeEquals("Cólm.   ", "C-olín")

    def testCompare_SEAN_SHAUN_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with "Séan" and "Shaun"
        result = encoder.isEncodeEquals("Séan", "Shaun")

        # Assert that the result is True
        self.assertTrue(result)

    def testCompare_BRIAN_BRYAN_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with "Brian" and "Bryan"
        result = encoder.isEncodeEquals("Brian", "Bryan")

        # Assert that the result is True
        self.assertTrue(result)

    def testCompare_CATHERINE_KATHRYN_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with "Catherine" and "Kathryn"
        result = encoder.isEncodeEquals("Catherine", "Kathryn")

        # Assert that the result is True
        self.assertTrue(result)

    def testCompare_ShortNames_AL_ED_WorksButNoMatch(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that the encoder does not consider "Al" and "Ed" as equal
        self.assertFalse(encoder.isEncodeEquals("Al", "Ed"))

    def testCompare_BURNS_BOURNE_SuccessfullyMatched(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with "Burns" and "Bourne"
        result = encoder.isEncodeEquals("Burns", "Bourne")

        # Assert that the result is True
        self.assertTrue(result)

    def testCompare_SMITH_SMYTH_SuccessfullyMatched(self) -> None:

        assert self.getStringEncoder().isEncodeEquals("smith", "smyth")

    def testCompareNameSameNames_ReturnsFalseSuccessfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with the same name
        result = encoder.isEncodeEquals("John", "John")

        # Assert that the result is True
        self.assertTrue(result)

    def testCompareNameNullSpace_ReturnsFalseSuccessfully(self) -> None:

        encoder = MatchRatingApproachEncoder()
        assert not encoder.isEncodeEquals(None, " ")

    def testGetEncoding_One_Letter_to_Nothing(self) -> None:

        encoder = MatchRatingApproachEncoder()
        self.assertEqual("", encoder.encode1("E"))

    def testGetEncoding_Null_to_Nothing(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that the encoding of None is an empty string
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

        # Call the encode1 method with a space as input
        result = encoder.encode1(" ")

        # Assert that the result is an empty string
        self.assertEqual("", result)

    def testGetEncoding_SMYTH_to_SMYTH(self) -> None:

        encoder = MatchRatingApproachEncoder()
        result = encoder.encode1("Smyth")
        self.assertEqual("SMYTH", result)

    def testGetEncoding_SMITH_to_SMTH(self) -> None:

        encoder = MatchRatingApproachEncoder()
        result = encoder.encode1("Smith")
        self.assertEqual("SMTH", result)

    def testGetEncoding_HARPER_HRPR(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the encode1 method with "HARPER" as input
        result = encoder.encode1("HARPER")

        # Assert that the result is "HRPR"
        self.assertEqual("HRPR", result)

    def testisEncodeEqualsSecondNameJust1Letter_ReturnsFalse(self) -> None:

        encoder = MatchRatingApproachEncoder()
        self.assertFalse(encoder.isEncodeEquals("test", "t"))

    def testisEncodeEquals_CornerCase_FirstNameJust1Letter_ReturnsFalse(self) -> None:

        encoder = MatchRatingApproachEncoder()
        self.assertFalse(encoder.isEncodeEquals("t", "test"))

    def testisEncodeEquals_CornerCase_FirstNameNull_ReturnsFalse(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with the first name as None and the second name as "test"
        result = encoder.isEncodeEquals(None, "test")

        # Assert that the result is False
        self.assertFalse(result)

    def testisEncodeEquals_CornerCase_SecondNameNull_ReturnsFalse(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Assert that the method returns False when the second name is None
        self.assertFalse(encoder.isEncodeEquals("test", None))

    def testisEncodeEquals_CornerCase_FirstNameJustSpace_ReturnsFalse(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with a space as the first name and "test" as the second name
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

        # Call the isEncodeEquals method with an empty string as the first name and "test" as the second name
        result = encoder.isEncodeEquals("", "test")

        # Assert that the result is False
        self.assertFalse(result)

    def testisEncodeEquals_CornerCase_SecondNameNothing_ReturnsFalse(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isEncodeEquals method with "test" and "" as arguments
        result = encoder.isEncodeEquals("test", "")

        # Assert that the result is False
        self.assertFalse(result)

    def testisVowel_SingleVowel_ReturnsTrue(self) -> None:
        self.assertTrue(self.getStringEncoder().isVowel("I"))

    def testcleanName_SuccessfullyClean(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the cleanName method
        result = encoder.cleanName("This-ís   a t.,es &t")

        # Assert that the result is as expected
        self.assertEqual(result, "THISISATEST")

    def testGetMinRating_13_Returns_1_Successfully(self) -> None:

        encoder = MatchRatingApproachEncoder()
        self.assertEqual(1, encoder.getMinRating(13))

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
        self.assertEqual(result, 3)

    def testgetMinRating_8_Returns3_Successfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getMinRating method with 8 as argument
        result = encoder.getMinRating(8)

        # Assert that the result is 3
        self.assertEqual(result, 3)

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

        # Call the getMinRating method with 5 as argument
        result = encoder.getMinRating(5)

        # Assert that the result is 4
        self.assertEqual(4, result)

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
        self.assertEqual(result, 5)

    def testGetMinRating_1_Returns5_Successfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getMinRating method with 1 as argument
        result = encoder.getMinRating(1)

        # Assert that the result is 5
        self.assertEqual(result, 5)

    def testGetMinRating_7_Return4_Successfully(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the getMinRating method with 7 as argument
        result = encoder.getMinRating(7)

        # Assert that the result is 4
        self.assertEqual(4, result)

    def testleftTorightThenRightToLeft_EINSTEIN_MICHAELA_Returns0(self) -> None:

        match_rating_approach_encoder = MatchRatingApproachEncoder()
        result = match_rating_approach_encoder.leftToRightThenRightToLeftProcessing(
            "EINSTEIN", "MICHAELA"
        )
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
        self.assertEqual("PETE", result)

    def testGetFirstLast3__ALEXANDER_Returns_Aleder(self) -> None:

        encoder = MatchRatingApproachEncoder()
        result = encoder.getFirst3Last3("Alexzander")
        self.assertEqual("Aleder", result)

    def testRemoveVowel__DECLAN_Returns_DCLN(self) -> None:

        encoder = MatchRatingApproachEncoder()
        result = encoder.removeVowels("DECLAN")
        self.assertEqual("DCLN", result)

    def testRemoveVowel__AIDAN_Returns_ADN(self) -> None:

        encoder = MatchRatingApproachEncoder()
        result = encoder.removeVowels("AIDAN")
        self.assertEqual("ADN", result)

    def testRemoveVowel_ALESSANDRA_Returns_ALSSNDR(self) -> None:

        encoder = MatchRatingApproachEncoder()
        result = encoder.removeVowels("ALESSANDRA")
        self.assertEqual("ALSSNDR", result)

    def testIsVowel_SmallD_ReturnsFalse(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the isVowel method with "d"
        result = encoder.isVowel("d")

        # Assert that the result is False
        self.assertFalse(result)

    def testIsVowel_CapitalA_ReturnsTrue(self) -> None:
        self.assertTrue(self.getStringEncoder().isVowel("A"))

    def testRemoveDoubleDoubleVowel_BEETLE_NotRemoved(self) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the removeDoubleConsonants method
        result = encoder.removeDoubleConsonants("BEETLE")

        # Assert that the result is equal to "BEETLE"
        self.assertEqual("BEETLE", result)

    def testRemoveDoubleConsonants_MISSISSIPPI_RemovedSuccessfully(self) -> None:

        encoder = MatchRatingApproachEncoder()
        result = encoder.removeDoubleConsonants("MISSISSIPPI")
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

        # Call the removeAccents method with None as argument
        result = encoder.removeAccents(None)

        # Assert that the result is None
        self.assertIsNone(result)

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

        # Define the input string
        input_string = "Colorless green ideas sleep furiously"

        # Call the removeAccents method
        result = encoder.removeAccents(input_string)

        # Assert that the result is the same as the input string
        self.assertEqual(result, input_string)

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

        # Call the removeAccents method
        result = encoder.removeAccents("äë��ßÄËÖÜñÑà")

        # Assert that the result is as expected
        self.assertEqual("aeoußAEOUnNa", result)

    def testAccentRemoval_MixedWithUnusualChars_SuccessfullyRemovedAndUnusualcharactersInvariant(
        self,
    ) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the removeAccents method
        result = encoder.removeAccents("�-e'í.,ó&�")

        # Assert that the result is as expected
        self.assertEqual("A-e'i.,o&u", result)

    def testAccentRemoval_UpperandLower_SuccessfullyRemovedAndCaseInvariant(
        self,
    ) -> None:

        # Create an instance of MatchRatingApproachEncoder
        encoder = MatchRatingApproachEncoder()

        # Call the removeAccents method with the test string
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

        # Check if the result is as expected
        self.assertEqual("ae io  u", result)

    def testAccentRemoval_AllLower_SuccessfullyRemoved(self) -> None:

        encoder = MatchRatingApproachEncoder()
        result = encoder.removeAccents("áéíó�")
        self.assertEqual("aeiou", result)
