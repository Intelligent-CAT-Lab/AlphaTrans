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
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import org.apache.commons.codec.StringEncoderAbstractTest;
import org.junit.Test;

/** */
public class MetaphoneTest extends StringEncoderAbstractTest<Metaphone> {

    public void assertIsMetaphoneEqual(final String source, final String[] matches) {
        for (final String matche : matches) {
            assertTrue(
                    "Source: " + source + ", should have same Metaphone as: " + matche,
                    this.getStringEncoder().isMetaphoneEqual(source, matche));
        }
        for (final String matche : matches) {
            for (final String matche2 : matches) {
                assertTrue(this.getStringEncoder().isMetaphoneEqual(matche, matche2));
            }
        }
    }

    public void assertMetaphoneEqual(final String[][] pairs) {
        this.validateFixture(pairs);
        for (final String[] pair : pairs) {
            final String name0 = pair[0];
            final String name1 = pair[1];
            final String failMsg = "Expected match between " + name0 + " and " + name1;
            assertTrue(failMsg, this.getStringEncoder().isMetaphoneEqual(name0, name1));
            assertTrue(failMsg, this.getStringEncoder().isMetaphoneEqual(name1, name0));
        }
    }

    @Override
    protected Metaphone createStringEncoder() {
        return new Metaphone();
    }

    

    /** Matches computed from http://www.lanw.com/java/phonetic/default.htm */
    

    /**
     * Initial AE case.
     *
     * <p>Match data computed from http://www.lanw.com/java/phonetic/default.htm
     */
    

    /**
     * Initial WH case.
     *
     * <p>Match data computed from http://www.lanw.com/java/phonetic/default.htm
     */
    

    /**
     * Initial A, not followed by an E case.
     *
     * <p>Match data computed from http://www.lanw.com/java/phonetic/default.htm
     */
    

    /** Match data computed from http://www.lanw.com/java/phonetic/default.htm */
    

    /** Match data computed from http://www.lanw.com/java/phonetic/default.htm */
    

    /**
     * Initial KN case.
     *
     * <p>Match data computed from http://www.lanw.com/java/phonetic/default.htm
     */
    

    /** Match data computed from http://www.lanw.com/java/phonetic/default.htm */
    

    /** Match data computed from http://www.lanw.com/java/phonetic/default.htm */
    

    /** Match data computed from http://www.lanw.com/java/phonetic/default.htm */
    

    /** Match data computed from http://www.lanw.com/java/phonetic/default.htm */
    

    /** Match data computed from http://www.lanw.com/java/phonetic/default.htm */
    

    /**
     * Initial WR case.
     *
     * <p>Match data computed from http://www.lanw.com/java/phonetic/default.htm
     */
    

    /** Match data computed from http://www.lanw.com/java/phonetic/default.htm */
    

    

    

    

    /**
     * Tests (CODEC-57) Metaphone.metaphone(String) returns an empty string when passed the word
     * "why"
     */
    

    

    

    

    

    

    

    

    

    

    

    

    public void validateFixture(final String[][] pairs) {
        if (pairs.length == 0) {
            fail("Test fixture is empty");
        }
        for (int i = 0; i < pairs.length; i++) {
            if (pairs[i].length != 2) {
                fail("Error in test fixture in the data array at index " + i);
            }
        }
    }

    @Test
    public void testIsMetaphoneEqual1_test0_decomposed()  {
        this.assertMetaphoneEqual(
                new String[][] {
                    {"Case", "case"}, {"CASE", "Case"}, {"caSe", "cAsE"}, {"quick", "cookie"}
                });
    }

    @Test
    public void testIsMetaphoneEqual2_test0_decomposed()  {
        this.assertMetaphoneEqual(
                new String[][] {
                    {"Lawrence", "Lorenza"}, {"Gary", "Cahra"},
                });
    }

    @Test
    public void testIsMetaphoneEqualAero_test0_decomposed()  {
        this.assertIsMetaphoneEqual("Aero", new String[] {"Eure"});
    }

    @Test
    public void testIsMetaphoneEqualWhite_test0_decomposed()  {
        this.assertIsMetaphoneEqual(
                "White",
                new String[] {
                    "Wade", "Wait", "Waite", "Wat", "Whit", "Wiatt", "Wit", "Wittie", "Witty",
                    "Wood", "Woodie", "Woody"
                });
    }

    @Test
    public void testIsMetaphoneEqualAlbert_test0_decomposed()  {
        this.assertIsMetaphoneEqual(
                "Albert", new String[] {"Ailbert", "Alberik", "Albert", "Alberto", "Albrecht"});
    }

