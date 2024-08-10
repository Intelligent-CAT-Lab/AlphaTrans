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

package org.apache.commons.codec.language.bm;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.StringEncoder;
import org.apache.commons.codec.StringEncoderAbstractTest;
import org.junit.Assert;
import org.junit.Test;

/**
 * Tests BeiderMorseEncoder.
 *
 * @since 1.6
 */
public class BeiderMorseEncoderTest extends StringEncoderAbstractTest<StringEncoder> {
    private static final char[] TEST_CHARS = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'o', 'u'};

    private void assertNotEmpty(final BeiderMorseEncoder bmpm, final String value)
            throws EncoderException {
        Assert.assertNotEquals(value, "", bmpm.encode1(value));
    }

    private BeiderMorseEncoder createGenericApproxEncoder() {
        final BeiderMorseEncoder encoder = new BeiderMorseEncoder();
        encoder.setNameType(NameType.GENERIC);
        encoder.setRuleType(RuleType.APPROX);
        return encoder;
    }

    @Override
    protected StringEncoder createStringEncoder() {
        return new BeiderMorseEncoder();
    }

    /**
     * Tests we do not blow up.
     *
     * @throws EncoderException for some failure scenarios
     */
    

    

    

    

    /**
     * Tests
     * https://issues.apache.org/jira/browse/CODEC-125?focusedCommentId=13071566&page=com.atlassian.jira.plugin.system.issuetabpanels:
     * comment-tabpanel#comment-13071566
     *
     * @throws EncoderException for some failure scenarios
     */
    

    

    

    

    

    

    

    

    

    

    

    /**
     * (Un)luckily, the worse performing test because of the data in the test characters.
     *
     * @throws EncoderException for some failure scenarios
     */

    @Test
    public void testAllChars_test0_decomposed() throws EncoderException {
        final BeiderMorseEncoder bmpm = createGenericApproxEncoder();
    }

    @Test
    public void testAllChars_test1_decomposed() throws EncoderException {
        final BeiderMorseEncoder bmpm = createGenericApproxEncoder();
        for (char c = Character.MIN_VALUE; c < Character.MAX_VALUE; c++) {
            bmpm.encode1(Character.toString(c));
        }
    }

    @Test
    public void testAsciiEncodeNotEmpty1Letter_test0_decomposed() throws EncoderException {
        final BeiderMorseEncoder bmpm = createGenericApproxEncoder();
    }

    @Test
    public void testAsciiEncodeNotEmpty1Letter_test1_decomposed() throws EncoderException {
        final BeiderMorseEncoder bmpm = createGenericApproxEncoder();
        for (char c = 'a'; c <= 'z'; c++) {
            final String value = Character.toString(c);
            final String valueU = value.toUpperCase();
            assertNotEmpty(bmpm, value);
            assertNotEmpty(bmpm, valueU);
        }
    }

    @Test
    public void testAsciiEncodeNotEmpty2Letters_test0_decomposed() throws EncoderException {
        final BeiderMorseEncoder bmpm = createGenericApproxEncoder();
    }

    @Test
    public void testAsciiEncodeNotEmpty2Letters_test1_decomposed() throws EncoderException {
        final BeiderMorseEncoder bmpm = createGenericApproxEncoder();
        for (char c1 = 'a'; c1 <= 'z'; c1++) {
            for (char c2 = 'a'; c2 <= 'z'; c2++) {
                final String value = new String(new char[] {c1, c2});
                final String valueU = value.toUpperCase();
                assertNotEmpty(bmpm, value);
                assertNotEmpty(bmpm, valueU);
            }
        }
    }

    @Test
    public void testEncodeAtzNotEmpty_test0_decomposed() throws EncoderException {
        final BeiderMorseEncoder bmpm = createGenericApproxEncoder();
    }

    @Test
    public void testEncodeAtzNotEmpty_test1_decomposed() throws EncoderException {
        final BeiderMorseEncoder bmpm = createGenericApproxEncoder();
        final String[] names = {"\u00e1cz", "\u00e1tz", "Ign\u00e1cz", "Ign\u00e1tz", "Ign\u00e1c"};
        for (final String name : names) {
            assertNotEmpty(bmpm, name);
        }
    }

    @Test
    public void testEncodeGna_test0_decomposed() throws EncoderException {
        final BeiderMorseEncoder bmpm = createGenericApproxEncoder();
    }

    @Test
    public void testEncodeGna_test1_decomposed() throws EncoderException {
        final BeiderMorseEncoder bmpm = createGenericApproxEncoder();
        bmpm.encode1("gna");
    }

    @Test(expected = IllegalArgumentException.class)
    public void testInvalidLangIllegalArgumentException_test0_decomposed()  {
        Rule.getInstance1(NameType.GENERIC, RuleType.APPROX, "noSuchLanguage");
    }

    @Test
    public void testInvalidLangIllegalStateException_test0_decomposed()  {
        Languages.getInstance0(NameType.GENERIC);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testInvalidLangIllegalStateException_test1_decomposed()  {
        Languages.getInstance0(NameType.GENERIC);
        Lang.loadFromResource(
                "thisIsAMadeUpResourceName", Languages.getInstance0(NameType.GENERIC));
    }

    @Test(expected = IllegalArgumentException.class)
    public void testInvalidLanguageIllegalArgumentException_test0_decomposed()  {
        Languages.getInstance1("thereIsNoSuchLanguage");
    }

    @Test(timeout = 10000L)
    public void testLongestEnglishSurname_test0_decomposed() throws EncoderException {
        final BeiderMorseEncoder bmpm = createGenericApproxEncoder();
    }

    @Test(timeout = 10000L)
    public void testLongestEnglishSurname_test1_decomposed() throws EncoderException {
        final BeiderMorseEncoder bmpm = createGenericApproxEncoder();
        bmpm.encode1("MacGhilleseatheanaich");
    }

    @Test
    public void testNegativeIndexForRuleMatchIndexOutOfBoundsException_test0_decomposed()  {
        final Rule r = new Rule("a", "", "", new Rule.Phoneme(2, "", Languages.ANY_LANGUAGE, null));
    }

    @Test(expected = IndexOutOfBoundsException.class)
    public void testNegativeIndexForRuleMatchIndexOutOfBoundsException_test1_decomposed()  {
        final Rule r = new Rule("a", "", "", new Rule.Phoneme(2, "", Languages.ANY_LANGUAGE, null));
        r.patternAndContextMatches("bob", -1);
    }

    @Test
    public void testOOM_test0_decomposed() throws EncoderException {
        final String phrase =
                "200697900'-->&#1913348150;</  bceaeef"
                    + " >aadaabcf\"aedfbff<!--\'-->?>caecfaaa><?&#<!--</script>&lang&fc;aadeaf?>>&bdquo<"
                    + "    cc =\"abff\"    /></   afe  ><script><!-- f(';<    cf aefbeef ="
                    + " \"bfabadcf\" ebbfeedd = fccabeb >";
        final BeiderMorseEncoder encoder = new BeiderMorseEncoder();
    }

    @Test
    public void testOOM_test1_decomposed() throws EncoderException {
        final String phrase =
                "200697900'-->&#1913348150;</  bceaeef"
                    + " >aadaabcf\"aedfbff<!--\'-->?>caecfaaa><?&#<!--</script>&lang&fc;aadeaf?>>&bdquo<"
                    + "    cc =\"abff\"    /></   afe  ><script><!-- f(';<    cf aefbeef ="
                    + " \"bfabadcf\" ebbfeedd = fccabeb >";
        final BeiderMorseEncoder encoder = new BeiderMorseEncoder();
        encoder.setNameType(NameType.GENERIC);
    }

    @Test
    public void testOOM_test2_decomposed() throws EncoderException {
        final String phrase =
                "200697900'-->&#1913348150;</  bceaeef"
                    + " >aadaabcf\"aedfbff<!--\'-->?>caecfaaa><?&#<!--</script>&lang&fc;aadeaf?>>&bdquo<"
                    + "    cc =\"abff\"    /></   afe  ><script><!-- f(';<    cf aefbeef ="
                    + " \"bfabadcf\" ebbfeedd = fccabeb >";
        final BeiderMorseEncoder encoder = new BeiderMorseEncoder();
        encoder.setNameType(NameType.GENERIC);
        encoder.setRuleType(RuleType.EXACT);
    }

    @Test
    public void testOOM_test3_decomposed() throws EncoderException {
        final String phrase =
                "200697900'-->&#1913348150;</  bceaeef"
                    + " >aadaabcf\"aedfbff<!--\'-->?>caecfaaa><?&#<!--</script>&lang&fc;aadeaf?>>&bdquo<"
                    + "    cc =\"abff\"    /></   afe  ><script><!-- f(';<    cf aefbeef ="
                    + " \"bfabadcf\" ebbfeedd = fccabeb >";
        final BeiderMorseEncoder encoder = new BeiderMorseEncoder();
        encoder.setNameType(NameType.GENERIC);
        encoder.setRuleType(RuleType.EXACT);
        encoder.setMaxPhonemes(10);
    }

    @Test
    public void testOOM_test4_decomposed() throws EncoderException {
        final String phrase =
                "200697900'-->&#1913348150;</  bceaeef"
                    + " >aadaabcf\"aedfbff<!--\'-->?>caecfaaa><?&#<!--</script>&lang&fc;aadeaf?>>&bdquo<"
                    + "    cc =\"abff\"    /></   afe  ><script><!-- f(';<    cf aefbeef ="
                    + " \"bfabadcf\" ebbfeedd = fccabeb >";
        final BeiderMorseEncoder encoder = new BeiderMorseEncoder();
        encoder.setNameType(NameType.GENERIC);
        encoder.setRuleType(RuleType.EXACT);
        encoder.setMaxPhonemes(10);
        final String phonemes = encoder.encode1(phrase);
    }

    @Test
    public void testOOM_test5_decomposed() throws EncoderException {
        final String phrase =
                "200697900'-->&#1913348150;</  bceaeef"
                    + " >aadaabcf\"aedfbff<!--\'-->?>caecfaaa><?&#<!--</script>&lang&fc;aadeaf?>>&bdquo<"
                    + "    cc =\"abff\"    /></   afe  ><script><!-- f(';<    cf aefbeef ="
                    + " \"bfabadcf\" ebbfeedd = fccabeb >";
        final BeiderMorseEncoder encoder = new BeiderMorseEncoder();
        encoder.setNameType(NameType.GENERIC);
        encoder.setRuleType(RuleType.EXACT);
        encoder.setMaxPhonemes(10);
        final String phonemes = encoder.encode1(phrase);
        assertFalse(phonemes.isEmpty());
    }

    @Test
    public void testOOM_test6_decomposed() throws EncoderException {
        final String phrase =
                "200697900'-->&#1913348150;</  bceaeef"
                    + " >aadaabcf\"aedfbff<!--\'-->?>caecfaaa><?&#<!--</script>&lang&fc;aadeaf?>>&bdquo<"
                    + "    cc =\"abff\"    /></   afe  ><script><!-- f(';<    cf aefbeef ="
                    + " \"bfabadcf\" ebbfeedd = fccabeb >";
        final BeiderMorseEncoder encoder = new BeiderMorseEncoder();
        encoder.setNameType(NameType.GENERIC);
        encoder.setRuleType(RuleType.EXACT);
        encoder.setMaxPhonemes(10);
        final String phonemes = encoder.encode1(phrase);
        assertFalse(phonemes.isEmpty());
        final String[] phonemeArr = phonemes.split("\\|");
        assertTrue(phonemeArr.length <= 10);
    }

    @Test
    public void testSetConcat_test0_decomposed()  {
        final BeiderMorseEncoder bmpm = new BeiderMorseEncoder();
    }

    @Test
    public void testSetConcat_test1_decomposed()  {
        final BeiderMorseEncoder bmpm = new BeiderMorseEncoder();
        bmpm.setConcat(false);
    }

    @Test
    public void testSetConcat_test2_decomposed()  {
        final BeiderMorseEncoder bmpm = new BeiderMorseEncoder();
        bmpm.setConcat(false);
        assertFalse("Should be able to set concat to false", bmpm.isConcat());
    }

    @Test
    public void testSetNameTypeAsh_test0_decomposed()  {
        final BeiderMorseEncoder bmpm = new BeiderMorseEncoder();
    }

    @Test
    public void testSetNameTypeAsh_test1_decomposed()  {
        final BeiderMorseEncoder bmpm = new BeiderMorseEncoder();
        bmpm.setNameType(NameType.ASHKENAZI);
    }

    @Test
    public void testSetNameTypeAsh_test2_decomposed()  {
        final BeiderMorseEncoder bmpm = new BeiderMorseEncoder();
        bmpm.setNameType(NameType.ASHKENAZI);
        assertEquals(
                "Name type should have been set to ash", NameType.ASHKENAZI, bmpm.getNameType());
    }

    @Test
    public void testSetRuleTypeExact_test0_decomposed()  {
        final BeiderMorseEncoder bmpm = new BeiderMorseEncoder();
    }

    @Test
    public void testSetRuleTypeExact_test1_decomposed()  {
        final BeiderMorseEncoder bmpm = new BeiderMorseEncoder();
        bmpm.setRuleType(RuleType.EXACT);
    }

    @Test
    public void testSetRuleTypeExact_test2_decomposed()  {
        final BeiderMorseEncoder bmpm = new BeiderMorseEncoder();
        bmpm.setRuleType(RuleType.EXACT);
        assertEquals("Rule type should have been set to exact", RuleType.EXACT, bmpm.getRuleType());
    }

    @Test
    public void testSetRuleTypeToRulesIllegalArgumentException_test0_decomposed()  {
        final BeiderMorseEncoder bmpm = new BeiderMorseEncoder();
    }

    @Test(expected = IllegalArgumentException.class)
    public void testSetRuleTypeToRulesIllegalArgumentException_test1_decomposed()  {
        final BeiderMorseEncoder bmpm = new BeiderMorseEncoder();
        bmpm.setRuleType(RuleType.RULES);
    }

    @Test(/* timeout = 20000L */ )
    public void testSpeedCheck_test0_decomposed() throws EncoderException {
        final BeiderMorseEncoder bmpm = this.createGenericApproxEncoder();
    }

    @Test(/* timeout = 20000L */ )
    public void testSpeedCheck_test1_decomposed() throws EncoderException {
        final BeiderMorseEncoder bmpm = this.createGenericApproxEncoder();
        final StringBuilder stringBuffer = new StringBuilder();
        stringBuffer.append(TEST_CHARS[0]);
    }

    @Test(/* timeout = 20000L */ )
    public void testSpeedCheck_test2_decomposed() throws EncoderException {
        final BeiderMorseEncoder bmpm = this.createGenericApproxEncoder();
        final StringBuilder stringBuffer = new StringBuilder();
        stringBuffer.append(TEST_CHARS[0]);
        for (int i = 0, j = 1; i < 40; i++, j++) {
            if (j == TEST_CHARS.length) {
                j = 0;
            }
            bmpm.encode1(stringBuffer.toString());
            stringBuffer.append(TEST_CHARS[j]);
        }
    }

    @Test
    public void testSpeedCheck2_test0_decomposed() throws EncoderException {
        final BeiderMorseEncoder bmpm = this.createGenericApproxEncoder();
    }

    @Test
    public void testSpeedCheck2_test1_decomposed() throws EncoderException {
        final BeiderMorseEncoder bmpm = this.createGenericApproxEncoder();
        final String phrase = "ItstheendoftheworldasweknowitandIfeelfine";
        for (int i = 1; i <= phrase.length(); i++) {
            bmpm.encode0(phrase.subSequence(0, i));
        }
    }

    @Test
    public void testSpeedCheck3_test0_decomposed() throws EncoderException {
        final BeiderMorseEncoder bmpm = this.createGenericApproxEncoder();
    }

    @Test
    public void testSpeedCheck3_test1_decomposed() throws EncoderException {
        final BeiderMorseEncoder bmpm = this.createGenericApproxEncoder();
        final String phrase = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz";
        for (int i = 1; i <= phrase.length(); i++) {
            bmpm.encode0(phrase.subSequence(0, i));
        }
    }
}