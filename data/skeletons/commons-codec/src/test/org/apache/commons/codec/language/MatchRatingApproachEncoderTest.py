# Imports Begin
from src.main.org.apache.commons.codec.language.MatchRatingApproachEncoder import *
from src.main.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.StringEncoder import *

# Imports End


class MatchRatingApproachEncoderTest:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def _createStringEncoder(self) -> MatchRatingApproachEncoder:
        pass

    def testCompare_Forenames_SEAN_PETE_NoMatchExpected(self) -> None:
        pass

    def testCompare_Forenames_SEAN_JOHN_MatchExpected(self) -> None:
        pass

    def testCompare_Surnames_MURPHY_LYNCH_NoMatchExpected(self) -> None:
        pass

    def testCompare_SurnameCornerCase_Nulls_NoMatch(self) -> None:
        pass

    def testCompare_SurnamesCornerCase_MURPHY_NoSpace_NoMatch(self) -> None:
        pass

    def testCompare_SurnamesCornerCase_MURPHY_Space_NoMatch(self) -> None:
        pass

    def testCompare_MCGOWAN_MCGEOGHEGAN_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_PETERSON_PETERS_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_Surname_PRZEMYSL_PSHEMESHIL_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_Surname_ROSOCHOWACIEC_ROSOKHOVATSETS_SuccessfullyMatched(
        self,
    ) -> None:
        pass

    def testCompare_Surname_SZLAMAWICZ_SHLAMOVITZ_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_Surname_LEWINSKY_LEVINSKI_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_Surname_LIPSHITZ_LIPPSZYC_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_Surname_MOSKOWITZ_MOSKOVITZ_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_Surname_AUERBACH_UHRBACH_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_Surname_HAILEY_HALLEY_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_Surname_COOPERFLYNN_SUPERLYN_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_LongSurnames_OMUIRCHEARTAIGH_OMIREADHAIGH_SuccessfulMatch(
        self,
    ) -> None:
        pass

    def testCompare_LongSurnames_MORIARTY_OMUIRCHEARTAIGH_DoesNotSuccessfulMatch(
        self,
    ) -> None:
        pass

    def testCompare_Surname_OSULLIVAN_OSUILLEABHAIN_SuccessfulMatch(self) -> None:
        pass

    def testCompare_Forenames_UNA_OONAGH_ShouldSuccessfullyMatchButDoesNot(
        self,
    ) -> None:
        pass

    def testCompare_KARL_ALESSANDRO_DoesNotMatch(self) -> None:
        pass

    def testCompare_ZACH_ZAKARIA_SuccessfullyMatched(self) -> None:
        pass

    def testCompareNameToSingleLetter_KARL_C_DoesNotMatch(self) -> None:
        pass

    def testCompare_SmallInput_CARK_Kl_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_TOMASZ_TOM_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_FRANCISZEK_FRANCES_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_SOPHIE_SOFIA_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_OONA_OONAGH_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_MICKY_MICHAEL_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_SAM_SAMUEL_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_STEPHEN_STEFAN_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_STEVEN_STEFAN_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_STEPHEN_STEVEN_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_COLM_COLIN_WithAccentsAndSymbolsAndSpaces_SuccessfullyMatched(
        self,
    ) -> None:
        pass

    def testCompare_SEAN_SHAUN_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_BRIAN_BRYAN_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_CATHERINE_KATHRYN_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_ShortNames_AL_ED_WorksButNoMatch(self) -> None:
        pass

    def testCompare_BURNS_BOURNE_SuccessfullyMatched(self) -> None:
        pass

    def testCompare_SMITH_SMYTH_SuccessfullyMatched(self) -> None:
        pass

    def testCompareNameSameNames_ReturnsFalseSuccessfully(self) -> None:
        pass

    def testCompareNameNullSpace_ReturnsFalseSuccessfully(self) -> None:
        pass

    def testGetEncoding_One_Letter_to_Nothing(self) -> None:
        pass

    def testGetEncoding_Null_to_Nothing(self) -> None:
        pass

    def testGetEncoding_NoSpace_to_Nothing(self) -> None:
        pass

    def testGetEncoding_Space_to_Nothing(self) -> None:
        pass

    def testGetEncoding_SMYTH_to_SMYTH(self) -> None:
        pass

    def testGetEncoding_SMITH_to_SMTH(self) -> None:
        pass

    def testGetEncoding_HARPER_HRPR(self) -> None:
        pass

    def testisEncodeEqualsSecondNameJust1Letter_ReturnsFalse(self) -> None:
        pass

    def testisEncodeEquals_CornerCase_FirstNameJust1Letter_ReturnsFalse(self) -> None:
        pass

    def testisEncodeEquals_CornerCase_FirstNameNull_ReturnsFalse(self) -> None:
        pass

    def testisEncodeEquals_CornerCase_SecondNameNull_ReturnsFalse(self) -> None:
        pass

    def testisEncodeEquals_CornerCase_FirstNameJustSpace_ReturnsFalse(self) -> None:
        pass

    def testisEncodeEquals_CornerCase_SecondNameJustSpace_ReturnsFalse(self) -> None:
        pass

    def testisEncodeEquals_CornerCase_FirstNameNothing_ReturnsFalse(self) -> None:
        pass

    def testisEncodeEquals_CornerCase_SecondNameNothing_ReturnsFalse(self) -> None:
        pass

    def testisVowel_SingleVowel_ReturnsTrue(self) -> None:
        pass

    def testcleanName_SuccessfullyClean(self) -> None:
        pass

    def testGetMinRating_13_Returns_1_Successfully(self) -> None:
        pass

    def testgetMinRating_11_Returns_3_Successfully(self) -> None:
        pass

    def testgetMinRating_10_Returns3_Successfully(self) -> None:
        pass

    def testgetMinRating_8_Returns3_Successfully(self) -> None:
        pass

    def testgetMinRating_7_Returns4_Successfully(self) -> None:
        pass

    def testgetMinRating_6_Returns4_Successfully(self) -> None:
        pass

    def testgetMinRating_5_Returns4_Successfully2(self) -> None:
        pass

    def testgetMinRating_5_Returns4_Successfully(self) -> None:
        pass

    def testGetMinRating_2_Returns5_Successfully(self) -> None:
        pass

    def testGetMinRating_1_Returns5_Successfully(self) -> None:
        pass

    def testGetMinRating_7_Return4_Successfully(self) -> None:
        pass

    def testleftTorightThenRightToLeft_EINSTEIN_MICHAELA_Returns0(self) -> None:
        pass

    def testleftTorightThenRightToLeft_ALEXANDER_ALEXANDRA_Returns4(self) -> None:
        pass

    def testGetFirstLast3_PETE_Returns_PETE(self) -> None:
        pass

    def testGetFirstLast3__ALEXANDER_Returns_Aleder(self) -> None:
        pass

    def testRemoveVowel__DECLAN_Returns_DCLN(self) -> None:
        pass

    def testRemoveVowel__AIDAN_Returns_ADN(self) -> None:
        pass

    def testRemoveVowel_ALESSANDRA_Returns_ALSSNDR(self) -> None:
        pass

    def testIsVowel_SmallD_ReturnsFalse(self) -> None:
        pass

    def testIsVowel_CapitalA_ReturnsTrue(self) -> None:
        pass

    def testRemoveDoubleDoubleVowel_BEETLE_NotRemoved(self) -> None:
        pass

    def testRemoveDoubleConsonants_MISSISSIPPI_RemovedSuccessfully(self) -> None:
        pass

    def testRemoveSingleDoubleConsonants_BUBLE_RemovedSuccessfully(self) -> None:
        pass

    def testAccentRemoval_NullValue_ReturnNullSuccessfully(self) -> None:
        pass

    def testAccentRemoval_NINO_NoChange(self) -> None:
        pass

    def testAccentRemovalNormalString_NoChange(self) -> None:
        pass

    def testAccentRemoval_ComprehensiveAccentMix_AllSuccessfullyRemoved(self) -> None:
        pass

    def testAccentRemoval_GerSpanFrenMix_SuccessfullyRemoved(self) -> None:
        pass

    def testAccentRemoval_MixedWithUnusualChars_SuccessfullyRemovedAndUnusualcharactersInvariant(
        self,
    ) -> None:
        pass

    def testAccentRemoval_UpperandLower_SuccessfullyRemovedAndCaseInvariant(
        self,
    ) -> None:
        pass

    def testAccentRemoval_WithSpaces_SuccessfullyRemovedAndSpacesInvariant(
        self,
    ) -> None:
        pass

    def testAccentRemoval_AllLower_SuccessfullyRemoved(self) -> None:
        pass

    # Class Methods End