    @Test
    public void testIsMetaphoneEqualGary_test0_decomposed()  {
        this.assertIsMetaphoneEqual(
                "Gary",
                new String[] {
                    "Cahra", "Cara", "Carey", "Cari", "Caria", "Carie", "Caro", "Carree", "Carri",
                    "Carrie", "Carry", "Cary", "Cora", "Corey", "Cori", "Corie", "Correy", "Corri",
                    "Corrie", "Corry", "Cory", "Gray", "Kara", "Kare", "Karee", "Kari", "Karia",
                    "Karie", "Karrah", "Karrie", "Karry", "Kary", "Keri", "Kerri", "Kerrie",
                    "Kerry", "Kira", "Kiri", "Kora", "Kore", "Kori", "Korie", "Korrie", "Korry"
                });
    }

    @Test
    public void testIsMetaphoneEqualJohn_test0_decomposed()  {
        this.assertIsMetaphoneEqual(
                "John",
                new String[] {
                    "Gena", "Gene", "Genia", "Genna", "Genni", "Gennie", "Genny", "Giana", "Gianna",
                    "Gina", "Ginni", "Ginnie", "Ginny", "Jaine", "Jan", "Jana", "Jane", "Janey",
                    "Jania", "Janie", "Janna", "Jany", "Jayne", "Jean", "Jeana", "Jeane", "Jeanie",
                    "Jeanna", "Jeanne", "Jeannie", "Jen", "Jena", "Jeni", "Jenn", "Jenna", "Jennee",
                    "Jenni", "Jennie", "Jenny", "Jinny", "Jo Ann", "Jo-Ann", "Jo-Anne", "Joan",
                    "Joana", "Joane", "Joanie", "Joann", "Joanna", "Joanne", "Joeann", "Johna",
                    "Johnna", "Joni", "Jonie", "Juana", "June", "Junia", "Junie"
                });
    }

    @Test
    public void testIsMetaphoneEqualKnight_test0_decomposed()  {
        this.assertIsMetaphoneEqual(
                "Knight",
                new String[] {
                    "Hynda", "Nada", "Nadia", "Nady", "Nat", "Nata", "Natty", "Neda", "Nedda",
                    "Nedi", "Netta", "Netti", "Nettie", "Netty", "Nita", "Nydia"
                });
    }

    @Test
    public void testIsMetaphoneEqualMary_test0_decomposed()  {
        this.assertIsMetaphoneEqual(
                "Mary",
                new String[] {
                    "Mair", "Maire", "Mara", "Mareah", "Mari", "Maria", "Marie", "Mary", "Maura",
                    "Maure", "Meara", "Merrie", "Merry", "Mira", "Moira", "Mora", "Moria", "Moyra",
                    "Muire", "Myra", "Myrah"
                });
    }

    @Test
    public void testIsMetaphoneEqualParis_test0_decomposed()  {
        this.assertIsMetaphoneEqual(
                "Paris", new String[] {"Pearcy", "Perris", "Piercy", "Pierz", "Pryse"});
    }

    @Test
    public void testIsMetaphoneEqualPeter_test0_decomposed()  {
        this.assertIsMetaphoneEqual(
                "Peter",
                new String[] {
                    "Peadar", "Peder", "Pedro", "Peter", "Petr", "Peyter", "Pieter", "Pietro",
                    "Piotr"
                });
    }

    @Test
    public void testIsMetaphoneEqualRay_test0_decomposed()  {
        this.assertIsMetaphoneEqual("Ray", new String[] {"Ray", "Rey", "Roi", "Roy", "Ruy"});
    }

    @Test
    public void testIsMetaphoneEqualSusan_test0_decomposed()  {
        this.assertIsMetaphoneEqual(
                "Susan",
                new String[] {
                    "Siusan",
                    "Sosanna",
                    "Susan",
                    "Susana",
                    "Susann",
                    "Susanna",
                    "Susannah",
                    "Susanne",
                    "Suzann",
                    "Suzanna",
                    "Suzanne",
                    "Zuzana"
                });
    }

    @Test
    public void testIsMetaphoneEqualWright_test0_decomposed()  {
        this.assertIsMetaphoneEqual("Wright", new String[] {"Rota", "Rudd", "Ryde"});
    }

    @Test
    public void testIsMetaphoneEqualXalan_test0_decomposed()  {
        this.assertIsMetaphoneEqual(
                "Xalan",
                new String[] {
                    "Celene", "Celina", "Celine", "Selena", "Selene", "Selina", "Seline", "Suellen",
                    "Xylina"
                });
    }

