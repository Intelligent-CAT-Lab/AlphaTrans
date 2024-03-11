# Imports Begin
from src.main.org.apache.commons.codec.language.MatchRatingApproachEncoder import *
from src.main.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.StringEncoder import *
import unittest
import os

# Imports End


class MatchRatingApproachEncoderTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def _createStringEncoder(self) -> MatchRatingApproachEncoder:

        return MatchRatingApproachEncoder()

    def testCompare_Forenames_SEAN_PETE_NoMatchExpected(self) -> None:

        assert not self.getStringEncoder().isEncodeEquals("Sean", "Pete")

    def testCompare_Forenames_SEAN_JOHN_MatchExpected(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("Sean", "John"))

    def testCompare_Surnames_MURPHY_LYNCH_NoMatchExpected(self) -> None:

        self.assertFalse(self.getStringEncoder().isEncodeEquals("Murphy", "Lynch"))

    def testCompare_SurnameCornerCase_Nulls_NoMatch(self) -> None:

        assert not self.getStringEncoder().isEncodeEquals(None, None)

    def testCompare_SurnamesCornerCase_MURPHY_NoSpace_NoMatch(self) -> None:

        self.assertFalse(self.getStringEncoder().isEncodeEquals("Murphy", ""))

    def testCompare_SurnamesCornerCase_MURPHY_Space_NoMatch(self) -> None:

        assert not self.getStringEncoder().isEncodeEquals("Murphy", " ")

    def testCompare_MCGOWAN_MCGEOGHEGAN_SuccessfullyMatched(self) -> None:

        self.assertTrue(
            self.getStringEncoder().isEncodeEquals("McGowan", "Mc Geoghegan")
        )

    def testCompare_PETERSON_PETERS_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("Peterson", "Peters"))

    def testCompare_Surname_PRZEMYSL_PSHEMESHIL_SuccessfullyMatched(self) -> None:

        self.assertTrue(
            self.getStringEncoder().isEncodeEquals(
                " P rz e m y s l", " P sh e m e sh i l"
            )
        )

    def testCompare_Surname_ROSOCHOWACIEC_ROSOKHOVATSETS_SuccessfullyMatched(
        self,
    ) -> None:

        self.assertTrue(
            self.getStringEncoder().isEncodeEquals(
                "R o s o ch o w a c ie c", " R o s o k ho v a ts e ts"
            )
        )

    def testCompare_Surname_SZLAMAWICZ_SHLAMOVITZ_SuccessfullyMatched(self) -> None:

        self.assertTrue(
            self.getStringEncoder().isEncodeEquals("SZLAMAWICZ", "SHLAMOVITZ")
        )

    def testCompare_Surname_LEWINSKY_LEVINSKI_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("LEWINSKY", "LEVINSKI"))

    def testCompare_Surname_LIPSHITZ_LIPPSZYC_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("LIPSHITZ", "LIPPSZYC"))

    def testCompare_Surname_MOSKOWITZ_MOSKOVITZ_SuccessfullyMatched(self) -> None:

        self.assertTrue(
            self.getStringEncoder().isEncodeEquals("Moskowitz", "Moskovitz")
        )

    def testCompare_Surname_AUERBACH_UHRBACH_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("Auerbach", "Uhrbach"))

    def testCompare_Surname_HAILEY_HALLEY_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("Hailey", "Halley"))

    def testCompare_Surname_COOPERFLYNN_SUPERLYN_SuccessfullyMatched(self) -> None:

        self.assertTrue(
            self.getStringEncoder().isEncodeEquals("Cooper-Flynn", "Super-Lyn")
        )

    def testCompare_LongSurnames_OMUIRCHEARTAIGH_OMIREADHAIGH_SuccessfulMatch(
        self,
    ) -> None:

        self.assertTrue(
            self.getStringEncoder().isEncodeEquals(
                "o'muireadhaigh", "Ó 'Muircheartaigh "
            )
        )

    def testCompare_LongSurnames_MORIARTY_OMUIRCHEARTAIGH_DoesNotSuccessfulMatch(
        self,
    ) -> None:

        self.assertFalse(
            self.getStringEncoder().isEncodeEquals("Moriarty", "OMuircheartaigh")
        )

    def testCompare_Surname_OSULLIVAN_OSUILLEABHAIN_SuccessfulMatch(self) -> None:

        self.assertTrue(
            self.getStringEncoder().isEncodeEquals("O'Sullivan", "Ó ' Súilleabháin")
        )

    def testCompare_Forenames_UNA_OONAGH_ShouldSuccessfullyMatchButDoesNot(
        self,
    ) -> None:

        assert not self.getStringEncoder().isEncodeEquals("Úna", "Oonagh")

    def testCompare_KARL_ALESSANDRO_DoesNotMatch(self) -> None:

        self.assertFalse(self.getStringEncoder().isEncodeEquals("Karl", "Alessandro"))

    def testCompare_ZACH_ZAKARIA_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("Zach", "Zacharia"))

    def testCompareNameToSingleLetter_KARL_C_DoesNotMatch(self) -> None:

        self.assertFalse(self.getStringEncoder().isEncodeEquals("Karl", "C"))

    def testCompare_SmallInput_CARK_Kl_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("Kl", "Karl"))

    def testCompare_TOMASZ_TOM_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("Tomasz", "tom"))

    def testCompare_FRANCISZEK_FRANCES_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("Franciszek", "Frances"))

    def testCompare_SOPHIE_SOFIA_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("Sophie", "Sofia"))

    def testCompare_OONA_OONAGH_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("Oona", "Oonagh"))

    def testCompare_MICKY_MICHAEL_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("Micky", "Michael"))

    def testCompare_SAM_SAMUEL_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("Sam", "Samuel"))

    def testCompare_STEPHEN_STEFAN_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("Stephen", "Stefan"))

    def testCompare_STEVEN_STEFAN_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("Steven", "Stefan"))

    def testCompare_STEPHEN_STEVEN_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("Stephen", "Steven"))

    def testCompare_COLM_COLIN_WithAccentsAndSymbolsAndSpaces_SuccessfullyMatched(
        self,
    ) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("Cólm.   ", "C-olín"))

    def testCompare_SEAN_SHAUN_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("Séan", "Shaun"))

    def testCompare_BRIAN_BRYAN_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("Brian", "Bryan"))

    def testCompare_CATHERINE_KATHRYN_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("Catherine", "Kathryn"))

    def testCompare_ShortNames_AL_ED_WorksButNoMatch(self) -> None:

        self.assertFalse(self.getStringEncoder().isEncodeEquals("Al", "Ed"))

    def testCompare_BURNS_BOURNE_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("Burns", "Bourne"))

    def testCompare_SMITH_SMYTH_SuccessfullyMatched(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("smith", "smyth"))

    def testCompareNameSameNames_ReturnsFalseSuccessfully(self) -> None:

        self.assertTrue(self.getStringEncoder().isEncodeEquals("John", "John"))

    def testCompareNameNullSpace_ReturnsFalseSuccessfully(self) -> None:

        assert not self.getStringEncoder().isEncodeEquals(None, " ")

    def testGetEncoding_One_Letter_to_Nothing(self) -> None:

        pass  # LLM could not translate method body

    def testGetEncoding_Null_to_Nothing(self) -> None:

        self.assertEqual("", self.getStringEncoder().encode1(None))

    def testGetEncoding_NoSpace_to_Nothing(self) -> None:

        self.assertEqual("", self.getStringEncoder().encode1(""))

    def testGetEncoding_Space_to_Nothing(self) -> None:

        self.assertEqual("", self.encode1(" "))

    def testGetEncoding_SMYTH_to_SMYTH(self) -> None:

        self.assertEqual("SMYTH", self.getStringEncoder().encode1("Smyth"))

    def testGetEncoding_SMITH_to_SMTH(self) -> None:

        self.assertEqual(self.getStringEncoder().encode1("Smith"), "SMTH")

    def testGetEncoding_HARPER_HRPR(self) -> None:

        self.assertEqual(self.getStringEncoder().encode1("HARPER"), "HRPR")

    def testisEncodeEqualsSecondNameJust1Letter_ReturnsFalse(self) -> None:

        pass  # LLM could not translate method body

    def testisEncodeEquals_CornerCase_FirstNameJust1Letter_ReturnsFalse(self) -> None:

        self.assertFalse(self.getStringEncoder().isEncodeEquals("t", "test"))

    def testisEncodeEquals_CornerCase_FirstNameNull_ReturnsFalse(self) -> None:

        self.assertFalse(self.getStringEncoder().isEncodeEquals(None, "test"))

    def testisEncodeEquals_CornerCase_SecondNameNull_ReturnsFalse(self) -> None:

        self.assertFalse(self.getStringEncoder().isEncodeEquals("test", None))

    def testisEncodeEquals_CornerCase_FirstNameJustSpace_ReturnsFalse(self) -> None:

        pass  # LLM could not translate method body

    def testisEncodeEquals_CornerCase_SecondNameJustSpace_ReturnsFalse(self) -> None:

        pass  # LLM could not translate method body

    def testisEncodeEquals_CornerCase_FirstNameNothing_ReturnsFalse(self) -> None:

        pass  # LLM could not translate method body

    def testisEncodeEquals_CornerCase_SecondNameNothing_ReturnsFalse(self) -> None:

        self.assertFalse(self.getStringEncoder().isEncodeEquals("test", ""))

    def testisVowel_SingleVowel_ReturnsTrue(self) -> None:

        self.assertTrue(self.getStringEncoder().isVowel("I"))

    def testcleanName_SuccessfullyClean(self) -> None:

        pass  # LLM could not translate method body

    def testGetMinRating_13_Returns_1_Successfully(self) -> None:

        pass  # LLM could not translate method body

    def testgetMinRating_11_Returns_3_Successfully(self) -> None:

        pass  # LLM could not translate method body

    def testgetMinRating_10_Returns3_Successfully(self) -> None:

        pass  # LLM could not translate method body

    def testgetMinRating_8_Returns3_Successfully(self) -> None:

        pass  # LLM could not translate method body

    def testgetMinRating_7_Returns4_Successfully(self) -> None:

        pass  # LLM could not translate method body

    def testgetMinRating_6_Returns4_Successfully(self) -> None:

        pass  # LLM could not translate method body

    def testgetMinRating_5_Returns4_Successfully2(self) -> None:

        pass  # LLM could not translate method body

    def testgetMinRating_5_Returns4_Successfully(self) -> None:

        pass  # LLM could not translate method body

    def testGetMinRating_2_Returns5_Successfully(self) -> None:

        pass  # LLM could not translate method body

    def testGetMinRating_1_Returns5_Successfully(self) -> None:

        pass  # LLM could not translate method body

    def testGetMinRating_7_Return4_Successfully(self) -> None:

        pass  # LLM could not translate method body

    def testleftTorightThenRightToLeft_EINSTEIN_MICHAELA_Returns0(self) -> None:

        pass  # LLM could not translate method body

    def testleftTorightThenRightToLeft_ALEXANDER_ALEXANDRA_Returns4(self) -> None:

        self.assertEqual(
            4,
            self.getStringEncoder().leftToRightThenRightToLeftProcessing(
                "ALEXANDER", "ALEXANDRA"
            ),
        )

    def testGetFirstLast3_PETE_Returns_PETE(self) -> None:

        pass  # LLM could not translate method body

    def testGetFirstLast3__ALEXANDER_Returns_Aleder(self) -> None:

        pass  # LLM could not translate method body

    def testRemoveVowel__DECLAN_Returns_DCLN(self) -> None:

        pass  # LLM could not translate method body

    def testRemoveVowel__AIDAN_Returns_ADN(self) -> None:

        pass  # LLM could not translate method body

    def testRemoveVowel_ALESSANDRA_Returns_ALSSNDR(self) -> None:

        pass  # LLM could not translate method body

    def testIsVowel_SmallD_ReturnsFalse(self) -> None:

        pass  # LLM could not translate method body

    def testIsVowel_CapitalA_ReturnsTrue(self) -> None:

        self.assertTrue(self.getStringEncoder().isVowel("A"))

    def testRemoveDoubleDoubleVowel_BEETLE_NotRemoved(self) -> None:

        self.assertEqual(
            "BEETLE", self.getStringEncoder().removeDoubleConsonants("BEETLE")
        )

    def testRemoveDoubleConsonants_MISSISSIPPI_RemovedSuccessfully(self) -> None:

        self.assertEqual(
            self.getStringEncoder().removeDoubleConsonants("MISSISSIPPI"), "MISISIPI"
        )

    def testRemoveSingleDoubleConsonants_BUBLE_RemovedSuccessfully(self) -> None:

        self.assertEqual(
            self.getStringEncoder().removeDoubleConsonants("BUBBLE"), "BUBLE"
        )

    def testAccentRemoval_NullValue_ReturnNullSuccessfully(self) -> None:

        assert self.getStringEncoder().removeAccents(None) is None

    def testAccentRemoval_NINO_NoChange(self) -> None:

        self.assertEqual(self.getStringEncoder().removeAccents(""), "")

    def testAccentRemovalNormalString_NoChange(self) -> None:

        self.assertEqual(
            "Colorless green ideas sleep furiously",
            self.getStringEncoder().removeAccents(
                "Colorless green ideas sleep furiously"
            ),
        )

    def testAccentRemoval_ComprehensiveAccentMix_AllSuccessfullyRemoved(self) -> None:

        self.assertEqual(
            "E,E,E,E,U,U,I,I,A,A,O,e,e,e,e,u,u,i,i,a,a,o,c",
            self.getStringEncoder().removeAccents(
                "È,É,Ê,Ë,Û,Ù,Ï,Î,À,Â,Ô,è,é,ê,ë,û,ù,ï,î,à,â,ô,ç"
            ),
        )

    def testAccentRemoval_GerSpanFrenMix_SuccessfullyRemoved(self) -> None:

        self.assertEqual(
            "aeoußAEOUnNa", self.getStringEncoder().removeAccents("äëöüßÄËÖÜñÑà")
        )

    def testAccentRemoval_MixedWithUnusualChars_SuccessfullyRemovedAndUnusualcharactersInvariant(
        self,
    ) -> None:

        self.assertEqual(
            self.getStringEncoder().removeAccents("Á-e'í.,ó&ú"), "A-e'i.,o&u"
        )

    def testAccentRemoval_UpperandLower_SuccessfullyRemovedAndCaseInvariant(
        self,
    ) -> None:

        self.assertEqual("AeiOuu", self.getStringEncoder().removeAccents("ÁeíÓuu"))

    def testAccentRemoval_WithSpaces_SuccessfullyRemovedAndSpacesInvariant(
        self,
    ) -> None:

        self.assertEqual("ae io  u", self.getStringEncoder().removeAccents("áé íó  ú"))

    def testAccentRemoval_AllLower_SuccessfullyRemoved(self) -> None:

        pass  # LLM could not translate method body

    # Class Methods End
