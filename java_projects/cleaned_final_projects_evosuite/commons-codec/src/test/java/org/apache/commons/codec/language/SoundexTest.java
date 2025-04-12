
/*
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
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

    @Test
    public void testB650() throws EncoderException {
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
    public void testBadCharacters() {
        Assert.assertEquals("H452", this.getStringEncoder().encode1("HOL>MES"));
    }

    @Test
    public void testDifference() throws EncoderException {
        Assert.assertEquals(0, this.getStringEncoder().difference(null, null));
        Assert.assertEquals(0, this.getStringEncoder().difference("", ""));
        Assert.assertEquals(0, this.getStringEncoder().difference(" ", " "));
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
        Assert.assertEquals(2, this.getStringEncoder().difference("Ann", "Andrew"));
        Assert.assertEquals(1, this.getStringEncoder().difference("Margaret", "Andrew"));
        Assert.assertEquals(0, this.getStringEncoder().difference("Janet", "Margaret"));
        Assert.assertEquals(4, this.getStringEncoder().difference("Green", "Greene"));
        Assert.assertEquals(0, this.getStringEncoder().difference("Blotchet-Halls", "Greene"));
        Assert.assertEquals(4, this.getStringEncoder().difference("Smith", "Smythe"));
        Assert.assertEquals(4, this.getStringEncoder().difference("Smithers", "Smythers"));
        Assert.assertEquals(2, this.getStringEncoder().difference("Anothers", "Brothers"));
    }

    @Test
    public void testEncodeBasic() {
        Assert.assertEquals("T235", this.getStringEncoder().encode1("testing"));
        Assert.assertEquals("T000", this.getStringEncoder().encode1("The"));
        Assert.assertEquals("Q200", this.getStringEncoder().encode1("quick"));
        Assert.assertEquals("B650", this.getStringEncoder().encode1("brown"));
        Assert.assertEquals("F200", this.getStringEncoder().encode1("fox"));
        Assert.assertEquals("J513", this.getStringEncoder().encode1("jumped"));
        Assert.assertEquals("O160", this.getStringEncoder().encode1("over"));
        Assert.assertEquals("T000", this.getStringEncoder().encode1("the"));
        Assert.assertEquals("L200", this.getStringEncoder().encode1("lazy"));
        Assert.assertEquals("D200", this.getStringEncoder().encode1("dogs"));
    }

    /** Examples from http://www.bradandkathy.com/genealogy/overviewofsoundex.html */
    @Test
    public void testEncodeBatch2() {
        Assert.assertEquals("A462", this.getStringEncoder().encode1("Allricht"));
        Assert.assertEquals("E166", this.getStringEncoder().encode1("Eberhard"));
        Assert.assertEquals("E521", this.getStringEncoder().encode1("Engebrethson"));
        Assert.assertEquals("H512", this.getStringEncoder().encode1("Heimbach"));
        Assert.assertEquals("H524", this.getStringEncoder().encode1("Hanselmann"));
        Assert.assertEquals("H431", this.getStringEncoder().encode1("Hildebrand"));
        Assert.assertEquals("K152", this.getStringEncoder().encode1("Kavanagh"));
        Assert.assertEquals("L530", this.getStringEncoder().encode1("Lind"));
        Assert.assertEquals("L222", this.getStringEncoder().encode1("Lukaschowsky"));
        Assert.assertEquals("M235", this.getStringEncoder().encode1("McDonnell"));
        Assert.assertEquals("M200", this.getStringEncoder().encode1("McGee"));
        Assert.assertEquals("O155", this.getStringEncoder().encode1("Opnian"));
        Assert.assertEquals("O155", this.getStringEncoder().encode1("Oppenheimer"));
        Assert.assertEquals("R355", this.getStringEncoder().encode1("Riedemanas"));
        Assert.assertEquals("Z300", this.getStringEncoder().encode1("Zita"));
        Assert.assertEquals("Z325", this.getStringEncoder().encode1("Zitzmeinn"));
    }

    /** Examples from http://www.archives.gov/research_room/genealogy/census/soundex.html */
    @Test
    public void testEncodeBatch3() {
        Assert.assertEquals("W252", this.getStringEncoder().encode1("Washington"));
        Assert.assertEquals("L000", this.getStringEncoder().encode1("Lee"));
        Assert.assertEquals("G362", this.getStringEncoder().encode1("Gutierrez"));
        Assert.assertEquals("P236", this.getStringEncoder().encode1("Pfister"));
        Assert.assertEquals("J250", this.getStringEncoder().encode1("Jackson"));
        Assert.assertEquals("T522", this.getStringEncoder().encode1("Tymczak"));
        Assert.assertEquals("V532", this.getStringEncoder().encode1("VanDeusen"));
    }

    /** Examples from: http://www.myatt.demon.co.uk/sxalg.htm */
    @Test
    public void testEncodeBatch4() {
        Assert.assertEquals("H452", this.getStringEncoder().encode1("HOLMES"));
        Assert.assertEquals("A355", this.getStringEncoder().encode1("ADOMOMI"));
        Assert.assertEquals("V536", this.getStringEncoder().encode1("VONDERLEHR"));
        Assert.assertEquals("B400", this.getStringEncoder().encode1("BALL"));
        Assert.assertEquals("S000", this.getStringEncoder().encode1("SHAW"));
        Assert.assertEquals("J250", this.getStringEncoder().encode1("JACKSON"));
        Assert.assertEquals("S545", this.getStringEncoder().encode1("SCANLON"));
        Assert.assertEquals("S532", this.getStringEncoder().encode1("SAINTJOHN"));
    }

    @Test
    public void testEncodeIgnoreApostrophes() throws EncoderException {
        this.checkEncodingVariations(
                "O165",
                new String[] {
                    "OBrien", "'OBrien", "O'Brien", "OB'rien", "OBr'ien", "OBri'en", "OBrie'n",
                    "OBrien'"
                });
    }

    /**
     * Test data from http://www.myatt.demon.co.uk/sxalg.htm
     *
     * @throws EncoderException for some failure scenarios
     */
    @Test
    public void testEncodeIgnoreHyphens() throws EncoderException {
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
    public void testEncodeIgnoreTrimmable() {
        Assert.assertEquals("W252", this.getStringEncoder().encode1(" \t\n\r Washington \t\n\r "));
    }

    /** Consonants from the same code group separated by W or H are treated as one. */
    @Test
    public void testHWRuleEx1() {
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcraft"));
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcroft"));
        Assert.assertEquals("Y330", this.getStringEncoder().encode1("yehudit"));
        Assert.assertEquals("Y330", this.getStringEncoder().encode1("yhwdyt"));
    }

    /**
     * Consonants from the same code group separated by W or H are treated as one.
     *
     * <p>Test data from http://www.myatt.demon.co.uk/sxalg.htm
     */
    @Test
    public void testHWRuleEx2() {
        Assert.assertEquals("B312", this.getStringEncoder().encode1("BOOTHDAVIS"));
        Assert.assertEquals("B312", this.getStringEncoder().encode1("BOOTH-DAVIS"));
    }

    /**
     * Consonants from the same code group separated by W or H are treated as one.
     *
     * @throws EncoderException for some failure scenarios
     */
    @Test
    public void testHWRuleEx3() throws EncoderException {
        Assert.assertEquals("S460", this.getStringEncoder().encode1("Sgler"));
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

    /**
     * Examples for MS SQLServer from
     * http://msdn.microsoft.com/library/default.asp?url=/library/en-us/tsqlref/ts_setu-sus_3o6w.asp
     */
    @Test
    public void testMsSqlServer1() {
        Assert.assertEquals("S530", this.getStringEncoder().encode1("Smith"));
        Assert.assertEquals("S530", this.getStringEncoder().encode1("Smythe"));
    }

    /**
     * Examples for MS SQLServer from
     * http://support.microsoft.com/default.aspx?scid=http://support.microsoft.com:80/support
     * /kb/articles/Q100/3/65.asp&NoWebContent=1
     *
     * @throws EncoderException for some failure scenarios
     */
    @Test
    public void testMsSqlServer2() throws EncoderException {
        this.checkEncodingVariations(
                "E625",
                new String[] {"Erickson", "Erickson", "Erikson", "Ericson", "Ericksen", "Ericsen"});
    }

    /** Examples for MS SQLServer from http://databases.about.com/library/weekly/aa042901a.htm */
    @Test
    public void testMsSqlServer3() {
        Assert.assertEquals("A500", this.getStringEncoder().encode1("Ann"));
        Assert.assertEquals("A536", this.getStringEncoder().encode1("Andrew"));
        Assert.assertEquals("J530", this.getStringEncoder().encode1("Janet"));
        Assert.assertEquals("M626", this.getStringEncoder().encode1("Margaret"));
        Assert.assertEquals("S315", this.getStringEncoder().encode1("Steven"));
        Assert.assertEquals("M240", this.getStringEncoder().encode1("Michael"));
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Robert"));
        Assert.assertEquals("L600", this.getStringEncoder().encode1("Laura"));
        Assert.assertEquals("A500", this.getStringEncoder().encode1("Anne"));
    }

    /**
     * https://issues.apache.org/jira/browse/CODEC-54 https://issues.apache.org/jira/browse/CODEC-56
     */
    @Test
    public void testNewInstance() {
        Assert.assertEquals("W452", new Soundex(3, false, null, null).soundex("Williams"));
    }

    @Test
    public void testNewInstance2() {
        Assert.assertEquals(
                "W452",
                new Soundex(2, false, null, Soundex.US_ENGLISH_MAPPING_STRING.toCharArray())
                        .soundex("Williams"));
    }

    @Test
    public void testNewInstance3() {
        Assert.assertEquals(
                "W452",
                new Soundex(1, false, Soundex.US_ENGLISH_MAPPING_STRING, null).soundex("Williams"));
    }

    @Test
    public void testSoundexUtilsConstructable() {
        new SoundexUtils();
    }

    @Test
    public void testSoundexUtilsNullBehaviour() {
        Assert.assertNull(SoundexUtils.clean(null));
        Assert.assertEquals("", SoundexUtils.clean(""));
        Assert.assertEquals(0, SoundexUtils.differenceEncoded(null, ""));
        Assert.assertEquals(0, SoundexUtils.differenceEncoded("", null));
    }

    /**
     * https://issues.apache.org/jira/browse/CODEC-54 https://issues.apache.org/jira/browse/CODEC-56
     */
    @Test
    public void testUsEnglishStatic() {
        Assert.assertEquals("W452", Soundex.US_ENGLISH.soundex("Williams"));
    }

    /**
     * Fancy characters are not mapped by the default US mapping.
     *
     * <p>https://issues.apache.org/jira/browse/CODEC-30
     */
    @Test
    public void testUsMappingEWithAcute() {
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

    /**
     * Fancy characters are not mapped by the default US mapping.
     *
     * <p>https://issues.apache.org/jira/browse/CODEC-30
     */
    @Test
    public void testUsMappingOWithDiaeresis() {
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

    /**
     * Tests example from http://en.wikipedia.org/wiki/Soundex#American_Soundex as of 2015-03-22.
     */
    @Test
    public void testWikipediaAmericanSoundex() {
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Robert"));
        Assert.assertEquals("R163", this.getStringEncoder().encode1("Rupert"));
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcraft"));
        Assert.assertEquals("A261", this.getStringEncoder().encode1("Ashcroft"));
        Assert.assertEquals("T522", this.getStringEncoder().encode1("Tymczak"));
        Assert.assertEquals("P236", this.getStringEncoder().encode1("Pfister"));
    }

    @Test
    public void testGenealogy() { // treat vowels and HW as silent
        final Soundex s = Soundex.US_ENGLISH_GENEALOGY;
        Assert.assertEquals("H251", s.encode1("Heggenburger"));
        Assert.assertEquals("B425", s.encode1("Blackman"));
        Assert.assertEquals("S530", s.encode1("Schmidt"));
        Assert.assertEquals("L150", s.encode1("Lippmann"));
        Assert.assertEquals(
                "D200", s.encode1("Dodds")); // 'o' is not a separator here - it is silent
        Assert.assertEquals("D200", s.encode1("Dhdds")); // 'h' is silent
        Assert.assertEquals("D200", s.encode1("Dwdds")); // 'w' is silent
    }

    @Test
    public void testSimplifiedSoundex() { // treat vowels and HW as separators
        final Soundex s = Soundex.US_ENGLISH_SIMPLIFIED;
        Assert.assertEquals("W452", s.encode1("WILLIAMS"));
        Assert.assertEquals("B625", s.encode1("BARAGWANATH"));
        Assert.assertEquals("D540", s.encode1("DONNELL"));
        Assert.assertEquals("L300", s.encode1("LLOYD"));
        Assert.assertEquals("W422", s.encode1("WOOLCOCK"));
        Assert.assertEquals("D320", s.encode1("Dodds"));
        Assert.assertEquals("D320", s.encode1("Dwdds")); // w is a separator
        Assert.assertEquals("D320", s.encode1("Dhdds")); // h is a separator
    }
}
