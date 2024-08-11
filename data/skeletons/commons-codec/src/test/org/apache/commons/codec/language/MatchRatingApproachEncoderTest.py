from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.language.MatchRatingApproachEncoder import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.StringEncoder import *
import unittest
import os
import io

# Imports End


class MatchRatingApproachEncoderTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testCompare_Forenames_SEAN_PETE_NoMatchExpected_test1_decomposed(self) -> None:
        pass

    def testCompare_Forenames_SEAN_PETE_NoMatchExpected_test0_decomposed(self) -> None:
        pass

    def testCompare_Forenames_SEAN_JOHN_MatchExpected_test1_decomposed(self) -> None:
        pass

    def testCompare_Forenames_SEAN_JOHN_MatchExpected_test0_decomposed(self) -> None:
        pass

    def testCompare_Surnames_MURPHY_LYNCH_NoMatchExpected_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_Surnames_MURPHY_LYNCH_NoMatchExpected_test0_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_SurnameCornerCase_Nulls_NoMatch_test1_decomposed(self) -> None:
        pass

    def testCompare_SurnameCornerCase_Nulls_NoMatch_test0_decomposed(self) -> None:
        pass

    def testCompare_SurnamesCornerCase_MURPHY_NoSpace_NoMatch_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_SurnamesCornerCase_MURPHY_NoSpace_NoMatch_test0_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_SurnamesCornerCase_MURPHY_Space_NoMatch_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_SurnamesCornerCase_MURPHY_Space_NoMatch_test0_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_MCGOWAN_MCGEOGHEGAN_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_MCGOWAN_MCGEOGHEGAN_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_PETERSON_PETERS_SuccessfullyMatched_test1_decomposed(self) -> None:
        pass

    def testCompare_PETERSON_PETERS_SuccessfullyMatched_test0_decomposed(self) -> None:
        pass

    def testCompare_Surname_PRZEMYSL_PSHEMESHIL_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_Surname_PRZEMYSL_PSHEMESHIL_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_Surname_ROSOCHOWACIEC_ROSOKHOVATSETS_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_Surname_ROSOCHOWACIEC_ROSOKHOVATSETS_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_Surname_SZLAMAWICZ_SHLAMOVITZ_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_Surname_SZLAMAWICZ_SHLAMOVITZ_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_Surname_LEWINSKY_LEVINSKI_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_Surname_LEWINSKY_LEVINSKI_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_Surname_LIPSHITZ_LIPPSZYC_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_Surname_LIPSHITZ_LIPPSZYC_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_Surname_MOSKOWITZ_MOSKOVITZ_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_Surname_MOSKOWITZ_MOSKOVITZ_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_Surname_AUERBACH_UHRBACH_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_Surname_AUERBACH_UHRBACH_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_Surname_HAILEY_HALLEY_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_Surname_HAILEY_HALLEY_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_Surname_COOPERFLYNN_SUPERLYN_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_Surname_COOPERFLYNN_SUPERLYN_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_LongSurnames_OMUIRCHEARTAIGH_OMIREADHAIGH_SuccessfulMatch_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_LongSurnames_OMUIRCHEARTAIGH_OMIREADHAIGH_SuccessfulMatch_test0_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_LongSurnames_MORIARTY_OMUIRCHEARTAIGH_DoesNotSuccessfulMatch_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_LongSurnames_MORIARTY_OMUIRCHEARTAIGH_DoesNotSuccessfulMatch_test0_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_Surname_OSULLIVAN_OSUILLEABHAIN_SuccessfulMatch_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_Surname_OSULLIVAN_OSUILLEABHAIN_SuccessfulMatch_test0_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_Forenames_UNA_OONAGH_ShouldSuccessfullyMatchButDoesNot_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_Forenames_UNA_OONAGH_ShouldSuccessfullyMatchButDoesNot_test0_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_KARL_ALESSANDRO_DoesNotMatch_test1_decomposed(self) -> None:
        pass

    def testCompare_KARL_ALESSANDRO_DoesNotMatch_test0_decomposed(self) -> None:
        pass

    def testCompare_ZACH_ZAKARIA_SuccessfullyMatched_test1_decomposed(self) -> None:
        pass

    def testCompare_ZACH_ZAKARIA_SuccessfullyMatched_test0_decomposed(self) -> None:
        pass

    def testCompareNameToSingleLetter_KARL_C_DoesNotMatch_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompareNameToSingleLetter_KARL_C_DoesNotMatch_test0_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_SmallInput_CARK_Kl_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_SmallInput_CARK_Kl_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_TOMASZ_TOM_SuccessfullyMatched_test1_decomposed(self) -> None:
        pass

    def testCompare_TOMASZ_TOM_SuccessfullyMatched_test0_decomposed(self) -> None:
        pass

    def testCompare_FRANCISZEK_FRANCES_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_FRANCISZEK_FRANCES_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_SOPHIE_SOFIA_SuccessfullyMatched_test1_decomposed(self) -> None:
        pass

    def testCompare_SOPHIE_SOFIA_SuccessfullyMatched_test0_decomposed(self) -> None:
        pass

    def testCompare_OONA_OONAGH_SuccessfullyMatched_test1_decomposed(self) -> None:
        pass

    def testCompare_OONA_OONAGH_SuccessfullyMatched_test0_decomposed(self) -> None:
        pass

    def testCompare_MICKY_MICHAEL_SuccessfullyMatched_test1_decomposed(self) -> None:
        pass

    def testCompare_MICKY_MICHAEL_SuccessfullyMatched_test0_decomposed(self) -> None:
        pass

    def testCompare_SAM_SAMUEL_SuccessfullyMatched_test1_decomposed(self) -> None:
        pass

    def testCompare_SAM_SAMUEL_SuccessfullyMatched_test0_decomposed(self) -> None:
        pass

    def testCompare_STEPHEN_STEFAN_SuccessfullyMatched_test1_decomposed(self) -> None:
        pass

    def testCompare_STEPHEN_STEFAN_SuccessfullyMatched_test0_decomposed(self) -> None:
        pass

    def testCompare_STEVEN_STEFAN_SuccessfullyMatched_test1_decomposed(self) -> None:
        pass

    def testCompare_STEVEN_STEFAN_SuccessfullyMatched_test0_decomposed(self) -> None:
        pass

    def testCompare_STEPHEN_STEVEN_SuccessfullyMatched_test1_decomposed(self) -> None:
        pass

    def testCompare_STEPHEN_STEVEN_SuccessfullyMatched_test0_decomposed(self) -> None:
        pass

    def testCompare_COLM_COLIN_WithAccentsAndSymbolsAndSpaces_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_COLM_COLIN_WithAccentsAndSymbolsAndSpaces_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_SEAN_SHAUN_SuccessfullyMatched_test1_decomposed(self) -> None:
        pass

    def testCompare_SEAN_SHAUN_SuccessfullyMatched_test0_decomposed(self) -> None:
        pass

    def testCompare_BRIAN_BRYAN_SuccessfullyMatched_test1_decomposed(self) -> None:
        pass

    def testCompare_BRIAN_BRYAN_SuccessfullyMatched_test0_decomposed(self) -> None:
        pass

    def testCompare_CATHERINE_KATHRYN_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_CATHERINE_KATHRYN_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        pass

    def testCompare_ShortNames_AL_ED_WorksButNoMatch_test1_decomposed(self) -> None:
        pass

    def testCompare_ShortNames_AL_ED_WorksButNoMatch_test0_decomposed(self) -> None:
        pass

    def testCompare_BURNS_BOURNE_SuccessfullyMatched_test1_decomposed(self) -> None:
        pass

    def testCompare_BURNS_BOURNE_SuccessfullyMatched_test0_decomposed(self) -> None:
        pass

    def testCompare_SMITH_SMYTH_SuccessfullyMatched_test1_decomposed(self) -> None:
        pass

    def testCompare_SMITH_SMYTH_SuccessfullyMatched_test0_decomposed(self) -> None:
        pass

    def testCompareNameSameNames_ReturnsFalseSuccessfully_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompareNameSameNames_ReturnsFalseSuccessfully_test0_decomposed(
        self,
    ) -> None:
        pass

    def testCompareNameNullSpace_ReturnsFalseSuccessfully_test1_decomposed(
        self,
    ) -> None:
        pass

    def testCompareNameNullSpace_ReturnsFalseSuccessfully_test0_decomposed(
        self,
    ) -> None:
        pass

    def testGetEncoding_One_Letter_to_Nothing_test1_decomposed(self) -> None:
        pass

    def testGetEncoding_One_Letter_to_Nothing_test0_decomposed(self) -> None:
        pass

    def testGetEncoding_Null_to_Nothing_test1_decomposed(self) -> None:
        pass

    def testGetEncoding_Null_to_Nothing_test0_decomposed(self) -> None:
        pass

    def testGetEncoding_NoSpace_to_Nothing_test1_decomposed(self) -> None:
        pass

    def testGetEncoding_NoSpace_to_Nothing_test0_decomposed(self) -> None:
        pass

    def testGetEncoding_Space_to_Nothing_test1_decomposed(self) -> None:
        pass

    def testGetEncoding_Space_to_Nothing_test0_decomposed(self) -> None:
        pass

    def testGetEncoding_SMYTH_to_SMYTH_test1_decomposed(self) -> None:
        pass

    def testGetEncoding_SMYTH_to_SMYTH_test0_decomposed(self) -> None:
        pass

    def testGetEncoding_SMITH_to_SMTH_test1_decomposed(self) -> None:
        pass

    def testGetEncoding_SMITH_to_SMTH_test0_decomposed(self) -> None:
        pass

    def testGetEncoding_HARPER_HRPR_test1_decomposed(self) -> None:
        pass

    def testGetEncoding_HARPER_HRPR_test0_decomposed(self) -> None:
        pass

    def testisEncodeEqualsSecondNameJust1Letter_ReturnsFalse_test1_decomposed(
        self,
    ) -> None:
        pass

    def testisEncodeEqualsSecondNameJust1Letter_ReturnsFalse_test0_decomposed(
        self,
    ) -> None:
        pass

    def testisEncodeEquals_CornerCase_FirstNameJust1Letter_ReturnsFalse_test1_decomposed(
        self,
    ) -> None:
        pass

    def testisEncodeEquals_CornerCase_FirstNameJust1Letter_ReturnsFalse_test0_decomposed(
        self,
    ) -> None:
        pass

    def testisEncodeEquals_CornerCase_FirstNameNull_ReturnsFalse_test1_decomposed(
        self,
    ) -> None:
        pass

    def testisEncodeEquals_CornerCase_FirstNameNull_ReturnsFalse_test0_decomposed(
        self,
    ) -> None:
        pass

    def testisEncodeEquals_CornerCase_SecondNameNull_ReturnsFalse_test1_decomposed(
        self,
    ) -> None:
        pass

    def testisEncodeEquals_CornerCase_SecondNameNull_ReturnsFalse_test0_decomposed(
        self,
    ) -> None:
        pass

    def testisEncodeEquals_CornerCase_FirstNameJustSpace_ReturnsFalse_test1_decomposed(
        self,
    ) -> None:
        pass

    def testisEncodeEquals_CornerCase_FirstNameJustSpace_ReturnsFalse_test0_decomposed(
        self,
    ) -> None:
        pass

    def testisEncodeEquals_CornerCase_SecondNameJustSpace_ReturnsFalse_test1_decomposed(
        self,
    ) -> None:
        pass

    def testisEncodeEquals_CornerCase_SecondNameJustSpace_ReturnsFalse_test0_decomposed(
        self,
    ) -> None:
        pass

    def testisEncodeEquals_CornerCase_FirstNameNothing_ReturnsFalse_test1_decomposed(
        self,
    ) -> None:
        pass

    def testisEncodeEquals_CornerCase_FirstNameNothing_ReturnsFalse_test0_decomposed(
        self,
    ) -> None:
        pass

    def testisEncodeEquals_CornerCase_SecondNameNothing_ReturnsFalse_test1_decomposed(
        self,
    ) -> None:
        pass

    def testisEncodeEquals_CornerCase_SecondNameNothing_ReturnsFalse_test0_decomposed(
        self,
    ) -> None:
        pass

    def testisVowel_SingleVowel_ReturnsTrue_test1_decomposed(self) -> None:
        pass

    def testisVowel_SingleVowel_ReturnsTrue_test0_decomposed(self) -> None:
        pass

    def testcleanName_SuccessfullyClean_test1_decomposed(self) -> None:
        pass

    def testcleanName_SuccessfullyClean_test0_decomposed(self) -> None:
        pass

    def testGetMinRating_13_Returns_1_Successfully_test1_decomposed(self) -> None:
        pass

    def testGetMinRating_13_Returns_1_Successfully_test0_decomposed(self) -> None:
        pass

    def testgetMinRating_11_Returns_3_Successfully_test1_decomposed(self) -> None:
        pass

    def testgetMinRating_11_Returns_3_Successfully_test0_decomposed(self) -> None:
        pass

    def testgetMinRating_10_Returns3_Successfully_test1_decomposed(self) -> None:
        pass

    def testgetMinRating_10_Returns3_Successfully_test0_decomposed(self) -> None:
        pass

    def testgetMinRating_8_Returns3_Successfully_test1_decomposed(self) -> None:
        pass

    def testgetMinRating_8_Returns3_Successfully_test0_decomposed(self) -> None:
        pass

    def testgetMinRating_7_Returns4_Successfully_test1_decomposed(self) -> None:
        pass

    def testgetMinRating_7_Returns4_Successfully_test0_decomposed(self) -> None:
        pass

    def testgetMinRating_6_Returns4_Successfully_test1_decomposed(self) -> None:
        pass

    def testgetMinRating_6_Returns4_Successfully_test0_decomposed(self) -> None:
        pass

    def testgetMinRating_5_Returns4_Successfully2_test1_decomposed(self) -> None:
        pass

    def testgetMinRating_5_Returns4_Successfully2_test0_decomposed(self) -> None:
        pass

    def testgetMinRating_5_Returns4_Successfully_test1_decomposed(self) -> None:
        pass

    def testgetMinRating_5_Returns4_Successfully_test0_decomposed(self) -> None:
        pass

    def testGetMinRating_2_Returns5_Successfully_test1_decomposed(self) -> None:
        pass

    def testGetMinRating_2_Returns5_Successfully_test0_decomposed(self) -> None:
        pass

    def testGetMinRating_1_Returns5_Successfully_test1_decomposed(self) -> None:
        pass

    def testGetMinRating_1_Returns5_Successfully_test0_decomposed(self) -> None:
        pass

    def testGetMinRating_7_Return4_Successfully_test1_decomposed(self) -> None:
        pass

    def testGetMinRating_7_Return4_Successfully_test0_decomposed(self) -> None:
        pass

    def testleftTorightThenRightToLeft_EINSTEIN_MICHAELA_Returns0_test1_decomposed(
        self,
    ) -> None:
        pass

    def testleftTorightThenRightToLeft_EINSTEIN_MICHAELA_Returns0_test0_decomposed(
        self,
    ) -> None:
        pass

    def testleftTorightThenRightToLeft_ALEXANDER_ALEXANDRA_Returns4_test1_decomposed(
        self,
    ) -> None:
        pass

    def testleftTorightThenRightToLeft_ALEXANDER_ALEXANDRA_Returns4_test0_decomposed(
        self,
    ) -> None:
        pass

    def testGetFirstLast3_PETE_Returns_PETE_test1_decomposed(self) -> None:
        pass

    def testGetFirstLast3_PETE_Returns_PETE_test0_decomposed(self) -> None:
        pass

    def testGetFirstLast3__ALEXANDER_Returns_Aleder_test1_decomposed(self) -> None:
        pass

    def testGetFirstLast3__ALEXANDER_Returns_Aleder_test0_decomposed(self) -> None:
        pass

    def testRemoveVowel__DECLAN_Returns_DCLN_test1_decomposed(self) -> None:
        pass

    def testRemoveVowel__DECLAN_Returns_DCLN_test0_decomposed(self) -> None:
        pass

    def testRemoveVowel__AIDAN_Returns_ADN_test1_decomposed(self) -> None:
        pass

    def testRemoveVowel__AIDAN_Returns_ADN_test0_decomposed(self) -> None:
        pass

    def testRemoveVowel_ALESSANDRA_Returns_ALSSNDR_test1_decomposed(self) -> None:
        pass

    def testRemoveVowel_ALESSANDRA_Returns_ALSSNDR_test0_decomposed(self) -> None:
        pass

    def testIsVowel_SmallD_ReturnsFalse_test1_decomposed(self) -> None:
        pass

    def testIsVowel_SmallD_ReturnsFalse_test0_decomposed(self) -> None:
        pass

    def testIsVowel_CapitalA_ReturnsTrue_test1_decomposed(self) -> None:
        pass

    def testIsVowel_CapitalA_ReturnsTrue_test0_decomposed(self) -> None:
        pass

    def testRemoveDoubleDoubleVowel_BEETLE_NotRemoved_test1_decomposed(self) -> None:
        pass

    def testRemoveDoubleDoubleVowel_BEETLE_NotRemoved_test0_decomposed(self) -> None:
        pass

    def testRemoveDoubleConsonants_MISSISSIPPI_RemovedSuccessfully_test1_decomposed(
        self,
    ) -> None:
        pass

    def testRemoveDoubleConsonants_MISSISSIPPI_RemovedSuccessfully_test0_decomposed(
        self,
    ) -> None:
        pass

    def testRemoveSingleDoubleConsonants_BUBLE_RemovedSuccessfully_test1_decomposed(
        self,
    ) -> None:
        pass

    def testRemoveSingleDoubleConsonants_BUBLE_RemovedSuccessfully_test0_decomposed(
        self,
    ) -> None:
        pass

    def testAccentRemoval_NullValue_ReturnNullSuccessfully_test1_decomposed(
        self,
    ) -> None:
        pass

    def testAccentRemoval_NullValue_ReturnNullSuccessfully_test0_decomposed(
        self,
    ) -> None:
        pass

    def testAccentRemoval_NINO_NoChange_test1_decomposed(self) -> None:
        pass

    def testAccentRemoval_NINO_NoChange_test0_decomposed(self) -> None:
        pass

    def testAccentRemovalNormalString_NoChange_test1_decomposed(self) -> None:
        pass

    def testAccentRemovalNormalString_NoChange_test0_decomposed(self) -> None:
        pass

    def testAccentRemoval_ComprehensiveAccentMix_AllSuccessfullyRemoved_test1_decomposed(
        self,
    ) -> None:
        pass

    def testAccentRemoval_ComprehensiveAccentMix_AllSuccessfullyRemoved_test0_decomposed(
        self,
    ) -> None:
        pass

    def testAccentRemoval_GerSpanFrenMix_SuccessfullyRemoved_test1_decomposed(
        self,
    ) -> None:
        pass

    def testAccentRemoval_GerSpanFrenMix_SuccessfullyRemoved_test0_decomposed(
        self,
    ) -> None:
        pass

    def testAccentRemoval_MixedWithUnusualChars_SuccessfullyRemovedAndUnusualcharactersInvariant_test1_decomposed(
        self,
    ) -> None:
        pass

    def testAccentRemoval_MixedWithUnusualChars_SuccessfullyRemovedAndUnusualcharactersInvariant_test0_decomposed(
        self,
    ) -> None:
        pass

    def testAccentRemoval_UpperandLower_SuccessfullyRemovedAndCaseInvariant_test1_decomposed(
        self,
    ) -> None:
        pass

    def testAccentRemoval_UpperandLower_SuccessfullyRemovedAndCaseInvariant_test0_decomposed(
        self,
    ) -> None:
        pass

    def testAccentRemoval_WithSpaces_SuccessfullyRemovedAndSpacesInvariant_test1_decomposed(
        self,
    ) -> None:
        pass

    def testAccentRemoval_WithSpaces_SuccessfullyRemovedAndSpacesInvariant_test0_decomposed(
        self,
    ) -> None:
        pass

    def testAccentRemoval_AllLower_SuccessfullyRemoved_test1_decomposed(self) -> None:
        pass

    def testAccentRemoval_AllLower_SuccessfullyRemoved_test0_decomposed(self) -> None:
        pass

    def _createStringEncoder(self) -> MatchRatingApproachEncoder:
        pass

    # Class Methods End
