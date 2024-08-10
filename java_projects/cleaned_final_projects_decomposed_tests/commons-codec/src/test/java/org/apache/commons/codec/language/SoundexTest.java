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

import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.StringEncoderAbstractTest;
import org.junit.Assert;
import org.junit.Test;

/**
 * Tests {@link Soundex}.
 *
 * <p>Keep this file in UTF-8 encoding for proper Javadoc processing.
 */
public class SoundexTest extends StringEncoderAbstractTest<Soundex> {

    @Override
    protected Soundex createStringEncoder() {
        return new Soundex(3, false, null, null);
    }

    

    

    

    

    /** Examples from http://www.bradandkathy.com/genealogy/overviewofsoundex.html */
    

    /** Examples from http://www.archives.gov/research_room/genealogy/census/soundex.html */
    

    /** Examples from: http://www.myatt.demon.co.uk/sxalg.htm */
    

    

    /**
     * Test data from http://www.myatt.demon.co.uk/sxalg.htm
     *
     * @throws EncoderException for some failure scenarios
     */
    

    

    /** Consonants from the same code group separated by W or H are treated as one. */
    

    /**
     * Consonants from the same code group separated by W or H are treated as one.
     *
     * <p>Test data from http://www.myatt.demon.co.uk/sxalg.htm
     */
    

    /**
     * Consonants from the same code group separated by W or H are treated as one.
     *
     * @throws EncoderException for some failure scenarios
     */
    

    /**
     * Examples for MS SQLServer from
     * http://msdn.microsoft.com/library/default.asp?url=/library/en-us/tsqlref/ts_setu-sus_3o6w.asp
     */
    

    /**
     * Examples for MS SQLServer from
     * http://support.microsoft.com/default.aspx?scid=http://support.microsoft.com:80/support
     * /kb/articles/Q100/3/65.asp&NoWebContent=1
     *
     * @throws EncoderException for some failure scenarios
     */
    

    /** Examples for MS SQLServer from http://databases.about.com/library/weekly/aa042901a.htm */
    

    /**
     * https://issues.apache.org/jira/browse/CODEC-54 https://issues.apache.org/jira/browse/CODEC-56
     */
    

    

    

    

    

    /**
     * https://issues.apache.org/jira/browse/CODEC-54 https://issues.apache.org/jira/browse/CODEC-56
     */
    

    /**
     * Fancy characters are not mapped by the default US mapping.
     *
     * <p>https://issues.apache.org/jira/browse/CODEC-30
     */
    

    /**
     * Fancy characters are not mapped by the default US mapping.
     *
     * <p>https://issues.apache.org/jira/browse/CODEC-30
     */
    

    /**
     * Tests example from http://en.wikipedia.org/wiki/Soundex#American_Soundex as of 2015-03-22.
     */

    @Test
    public void testB650_test0_decomposed() throws EncoderException {
        this.checkEncodingVariations(
                "B650",
                new String[] {
                    "BARHAM", "BARONE", "BARRON", "BERNA", "BIRNEY", "BIRNIE", "BOOROM", "BOREN",
                    "BORN", "BOURN", "BOURNE", "BOWRON", "BRAIN", "BRAME", "BRANN", "BRAUN",
                    "BREEN", "BRIEN", "BRIM", "BRIMM", "BRINN", "BRION", "BROOM", "BROOME", "BROWN",
                    "BROWNE", "BRUEN", "BRUHN", "BRUIN", "BRUMM", "BRUN", "BRUNO", "BRYAN",
                    "BURIAN", "BURN", "BURNEY", "BYRAM", "BYRNE", "BYRON", "BYRUM"
                });
    }

