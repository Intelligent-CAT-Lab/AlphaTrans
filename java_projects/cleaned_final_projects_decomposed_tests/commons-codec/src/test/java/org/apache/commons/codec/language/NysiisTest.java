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
 * Tests {@link Nysiis}
 *
 * @since 1.7
 */
public class NysiisTest extends StringEncoderAbstractTest<Nysiis> {

    private final Nysiis fullNysiis = new Nysiis(false);

    /**
     * Takes an array of String pairs where each pair's first element is the input and the second
     * element the expected encoding.
     *
     * @param testValues an array of String pairs where each pair's first element is the input and
     *     the second element the expected encoding.
     * @throws EncoderException for some failure scenarios
     */
    private void assertEncodings(final String[]... testValues) throws EncoderException {
        for (final String[] arr : testValues) {
            Assert.assertEquals("Problem with " + arr[0], arr[1], this.fullNysiis.encode1(arr[0]));
        }
    }

    @Override
    protected Nysiis createStringEncoder() {
        return Nysiis.Nysiis1();
    }

    private void encodeAll(final String[] strings, final String expectedEncoding) {
        for (final String string : strings) {
            Assert.assertEquals(
                    "Problem with " + string, expectedEncoding, getStringEncoder().encode1(string));
        }
    }

    

    

    

    

    /**
     * Tests data gathered from around the internet.
     *
     * @see <a
     *     href="http://www.dropby.com/NYSIISTextStrings.html">http://www.dropby.com/NYSIISTextStrings.html</a>
     * @throws EncoderException for some failure scenarios
     */
    

    

    /**
     * Tests data gathered from around the internets.
     *
     * @throws EncoderException for some failure scenarios
     */
    

    /**
     * Tests rule 1: Translate first characters of name: MAC → MCC, KN → N, K → C, PH, PF → FF, SCH
     * → SSS
     *
     * @throws EncoderException for some failure scenarios
     */
    

    /**
     * Tests rule 2: Translate last characters of name: EE → Y, IE → Y, DT, RT, RD, NT, ND → D
     *
     * @throws EncoderException for some failure scenarios
     */
    

    /**
     * Tests rule 4.1: EV → AF else A, E, I, O, U → A
     *
     * @throws EncoderException for some failure scenarios
     */
    

    /**
     * Tests rule 4.2: Q → G, Z → S, M → N
     *
     * @throws EncoderException for some failure scenarios
     */
    

    /**
     * Tests rule 5: If last character is S, remove it.
     *
     * @throws EncoderException for some failure scenarios
     */
    

    /**
     * Tests rule 6: If last characters are AY, replace with Y.
     *
     * @throws EncoderException for some failure scenarios
     */
    

    /**
     * Tests rule 7: If last character is A, remove it.
     *
     * @throws EncoderException for some failure scenarios
     */

    @Test
    public void testBran_test0_decomposed()  {
        encodeAll(new String[] {"Brian", "Brown", "Brun"}, "BRAN");
    }

    @Test
    public void testCap_test0_decomposed()  {
        this.encodeAll(new String[] {"Capp", "Cope", "Copp", "Kipp"}, "CAP");
    }

    @Test
    public void testDad_test0_decomposed()  {
        this.encodeAll(new String[] {"Dent"}, "DAD");
    }

    @Test
    public void testDan_test0_decomposed()  {
        this.encodeAll(new String[] {"Dane", "Dean", "Dionne"}, "DAN");
    }

    @Test
    public void testDropBy_test0_decomposed() throws EncoderException {
        this.assertEncodings(
                new String[] {"MACINTOSH", "MCANT"},
                new String[] {"KNUTH", "NAT"}, // Original: NNAT; modified: NATH
                new String[] {"KOEHN", "CAN"}, // Original: C
                new String[] {"PHILLIPSON", "FALAPSAN"}, // Original: FFALAP[SAN]
                new String[] {"PFEISTER", "FASTAR"}, // Original: FFASTA[R]
                new String[] {"SCHOENHOEFT", "SANAFT"}, // Original: SSANAF[T]
                new String[] {"MCKEE", "MCY"},
                new String[] {"MACKIE", "MCY"},
                new String[] {"HEITSCHMIDT", "HATSNAD"},
                new String[] {"BART", "BAD"},
                new String[] {"HURD", "HAD"},
                new String[] {"HUNT", "HAD"},
                new String[] {"WESTERLUND", "WASTARLAD"},
                new String[] {"CASSTEVENS", "CASTAFAN"},
                new String[] {"VASQUEZ", "VASG"},
                new String[] {"FRAZIER", "FRASAR"},
                new String[] {"BOWMAN", "BANAN"},
                new String[] {"MCKNIGHT", "MCNAGT"},
                new String[] {"RICKERT", "RACAD"},
                new String[] {"DEUTSCH", "DAT"}, // Original: DATS
                new String[] {"WESTPHAL", "WASTFAL"},
                new String[] {"SHRIVER", "SRAVAR"}, // Original: SHRAVA[R]
                new String[] {"KUHL", "CAL"}, // Original: C
                new String[] {"RAWSON", "RASAN"},
                new String[] {"JILES", "JAL"},
                new String[] {"CARRAWAY", "CARY"}, // Original: CARAY
                new String[] {"YAMADA", "YANAD"});
    }