    @Test
    public void testMetaphone_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testMetaphone_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("HL", this.getStringEncoder().metaphone("howl"));
    }

    @Test
    public void testMetaphone_test2_decomposed()  {
        this.getStringEncoder();
        assertEquals("HL", this.getStringEncoder().metaphone("howl"));
        this.getStringEncoder();
    }

    @Test
    public void testMetaphone_test3_decomposed()  {
        this.getStringEncoder();
        assertEquals("HL", this.getStringEncoder().metaphone("howl"));
        this.getStringEncoder();
        assertEquals("TSTN", this.getStringEncoder().metaphone("testing"));
    }

    @Test
    public void testMetaphone_test4_decomposed()  {
        this.getStringEncoder();
        assertEquals("HL", this.getStringEncoder().metaphone("howl"));
        this.getStringEncoder();
        assertEquals("TSTN", this.getStringEncoder().metaphone("testing"));
        this.getStringEncoder();
    }

    @Test
    public void testMetaphone_test5_decomposed()  {
        this.getStringEncoder();
        assertEquals("HL", this.getStringEncoder().metaphone("howl"));
        this.getStringEncoder();
        assertEquals("TSTN", this.getStringEncoder().metaphone("testing"));
        this.getStringEncoder();
        assertEquals("0", this.getStringEncoder().metaphone("The"));
    }

    @Test
    public void testMetaphone_test6_decomposed()  {
        this.getStringEncoder();
        assertEquals("HL", this.getStringEncoder().metaphone("howl"));
        this.getStringEncoder();
        assertEquals("TSTN", this.getStringEncoder().metaphone("testing"));
        this.getStringEncoder();
        assertEquals("0", this.getStringEncoder().metaphone("The"));
        this.getStringEncoder();
    }

    @Test
    public void testMetaphone_test7_decomposed()  {
        this.getStringEncoder();
        assertEquals("HL", this.getStringEncoder().metaphone("howl"));
        this.getStringEncoder();
        assertEquals("TSTN", this.getStringEncoder().metaphone("testing"));
        this.getStringEncoder();
        assertEquals("0", this.getStringEncoder().metaphone("The"));
        this.getStringEncoder();
        assertEquals("KK", this.getStringEncoder().metaphone("quick"));
    }

    @Test
    public void testMetaphone_test8_decomposed()  {
        this.getStringEncoder();
        assertEquals("HL", this.getStringEncoder().metaphone("howl"));
        this.getStringEncoder();
        assertEquals("TSTN", this.getStringEncoder().metaphone("testing"));
        this.getStringEncoder();
        assertEquals("0", this.getStringEncoder().metaphone("The"));
        this.getStringEncoder();
        assertEquals("KK", this.getStringEncoder().metaphone("quick"));
        this.getStringEncoder();
    }

    @Test
    public void testMetaphone_test9_decomposed()  {
        this.getStringEncoder();
        assertEquals("HL", this.getStringEncoder().metaphone("howl"));
        this.getStringEncoder();
        assertEquals("TSTN", this.getStringEncoder().metaphone("testing"));
        this.getStringEncoder();
        assertEquals("0", this.getStringEncoder().metaphone("The"));
        this.getStringEncoder();
        assertEquals("KK", this.getStringEncoder().metaphone("quick"));
        this.getStringEncoder();
        assertEquals("BRN", this.getStringEncoder().metaphone("brown"));
    }

    @Test
    public void testMetaphone_test10_decomposed()  {
        this.getStringEncoder();
        assertEquals("HL", this.getStringEncoder().metaphone("howl"));
        this.getStringEncoder();
        assertEquals("TSTN", this.getStringEncoder().metaphone("testing"));
        this.getStringEncoder();
        assertEquals("0", this.getStringEncoder().metaphone("The"));
        this.getStringEncoder();
        assertEquals("KK", this.getStringEncoder().metaphone("quick"));
        this.getStringEncoder();
        assertEquals("BRN", this.getStringEncoder().metaphone("brown"));
        this.getStringEncoder();
    }

    @Test
    public void testMetaphone_test11_decomposed()  {
        this.getStringEncoder();
        assertEquals("HL", this.getStringEncoder().metaphone("howl"));
        this.getStringEncoder();
        assertEquals("TSTN", this.getStringEncoder().metaphone("testing"));
        this.getStringEncoder();
        assertEquals("0", this.getStringEncoder().metaphone("The"));
        this.getStringEncoder();
        assertEquals("KK", this.getStringEncoder().metaphone("quick"));
        this.getStringEncoder();
        assertEquals("BRN", this.getStringEncoder().metaphone("brown"));
        this.getStringEncoder();
        assertEquals("FKS", this.getStringEncoder().metaphone("fox"));
    }

    @Test
    public void testMetaphone_test12_decomposed()  {
        this.getStringEncoder();
        assertEquals("HL", this.getStringEncoder().metaphone("howl"));
        this.getStringEncoder();
        assertEquals("TSTN", this.getStringEncoder().metaphone("testing"));
        this.getStringEncoder();
        assertEquals("0", this.getStringEncoder().metaphone("The"));
        this.getStringEncoder();
        assertEquals("KK", this.getStringEncoder().metaphone("quick"));
        this.getStringEncoder();
        assertEquals("BRN", this.getStringEncoder().metaphone("brown"));
        this.getStringEncoder();
        assertEquals("FKS", this.getStringEncoder().metaphone("fox"));
        this.getStringEncoder();
    }

    @Test
    public void testMetaphone_test13_decomposed()  {
        this.getStringEncoder();
        assertEquals("HL", this.getStringEncoder().metaphone("howl"));
        this.getStringEncoder();
        assertEquals("TSTN", this.getStringEncoder().metaphone("testing"));
        this.getStringEncoder();
        assertEquals("0", this.getStringEncoder().metaphone("The"));
        this.getStringEncoder();
        assertEquals("KK", this.getStringEncoder().metaphone("quick"));
        this.getStringEncoder();
        assertEquals("BRN", this.getStringEncoder().metaphone("brown"));
        this.getStringEncoder();
        assertEquals("FKS", this.getStringEncoder().metaphone("fox"));
        this.getStringEncoder();
        assertEquals("JMPT", this.getStringEncoder().metaphone("jumped"));
    }

    @Test
    public void testMetaphone_test14_decomposed()  {
        this.getStringEncoder();
        assertEquals("HL", this.getStringEncoder().metaphone("howl"));
        this.getStringEncoder();
        assertEquals("TSTN", this.getStringEncoder().metaphone("testing"));
        this.getStringEncoder();
        assertEquals("0", this.getStringEncoder().metaphone("The"));
        this.getStringEncoder();
        assertEquals("KK", this.getStringEncoder().metaphone("quick"));
        this.getStringEncoder();
        assertEquals("BRN", this.getStringEncoder().metaphone("brown"));
        this.getStringEncoder();
        assertEquals("FKS", this.getStringEncoder().metaphone("fox"));
        this.getStringEncoder();
        assertEquals("JMPT", this.getStringEncoder().metaphone("jumped"));
        this.getStringEncoder();
    }

    @Test
    public void testMetaphone_test15_decomposed()  {
        this.getStringEncoder();
        assertEquals("HL", this.getStringEncoder().metaphone("howl"));
        this.getStringEncoder();
        assertEquals("TSTN", this.getStringEncoder().metaphone("testing"));
        this.getStringEncoder();
        assertEquals("0", this.getStringEncoder().metaphone("The"));
        this.getStringEncoder();
        assertEquals("KK", this.getStringEncoder().metaphone("quick"));
        this.getStringEncoder();
        assertEquals("BRN", this.getStringEncoder().metaphone("brown"));
        this.getStringEncoder();
        assertEquals("FKS", this.getStringEncoder().metaphone("fox"));
        this.getStringEncoder();
        assertEquals("JMPT", this.getStringEncoder().metaphone("jumped"));
        this.getStringEncoder();
        assertEquals("OFR", this.getStringEncoder().metaphone("over"));
    }

    @Test
    public void testMetaphone_test16_decomposed()  {
        this.getStringEncoder();
        assertEquals("HL", this.getStringEncoder().metaphone("howl"));
        this.getStringEncoder();
        assertEquals("TSTN", this.getStringEncoder().metaphone("testing"));
        this.getStringEncoder();
        assertEquals("0", this.getStringEncoder().metaphone("The"));
        this.getStringEncoder();
        assertEquals("KK", this.getStringEncoder().metaphone("quick"));
        this.getStringEncoder();
        assertEquals("BRN", this.getStringEncoder().metaphone("brown"));
        this.getStringEncoder();
        assertEquals("FKS", this.getStringEncoder().metaphone("fox"));
        this.getStringEncoder();
        assertEquals("JMPT", this.getStringEncoder().metaphone("jumped"));
        this.getStringEncoder();
        assertEquals("OFR", this.getStringEncoder().metaphone("over"));
        this.getStringEncoder();
    }

    @Test
    public void testMetaphone_test17_decomposed()  {
        this.getStringEncoder();
        assertEquals("HL", this.getStringEncoder().metaphone("howl"));
        this.getStringEncoder();
        assertEquals("TSTN", this.getStringEncoder().metaphone("testing"));
        this.getStringEncoder();
        assertEquals("0", this.getStringEncoder().metaphone("The"));
        this.getStringEncoder();
        assertEquals("KK", this.getStringEncoder().metaphone("quick"));
        this.getStringEncoder();
        assertEquals("BRN", this.getStringEncoder().metaphone("brown"));
        this.getStringEncoder();
        assertEquals("FKS", this.getStringEncoder().metaphone("fox"));
        this.getStringEncoder();
        assertEquals("JMPT", this.getStringEncoder().metaphone("jumped"));
        this.getStringEncoder();
        assertEquals("OFR", this.getStringEncoder().metaphone("over"));
        this.getStringEncoder();
        assertEquals("0", this.getStringEncoder().metaphone("the"));
    }

    @Test
    public void testMetaphone_test18_decomposed()  {
        this.getStringEncoder();
        assertEquals("HL", this.getStringEncoder().metaphone("howl"));
        this.getStringEncoder();
        assertEquals("TSTN", this.getStringEncoder().metaphone("testing"));
        this.getStringEncoder();
        assertEquals("0", this.getStringEncoder().metaphone("The"));
        this.getStringEncoder();
        assertEquals("KK", this.getStringEncoder().metaphone("quick"));
        this.getStringEncoder();
        assertEquals("BRN", this.getStringEncoder().metaphone("brown"));
        this.getStringEncoder();
        assertEquals("FKS", this.getStringEncoder().metaphone("fox"));
        this.getStringEncoder();
        assertEquals("JMPT", this.getStringEncoder().metaphone("jumped"));
        this.getStringEncoder();
        assertEquals("OFR", this.getStringEncoder().metaphone("over"));
        this.getStringEncoder();
        assertEquals("0", this.getStringEncoder().metaphone("the"));
        this.getStringEncoder();
    }

    @Test
    public void testMetaphone_test19_decomposed()  {
        this.getStringEncoder();
        assertEquals("HL", this.getStringEncoder().metaphone("howl"));
        this.getStringEncoder();
        assertEquals("TSTN", this.getStringEncoder().metaphone("testing"));
        this.getStringEncoder();
        assertEquals("0", this.getStringEncoder().metaphone("The"));
        this.getStringEncoder();
        assertEquals("KK", this.getStringEncoder().metaphone("quick"));
        this.getStringEncoder();
        assertEquals("BRN", this.getStringEncoder().metaphone("brown"));
        this.getStringEncoder();
        assertEquals("FKS", this.getStringEncoder().metaphone("fox"));
        this.getStringEncoder();
        assertEquals("JMPT", this.getStringEncoder().metaphone("jumped"));
        this.getStringEncoder();
        assertEquals("OFR", this.getStringEncoder().metaphone("over"));
        this.getStringEncoder();
        assertEquals("0", this.getStringEncoder().metaphone("the"));
        this.getStringEncoder();
        assertEquals("LS", this.getStringEncoder().metaphone("lazy"));
    }

    @Test
    public void testMetaphone_test20_decomposed()  {
        this.getStringEncoder();
        assertEquals("HL", this.getStringEncoder().metaphone("howl"));
        this.getStringEncoder();
        assertEquals("TSTN", this.getStringEncoder().metaphone("testing"));
        this.getStringEncoder();
        assertEquals("0", this.getStringEncoder().metaphone("The"));
        this.getStringEncoder();
        assertEquals("KK", this.getStringEncoder().metaphone("quick"));
        this.getStringEncoder();
        assertEquals("BRN", this.getStringEncoder().metaphone("brown"));
        this.getStringEncoder();
        assertEquals("FKS", this.getStringEncoder().metaphone("fox"));
        this.getStringEncoder();
        assertEquals("JMPT", this.getStringEncoder().metaphone("jumped"));
        this.getStringEncoder();
        assertEquals("OFR", this.getStringEncoder().metaphone("over"));
        this.getStringEncoder();
        assertEquals("0", this.getStringEncoder().metaphone("the"));
        this.getStringEncoder();
        assertEquals("LS", this.getStringEncoder().metaphone("lazy"));
        this.getStringEncoder();
    }

    @Test
    public void testMetaphone_test21_decomposed()  {
        this.getStringEncoder();
        assertEquals("HL", this.getStringEncoder().metaphone("howl"));
        this.getStringEncoder();
        assertEquals("TSTN", this.getStringEncoder().metaphone("testing"));
        this.getStringEncoder();
        assertEquals("0", this.getStringEncoder().metaphone("The"));
        this.getStringEncoder();
        assertEquals("KK", this.getStringEncoder().metaphone("quick"));
        this.getStringEncoder();
        assertEquals("BRN", this.getStringEncoder().metaphone("brown"));
        this.getStringEncoder();
        assertEquals("FKS", this.getStringEncoder().metaphone("fox"));
        this.getStringEncoder();
        assertEquals("JMPT", this.getStringEncoder().metaphone("jumped"));
        this.getStringEncoder();
        assertEquals("OFR", this.getStringEncoder().metaphone("over"));
        this.getStringEncoder();
        assertEquals("0", this.getStringEncoder().metaphone("the"));
        this.getStringEncoder();
        assertEquals("LS", this.getStringEncoder().metaphone("lazy"));
        this.getStringEncoder();
        assertEquals("TKS", this.getStringEncoder().metaphone("dogs"));
    }

    @Test
    public void testWordEndingInMB_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testWordEndingInMB_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("KM", this.getStringEncoder().metaphone("COMB"));
    }

    @Test
    public void testWordEndingInMB_test2_decomposed()  {
        this.getStringEncoder();
        assertEquals("KM", this.getStringEncoder().metaphone("COMB"));
        this.getStringEncoder();
    }

    @Test
    public void testWordEndingInMB_test3_decomposed()  {
        this.getStringEncoder();
        assertEquals("KM", this.getStringEncoder().metaphone("COMB"));
        this.getStringEncoder();
        assertEquals("TM", this.getStringEncoder().metaphone("TOMB"));
    }

    @Test
    public void testWordEndingInMB_test4_decomposed()  {
        this.getStringEncoder();
        assertEquals("KM", this.getStringEncoder().metaphone("COMB"));
        this.getStringEncoder();
        assertEquals("TM", this.getStringEncoder().metaphone("TOMB"));
        this.getStringEncoder();
    }

    @Test
    public void testWordEndingInMB_test5_decomposed()  {
        this.getStringEncoder();
        assertEquals("KM", this.getStringEncoder().metaphone("COMB"));
        this.getStringEncoder();
        assertEquals("TM", this.getStringEncoder().metaphone("TOMB"));
        this.getStringEncoder();
        assertEquals("WM", this.getStringEncoder().metaphone("WOMB"));
    }

    @Test
    public void testDiscardOfSCEOrSCIOrSCY_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testDiscardOfSCEOrSCIOrSCY_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("SNS", this.getStringEncoder().metaphone("SCIENCE"));
    }

    @Test
    public void testDiscardOfSCEOrSCIOrSCY_test2_decomposed()  {
        this.getStringEncoder();
        assertEquals("SNS", this.getStringEncoder().metaphone("SCIENCE"));
        this.getStringEncoder();
    }

    @Test
    public void testDiscardOfSCEOrSCIOrSCY_test3_decomposed()  {
        this.getStringEncoder();
        assertEquals("SNS", this.getStringEncoder().metaphone("SCIENCE"));
        this.getStringEncoder();
        assertEquals("SN", this.getStringEncoder().metaphone("SCENE"));
    }

    @Test
    public void testDiscardOfSCEOrSCIOrSCY_test4_decomposed()  {
        this.getStringEncoder();
        assertEquals("SNS", this.getStringEncoder().metaphone("SCIENCE"));
        this.getStringEncoder();
        assertEquals("SN", this.getStringEncoder().metaphone("SCENE"));
        this.getStringEncoder();
    }

    @Test
    public void testDiscardOfSCEOrSCIOrSCY_test5_decomposed()  {
        this.getStringEncoder();
        assertEquals("SNS", this.getStringEncoder().metaphone("SCIENCE"));
        this.getStringEncoder();
        assertEquals("SN", this.getStringEncoder().metaphone("SCENE"));
        this.getStringEncoder();
        assertEquals("S", this.getStringEncoder().metaphone("SCY"));
    }

    @Test
    public void testWhy_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testWhy_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("", this.getStringEncoder().metaphone("WHY"));
    }

    @Test
    public void testWordsWithCIA_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testWordsWithCIA_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("XP", this.getStringEncoder().metaphone("CIAPO"));
    }

    @Test
    public void testTranslateOfSCHAndCH_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testTranslateOfSCHAndCH_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("SKTL", this.getStringEncoder().metaphone("SCHEDULE"));
    }

    @Test
    public void testTranslateOfSCHAndCH_test2_decomposed()  {
        this.getStringEncoder();
        assertEquals("SKTL", this.getStringEncoder().metaphone("SCHEDULE"));
        this.getStringEncoder();
    }

    @Test
    public void testTranslateOfSCHAndCH_test3_decomposed()  {
        this.getStringEncoder();
        assertEquals("SKTL", this.getStringEncoder().metaphone("SCHEDULE"));
        this.getStringEncoder();
        assertEquals("SKMT", this.getStringEncoder().metaphone("SCHEMATIC"));
    }

    @Test
    public void testTranslateOfSCHAndCH_test4_decomposed()  {
        this.getStringEncoder();
        assertEquals("SKTL", this.getStringEncoder().metaphone("SCHEDULE"));
        this.getStringEncoder();
        assertEquals("SKMT", this.getStringEncoder().metaphone("SCHEMATIC"));
        this.getStringEncoder();
    }

    @Test
    public void testTranslateOfSCHAndCH_test5_decomposed()  {
        this.getStringEncoder();
        assertEquals("SKTL", this.getStringEncoder().metaphone("SCHEDULE"));
        this.getStringEncoder();
        assertEquals("SKMT", this.getStringEncoder().metaphone("SCHEMATIC"));
        this.getStringEncoder();
        assertEquals("KRKT", this.getStringEncoder().metaphone("CHARACTER"));
    }

    @Test
    public void testTranslateOfSCHAndCH_test6_decomposed()  {
        this.getStringEncoder();
        assertEquals("SKTL", this.getStringEncoder().metaphone("SCHEDULE"));
        this.getStringEncoder();
        assertEquals("SKMT", this.getStringEncoder().metaphone("SCHEMATIC"));
        this.getStringEncoder();
        assertEquals("KRKT", this.getStringEncoder().metaphone("CHARACTER"));
        this.getStringEncoder();
    }

    @Test
    public void testTranslateOfSCHAndCH_test7_decomposed()  {
        this.getStringEncoder();
        assertEquals("SKTL", this.getStringEncoder().metaphone("SCHEDULE"));
        this.getStringEncoder();
        assertEquals("SKMT", this.getStringEncoder().metaphone("SCHEMATIC"));
        this.getStringEncoder();
        assertEquals("KRKT", this.getStringEncoder().metaphone("CHARACTER"));
        this.getStringEncoder();
        assertEquals("TX", this.getStringEncoder().metaphone("TEACH"));
    }

    @Test
    public void testTranslateToJOfDGEOrDGIOrDGY_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testTranslateToJOfDGEOrDGIOrDGY_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("TJ", this.getStringEncoder().metaphone("DODGY"));
    }

    @Test
    public void testTranslateToJOfDGEOrDGIOrDGY_test2_decomposed()  {
        this.getStringEncoder();
        assertEquals("TJ", this.getStringEncoder().metaphone("DODGY"));
        this.getStringEncoder();
    }

    @Test
    public void testTranslateToJOfDGEOrDGIOrDGY_test3_decomposed()  {
        this.getStringEncoder();
        assertEquals("TJ", this.getStringEncoder().metaphone("DODGY"));
        this.getStringEncoder();
        assertEquals("TJ", this.getStringEncoder().metaphone("DODGE"));
    }

    @Test
    public void testTranslateToJOfDGEOrDGIOrDGY_test4_decomposed()  {
        this.getStringEncoder();
        assertEquals("TJ", this.getStringEncoder().metaphone("DODGY"));
        this.getStringEncoder();
        assertEquals("TJ", this.getStringEncoder().metaphone("DODGE"));
        this.getStringEncoder();
    }

    @Test
    public void testTranslateToJOfDGEOrDGIOrDGY_test5_decomposed()  {
        this.getStringEncoder();
        assertEquals("TJ", this.getStringEncoder().metaphone("DODGY"));
        this.getStringEncoder();
        assertEquals("TJ", this.getStringEncoder().metaphone("DODGE"));
        this.getStringEncoder();
        assertEquals("AJMT", this.getStringEncoder().metaphone("ADGIEMTI"));
    }

    @Test
    public void testDiscardOfSilentHAfterG_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testDiscardOfSilentHAfterG_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("KNT", this.getStringEncoder().metaphone("GHENT"));
    }

    @Test
    public void testDiscardOfSilentHAfterG_test2_decomposed()  {
        this.getStringEncoder();
        assertEquals("KNT", this.getStringEncoder().metaphone("GHENT"));
        this.getStringEncoder();
    }

    @Test
    public void testDiscardOfSilentHAfterG_test3_decomposed()  {
        this.getStringEncoder();
        assertEquals("KNT", this.getStringEncoder().metaphone("GHENT"));
        this.getStringEncoder();
        assertEquals("B", this.getStringEncoder().metaphone("BAUGH"));
    }

    @Test
    public void testDiscardOfSilentGN_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testDiscardOfSilentGN_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("N", this.getStringEncoder().metaphone("GNU"));
    }

    @Test
    public void testDiscardOfSilentGN_test2_decomposed()  {
        this.getStringEncoder();
        assertEquals("N", this.getStringEncoder().metaphone("GNU"));
        this.getStringEncoder();
    }

    @Test
    public void testDiscardOfSilentGN_test3_decomposed()  {
        this.getStringEncoder();
        assertEquals("N", this.getStringEncoder().metaphone("GNU"));
        this.getStringEncoder();
        assertEquals("SNT", this.getStringEncoder().metaphone("SIGNED"));
    }

    @Test
    public void testPHTOF_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testPHTOF_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("FX", this.getStringEncoder().metaphone("PHISH"));
    }

    @Test
    public void testSHAndSIOAndSIAToX_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testSHAndSIOAndSIAToX_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("XT", this.getStringEncoder().metaphone("SHOT"));
    }

    @Test
    public void testSHAndSIOAndSIAToX_test2_decomposed()  {
        this.getStringEncoder();
        assertEquals("XT", this.getStringEncoder().metaphone("SHOT"));
        this.getStringEncoder();
    }

    @Test
    public void testSHAndSIOAndSIAToX_test3_decomposed()  {
        this.getStringEncoder();
        assertEquals("XT", this.getStringEncoder().metaphone("SHOT"));
        this.getStringEncoder();
        assertEquals("OTXN", this.getStringEncoder().metaphone("ODSIAN"));
    }

    @Test
    public void testSHAndSIOAndSIAToX_test4_decomposed()  {
        this.getStringEncoder();
        assertEquals("XT", this.getStringEncoder().metaphone("SHOT"));
        this.getStringEncoder();
        assertEquals("OTXN", this.getStringEncoder().metaphone("ODSIAN"));
        this.getStringEncoder();
    }

    @Test
    public void testSHAndSIOAndSIAToX_test5_decomposed()  {
        this.getStringEncoder();
        assertEquals("XT", this.getStringEncoder().metaphone("SHOT"));
        this.getStringEncoder();
        assertEquals("OTXN", this.getStringEncoder().metaphone("ODSIAN"));
        this.getStringEncoder();
        assertEquals("PLXN", this.getStringEncoder().metaphone("PULSION"));
    }

    @Test
    public void testTIOAndTIAToX_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testTIOAndTIAToX_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("OX", this.getStringEncoder().metaphone("OTIA"));
    }

    @Test
    public void testTIOAndTIAToX_test2_decomposed()  {
        this.getStringEncoder();
        assertEquals("OX", this.getStringEncoder().metaphone("OTIA"));
        this.getStringEncoder();
    }

    @Test
    public void testTIOAndTIAToX_test3_decomposed()  {
        this.getStringEncoder();
        assertEquals("OX", this.getStringEncoder().metaphone("OTIA"));
        this.getStringEncoder();
        assertEquals("PRXN", this.getStringEncoder().metaphone("PORTION"));
    }

    @Test
    public void testTCH_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testTCH_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("RX", this.getStringEncoder().metaphone("RETCH"));
    }

    @Test
    public void testTCH_test2_decomposed()  {
        this.getStringEncoder();
        assertEquals("RX", this.getStringEncoder().metaphone("RETCH"));
        this.getStringEncoder();
    }

    @Test
    public void testTCH_test3_decomposed()  {
        this.getStringEncoder();
        assertEquals("RX", this.getStringEncoder().metaphone("RETCH"));
        this.getStringEncoder();
        assertEquals("WX", this.getStringEncoder().metaphone("WATCH"));
    }

    @Test
    public void testExceedLength_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testExceedLength_test1_decomposed()  {
        this.getStringEncoder();
        assertEquals("AKSK", this.getStringEncoder().metaphone("AXEAXE"));
    }

    @Test
    public void testSetMaxLengthWithTruncation_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testSetMaxLengthWithTruncation_test1_decomposed()  {
        this.getStringEncoder();
        this.getStringEncoder().setMaxCodeLen(6);
    }

    @Test
    public void testSetMaxLengthWithTruncation_test2_decomposed()  {
        this.getStringEncoder();
        this.getStringEncoder().setMaxCodeLen(6);
        this.getStringEncoder();
    }

    @Test
    public void testSetMaxLengthWithTruncation_test3_decomposed()  {
        this.getStringEncoder();
        this.getStringEncoder().setMaxCodeLen(6);
        this.getStringEncoder();
        assertEquals("AKSKSK", this.getStringEncoder().metaphone("AXEAXEAXE"));
    }
}