    @Test
    public void testBadCharacters_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testBadCharacters_test1_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("H452", this.getStringEncoder().encode1("HOL>MES"));
    }

    @Test
    public void testDifference_test0_decomposed() throws EncoderException {
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test1_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
    }

    @Test
    public void testDifference_test2_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test3_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("", ""));
    }

    @Test
    public void testDifference_test4_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test5_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(" ", " "));
    }

    @Test
    public void testDifference_test6_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test7_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
    }

    @Test
    public void testDifference_test8_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test9_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        Assert.assertEquals(2, this.getStringEncoder().difference("Ann", "Andrew"));
    }

    @Test
    public void testDifference_test10_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        Assert.assertEquals(2, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test11_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        Assert.assertEquals(2, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
    }

    @Test
    public void testDifference_test12_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        Assert.assertEquals(2, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test13_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        Assert.assertEquals(2, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("Janet", "Margaret"));
    }

    @Test
    public void testDifference_test14_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        Assert.assertEquals(2, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("Janet", "Margaret"));
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test15_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        Assert.assertEquals(2, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("Janet", "Margaret"));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Green", "Greene"));
    }

    @Test
    public void testDifference_test16_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        Assert.assertEquals(2, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("Janet", "Margaret"));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Green", "Greene"));
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test17_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        Assert.assertEquals(2, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("Janet", "Margaret"));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Green", "Greene"));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("Blotchet-Halls", "Greene"));
    }

    @Test
    public void testDifference_test18_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        Assert.assertEquals(2, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("Janet", "Margaret"));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Green", "Greene"));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("Blotchet-Halls", "Greene"));
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test19_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        Assert.assertEquals(2, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("Janet", "Margaret"));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Green", "Greene"));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("Blotchet-Halls", "Greene"));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
    }

    @Test
    public void testDifference_test20_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        Assert.assertEquals(2, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("Janet", "Margaret"));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Green", "Greene"));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("Blotchet-Halls", "Greene"));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test21_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        Assert.assertEquals(2, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("Janet", "Margaret"));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Green", "Greene"));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("Blotchet-Halls", "Greene"));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smithers", "Smythers"));
    }

    @Test
    public void testDifference_test22_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        Assert.assertEquals(2, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("Janet", "Margaret"));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Green", "Greene"));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("Blotchet-Halls", "Greene"));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smithers", "Smythers"));
        this.getStringEncoder();
    }

    @Test
    public void testDifference_test23_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("", ""));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference(" ", " "));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        Assert.assertEquals(2, this.getStringEncoder().difference("Ann", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("Janet", "Margaret"));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Green", "Greene"));
        this.getStringEncoder();
        Assert.assertEquals(0, this.getStringEncoder().difference("Blotchet-Halls", "Greene"));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
        this.getStringEncoder();
        Assert.assertEquals(4, this.getStringEncoder().difference("Smithers", "Smythers"));
        this.getStringEncoder();
        Assert.assertEquals(2, this.getStringEncoder().difference("Anothers", "Brothers"));
    }

    @Test
    public void testEncodeBasic_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBasic_test1_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("T235", this.getStringEncoder().encode1("testing"));
    }

    @Test
    public void testEncodeBasic_test2_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("T235", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBasic_test3_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("T235", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        Assert.assertEquals("T000", this.getStringEncoder().encode1("The"));
    }

    @Test
    public void testEncodeBasic_test4_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("T235", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        Assert.assertEquals("T000", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBasic_test5_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("T235", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        Assert.assertEquals("T000", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        Assert.assertEquals("Q200", this.getStringEncoder().encode1("quick"));
    }

    @Test
    public void testEncodeBasic_test6_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("T235", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        Assert.assertEquals("T000", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        Assert.assertEquals("Q200", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBasic_test7_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("T235", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        Assert.assertEquals("T000", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        Assert.assertEquals("Q200", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        Assert.assertEquals("B650", this.getStringEncoder().encode1("brown"));
    }

    @Test
    public void testEncodeBasic_test8_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("T235", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        Assert.assertEquals("T000", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        Assert.assertEquals("Q200", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        Assert.assertEquals("B650", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBasic_test9_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("T235", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        Assert.assertEquals("T000", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        Assert.assertEquals("Q200", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        Assert.assertEquals("B650", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
        Assert.assertEquals("F200", this.getStringEncoder().encode1("fox"));
    }

    @Test
    public void testEncodeBasic_test10_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("T235", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        Assert.assertEquals("T000", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        Assert.assertEquals("Q200", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        Assert.assertEquals("B650", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
        Assert.assertEquals("F200", this.getStringEncoder().encode1("fox"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBasic_test11_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("T235", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        Assert.assertEquals("T000", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        Assert.assertEquals("Q200", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        Assert.assertEquals("B650", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
        Assert.assertEquals("F200", this.getStringEncoder().encode1("fox"));
        this.getStringEncoder();
        Assert.assertEquals("J513", this.getStringEncoder().encode1("jumped"));
    }

    @Test
    public void testEncodeBasic_test12_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("T235", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        Assert.assertEquals("T000", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        Assert.assertEquals("Q200", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        Assert.assertEquals("B650", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
        Assert.assertEquals("F200", this.getStringEncoder().encode1("fox"));
        this.getStringEncoder();
        Assert.assertEquals("J513", this.getStringEncoder().encode1("jumped"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBasic_test13_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("T235", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        Assert.assertEquals("T000", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        Assert.assertEquals("Q200", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        Assert.assertEquals("B650", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
        Assert.assertEquals("F200", this.getStringEncoder().encode1("fox"));
        this.getStringEncoder();
        Assert.assertEquals("J513", this.getStringEncoder().encode1("jumped"));
        this.getStringEncoder();
        Assert.assertEquals("O160", this.getStringEncoder().encode1("over"));
    }

    @Test
    public void testEncodeBasic_test14_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("T235", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        Assert.assertEquals("T000", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        Assert.assertEquals("Q200", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        Assert.assertEquals("B650", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
        Assert.assertEquals("F200", this.getStringEncoder().encode1("fox"));
        this.getStringEncoder();
        Assert.assertEquals("J513", this.getStringEncoder().encode1("jumped"));
        this.getStringEncoder();
        Assert.assertEquals("O160", this.getStringEncoder().encode1("over"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBasic_test15_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("T235", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        Assert.assertEquals("T000", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        Assert.assertEquals("Q200", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        Assert.assertEquals("B650", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
        Assert.assertEquals("F200", this.getStringEncoder().encode1("fox"));
        this.getStringEncoder();
        Assert.assertEquals("J513", this.getStringEncoder().encode1("jumped"));
        this.getStringEncoder();
        Assert.assertEquals("O160", this.getStringEncoder().encode1("over"));
        this.getStringEncoder();
        Assert.assertEquals("T000", this.getStringEncoder().encode1("the"));
    }

    @Test
    public void testEncodeBasic_test16_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("T235", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        Assert.assertEquals("T000", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        Assert.assertEquals("Q200", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        Assert.assertEquals("B650", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
        Assert.assertEquals("F200", this.getStringEncoder().encode1("fox"));
        this.getStringEncoder();
        Assert.assertEquals("J513", this.getStringEncoder().encode1("jumped"));
        this.getStringEncoder();
        Assert.assertEquals("O160", this.getStringEncoder().encode1("over"));
        this.getStringEncoder();
        Assert.assertEquals("T000", this.getStringEncoder().encode1("the"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBasic_test17_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("T235", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        Assert.assertEquals("T000", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        Assert.assertEquals("Q200", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        Assert.assertEquals("B650", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
        Assert.assertEquals("F200", this.getStringEncoder().encode1("fox"));
        this.getStringEncoder();
        Assert.assertEquals("J513", this.getStringEncoder().encode1("jumped"));
        this.getStringEncoder();
        Assert.assertEquals("O160", this.getStringEncoder().encode1("over"));
        this.getStringEncoder();
        Assert.assertEquals("T000", this.getStringEncoder().encode1("the"));
        this.getStringEncoder();
        Assert.assertEquals("L200", this.getStringEncoder().encode1("lazy"));
    }

    @Test
    public void testEncodeBasic_test18_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("T235", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        Assert.assertEquals("T000", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        Assert.assertEquals("Q200", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        Assert.assertEquals("B650", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
        Assert.assertEquals("F200", this.getStringEncoder().encode1("fox"));
        this.getStringEncoder();
        Assert.assertEquals("J513", this.getStringEncoder().encode1("jumped"));
        this.getStringEncoder();
        Assert.assertEquals("O160", this.getStringEncoder().encode1("over"));
        this.getStringEncoder();
        Assert.assertEquals("T000", this.getStringEncoder().encode1("the"));
        this.getStringEncoder();
        Assert.assertEquals("L200", this.getStringEncoder().encode1("lazy"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBasic_test19_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("T235", this.getStringEncoder().encode1("testing"));
        this.getStringEncoder();
        Assert.assertEquals("T000", this.getStringEncoder().encode1("The"));
        this.getStringEncoder();
        Assert.assertEquals("Q200", this.getStringEncoder().encode1("quick"));
        this.getStringEncoder();
        Assert.assertEquals("B650", this.getStringEncoder().encode1("brown"));
        this.getStringEncoder();
        Assert.assertEquals("F200", this.getStringEncoder().encode1("fox"));
        this.getStringEncoder();
        Assert.assertEquals("J513", this.getStringEncoder().encode1("jumped"));
        this.getStringEncoder();
        Assert.assertEquals("O160", this.getStringEncoder().encode1("over"));
        this.getStringEncoder();
        Assert.assertEquals("T000", this.getStringEncoder().encode1("the"));
        this.getStringEncoder();
        Assert.assertEquals("L200", this.getStringEncoder().encode1("lazy"));
        this.getStringEncoder();
        Assert.assertEquals("D200", this.getStringEncoder().encode1("dogs"));
    }

    @Test
    public void testEncodeBatch2_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch2_test1_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
    }

    @Test
    public void testEncodeBatch2_test2_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch2_test3_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
    }

    @Test
    public void testEncodeBatch2_test4_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch2_test5_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
    }

    @Test
    public void testEncodeBatch2_test6_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch2_test7_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
    }

    @Test
    public void testEncodeBatch2_test8_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch2_test9_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
    }

    @Test
    public void testEncodeBatch2_test10_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch2_test11_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
        this.getStringEncoder();
        Assert.assertEquals("H431", this.getStringEncoder().encode1("Hildebrand"));
    }

    @Test
    public void testEncodeBatch2_test12_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
        this.getStringEncoder();
        Assert.assertEquals("H431", this.getStringEncoder().encode1("Hildebrand"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch2_test13_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
        this.getStringEncoder();
        Assert.assertEquals("H431", this.getStringEncoder().encode1("Hildebrand"));
        this.getStringEncoder();
        Assert.assertEquals("K152", this.getStringEncoder().encode1("Kavanagh"));
    }

    @Test
    public void testEncodeBatch2_test14_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
        this.getStringEncoder();
        Assert.assertEquals("H431", this.getStringEncoder().encode1("Hildebrand"));
        this.getStringEncoder();
        Assert.assertEquals("K152", this.getStringEncoder().encode1("Kavanagh"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch2_test15_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
        this.getStringEncoder();
        Assert.assertEquals("H431", this.getStringEncoder().encode1("Hildebrand"));
        this.getStringEncoder();
        Assert.assertEquals("K152", this.getStringEncoder().encode1("Kavanagh"));
        this.getStringEncoder();
        Assert.assertEquals("L530", this.getStringEncoder().encode1("Lind"));
    }

    @Test
    public void testEncodeBatch2_test16_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
        this.getStringEncoder();
        Assert.assertEquals("H431", this.getStringEncoder().encode1("Hildebrand"));
        this.getStringEncoder();
        Assert.assertEquals("K152", this.getStringEncoder().encode1("Kavanagh"));
        this.getStringEncoder();
        Assert.assertEquals("L530", this.getStringEncoder().encode1("Lind"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch2_test17_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
        this.getStringEncoder();
        Assert.assertEquals("H431", this.getStringEncoder().encode1("Hildebrand"));
        this.getStringEncoder();
        Assert.assertEquals("K152", this.getStringEncoder().encode1("Kavanagh"));
        this.getStringEncoder();
        Assert.assertEquals("L530", this.getStringEncoder().encode1("Lind"));
        this.getStringEncoder();
        Assert.assertEquals("L222", this.getStringEncoder().encode1("Lukaschowsky"));
    }

    @Test
    public void testEncodeBatch2_test18_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
        this.getStringEncoder();
        Assert.assertEquals("H431", this.getStringEncoder().encode1("Hildebrand"));
        this.getStringEncoder();
        Assert.assertEquals("K152", this.getStringEncoder().encode1("Kavanagh"));
        this.getStringEncoder();
        Assert.assertEquals("L530", this.getStringEncoder().encode1("Lind"));
        this.getStringEncoder();
        Assert.assertEquals("L222", this.getStringEncoder().encode1("Lukaschowsky"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch2_test19_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
        this.getStringEncoder();
        Assert.assertEquals("H431", this.getStringEncoder().encode1("Hildebrand"));
        this.getStringEncoder();
        Assert.assertEquals("K152", this.getStringEncoder().encode1("Kavanagh"));
        this.getStringEncoder();
        Assert.assertEquals("L530", this.getStringEncoder().encode1("Lind"));
        this.getStringEncoder();
        Assert.assertEquals("L222", this.getStringEncoder().encode1("Lukaschowsky"));
        this.getStringEncoder();
        Assert.assertEquals("M235", this.getStringEncoder().encode1("McDonnell"));
    }

    @Test
    public void testEncodeBatch2_test20_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
        this.getStringEncoder();
        Assert.assertEquals("H431", this.getStringEncoder().encode1("Hildebrand"));
        this.getStringEncoder();
        Assert.assertEquals("K152", this.getStringEncoder().encode1("Kavanagh"));
        this.getStringEncoder();
        Assert.assertEquals("L530", this.getStringEncoder().encode1("Lind"));
        this.getStringEncoder();
        Assert.assertEquals("L222", this.getStringEncoder().encode1("Lukaschowsky"));
        this.getStringEncoder();
        Assert.assertEquals("M235", this.getStringEncoder().encode1("McDonnell"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch2_test21_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
        this.getStringEncoder();
        Assert.assertEquals("H431", this.getStringEncoder().encode1("Hildebrand"));
        this.getStringEncoder();
        Assert.assertEquals("K152", this.getStringEncoder().encode1("Kavanagh"));
        this.getStringEncoder();
        Assert.assertEquals("L530", this.getStringEncoder().encode1("Lind"));
        this.getStringEncoder();
        Assert.assertEquals("L222", this.getStringEncoder().encode1("Lukaschowsky"));
        this.getStringEncoder();
        Assert.assertEquals("M235", this.getStringEncoder().encode1("McDonnell"));
        this.getStringEncoder();
        Assert.assertEquals("M200", this.getStringEncoder().encode1("McGee"));
    }

    @Test
    public void testEncodeBatch2_test22_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
        this.getStringEncoder();
        Assert.assertEquals("H431", this.getStringEncoder().encode1("Hildebrand"));
        this.getStringEncoder();
        Assert.assertEquals("K152", this.getStringEncoder().encode1("Kavanagh"));
        this.getStringEncoder();
        Assert.assertEquals("L530", this.getStringEncoder().encode1("Lind"));
        this.getStringEncoder();
        Assert.assertEquals("L222", this.getStringEncoder().encode1("Lukaschowsky"));
        this.getStringEncoder();
        Assert.assertEquals("M235", this.getStringEncoder().encode1("McDonnell"));
        this.getStringEncoder();
        Assert.assertEquals("M200", this.getStringEncoder().encode1("McGee"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch2_test23_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
        this.getStringEncoder();
        Assert.assertEquals("H431", this.getStringEncoder().encode1("Hildebrand"));
        this.getStringEncoder();
        Assert.assertEquals("K152", this.getStringEncoder().encode1("Kavanagh"));
        this.getStringEncoder();
        Assert.assertEquals("L530", this.getStringEncoder().encode1("Lind"));
        this.getStringEncoder();
        Assert.assertEquals("L222", this.getStringEncoder().encode1("Lukaschowsky"));
        this.getStringEncoder();
        Assert.assertEquals("M235", this.getStringEncoder().encode1("McDonnell"));
        this.getStringEncoder();
        Assert.assertEquals("M200", this.getStringEncoder().encode1("McGee"));
        this.getStringEncoder();
        Assert.assertEquals("O155", this.getStringEncoder().encode1("Opnian"));
    }

    @Test
    public void testEncodeBatch2_test24_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
        this.getStringEncoder();
        Assert.assertEquals("H431", this.getStringEncoder().encode1("Hildebrand"));
        this.getStringEncoder();
        Assert.assertEquals("K152", this.getStringEncoder().encode1("Kavanagh"));
        this.getStringEncoder();
        Assert.assertEquals("L530", this.getStringEncoder().encode1("Lind"));
        this.getStringEncoder();
        Assert.assertEquals("L222", this.getStringEncoder().encode1("Lukaschowsky"));
        this.getStringEncoder();
        Assert.assertEquals("M235", this.getStringEncoder().encode1("McDonnell"));
        this.getStringEncoder();
        Assert.assertEquals("M200", this.getStringEncoder().encode1("McGee"));
        this.getStringEncoder();
        Assert.assertEquals("O155", this.getStringEncoder().encode1("Opnian"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch2_test25_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
        this.getStringEncoder();
        Assert.assertEquals("H431", this.getStringEncoder().encode1("Hildebrand"));
        this.getStringEncoder();
        Assert.assertEquals("K152", this.getStringEncoder().encode1("Kavanagh"));
        this.getStringEncoder();
        Assert.assertEquals("L530", this.getStringEncoder().encode1("Lind"));
        this.getStringEncoder();
        Assert.assertEquals("L222", this.getStringEncoder().encode1("Lukaschowsky"));
        this.getStringEncoder();
        Assert.assertEquals("M235", this.getStringEncoder().encode1("McDonnell"));
        this.getStringEncoder();
        Assert.assertEquals("M200", this.getStringEncoder().encode1("McGee"));
        this.getStringEncoder();
        Assert.assertEquals("O155", this.getStringEncoder().encode1("Opnian"));
        this.getStringEncoder();
        Assert.assertEquals("O155", this.getStringEncoder().encode1("Oppenheimer"));
    }

    @Test
    public void testEncodeBatch2_test26_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
        this.getStringEncoder();
        Assert.assertEquals("H431", this.getStringEncoder().encode1("Hildebrand"));
        this.getStringEncoder();
        Assert.assertEquals("K152", this.getStringEncoder().encode1("Kavanagh"));
        this.getStringEncoder();
        Assert.assertEquals("L530", this.getStringEncoder().encode1("Lind"));
        this.getStringEncoder();
        Assert.assertEquals("L222", this.getStringEncoder().encode1("Lukaschowsky"));
        this.getStringEncoder();
        Assert.assertEquals("M235", this.getStringEncoder().encode1("McDonnell"));
        this.getStringEncoder();
        Assert.assertEquals("M200", this.getStringEncoder().encode1("McGee"));
        this.getStringEncoder();
        Assert.assertEquals("O155", this.getStringEncoder().encode1("Opnian"));
        this.getStringEncoder();
        Assert.assertEquals("O155", this.getStringEncoder().encode1("Oppenheimer"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch2_test27_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
        this.getStringEncoder();
        Assert.assertEquals("H431", this.getStringEncoder().encode1("Hildebrand"));
        this.getStringEncoder();
        Assert.assertEquals("K152", this.getStringEncoder().encode1("Kavanagh"));
        this.getStringEncoder();
        Assert.assertEquals("L530", this.getStringEncoder().encode1("Lind"));
        this.getStringEncoder();
        Assert.assertEquals("L222", this.getStringEncoder().encode1("Lukaschowsky"));
        this.getStringEncoder();
        Assert.assertEquals("M235", this.getStringEncoder().encode1("McDonnell"));
        this.getStringEncoder();
        Assert.assertEquals("M200", this.getStringEncoder().encode1("McGee"));
        this.getStringEncoder();
        Assert.assertEquals("O155", this.getStringEncoder().encode1("Opnian"));
        this.getStringEncoder();
        Assert.assertEquals("O155", this.getStringEncoder().encode1("Oppenheimer"));
        this.getStringEncoder();
        Assert.assertEquals("R355", this.getStringEncoder().encode1("Riedemanas"));
    }

    @Test
    public void testEncodeBatch2_test28_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
        this.getStringEncoder();
        Assert.assertEquals("H431", this.getStringEncoder().encode1("Hildebrand"));
        this.getStringEncoder();
        Assert.assertEquals("K152", this.getStringEncoder().encode1("Kavanagh"));
        this.getStringEncoder();
        Assert.assertEquals("L530", this.getStringEncoder().encode1("Lind"));
        this.getStringEncoder();
        Assert.assertEquals("L222", this.getStringEncoder().encode1("Lukaschowsky"));
        this.getStringEncoder();
        Assert.assertEquals("M235", this.getStringEncoder().encode1("McDonnell"));
        this.getStringEncoder();
        Assert.assertEquals("M200", this.getStringEncoder().encode1("McGee"));
        this.getStringEncoder();
        Assert.assertEquals("O155", this.getStringEncoder().encode1("Opnian"));
        this.getStringEncoder();
        Assert.assertEquals("O155", this.getStringEncoder().encode1("Oppenheimer"));
        this.getStringEncoder();
        Assert.assertEquals("R355", this.getStringEncoder().encode1("Riedemanas"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch2_test29_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
        this.getStringEncoder();
        Assert.assertEquals("H431", this.getStringEncoder().encode1("Hildebrand"));
        this.getStringEncoder();
        Assert.assertEquals("K152", this.getStringEncoder().encode1("Kavanagh"));
        this.getStringEncoder();
        Assert.assertEquals("L530", this.getStringEncoder().encode1("Lind"));
        this.getStringEncoder();
        Assert.assertEquals("L222", this.getStringEncoder().encode1("Lukaschowsky"));
        this.getStringEncoder();
        Assert.assertEquals("M235", this.getStringEncoder().encode1("McDonnell"));
        this.getStringEncoder();
        Assert.assertEquals("M200", this.getStringEncoder().encode1("McGee"));
        this.getStringEncoder();
        Assert.assertEquals("O155", this.getStringEncoder().encode1("Opnian"));
        this.getStringEncoder();
        Assert.assertEquals("O155", this.getStringEncoder().encode1("Oppenheimer"));
        this.getStringEncoder();
        Assert.assertEquals("R355", this.getStringEncoder().encode1("Riedemanas"));
        this.getStringEncoder();
        Assert.assertEquals("Z300", this.getStringEncoder().encode1("Zita"));
    }

    @Test
    public void testEncodeBatch2_test30_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
        this.getStringEncoder();
        Assert.assertEquals("H431", this.getStringEncoder().encode1("Hildebrand"));
        this.getStringEncoder();
        Assert.assertEquals("K152", this.getStringEncoder().encode1("Kavanagh"));
        this.getStringEncoder();
        Assert.assertEquals("L530", this.getStringEncoder().encode1("Lind"));
        this.getStringEncoder();
        Assert.assertEquals("L222", this.getStringEncoder().encode1("Lukaschowsky"));
        this.getStringEncoder();
        Assert.assertEquals("M235", this.getStringEncoder().encode1("McDonnell"));
        this.getStringEncoder();
        Assert.assertEquals("M200", this.getStringEncoder().encode1("McGee"));
        this.getStringEncoder();
        Assert.assertEquals("O155", this.getStringEncoder().encode1("Opnian"));
        this.getStringEncoder();
        Assert.assertEquals("O155", this.getStringEncoder().encode1("Oppenheimer"));
        this.getStringEncoder();
        Assert.assertEquals("R355", this.getStringEncoder().encode1("Riedemanas"));
        this.getStringEncoder();
        Assert.assertEquals("Z300", this.getStringEncoder().encode1("Zita"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch2_test31_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        this.getStringEncoder();
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        this.getStringEncoder();
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        this.getStringEncoder();
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        this.getStringEncoder();
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
        this.getStringEncoder();
        Assert.assertEquals("H431", this.getStringEncoder().encode1("Hildebrand"));
        this.getStringEncoder();
        Assert.assertEquals("K152", this.getStringEncoder().encode1("Kavanagh"));
        this.getStringEncoder();
        Assert.assertEquals("L530", this.getStringEncoder().encode1("Lind"));
        this.getStringEncoder();
        Assert.assertEquals("L222", this.getStringEncoder().encode1("Lukaschowsky"));
        this.getStringEncoder();
        Assert.assertEquals("M235", this.getStringEncoder().encode1("McDonnell"));
        this.getStringEncoder();
        Assert.assertEquals("M200", this.getStringEncoder().encode1("McGee"));
        this.getStringEncoder();
        Assert.assertEquals("O155", this.getStringEncoder().encode1("Opnian"));
        this.getStringEncoder();
        Assert.assertEquals("O155", this.getStringEncoder().encode1("Oppenheimer"));
        this.getStringEncoder();
        Assert.assertEquals("R355", this.getStringEncoder().encode1("Riedemanas"));
        this.getStringEncoder();
        Assert.assertEquals("Z300", this.getStringEncoder().encode1("Zita"));
        this.getStringEncoder();
        Assert.assertEquals("Z325", this.getStringEncoder().encode1("Zitzmeinn"));
    }

    @Test
    public void testEncodeBatch3_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch3_test1_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("W252", this.getStringEncoder().encode1("Washington"));
    }

    @Test
    public void testEncodeBatch3_test2_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("W252", this.getStringEncoder().encode1("Washington"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch3_test3_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("W252", this.getStringEncoder().encode1("Washington"));
        this.getStringEncoder();
        Assert.assertEquals("L000", this.getStringEncoder().encode1("Lee"));
    }

    @Test
    public void testEncodeBatch3_test4_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("W252", this.getStringEncoder().encode1("Washington"));
        this.getStringEncoder();
        Assert.assertEquals("L000", this.getStringEncoder().encode1("Lee"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch3_test5_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("W252", this.getStringEncoder().encode1("Washington"));
        this.getStringEncoder();
        Assert.assertEquals("L000", this.getStringEncoder().encode1("Lee"));
        this.getStringEncoder();
        Assert.assertEquals("G362", this.getStringEncoder().encode1("Gutierrez"));
    }

    @Test
    public void testEncodeBatch3_test6_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("W252", this.getStringEncoder().encode1("Washington"));
        this.getStringEncoder();
        Assert.assertEquals("L000", this.getStringEncoder().encode1("Lee"));
        this.getStringEncoder();
        Assert.assertEquals("G362", this.getStringEncoder().encode1("Gutierrez"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch3_test7_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("W252", this.getStringEncoder().encode1("Washington"));
        this.getStringEncoder();
        Assert.assertEquals("L000", this.getStringEncoder().encode1("Lee"));
        this.getStringEncoder();
        Assert.assertEquals("G362", this.getStringEncoder().encode1("Gutierrez"));
        this.getStringEncoder();
        Assert.assertEquals("P236", this.getStringEncoder().encode1("Pfister"));
    }

    @Test
    public void testEncodeBatch3_test8_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("W252", this.getStringEncoder().encode1("Washington"));
        this.getStringEncoder();
        Assert.assertEquals("L000", this.getStringEncoder().encode1("Lee"));
        this.getStringEncoder();
        Assert.assertEquals("G362", this.getStringEncoder().encode1("Gutierrez"));
        this.getStringEncoder();
        Assert.assertEquals("P236", this.getStringEncoder().encode1("Pfister"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch3_test9_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("W252", this.getStringEncoder().encode1("Washington"));
        this.getStringEncoder();
        Assert.assertEquals("L000", this.getStringEncoder().encode1("Lee"));
        this.getStringEncoder();
        Assert.assertEquals("G362", this.getStringEncoder().encode1("Gutierrez"));
        this.getStringEncoder();
        Assert.assertEquals("P236", this.getStringEncoder().encode1("Pfister"));
        this.getStringEncoder();
        Assert.assertEquals("J250", this.getStringEncoder().encode1("Jackson"));
    }

    @Test
    public void testEncodeBatch3_test10_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("W252", this.getStringEncoder().encode1("Washington"));
        this.getStringEncoder();
        Assert.assertEquals("L000", this.getStringEncoder().encode1("Lee"));
        this.getStringEncoder();
        Assert.assertEquals("G362", this.getStringEncoder().encode1("Gutierrez"));
        this.getStringEncoder();
        Assert.assertEquals("P236", this.getStringEncoder().encode1("Pfister"));
        this.getStringEncoder();
        Assert.assertEquals("J250", this.getStringEncoder().encode1("Jackson"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch3_test11_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("W252", this.getStringEncoder().encode1("Washington"));
        this.getStringEncoder();
        Assert.assertEquals("L000", this.getStringEncoder().encode1("Lee"));
        this.getStringEncoder();
        Assert.assertEquals("G362", this.getStringEncoder().encode1("Gutierrez"));
        this.getStringEncoder();
        Assert.assertEquals("P236", this.getStringEncoder().encode1("Pfister"));
        this.getStringEncoder();
        Assert.assertEquals("J250", this.getStringEncoder().encode1("Jackson"));
        this.getStringEncoder();
        Assert.assertEquals("T522", this.getStringEncoder().encode1("Tymczak"));
    }

    @Test
    public void testEncodeBatch3_test12_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("W252", this.getStringEncoder().encode1("Washington"));
        this.getStringEncoder();
        Assert.assertEquals("L000", this.getStringEncoder().encode1("Lee"));
        this.getStringEncoder();
        Assert.assertEquals("G362", this.getStringEncoder().encode1("Gutierrez"));
        this.getStringEncoder();
        Assert.assertEquals("P236", this.getStringEncoder().encode1("Pfister"));
        this.getStringEncoder();
        Assert.assertEquals("J250", this.getStringEncoder().encode1("Jackson"));
        this.getStringEncoder();
        Assert.assertEquals("T522", this.getStringEncoder().encode1("Tymczak"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch3_test13_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("W252", this.getStringEncoder().encode1("Washington"));
        this.getStringEncoder();
        Assert.assertEquals("L000", this.getStringEncoder().encode1("Lee"));
        this.getStringEncoder();
        Assert.assertEquals("G362", this.getStringEncoder().encode1("Gutierrez"));
        this.getStringEncoder();
        Assert.assertEquals("P236", this.getStringEncoder().encode1("Pfister"));
        this.getStringEncoder();
        Assert.assertEquals("J250", this.getStringEncoder().encode1("Jackson"));
        this.getStringEncoder();
        Assert.assertEquals("T522", this.getStringEncoder().encode1("Tymczak"));
        this.getStringEncoder();
        Assert.assertEquals("V532", this.getStringEncoder().encode1("VanDeusen"));
    }

    @Test
    public void testEncodeBatch4_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch4_test1_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("H452", this.getStringEncoder().encode1("HOLMES"));
    }

    @Test
    public void testEncodeBatch4_test2_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("H452", this.getStringEncoder().encode1("HOLMES"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch4_test3_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("H452", this.getStringEncoder().encode1("HOLMES"));
        this.getStringEncoder();
        Assert.assertEquals("A355", this.getStringEncoder().encode1("ADOMOMI"));
    }

    @Test
    public void testEncodeBatch4_test4_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("H452", this.getStringEncoder().encode1("HOLMES"));
        this.getStringEncoder();
        Assert.assertEquals("A355", this.getStringEncoder().encode1("ADOMOMI"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch4_test5_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("H452", this.getStringEncoder().encode1("HOLMES"));
        this.getStringEncoder();
        Assert.assertEquals("A355", this.getStringEncoder().encode1("ADOMOMI"));
        this.getStringEncoder();
        Assert.assertEquals("V536", this.getStringEncoder().encode1("VONDERLEHR"));
    }

    @Test
    public void testEncodeBatch4_test6_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("H452", this.getStringEncoder().encode1("HOLMES"));
        this.getStringEncoder();
        Assert.assertEquals("A355", this.getStringEncoder().encode1("ADOMOMI"));
        this.getStringEncoder();
        Assert.assertEquals("V536", this.getStringEncoder().encode1("VONDERLEHR"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch4_test7_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("H452", this.getStringEncoder().encode1("HOLMES"));
        this.getStringEncoder();
        Assert.assertEquals("A355", this.getStringEncoder().encode1("ADOMOMI"));
        this.getStringEncoder();
        Assert.assertEquals("V536", this.getStringEncoder().encode1("VONDERLEHR"));
        this.getStringEncoder();
        Assert.assertEquals("B400", this.getStringEncoder().encode1("BALL"));
    }

    @Test
    public void testEncodeBatch4_test8_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("H452", this.getStringEncoder().encode1("HOLMES"));
        this.getStringEncoder();
        Assert.assertEquals("A355", this.getStringEncoder().encode1("ADOMOMI"));
        this.getStringEncoder();
        Assert.assertEquals("V536", this.getStringEncoder().encode1("VONDERLEHR"));
        this.getStringEncoder();
        Assert.assertEquals("B400", this.getStringEncoder().encode1("BALL"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch4_test9_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("H452", this.getStringEncoder().encode1("HOLMES"));
        this.getStringEncoder();
        Assert.assertEquals("A355", this.getStringEncoder().encode1("ADOMOMI"));
        this.getStringEncoder();
        Assert.assertEquals("V536", this.getStringEncoder().encode1("VONDERLEHR"));
        this.getStringEncoder();
        Assert.assertEquals("B400", this.getStringEncoder().encode1("BALL"));
        this.getStringEncoder();
        Assert.assertEquals("S000", this.getStringEncoder().encode1("SHAW"));
    }

    @Test
    public void testEncodeBatch4_test10_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("H452", this.getStringEncoder().encode1("HOLMES"));
        this.getStringEncoder();
        Assert.assertEquals("A355", this.getStringEncoder().encode1("ADOMOMI"));
        this.getStringEncoder();
        Assert.assertEquals("V536", this.getStringEncoder().encode1("VONDERLEHR"));
        this.getStringEncoder();
        Assert.assertEquals("B400", this.getStringEncoder().encode1("BALL"));
        this.getStringEncoder();
        Assert.assertEquals("S000", this.getStringEncoder().encode1("SHAW"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch4_test11_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("H452", this.getStringEncoder().encode1("HOLMES"));
        this.getStringEncoder();
        Assert.assertEquals("A355", this.getStringEncoder().encode1("ADOMOMI"));
        this.getStringEncoder();
        Assert.assertEquals("V536", this.getStringEncoder().encode1("VONDERLEHR"));
        this.getStringEncoder();
        Assert.assertEquals("B400", this.getStringEncoder().encode1("BALL"));
        this.getStringEncoder();
        Assert.assertEquals("S000", this.getStringEncoder().encode1("SHAW"));
        this.getStringEncoder();
        Assert.assertEquals("J250", this.getStringEncoder().encode1("JACKSON"));
    }

    @Test
    public void testEncodeBatch4_test12_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("H452", this.getStringEncoder().encode1("HOLMES"));
        this.getStringEncoder();
        Assert.assertEquals("A355", this.getStringEncoder().encode1("ADOMOMI"));
        this.getStringEncoder();
        Assert.assertEquals("V536", this.getStringEncoder().encode1("VONDERLEHR"));
        this.getStringEncoder();
        Assert.assertEquals("B400", this.getStringEncoder().encode1("BALL"));
        this.getStringEncoder();
        Assert.assertEquals("S000", this.getStringEncoder().encode1("SHAW"));
        this.getStringEncoder();
        Assert.assertEquals("J250", this.getStringEncoder().encode1("JACKSON"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch4_test13_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("H452", this.getStringEncoder().encode1("HOLMES"));
        this.getStringEncoder();
        Assert.assertEquals("A355", this.getStringEncoder().encode1("ADOMOMI"));
        this.getStringEncoder();
        Assert.assertEquals("V536", this.getStringEncoder().encode1("VONDERLEHR"));
        this.getStringEncoder();
        Assert.assertEquals("B400", this.getStringEncoder().encode1("BALL"));
        this.getStringEncoder();
        Assert.assertEquals("S000", this.getStringEncoder().encode1("SHAW"));
        this.getStringEncoder();
        Assert.assertEquals("J250", this.getStringEncoder().encode1("JACKSON"));
        this.getStringEncoder();
        Assert.assertEquals("S545", this.getStringEncoder().encode1("SCANLON"));
    }

    @Test
    public void testEncodeBatch4_test14_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("H452", this.getStringEncoder().encode1("HOLMES"));
        this.getStringEncoder();
        Assert.assertEquals("A355", this.getStringEncoder().encode1("ADOMOMI"));
        this.getStringEncoder();
        Assert.assertEquals("V536", this.getStringEncoder().encode1("VONDERLEHR"));
        this.getStringEncoder();
        Assert.assertEquals("B400", this.getStringEncoder().encode1("BALL"));
        this.getStringEncoder();
        Assert.assertEquals("S000", this.getStringEncoder().encode1("SHAW"));
        this.getStringEncoder();
        Assert.assertEquals("J250", this.getStringEncoder().encode1("JACKSON"));
        this.getStringEncoder();
        Assert.assertEquals("S545", this.getStringEncoder().encode1("SCANLON"));
        this.getStringEncoder();
    }

    @Test
    public void testEncodeBatch4_test15_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("H452", this.getStringEncoder().encode1("HOLMES"));
        this.getStringEncoder();
        Assert.assertEquals("A355", this.getStringEncoder().encode1("ADOMOMI"));
        this.getStringEncoder();
        Assert.assertEquals("V536", this.getStringEncoder().encode1("VONDERLEHR"));
        this.getStringEncoder();
        Assert.assertEquals("B400", this.getStringEncoder().encode1("BALL"));
        this.getStringEncoder();
        Assert.assertEquals("S000", this.getStringEncoder().encode1("SHAW"));
        this.getStringEncoder();
        Assert.assertEquals("J250", this.getStringEncoder().encode1("JACKSON"));
        this.getStringEncoder();
        Assert.assertEquals("S545", this.getStringEncoder().encode1("SCANLON"));
        this.getStringEncoder();
        Assert.assertEquals("S532", this.getStringEncoder().encode1("SAINTJOHN"));
    }

    @Test
    public void testEncodeIgnoreApostrophes_test0_decomposed() throws EncoderException {
        this.checkEncodingVariations(
                "O165",
                new String[] {
                    "OBrien", "'OBrien", "O'Brien", "OB'rien", "OBr'ien", "OBri'en", "OBrie'n",
                    "OBrien'"
                });
    }

    @Test
    public void testEncodeIgnoreHyphens_test0_decomposed() throws EncoderException {
        this.checkEncodingVariations(
                "K525",
                new String[] {
                    "KINGSMITH",
                    "-KINGSMITH",
                    "K-INGSMITH",
                    "KI-NGSMITH",
                    "KIN-GSMITH",
                    "KING-SMITH",
                    "KINGS-MITH",
                    "KINGSM-ITH",
                    "KINGSMI-TH",
                    "KINGSMIT-H",
                    "KINGSMITH-"
                });
    }

    @Test
    public void testEncodeIgnoreTrimmable_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testEncodeIgnoreTrimmable_test1_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("W252", this.getStringEncoder().encode1(" \t\n\r Washington \t\n\r "));
    }

    @Test
    public void testHWRuleEx1_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testHWRuleEx1_test1_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcraft"));
    }

    @Test
    public void testHWRuleEx1_test2_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcraft"));
        this.getStringEncoder();
    }

    @Test
    public void testHWRuleEx1_test3_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcraft"));
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcroft"));
    }

    @Test
    public void testHWRuleEx1_test4_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcraft"));
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcroft"));
        this.getStringEncoder();
    }

    @Test
    public void testHWRuleEx1_test5_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcraft"));
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcroft"));
        this.getStringEncoder();
        Assert.assertEquals("Y330", this.getStringEncoder().encode1("yehudit"));
    }

    @Test
    public void testHWRuleEx1_test6_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcraft"));
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcroft"));
        this.getStringEncoder();
        Assert.assertEquals("Y330", this.getStringEncoder().encode1("yehudit"));
        this.getStringEncoder();
    }

    @Test
    public void testHWRuleEx1_test7_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcraft"));
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcroft"));
        this.getStringEncoder();
        Assert.assertEquals("Y330", this.getStringEncoder().encode1("yehudit"));
        this.getStringEncoder();
        Assert.assertEquals("Y330", this.getStringEncoder().encode1("yhwdyt"));
    }

    @Test
    public void testHWRuleEx2_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testHWRuleEx2_test1_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("B312", this.getStringEncoder().encode1("BOOTHDAVIS"));
    }

    @Test
    public void testHWRuleEx2_test2_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("B312", this.getStringEncoder().encode1("BOOTHDAVIS"));
        this.getStringEncoder();
    }

    @Test
    public void testHWRuleEx2_test3_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("B312", this.getStringEncoder().encode1("BOOTHDAVIS"));
        this.getStringEncoder();
        Assert.assertEquals("B312", this.getStringEncoder().encode1("BOOTH-DAVIS"));
    }

    @Test
    public void testHWRuleEx3_test0_decomposed() throws EncoderException {
        this.getStringEncoder();
    }

    @Test
    public void testHWRuleEx3_test1_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals("S460", this.getStringEncoder().encode1("Sgler"));
    }

    @Test
    public void testHWRuleEx3_test2_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals("S460", this.getStringEncoder().encode1("Sgler"));
        this.getStringEncoder();
    }

    @Test
    public void testHWRuleEx3_test3_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals("S460", this.getStringEncoder().encode1("Sgler"));
        this.getStringEncoder();
        Assert.assertEquals("S460", this.getStringEncoder().encode1("Swhgler"));
    }

    @Test
    public void testHWRuleEx3_test4_decomposed() throws EncoderException {
        this.getStringEncoder();
        Assert.assertEquals("S460", this.getStringEncoder().encode1("Sgler"));
        this.getStringEncoder();
        Assert.assertEquals("S460", this.getStringEncoder().encode1("Swhgler"));
        this.checkEncodingVariations(
                "S460",
                new String[] {
                    "SAILOR",
                    "SALYER",
                    "SAYLOR",
                    "SCHALLER",
                    "SCHELLER",
                    "SCHILLER",
                    "SCHOOLER",
                    "SCHULER",
                    "SCHUYLER",
                    "SEILER",
                    "SEYLER",
                    "SHOLAR",
                    "SHULER",
                    "SILAR",
                    "SILER",
                    "SILLER"
                });
    }

    @Test
    public void testMsSqlServer1_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testMsSqlServer1_test1_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("S530", this.getStringEncoder().encode1("Smith"));
    }

    @Test
    public void testMsSqlServer1_test2_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("S530", this.getStringEncoder().encode1("Smith"));
        this.getStringEncoder();
    }

    @Test
    public void testMsSqlServer1_test3_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("S530", this.getStringEncoder().encode1("Smith"));
        this.getStringEncoder();
        Assert.assertEquals("S530", this.getStringEncoder().encode1("Smythe"));
    }

    @Test
    public void testMsSqlServer2_test0_decomposed() throws EncoderException {
        this.checkEncodingVariations(
                "E625",
                new String[] {"Erickson", "Erickson", "Erikson", "Ericson", "Ericksen", "Ericsen"});
    }

    @Test
    public void testMsSqlServer3_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testMsSqlServer3_test1_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A500", this.getStringEncoder().encode1("Ann"));
    }

    @Test
    public void testMsSqlServer3_test2_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A500", this.getStringEncoder().encode1("Ann"));
        this.getStringEncoder();
    }

    @Test
    public void testMsSqlServer3_test3_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A500", this.getStringEncoder().encode1("Ann"));
        this.getStringEncoder();
        Assert.assertEquals("A536", this.getStringEncoder().encode1("Andrew"));
    }

    @Test
    public void testMsSqlServer3_test4_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A500", this.getStringEncoder().encode1("Ann"));
        this.getStringEncoder();
        Assert.assertEquals("A536", this.getStringEncoder().encode1("Andrew"));
        this.getStringEncoder();
    }

    @Test
    public void testMsSqlServer3_test5_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A500", this.getStringEncoder().encode1("Ann"));
        this.getStringEncoder();
        Assert.assertEquals("A536", this.getStringEncoder().encode1("Andrew"));
        this.getStringEncoder();
        Assert.assertEquals("J530", this.getStringEncoder().encode1("Janet"));
    }

    @Test
    public void testMsSqlServer3_test6_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A500", this.getStringEncoder().encode1("Ann"));
        this.getStringEncoder();
        Assert.assertEquals("A536", this.getStringEncoder().encode1("Andrew"));
        this.getStringEncoder();
        Assert.assertEquals("J530", this.getStringEncoder().encode1("Janet"));
        this.getStringEncoder();
    }

    @Test
    public void testMsSqlServer3_test7_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A500", this.getStringEncoder().encode1("Ann"));
        this.getStringEncoder();
        Assert.assertEquals("A536", this.getStringEncoder().encode1("Andrew"));
        this.getStringEncoder();
        Assert.assertEquals("J530", this.getStringEncoder().encode1("Janet"));
        this.getStringEncoder();
        Assert.assertEquals("M626", this.getStringEncoder().encode1("Margaret"));
    }

    @Test
    public void testMsSqlServer3_test8_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A500", this.getStringEncoder().encode1("Ann"));
        this.getStringEncoder();
        Assert.assertEquals("A536", this.getStringEncoder().encode1("Andrew"));
        this.getStringEncoder();
        Assert.assertEquals("J530", this.getStringEncoder().encode1("Janet"));
        this.getStringEncoder();
        Assert.assertEquals("M626", this.getStringEncoder().encode1("Margaret"));
        this.getStringEncoder();
    }

    @Test
    public void testMsSqlServer3_test9_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A500", this.getStringEncoder().encode1("Ann"));
        this.getStringEncoder();
        Assert.assertEquals("A536", this.getStringEncoder().encode1("Andrew"));
        this.getStringEncoder();
        Assert.assertEquals("J530", this.getStringEncoder().encode1("Janet"));
        this.getStringEncoder();
        Assert.assertEquals("M626", this.getStringEncoder().encode1("Margaret"));
        this.getStringEncoder();
        Assert.assertEquals("S315", this.getStringEncoder().encode1("Steven"));
    }

    @Test
    public void testMsSqlServer3_test10_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A500", this.getStringEncoder().encode1("Ann"));
        this.getStringEncoder();
        Assert.assertEquals("A536", this.getStringEncoder().encode1("Andrew"));
        this.getStringEncoder();
        Assert.assertEquals("J530", this.getStringEncoder().encode1("Janet"));
        this.getStringEncoder();
        Assert.assertEquals("M626", this.getStringEncoder().encode1("Margaret"));
        this.getStringEncoder();
        Assert.assertEquals("S315", this.getStringEncoder().encode1("Steven"));
        this.getStringEncoder();
    }

    @Test
    public void testMsSqlServer3_test11_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A500", this.getStringEncoder().encode1("Ann"));
        this.getStringEncoder();
        Assert.assertEquals("A536", this.getStringEncoder().encode1("Andrew"));
        this.getStringEncoder();
        Assert.assertEquals("J530", this.getStringEncoder().encode1("Janet"));
        this.getStringEncoder();
        Assert.assertEquals("M626", this.getStringEncoder().encode1("Margaret"));
        this.getStringEncoder();
        Assert.assertEquals("S315", this.getStringEncoder().encode1("Steven"));
        this.getStringEncoder();
        Assert.assertEquals("M240", this.getStringEncoder().encode1("Michael"));
    }

    @Test
    public void testMsSqlServer3_test12_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A500", this.getStringEncoder().encode1("Ann"));
        this.getStringEncoder();
        Assert.assertEquals("A536", this.getStringEncoder().encode1("Andrew"));
        this.getStringEncoder();
        Assert.assertEquals("J530", this.getStringEncoder().encode1("Janet"));
        this.getStringEncoder();
        Assert.assertEquals("M626", this.getStringEncoder().encode1("Margaret"));
        this.getStringEncoder();
        Assert.assertEquals("S315", this.getStringEncoder().encode1("Steven"));
        this.getStringEncoder();
        Assert.assertEquals("M240", this.getStringEncoder().encode1("Michael"));
        this.getStringEncoder();
    }

    @Test
    public void testMsSqlServer3_test13_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A500", this.getStringEncoder().encode1("Ann"));
        this.getStringEncoder();
        Assert.assertEquals("A536", this.getStringEncoder().encode1("Andrew"));
        this.getStringEncoder();
        Assert.assertEquals("J530", this.getStringEncoder().encode1("Janet"));
        this.getStringEncoder();
        Assert.assertEquals("M626", this.getStringEncoder().encode1("Margaret"));
        this.getStringEncoder();
        Assert.assertEquals("S315", this.getStringEncoder().encode1("Steven"));
        this.getStringEncoder();
        Assert.assertEquals("M240", this.getStringEncoder().encode1("Michael"));
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Robert"));
    }

    @Test
    public void testMsSqlServer3_test14_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A500", this.getStringEncoder().encode1("Ann"));
        this.getStringEncoder();
        Assert.assertEquals("A536", this.getStringEncoder().encode1("Andrew"));
        this.getStringEncoder();
        Assert.assertEquals("J530", this.getStringEncoder().encode1("Janet"));
        this.getStringEncoder();
        Assert.assertEquals("M626", this.getStringEncoder().encode1("Margaret"));
        this.getStringEncoder();
        Assert.assertEquals("S315", this.getStringEncoder().encode1("Steven"));
        this.getStringEncoder();
        Assert.assertEquals("M240", this.getStringEncoder().encode1("Michael"));
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Robert"));
        this.getStringEncoder();
    }

    @Test
    public void testMsSqlServer3_test15_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A500", this.getStringEncoder().encode1("Ann"));
        this.getStringEncoder();
        Assert.assertEquals("A536", this.getStringEncoder().encode1("Andrew"));
        this.getStringEncoder();
        Assert.assertEquals("J530", this.getStringEncoder().encode1("Janet"));
        this.getStringEncoder();
        Assert.assertEquals("M626", this.getStringEncoder().encode1("Margaret"));
        this.getStringEncoder();
        Assert.assertEquals("S315", this.getStringEncoder().encode1("Steven"));
        this.getStringEncoder();
        Assert.assertEquals("M240", this.getStringEncoder().encode1("Michael"));
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Robert"));
        this.getStringEncoder();
        Assert.assertEquals("L600", this.getStringEncoder().encode1("Laura"));
    }

    @Test
    public void testMsSqlServer3_test16_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A500", this.getStringEncoder().encode1("Ann"));
        this.getStringEncoder();
        Assert.assertEquals("A536", this.getStringEncoder().encode1("Andrew"));
        this.getStringEncoder();
        Assert.assertEquals("J530", this.getStringEncoder().encode1("Janet"));
        this.getStringEncoder();
        Assert.assertEquals("M626", this.getStringEncoder().encode1("Margaret"));
        this.getStringEncoder();
        Assert.assertEquals("S315", this.getStringEncoder().encode1("Steven"));
        this.getStringEncoder();
        Assert.assertEquals("M240", this.getStringEncoder().encode1("Michael"));
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Robert"));
        this.getStringEncoder();
        Assert.assertEquals("L600", this.getStringEncoder().encode1("Laura"));
        this.getStringEncoder();
    }

    @Test
    public void testMsSqlServer3_test17_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("A500", this.getStringEncoder().encode1("Ann"));
        this.getStringEncoder();
        Assert.assertEquals("A536", this.getStringEncoder().encode1("Andrew"));
        this.getStringEncoder();
        Assert.assertEquals("J530", this.getStringEncoder().encode1("Janet"));
        this.getStringEncoder();
        Assert.assertEquals("M626", this.getStringEncoder().encode1("Margaret"));
        this.getStringEncoder();
        Assert.assertEquals("S315", this.getStringEncoder().encode1("Steven"));
        this.getStringEncoder();
        Assert.assertEquals("M240", this.getStringEncoder().encode1("Michael"));
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Robert"));
        this.getStringEncoder();
        Assert.assertEquals("L600", this.getStringEncoder().encode1("Laura"));
        this.getStringEncoder();
        Assert.assertEquals("A500", this.getStringEncoder().encode1("Anne"));
    }

    @Test
    public void testNewInstance_test0_decomposed()  {
        Assert.assertEquals("W452", new Soundex(3, false, null, null).soundex("Williams"));
    }

    @Test
    public void testNewInstance2_test0_decomposed()  {
        Assert.assertEquals(
                "W452",
                new Soundex(2, false, null, Soundex.US_ENGLISH_MAPPING_STRING.toCharArray())
                        .soundex("Williams"));
    }

    @Test
    public void testNewInstance3_test0_decomposed()  {
        Assert.assertEquals(
                "W452",
                new Soundex(1, false, Soundex.US_ENGLISH_MAPPING_STRING, null).soundex("Williams"));
    }

    @Test
    public void testSoundexUtilsConstructable_test0_decomposed()  {
        new SoundexUtils();
    }

    @Test
    public void testSoundexUtilsNullBehaviour_test0_decomposed()  {
        Assert.assertNull(SoundexUtils.clean(null));
        Assert.assertEquals("", SoundexUtils.clean(""));
    }

    @Test
    public void testSoundexUtilsNullBehaviour_test1_decomposed()  {
        Assert.assertNull(SoundexUtils.clean(null));
        Assert.assertEquals("", SoundexUtils.clean(""));
        Assert.assertEquals(0, SoundexUtils.differenceEncoded(null, ""));
        Assert.assertEquals(0, SoundexUtils.differenceEncoded("", null));
    }

    @Test
    public void testUsEnglishStatic_test0_decomposed()  {
        Assert.assertEquals("W452", Soundex.US_ENGLISH.soundex("Williams"));
    }

    @Test
    public void testUsMappingEWithAcute_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testUsMappingEWithAcute_test1_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("E000", this.getStringEncoder().encode1("e"));
        if (Character.isLetter('\u00e9')) { // e-acute
            try {
                Assert.assertEquals("\u00c9000", this.getStringEncoder().encode1("\u00e9"));
                Assert.fail("Expected IllegalArgumentException not thrown");
            } catch (final IllegalArgumentException e) {
            }
        } else {
            Assert.assertEquals("", this.getStringEncoder().encode1("\u00e9"));
        }
    }

    @Test
    public void testUsMappingOWithDiaeresis_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testUsMappingOWithDiaeresis_test1_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("O000", this.getStringEncoder().encode1("o"));
        if (Character.isLetter('\u00f6')) { // o-umlaut
            try {
                Assert.assertEquals("\u00d6000", this.getStringEncoder().encode1("\u00f6"));
                Assert.fail("Expected IllegalArgumentException not thrown");
            } catch (final IllegalArgumentException e) {
            }
        } else {
            Assert.assertEquals("", this.getStringEncoder().encode1("\u00f6"));
        }
    }

    @Test
    public void testWikipediaAmericanSoundex_test0_decomposed()  {
        this.getStringEncoder();
    }

    @Test
    public void testWikipediaAmericanSoundex_test1_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Robert"));
    }

    @Test
    public void testWikipediaAmericanSoundex_test2_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Robert"));
        this.getStringEncoder();
    }

    @Test
    public void testWikipediaAmericanSoundex_test3_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Robert"));
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Rupert"));
    }

    @Test
    public void testWikipediaAmericanSoundex_test4_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Robert"));
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Rupert"));
        this.getStringEncoder();
    }

    @Test
    public void testWikipediaAmericanSoundex_test5_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Robert"));
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Rupert"));
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcraft"));
    }

    @Test
    public void testWikipediaAmericanSoundex_test6_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Robert"));
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Rupert"));
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcraft"));
        this.getStringEncoder();
    }

    @Test
    public void testWikipediaAmericanSoundex_test7_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Robert"));
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Rupert"));
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcraft"));
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcroft"));
    }

    @Test
    public void testWikipediaAmericanSoundex_test8_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Robert"));
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Rupert"));
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcraft"));
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcroft"));
        this.getStringEncoder();
    }

    @Test
    public void testWikipediaAmericanSoundex_test9_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Robert"));
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Rupert"));
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcraft"));
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcroft"));
        this.getStringEncoder();
        Assert.assertEquals("T522", this.getStringEncoder().encode1("Tymczak"));
    }

    @Test
    public void testWikipediaAmericanSoundex_test10_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Robert"));
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Rupert"));
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcraft"));
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcroft"));
        this.getStringEncoder();
        Assert.assertEquals("T522", this.getStringEncoder().encode1("Tymczak"));
        this.getStringEncoder();
    }

    @Test
    public void testWikipediaAmericanSoundex_test11_decomposed()  {
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Robert"));
        this.getStringEncoder();
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Rupert"));
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcraft"));
        this.getStringEncoder();
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcroft"));
        this.getStringEncoder();
        Assert.assertEquals("T522", this.getStringEncoder().encode1("Tymczak"));
        this.getStringEncoder();
        Assert.assertEquals("P236", this.getStringEncoder().encode1("Pfister"));
    }

    @Test
    public void testGenealogy_test0_decomposed()  {
        final Soundex s = Soundex.US_ENGLISH_GENEALOGY;
        Assert.assertEquals("H251", s.encode1("Heggenburger"));
    }

    @Test
    public void testGenealogy_test1_decomposed()  {
        final Soundex s = Soundex.US_ENGLISH_GENEALOGY;
        Assert.assertEquals("H251", s.encode1("Heggenburger"));
        Assert.assertEquals("B425", s.encode1("Blackman"));
        Assert.assertEquals("S530", s.encode1("Schmidt"));
        Assert.assertEquals("L150", s.encode1("Lippmann"));
        Assert.assertEquals(
                "D200", s.encode1("Dodds"));
        Assert.assertEquals("D200", s.encode1("Dhdds"));
        Assert.assertEquals("D200", s.encode1("Dwdds"));
    }

    @Test
    public void testSimplifiedSoundex_test0_decomposed()  {
        final Soundex s = Soundex.US_ENGLISH_SIMPLIFIED;
        Assert.assertEquals("W452", s.encode1("WILLIAMS"));
    }

    @Test
    public void testSimplifiedSoundex_test1_decomposed()  {
        final Soundex s = Soundex.US_ENGLISH_SIMPLIFIED;
        Assert.assertEquals("W452", s.encode1("WILLIAMS"));
        Assert.assertEquals("B625", s.encode1("BARAGWANATH"));
        Assert.assertEquals("D540", s.encode1("DONNELL"));
        Assert.assertEquals("L300", s.encode1("LLOYD"));
        Assert.assertEquals("W422", s.encode1("WOOLCOCK"));
        Assert.assertEquals("D320", s.encode1("Dodds"));
        Assert.assertEquals("D320", s.encode1("Dwdds"));
        Assert.assertEquals("D320", s.encode1("Dhdds"));
    }
}