    @Test
    public void testFal_test0_decomposed()  {
        this.encodeAll(new String[] {"Phil"}, "FAL");
    }

    @Test
    public void testOthers_test0_decomposed() throws EncoderException {
        this.assertEncodings(
                new String[] {"O'Daniel", "ODANAL"},
                new String[] {"O'Donnel", "ODANAL"},
                new String[] {"Cory", "CARY"},
                new String[] {"Corey", "CARY"},
                new String[] {"Kory", "CARY"},
                new String[] {"FUZZY", "FASY"});
    }

    @Test
    public void testRule1_test0_decomposed() throws EncoderException {
        this.assertEncodings(
                new String[] {"MACX", "MCX"},
                new String[] {"KNX", "NX"},
                new String[] {"KX", "CX"},
                new String[] {"PHX", "FX"},
                new String[] {"PFX", "FX"},
                new String[] {"SCHX", "SX"});
    }

    @Test
    public void testRule2_test0_decomposed() throws EncoderException {
        this.assertEncodings(
                new String[] {"XEE", "XY"},
                new String[] {"XIE", "XY"},
                new String[] {"XDT", "XD"},
                new String[] {"XRT", "XD"},
                new String[] {"XRD", "XD"},
                new String[] {"XNT", "XD"},
                new String[] {"XND", "XD"});
    }

    @Test
    public void testRule4Dot1_test0_decomposed() throws EncoderException {
        this.assertEncodings(
                new String[] {"XEV", "XAF"},
                new String[] {"XAX", "XAX"},
                new String[] {"XEX", "XAX"},
                new String[] {"XIX", "XAX"},
                new String[] {"XOX", "XAX"},
                new String[] {"XUX", "XAX"});
    }

    @Test
    public void testRule4Dot2_test0_decomposed() throws EncoderException {
        this.assertEncodings(
                new String[] {"XQ", "XG"}, new String[] {"XZ", "X"}, new String[] {"XM", "XN"});
    }

    @Test
    public void testRule5_test0_decomposed() throws EncoderException {
        this.assertEncodings(new String[] {"XS", "X"}, new String[] {"XSS", "X"});
    }

    @Test
    public void testRule6_test0_decomposed() throws EncoderException {
        this.assertEncodings(new String[] {"XAY", "XY"}, new String[] {"XAYS", "XY"});
    }

    @Test
    public void testRule7_test0_decomposed() throws EncoderException {
        this.assertEncodings(new String[] {"XA", "X"}, new String[] {"XAS", "X"});
    }

    @Test
    public void testSnad_test0_decomposed()  {
        this.encodeAll(new String[] {"Schmidt"}, "SNAD");
    }

    @Test
    public void testSnat_test0_decomposed()  {
        this.encodeAll(new String[] {"Smith", "Schmit"}, "SNAT");
    }

    @Test
    public void testSpecialBranches_test0_decomposed()  {
        this.encodeAll(new String[] {"Kobwick"}, "CABWAC");
        this.encodeAll(new String[] {"Kocher"}, "CACAR");
        this.encodeAll(new String[] {"Fesca"}, "FASC");
        this.encodeAll(new String[] {"Shom"}, "SAN");
        this.encodeAll(new String[] {"Ohlo"}, "OL");
        this.encodeAll(new String[] {"Uhu"}, "UH");
        this.encodeAll(new String[] {"Um"}, "UN");
    }

    @Test
    public void testTranan_test0_decomposed()  {
        this.encodeAll(new String[] {"Trueman", "Truman"}, "TRANAN");
    }

    @Test
    public void testTrueVariant_test0_decomposed()  {
        final Nysiis encoder = new Nysiis(true);
    }

    @Test
    public void testTrueVariant_test1_decomposed()  {
        final Nysiis encoder = new Nysiis(true);
        final String encoded = encoder.encode1("WESTERLUND");
    }

    @Test
    public void testTrueVariant_test2_decomposed()  {
        final Nysiis encoder = new Nysiis(true);
        final String encoded = encoder.encode1("WESTERLUND");
        Assert.assertTrue(encoded.length() <= 6);
    }

    @Test
    public void testTrueVariant_test3_decomposed()  {
        final Nysiis encoder = new Nysiis(true);
        final String encoded = encoder.encode1("WESTERLUND");
        Assert.assertTrue(encoded.length() <= 6);
        Assert.assertEquals("WASTAR", encoded);
    }
}