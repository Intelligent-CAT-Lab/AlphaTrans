/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.commons.codec.language;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;

import org.apache.commons.codec.StringEncoderAbstractTest;
import org.junit.Test;

/**
 * Series of tests for the Match Rating Approach algorithm.
 *
 * <p>General naming nomenclature for the test is of the form:
 * GeneralMetadataOnTheTestArea_ActualTestValues_ExpectedResult
 *
 * <p>An unusual value is indicated by the term "corner case"
 */
public class MatchRatingApproachEncoderTest
        extends StringEncoderAbstractTest<MatchRatingApproachEncoder> {

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    @Override
    protected MatchRatingApproachEncoder createStringEncoder() {
        return new MatchRatingApproachEncoder();
    }

    @Test
    public void testAccentRemoval_AllLower_SuccessfullyRemoved_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testAccentRemoval_AllLower_SuccessfullyRemoved_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("aeiou", this.getStringEncoder().removeAccents("áéíóú"));
    }

    @Test
    public void testAccentRemoval_WithSpaces_SuccessfullyRemovedAndSpacesInvariant_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testAccentRemoval_WithSpaces_SuccessfullyRemovedAndSpacesInvariant_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("ae io  u", this.getStringEncoder().removeAccents("áé íó  ú"));
    }

    @Test
    public void testAccentRemoval_UpperandLower_SuccessfullyRemovedAndCaseInvariant_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testAccentRemoval_UpperandLower_SuccessfullyRemovedAndCaseInvariant_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("AeiOuu", this.getStringEncoder().removeAccents("ÁeíÓuu"));
    }

    @Test
    public void testAccentRemoval_MixedWithUnusualChars_SuccessfullyRemovedAndUnusualcharactersInvariant_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testAccentRemoval_MixedWithUnusualChars_SuccessfullyRemovedAndUnusualcharactersInvariant_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("A-e'i.,o&u", this.getStringEncoder().removeAccents("Á-e'í.,ó&ú"));
    }

    @Test
    public void testAccentRemoval_GerSpanFrenMix_SuccessfullyRemoved_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testAccentRemoval_GerSpanFrenMix_SuccessfullyRemoved_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("aeoußAEOUnNa", this.getStringEncoder().removeAccents("äëöüßÄËÖÜñÑà"));
    }

    @Test
    public void testAccentRemoval_ComprehensiveAccentMix_AllSuccessfullyRemoved_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testAccentRemoval_ComprehensiveAccentMix_AllSuccessfullyRemoved_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals(
                "E,E,E,E,U,U,I,I,A,A,O,e,e,e,e,u,u,i,i,a,a,o,c",
                this.getStringEncoder()
                        .removeAccents("È,É,Ê,Ë,Û,Ù,Ï,Î,À,Â,Ô,è,é,ê,ë,û,ù,ï,î,à,â,ô,ç"));
    }

    @Test
    public void testAccentRemovalNormalString_NoChange_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testAccentRemovalNormalString_NoChange_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals(
                "Colorless green ideas sleep furiously",
                this.getStringEncoder().removeAccents("Colorless green ideas sleep furiously"));
    }

    @Test
    public void testAccentRemoval_NINO_NoChange_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testAccentRemoval_NINO_NoChange_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("", this.getStringEncoder().removeAccents(""));
    }

    @Test
    public void testAccentRemoval_NullValue_ReturnNullSuccessfully_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testAccentRemoval_NullValue_ReturnNullSuccessfully_test1_decomposed()  {
        this.getStringEncoder();
        assertNull(this.getStringEncoder().removeAccents(null));
    }

    @Test
    public void testRemoveSingleDoubleConsonants_BUBLE_RemovedSuccessfully_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testRemoveSingleDoubleConsonants_BUBLE_RemovedSuccessfully_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("BUBLE", this.getStringEncoder().removeDoubleConsonants("BUBBLE"));
    }

    @Test
    public void testRemoveDoubleConsonants_MISSISSIPPI_RemovedSuccessfully_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testRemoveDoubleConsonants_MISSISSIPPI_RemovedSuccessfully_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("MISISIPI", this.getStringEncoder().removeDoubleConsonants("MISSISSIPPI"));
    }

    @Test
    public void testRemoveDoubleDoubleVowel_BEETLE_NotRemoved_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testRemoveDoubleDoubleVowel_BEETLE_NotRemoved_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("BEETLE", this.getStringEncoder().removeDoubleConsonants("BEETLE"));
    }

    @Test
    public void testIsVowel_CapitalA_ReturnsTrue_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testIsVowel_CapitalA_ReturnsTrue_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isVowel("A"));
    }

    @Test
    public void testIsVowel_SmallD_ReturnsFalse_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testIsVowel_SmallD_ReturnsFalse_test1_decomposed()  {
        this.getStringEncoder();
        assertFalse(this.getStringEncoder().isVowel("d"));
    }

    @Test
    public void testRemoveVowel_ALESSANDRA_Returns_ALSSNDR_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testRemoveVowel_ALESSANDRA_Returns_ALSSNDR_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("ALSSNDR", this.getStringEncoder().removeVowels("ALESSANDRA"));
    }

    @Test
    public void testRemoveVowel__AIDAN_Returns_ADN_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testRemoveVowel__AIDAN_Returns_ADN_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("ADN", this.getStringEncoder().removeVowels("AIDAN"));
    }

    @Test
    public void testRemoveVowel__DECLAN_Returns_DCLN_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testRemoveVowel__DECLAN_Returns_DCLN_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("DCLN", this.getStringEncoder().removeVowels("DECLAN"));
    }

    @Test
    public void testGetFirstLast3__ALEXANDER_Returns_Aleder_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testGetFirstLast3__ALEXANDER_Returns_Aleder_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("Aleder", this.getStringEncoder().getFirst3Last3("Alexzander"));
    }

    @Test
    public void testGetFirstLast3_PETE_Returns_PETE_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testGetFirstLast3_PETE_Returns_PETE_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("PETE", this.getStringEncoder().getFirst3Last3("PETE"));
    }

    @Test
    public void testleftTorightThenRightToLeft_ALEXANDER_ALEXANDRA_Returns4_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testleftTorightThenRightToLeft_ALEXANDER_ALEXANDRA_Returns4_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals(
                4,
                this.getStringEncoder()
                        .leftToRightThenRightToLeftProcessing("ALEXANDER", "ALEXANDRA"));
    }

    @Test
    public void testleftTorightThenRightToLeft_EINSTEIN_MICHAELA_Returns0_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testleftTorightThenRightToLeft_EINSTEIN_MICHAELA_Returns0_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals(
                0,
                this.getStringEncoder()
                        .leftToRightThenRightToLeftProcessing("EINSTEIN", "MICHAELA"));
    }

    @Test
    public void testGetMinRating_7_Return4_Successfully_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testGetMinRating_7_Return4_Successfully_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals(4, this.getStringEncoder().getMinRating(7));
    }

    @Test
    public void testGetMinRating_1_Returns5_Successfully_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testGetMinRating_1_Returns5_Successfully_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals(5, this.getStringEncoder().getMinRating(1));
    }

    @Test
    public void testGetMinRating_2_Returns5_Successfully_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testGetMinRating_2_Returns5_Successfully_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals(5, this.getStringEncoder().getMinRating(2));
    }

    @Test
    public void testgetMinRating_5_Returns4_Successfully_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testgetMinRating_5_Returns4_Successfully_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals(4, this.getStringEncoder().getMinRating(5));
    }

    @Test
    public void testgetMinRating_5_Returns4_Successfully2_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testgetMinRating_5_Returns4_Successfully2_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals(4, this.getStringEncoder().getMinRating(5));
    }

    @Test
    public void testgetMinRating_6_Returns4_Successfully_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testgetMinRating_6_Returns4_Successfully_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals(4, this.getStringEncoder().getMinRating(6));
    }

    @Test
    public void testgetMinRating_7_Returns4_Successfully_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testgetMinRating_7_Returns4_Successfully_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals(4, this.getStringEncoder().getMinRating(7));
    }

    @Test
    public void testgetMinRating_8_Returns3_Successfully_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testgetMinRating_8_Returns3_Successfully_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals(3, this.getStringEncoder().getMinRating(8));
    }

    @Test
    public void testgetMinRating_10_Returns3_Successfully_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testgetMinRating_10_Returns3_Successfully_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals(3, this.getStringEncoder().getMinRating(10));
    }

    @Test
    public void testgetMinRating_11_Returns_3_Successfully_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testgetMinRating_11_Returns_3_Successfully_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals(3, this.getStringEncoder().getMinRating(11));
    }

    @Test
    public void testGetMinRating_13_Returns_1_Successfully_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testGetMinRating_13_Returns_1_Successfully_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals(1, this.getStringEncoder().getMinRating(13));
    }

    @Test
    public void testcleanName_SuccessfullyClean_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testcleanName_SuccessfullyClean_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("THISISATEST", this.getStringEncoder().cleanName("This-ís   a t.,es &t"));
    }

    @Test
    public void testisVowel_SingleVowel_ReturnsTrue_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testisVowel_SingleVowel_ReturnsTrue_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isVowel(("I")));
    }

    @Test
    public void testisEncodeEquals_CornerCase_SecondNameNothing_ReturnsFalse_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testisEncodeEquals_CornerCase_SecondNameNothing_ReturnsFalse_test1_decomposed()  {
        this.getStringEncoder();
        assertFalse(this.getStringEncoder().isEncodeEquals("test", ""));
    }

    @Test
    public void testisEncodeEquals_CornerCase_FirstNameNothing_ReturnsFalse_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testisEncodeEquals_CornerCase_FirstNameNothing_ReturnsFalse_test1_decomposed()  {
        this.getStringEncoder();
        assertFalse(this.getStringEncoder().isEncodeEquals("", "test"));
    }

    @Test
    public void testisEncodeEquals_CornerCase_SecondNameJustSpace_ReturnsFalse_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testisEncodeEquals_CornerCase_SecondNameJustSpace_ReturnsFalse_test1_decomposed()  {
        this.getStringEncoder();
        assertFalse(this.getStringEncoder().isEncodeEquals("test", " "));
    }

    @Test
    public void testisEncodeEquals_CornerCase_FirstNameJustSpace_ReturnsFalse_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testisEncodeEquals_CornerCase_FirstNameJustSpace_ReturnsFalse_test1_decomposed()  {
        this.getStringEncoder();
        assertFalse(this.getStringEncoder().isEncodeEquals(" ", "test"));
    }

    @Test
    public void testisEncodeEquals_CornerCase_SecondNameNull_ReturnsFalse_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testisEncodeEquals_CornerCase_SecondNameNull_ReturnsFalse_test1_decomposed()  {
        this.getStringEncoder();
        assertFalse(this.getStringEncoder().isEncodeEquals("test", null));
    }

    @Test
    public void testisEncodeEquals_CornerCase_FirstNameNull_ReturnsFalse_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testisEncodeEquals_CornerCase_FirstNameNull_ReturnsFalse_test1_decomposed()  {
        this.getStringEncoder();
        assertFalse(this.getStringEncoder().isEncodeEquals(null, "test"));
    }

    @Test
    public void testisEncodeEquals_CornerCase_FirstNameJust1Letter_ReturnsFalse_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testisEncodeEquals_CornerCase_FirstNameJust1Letter_ReturnsFalse_test1_decomposed()  {
        this.getStringEncoder();
        assertFalse(this.getStringEncoder().isEncodeEquals("t", "test"));
    }

    @Test
    public void testisEncodeEqualsSecondNameJust1Letter_ReturnsFalse_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testisEncodeEqualsSecondNameJust1Letter_ReturnsFalse_test1_decomposed()  {
        this.getStringEncoder();
        assertFalse(this.getStringEncoder().isEncodeEquals("test", "t"));
    }

    @Test
    public void testGetEncoding_HARPER_HRPR_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testGetEncoding_HARPER_HRPR_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("HRPR", this.getStringEncoder().encode1("HARPER"));
    }

    @Test
    public void testGetEncoding_SMITH_to_SMTH_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testGetEncoding_SMITH_to_SMTH_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("SMTH", this.getStringEncoder().encode1("Smith"));
    }

    @Test
    public void testGetEncoding_SMYTH_to_SMYTH_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testGetEncoding_SMYTH_to_SMYTH_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("SMYTH", this.getStringEncoder().encode1("Smyth"));
    }

    @Test
    public void testGetEncoding_Space_to_Nothing_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testGetEncoding_Space_to_Nothing_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("", this.getStringEncoder().encode1(" "));
    }

    @Test
    public void testGetEncoding_NoSpace_to_Nothing_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testGetEncoding_NoSpace_to_Nothing_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("", this.getStringEncoder().encode1(""));
    }

    @Test
    public void testGetEncoding_Null_to_Nothing_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testGetEncoding_Null_to_Nothing_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("", this.getStringEncoder().encode1(null));
    }

    @Test
    public void testGetEncoding_One_Letter_to_Nothing_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testGetEncoding_One_Letter_to_Nothing_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("", this.getStringEncoder().encode1("E"));
    }

    @Test
    public void testCompareNameNullSpace_ReturnsFalseSuccessfully_test0_decomposed()  {
        getStringEncoder();
    }

    @Test
    public void testCompareNameNullSpace_ReturnsFalseSuccessfully_test1_decomposed()  {
        getStringEncoder();
        assertFalse(getStringEncoder().isEncodeEquals(null, " "));
    }

    @Test
    public void testCompareNameSameNames_ReturnsFalseSuccessfully_test0_decomposed()  {
        getStringEncoder();
    }

    @Test
    public void testCompareNameSameNames_ReturnsFalseSuccessfully_test1_decomposed()  {
        getStringEncoder();
        assertTrue(getStringEncoder().isEncodeEquals("John", "John"));
    }

    @Test
    public void testCompare_SMITH_SMYTH_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_SMITH_SMYTH_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("smith", "smyth"));
    }

    @Test
    public void testCompare_BURNS_BOURNE_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_BURNS_BOURNE_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("Burns", "Bourne"));
    }

    @Test
    public void testCompare_ShortNames_AL_ED_WorksButNoMatch_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_ShortNames_AL_ED_WorksButNoMatch_test1_decomposed()  {
        this.getStringEncoder();
        assertFalse(this.getStringEncoder().isEncodeEquals("Al", "Ed"));
    }

    @Test
    public void testCompare_CATHERINE_KATHRYN_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_CATHERINE_KATHRYN_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("Catherine", "Kathryn"));
    }

    @Test
    public void testCompare_BRIAN_BRYAN_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_BRIAN_BRYAN_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("Brian", "Bryan"));
    }

    @Test
    public void testCompare_SEAN_SHAUN_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_SEAN_SHAUN_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("Séan", "Shaun"));
    }

    @Test
    public void testCompare_COLM_COLIN_WithAccentsAndSymbolsAndSpaces_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_COLM_COLIN_WithAccentsAndSymbolsAndSpaces_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("Cólm.   ", "C-olín"));
    }

    @Test
    public void testCompare_STEPHEN_STEVEN_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_STEPHEN_STEVEN_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("Stephen", "Steven"));
    }

    @Test
    public void testCompare_STEVEN_STEFAN_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_STEVEN_STEFAN_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("Steven", "Stefan"));
    }

    @Test
    public void testCompare_STEPHEN_STEFAN_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_STEPHEN_STEFAN_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("Stephen", "Stefan"));
    }

    @Test
    public void testCompare_SAM_SAMUEL_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_SAM_SAMUEL_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("Sam", "Samuel"));
    }

    @Test
    public void testCompare_MICKY_MICHAEL_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_MICKY_MICHAEL_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("Micky", "Michael"));
    }

    @Test
    public void testCompare_OONA_OONAGH_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_OONA_OONAGH_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("Oona", "Oonagh"));
    }

    @Test
    public void testCompare_SOPHIE_SOFIA_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_SOPHIE_SOFIA_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("Sophie", "Sofia"));
    }

    @Test
    public void testCompare_FRANCISZEK_FRANCES_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_FRANCISZEK_FRANCES_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("Franciszek", "Frances"));
    }

    @Test
    public void testCompare_TOMASZ_TOM_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_TOMASZ_TOM_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("Tomasz", "tom"));
    }

    @Test
    public void testCompare_SmallInput_CARK_Kl_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_SmallInput_CARK_Kl_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("Kl", "Karl"));
    }

    @Test
    public void testCompareNameToSingleLetter_KARL_C_DoesNotMatch_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompareNameToSingleLetter_KARL_C_DoesNotMatch_test1_decomposed()  {
        this.getStringEncoder();
        assertFalse(this.getStringEncoder().isEncodeEquals("Karl", "C"));
    }

    @Test
    public void testCompare_ZACH_ZAKARIA_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_ZACH_ZAKARIA_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("Zach", "Zacharia"));
    }

    @Test
    public void testCompare_KARL_ALESSANDRO_DoesNotMatch_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_KARL_ALESSANDRO_DoesNotMatch_test1_decomposed()  {
        this.getStringEncoder();
        assertFalse(this.getStringEncoder().isEncodeEquals("Karl", "Alessandro"));
    }

    @Test
    public void testCompare_Forenames_UNA_OONAGH_ShouldSuccessfullyMatchButDoesNot_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_Forenames_UNA_OONAGH_ShouldSuccessfullyMatchButDoesNot_test1_decomposed()  {
        this.getStringEncoder();
        assertFalse(this.getStringEncoder().isEncodeEquals("Úna", "Oonagh"));
    }

    @Test
    public void testCompare_Surname_OSULLIVAN_OSUILLEABHAIN_SuccessfulMatch_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_Surname_OSULLIVAN_OSUILLEABHAIN_SuccessfulMatch_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("O'Sullivan", "Ó ' Súilleabháin"));
    }

    @Test
    public void testCompare_LongSurnames_MORIARTY_OMUIRCHEARTAIGH_DoesNotSuccessfulMatch_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_LongSurnames_MORIARTY_OMUIRCHEARTAIGH_DoesNotSuccessfulMatch_test1_decomposed()  {
        this.getStringEncoder();
        assertFalse(this.getStringEncoder().isEncodeEquals("Moriarty", "OMuircheartaigh"));
    }

    @Test
    public void testCompare_LongSurnames_OMUIRCHEARTAIGH_OMIREADHAIGH_SuccessfulMatch_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_LongSurnames_OMUIRCHEARTAIGH_OMIREADHAIGH_SuccessfulMatch_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("o'muireadhaigh", "Ó 'Muircheartaigh "));
    }

    @Test
    public void testCompare_Surname_COOPERFLYNN_SUPERLYN_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_Surname_COOPERFLYNN_SUPERLYN_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("Cooper-Flynn", "Super-Lyn"));
    }

    @Test
    public void testCompare_Surname_HAILEY_HALLEY_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_Surname_HAILEY_HALLEY_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("Hailey", "Halley"));
    }

    @Test
    public void testCompare_Surname_AUERBACH_UHRBACH_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_Surname_AUERBACH_UHRBACH_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("Auerbach", "Uhrbach"));
    }

    @Test
    public void testCompare_Surname_MOSKOWITZ_MOSKOVITZ_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_Surname_MOSKOWITZ_MOSKOVITZ_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("Moskowitz", "Moskovitz"));
    }

    @Test
    public void testCompare_Surname_LIPSHITZ_LIPPSZYC_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_Surname_LIPSHITZ_LIPPSZYC_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("LIPSHITZ", "LIPPSZYC"));
    }

    @Test
    public void testCompare_Surname_LEWINSKY_LEVINSKI_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_Surname_LEWINSKY_LEVINSKI_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("LEWINSKY", "LEVINSKI"));
    }

    @Test
    public void testCompare_Surname_SZLAMAWICZ_SHLAMOVITZ_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_Surname_SZLAMAWICZ_SHLAMOVITZ_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("SZLAMAWICZ", "SHLAMOVITZ"));
    }

    @Test
    public void testCompare_Surname_ROSOCHOWACIEC_ROSOKHOVATSETS_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_Surname_ROSOCHOWACIEC_ROSOKHOVATSETS_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(
                this.getStringEncoder()
                        .isEncodeEquals("R o s o ch o w a c ie c", " R o s o k ho v a ts e ts"));
    }

    @Test
    public void testCompare_Surname_PRZEMYSL_PSHEMESHIL_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_Surname_PRZEMYSL_PSHEMESHIL_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals(" P rz e m y s l", " P sh e m e sh i l"));
    }

    @Test
    public void testCompare_PETERSON_PETERS_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_PETERSON_PETERS_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("Peterson", "Peters"));
    }

    @Test
    public void testCompare_MCGOWAN_MCGEOGHEGAN_SuccessfullyMatched_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_MCGOWAN_MCGEOGHEGAN_SuccessfullyMatched_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("McGowan", "Mc Geoghegan"));
    }

    @Test
    public void testCompare_SurnamesCornerCase_MURPHY_Space_NoMatch_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_SurnamesCornerCase_MURPHY_Space_NoMatch_test1_decomposed()  {
        this.getStringEncoder();
        assertFalse(this.getStringEncoder().isEncodeEquals("Murphy", " "));
    }

    @Test
    public void testCompare_SurnamesCornerCase_MURPHY_NoSpace_NoMatch_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_SurnamesCornerCase_MURPHY_NoSpace_NoMatch_test1_decomposed()  {
        this.getStringEncoder();
        assertFalse(this.getStringEncoder().isEncodeEquals("Murphy", ""));
    }

    @Test
    public void testCompare_SurnameCornerCase_Nulls_NoMatch_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_SurnameCornerCase_Nulls_NoMatch_test1_decomposed()  {
        this.getStringEncoder();
        assertFalse(this.getStringEncoder().isEncodeEquals(null, null));
    }

    @Test
    public void testCompare_Surnames_MURPHY_LYNCH_NoMatchExpected_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_Surnames_MURPHY_LYNCH_NoMatchExpected_test1_decomposed()  {
        this.getStringEncoder();
        assertFalse(this.getStringEncoder().isEncodeEquals("Murphy", "Lynch"));
    }

    @Test
    public void testCompare_Forenames_SEAN_JOHN_MatchExpected_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_Forenames_SEAN_JOHN_MatchExpected_test1_decomposed()  {
        this.getStringEncoder();
        assertTrue(this.getStringEncoder().isEncodeEquals("Sean", "John"));
    }

    @Test
    public void testCompare_Forenames_SEAN_PETE_NoMatchExpected_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testCompare_Forenames_SEAN_PETE_NoMatchExpected_test1_decomposed()  {
        this.getStringEncoder();
        assertFalse(this.getStringEncoder().isEncodeEquals("Sean", "Pete"));
    }
}