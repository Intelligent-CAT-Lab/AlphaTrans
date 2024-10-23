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
package org.apache.commons.validator.routines;
import org.junit.Test;

import junit.framework.TestCase;

import java.util.regex.PatternSyntaxException;

/**
 * Test Case for RegexValidatorTest.
 *
 * @version $Revision$
 * @since Validator 1.4
 */
public class RegexValidatorTest extends TestCase {

    private static final String REGEX = "^([abc]*)(?:\\-)([DEF]*)(?:\\-)([123]*)$";

    private static final String COMPONENT_1 = "([abc]{3})";
    private static final String COMPONENT_2 = "([DEF]{3})";
    private static final String COMPONENT_3 = "([123]{3})";
    private static final String SEPARATOR_1 = "(?:\\-)";
    private static final String SEPARATOR_2 = "(?:\\s)";
    private static final String REGEX_1 =
            "^" + COMPONENT_1 + SEPARATOR_1 + COMPONENT_2 + SEPARATOR_1 + COMPONENT_3 + "$";
    private static final String REGEX_2 =
            "^" + COMPONENT_1 + SEPARATOR_2 + COMPONENT_2 + SEPARATOR_2 + COMPONENT_3 + "$";
    private static final String REGEX_3 = "^" + COMPONENT_1 + COMPONENT_2 + COMPONENT_3 + "$";
    private static final String[] MULTIPLE_REGEX = new String[] {REGEX_1, REGEX_2, REGEX_3};

    /**
     * Constrct a new test case.
     *
     * @param name The name of the test
     */
    public RegexValidatorTest(String name) {
        super(name);
    }

    /** Set Up. */
    @Override
    protected void setUp() throws Exception {
        super.setUp();
    }

    /** Tear Down. */
    @Override
    protected void tearDown() throws Exception {
        super.tearDown();
    }

    /** Test instance methods with single regular expression. */
    

    /** Test with multiple regular expressions (case sensitive). */
    

    /** Test with multiple regular expressions (case in-sensitive). */
    

    /** Test Null value */
    

    /** Test exceptions */
    

    /** Test exceptions */
    

    /** Test toString() method */
    

    /**
     * Compare two arrays
     *
     * @param label Label for the test
     * @param expect Expected array
     * @param result Actual array
     */
    private void checkArray(String label, String[] expect, String[] result) {

        if (expect == null || result == null) {
            if (expect == null && result == null) {
                return; // valid, both null
            } else {
                fail(label + " Null expect=" + expect + " result=" + result);
            }
            return; // not strictly necessary, but prevents possible NPE below
        }

        if (expect.length != result.length) {
            fail(label + " Length expect=" + expect.length + " result=" + result.length);
        }

        for (int i = 0; i < expect.length; i++) {
            assertEquals(label + " value[" + i + "]", expect[i], result[i]);
        }
    }

    @Test
    public void testSingle_test0_decomposed()  {
        RegexValidator sensitive = RegexValidator.RegexValidator3(REGEX);
    }

    @Test
    public void testSingle_test1_decomposed()  {
        RegexValidator sensitive = RegexValidator.RegexValidator3(REGEX);
        RegexValidator insensitive = RegexValidator.RegexValidator2(REGEX, false);
    }

    @Test
    public void testSingle_test2_decomposed()  {
        RegexValidator sensitive = RegexValidator.RegexValidator3(REGEX);
        RegexValidator insensitive = RegexValidator.RegexValidator2(REGEX, false);
        assertEquals("Sensitive isValid() valid", true, sensitive.isValid("ac-DE-1"));
        assertEquals("Sensitive isValid() invalid", false, sensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() valid", true, insensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() invalid", false, insensitive.isValid("ABd-de-1"));
    }

    @Test
    public void testSingle_test3_decomposed()  {
        RegexValidator sensitive = RegexValidator.RegexValidator3(REGEX);
        RegexValidator insensitive = RegexValidator.RegexValidator2(REGEX, false);
        assertEquals("Sensitive isValid() valid", true, sensitive.isValid("ac-DE-1"));
        assertEquals("Sensitive isValid() invalid", false, sensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() valid", true, insensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() invalid", false, insensitive.isValid("ABd-de-1"));
        assertEquals("Sensitive validate() valid", "acDE1", sensitive.validate("ac-DE-1"));
        assertEquals("Sensitive validate() invalid", null, sensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() valid", "ABde1", insensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() invalid", null, insensitive.validate("ABd-de-1"));
    }

    @Test
    public void testSingle_test4_decomposed()  {
        RegexValidator sensitive = RegexValidator.RegexValidator3(REGEX);
        RegexValidator insensitive = RegexValidator.RegexValidator2(REGEX, false);
        assertEquals("Sensitive isValid() valid", true, sensitive.isValid("ac-DE-1"));
        assertEquals("Sensitive isValid() invalid", false, sensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() valid", true, insensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() invalid", false, insensitive.isValid("ABd-de-1"));
        assertEquals("Sensitive validate() valid", "acDE1", sensitive.validate("ac-DE-1"));
        assertEquals("Sensitive validate() invalid", null, sensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() valid", "ABde1", insensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() invalid", null, insensitive.validate("ABd-de-1"));
        sensitive.match("ac-DE-1");
    }

    @Test
    public void testSingle_test5_decomposed()  {
        RegexValidator sensitive = RegexValidator.RegexValidator3(REGEX);
        RegexValidator insensitive = RegexValidator.RegexValidator2(REGEX, false);
        assertEquals("Sensitive isValid() valid", true, sensitive.isValid("ac-DE-1"));
        assertEquals("Sensitive isValid() invalid", false, sensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() valid", true, insensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() invalid", false, insensitive.isValid("ABd-de-1"));
        assertEquals("Sensitive validate() valid", "acDE1", sensitive.validate("ac-DE-1"));
        assertEquals("Sensitive validate() invalid", null, sensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() valid", "ABde1", insensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() invalid", null, insensitive.validate("ABd-de-1"));
        sensitive.match("ac-DE-1");
        checkArray(
                "Sensitive match() valid",
                new String[] {"ac", "DE", "1"},
                sensitive.match("ac-DE-1"));
    }

    @Test
    public void testSingle_test6_decomposed()  {
        RegexValidator sensitive = RegexValidator.RegexValidator3(REGEX);
        RegexValidator insensitive = RegexValidator.RegexValidator2(REGEX, false);
        assertEquals("Sensitive isValid() valid", true, sensitive.isValid("ac-DE-1"));
        assertEquals("Sensitive isValid() invalid", false, sensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() valid", true, insensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() invalid", false, insensitive.isValid("ABd-de-1"));
        assertEquals("Sensitive validate() valid", "acDE1", sensitive.validate("ac-DE-1"));
        assertEquals("Sensitive validate() invalid", null, sensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() valid", "ABde1", insensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() invalid", null, insensitive.validate("ABd-de-1"));
        sensitive.match("ac-DE-1");
        checkArray(
                "Sensitive match() valid",
                new String[] {"ac", "DE", "1"},
                sensitive.match("ac-DE-1"));
        sensitive.match("AB-de-1");
    }

    @Test
    public void testSingle_test7_decomposed()  {
        RegexValidator sensitive = RegexValidator.RegexValidator3(REGEX);
        RegexValidator insensitive = RegexValidator.RegexValidator2(REGEX, false);
        assertEquals("Sensitive isValid() valid", true, sensitive.isValid("ac-DE-1"));
        assertEquals("Sensitive isValid() invalid", false, sensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() valid", true, insensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() invalid", false, insensitive.isValid("ABd-de-1"));
        assertEquals("Sensitive validate() valid", "acDE1", sensitive.validate("ac-DE-1"));
        assertEquals("Sensitive validate() invalid", null, sensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() valid", "ABde1", insensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() invalid", null, insensitive.validate("ABd-de-1"));
        sensitive.match("ac-DE-1");
        checkArray(
                "Sensitive match() valid",
                new String[] {"ac", "DE", "1"},
                sensitive.match("ac-DE-1"));
        sensitive.match("AB-de-1");
        checkArray("Sensitive match() invalid", null, sensitive.match("AB-de-1"));
    }

    @Test
    public void testSingle_test8_decomposed()  {
        RegexValidator sensitive = RegexValidator.RegexValidator3(REGEX);
        RegexValidator insensitive = RegexValidator.RegexValidator2(REGEX, false);
        assertEquals("Sensitive isValid() valid", true, sensitive.isValid("ac-DE-1"));
        assertEquals("Sensitive isValid() invalid", false, sensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() valid", true, insensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() invalid", false, insensitive.isValid("ABd-de-1"));
        assertEquals("Sensitive validate() valid", "acDE1", sensitive.validate("ac-DE-1"));
        assertEquals("Sensitive validate() invalid", null, sensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() valid", "ABde1", insensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() invalid", null, insensitive.validate("ABd-de-1"));
        sensitive.match("ac-DE-1");
        checkArray(
                "Sensitive match() valid",
                new String[] {"ac", "DE", "1"},
                sensitive.match("ac-DE-1"));
        sensitive.match("AB-de-1");
        checkArray("Sensitive match() invalid", null, sensitive.match("AB-de-1"));
        insensitive.match("AB-de-1");
    }

    @Test
    public void testSingle_test9_decomposed()  {
        RegexValidator sensitive = RegexValidator.RegexValidator3(REGEX);
        RegexValidator insensitive = RegexValidator.RegexValidator2(REGEX, false);
        assertEquals("Sensitive isValid() valid", true, sensitive.isValid("ac-DE-1"));
        assertEquals("Sensitive isValid() invalid", false, sensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() valid", true, insensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() invalid", false, insensitive.isValid("ABd-de-1"));
        assertEquals("Sensitive validate() valid", "acDE1", sensitive.validate("ac-DE-1"));
        assertEquals("Sensitive validate() invalid", null, sensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() valid", "ABde1", insensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() invalid", null, insensitive.validate("ABd-de-1"));
        sensitive.match("ac-DE-1");
        checkArray(
                "Sensitive match() valid",
                new String[] {"ac", "DE", "1"},
                sensitive.match("ac-DE-1"));
        sensitive.match("AB-de-1");
        checkArray("Sensitive match() invalid", null, sensitive.match("AB-de-1"));
        insensitive.match("AB-de-1");
        checkArray(
                "Insensitive match() valid",
                new String[] {"AB", "de", "1"},
                insensitive.match("AB-de-1"));
    }

    @Test
    public void testSingle_test10_decomposed()  {
        RegexValidator sensitive = RegexValidator.RegexValidator3(REGEX);
        RegexValidator insensitive = RegexValidator.RegexValidator2(REGEX, false);
        assertEquals("Sensitive isValid() valid", true, sensitive.isValid("ac-DE-1"));
        assertEquals("Sensitive isValid() invalid", false, sensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() valid", true, insensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() invalid", false, insensitive.isValid("ABd-de-1"));
        assertEquals("Sensitive validate() valid", "acDE1", sensitive.validate("ac-DE-1"));
        assertEquals("Sensitive validate() invalid", null, sensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() valid", "ABde1", insensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() invalid", null, insensitive.validate("ABd-de-1"));
        sensitive.match("ac-DE-1");
        checkArray(
                "Sensitive match() valid",
                new String[] {"ac", "DE", "1"},
                sensitive.match("ac-DE-1"));
        sensitive.match("AB-de-1");
        checkArray("Sensitive match() invalid", null, sensitive.match("AB-de-1"));
        insensitive.match("AB-de-1");
        checkArray(
                "Insensitive match() valid",
                new String[] {"AB", "de", "1"},
                insensitive.match("AB-de-1"));
        insensitive.match("ABd-de-1");
    }

    @Test
    public void testSingle_test11_decomposed()  {
        RegexValidator sensitive = RegexValidator.RegexValidator3(REGEX);
        RegexValidator insensitive = RegexValidator.RegexValidator2(REGEX, false);
        assertEquals("Sensitive isValid() valid", true, sensitive.isValid("ac-DE-1"));
        assertEquals("Sensitive isValid() invalid", false, sensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() valid", true, insensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() invalid", false, insensitive.isValid("ABd-de-1"));
        assertEquals("Sensitive validate() valid", "acDE1", sensitive.validate("ac-DE-1"));
        assertEquals("Sensitive validate() invalid", null, sensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() valid", "ABde1", insensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() invalid", null, insensitive.validate("ABd-de-1"));
        sensitive.match("ac-DE-1");
        checkArray(
                "Sensitive match() valid",
                new String[] {"ac", "DE", "1"},
                sensitive.match("ac-DE-1"));
        sensitive.match("AB-de-1");
        checkArray("Sensitive match() invalid", null, sensitive.match("AB-de-1"));
        insensitive.match("AB-de-1");
        checkArray(
                "Insensitive match() valid",
                new String[] {"AB", "de", "1"},
                insensitive.match("AB-de-1"));
        insensitive.match("ABd-de-1");
        checkArray("Insensitive match() invalid", null, insensitive.match("ABd-de-1"));
    }

    @Test
    public void testSingle_test12_decomposed()  {
        RegexValidator sensitive = RegexValidator.RegexValidator3(REGEX);
        RegexValidator insensitive = RegexValidator.RegexValidator2(REGEX, false);
        assertEquals("Sensitive isValid() valid", true, sensitive.isValid("ac-DE-1"));
        assertEquals("Sensitive isValid() invalid", false, sensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() valid", true, insensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() invalid", false, insensitive.isValid("ABd-de-1"));
        assertEquals("Sensitive validate() valid", "acDE1", sensitive.validate("ac-DE-1"));
        assertEquals("Sensitive validate() invalid", null, sensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() valid", "ABde1", insensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() invalid", null, insensitive.validate("ABd-de-1"));
        sensitive.match("ac-DE-1");
        checkArray(
                "Sensitive match() valid",
                new String[] {"ac", "DE", "1"},
                sensitive.match("ac-DE-1"));
        sensitive.match("AB-de-1");
        checkArray("Sensitive match() invalid", null, sensitive.match("AB-de-1"));
        insensitive.match("AB-de-1");
        checkArray(
                "Insensitive match() valid",
                new String[] {"AB", "de", "1"},
                insensitive.match("AB-de-1"));
        insensitive.match("ABd-de-1");
        checkArray("Insensitive match() invalid", null, insensitive.match("ABd-de-1"));
        RegexValidator.RegexValidator3("^([A-Z]*)$");
    }

    @Test
    public void testSingle_test13_decomposed()  {
        RegexValidator sensitive = RegexValidator.RegexValidator3(REGEX);
        RegexValidator insensitive = RegexValidator.RegexValidator2(REGEX, false);
        assertEquals("Sensitive isValid() valid", true, sensitive.isValid("ac-DE-1"));
        assertEquals("Sensitive isValid() invalid", false, sensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() valid", true, insensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() invalid", false, insensitive.isValid("ABd-de-1"));
        assertEquals("Sensitive validate() valid", "acDE1", sensitive.validate("ac-DE-1"));
        assertEquals("Sensitive validate() invalid", null, sensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() valid", "ABde1", insensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() invalid", null, insensitive.validate("ABd-de-1"));
        sensitive.match("ac-DE-1");
        checkArray(
                "Sensitive match() valid",
                new String[] {"ac", "DE", "1"},
                sensitive.match("ac-DE-1"));
        sensitive.match("AB-de-1");
        checkArray("Sensitive match() invalid", null, sensitive.match("AB-de-1"));
        insensitive.match("AB-de-1");
        checkArray(
                "Insensitive match() valid",
                new String[] {"AB", "de", "1"},
                insensitive.match("AB-de-1"));
        insensitive.match("ABd-de-1");
        checkArray("Insensitive match() invalid", null, insensitive.match("ABd-de-1"));
        RegexValidator.RegexValidator3("^([A-Z]*)$");
        assertEquals(
                "validate one",
                "ABC",
                (RegexValidator.RegexValidator3("^([A-Z]*)$")).validate("ABC"));
    }

    @Test
    public void testSingle_test14_decomposed()  {
        RegexValidator sensitive = RegexValidator.RegexValidator3(REGEX);
        RegexValidator insensitive = RegexValidator.RegexValidator2(REGEX, false);
        assertEquals("Sensitive isValid() valid", true, sensitive.isValid("ac-DE-1"));
        assertEquals("Sensitive isValid() invalid", false, sensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() valid", true, insensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() invalid", false, insensitive.isValid("ABd-de-1"));
        assertEquals("Sensitive validate() valid", "acDE1", sensitive.validate("ac-DE-1"));
        assertEquals("Sensitive validate() invalid", null, sensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() valid", "ABde1", insensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() invalid", null, insensitive.validate("ABd-de-1"));
        sensitive.match("ac-DE-1");
        checkArray(
                "Sensitive match() valid",
                new String[] {"ac", "DE", "1"},
                sensitive.match("ac-DE-1"));
        sensitive.match("AB-de-1");
        checkArray("Sensitive match() invalid", null, sensitive.match("AB-de-1"));
        insensitive.match("AB-de-1");
        checkArray(
                "Insensitive match() valid",
                new String[] {"AB", "de", "1"},
                insensitive.match("AB-de-1"));
        insensitive.match("ABd-de-1");
        checkArray("Insensitive match() invalid", null, insensitive.match("ABd-de-1"));
        RegexValidator.RegexValidator3("^([A-Z]*)$");
        assertEquals(
                "validate one",
                "ABC",
                (RegexValidator.RegexValidator3("^([A-Z]*)$")).validate("ABC"));
        RegexValidator.RegexValidator3("^([A-Z]*)$");
    }

    @Test
    public void testSingle_test15_decomposed()  {
        RegexValidator sensitive = RegexValidator.RegexValidator3(REGEX);
        RegexValidator insensitive = RegexValidator.RegexValidator2(REGEX, false);
        assertEquals("Sensitive isValid() valid", true, sensitive.isValid("ac-DE-1"));
        assertEquals("Sensitive isValid() invalid", false, sensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() valid", true, insensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() invalid", false, insensitive.isValid("ABd-de-1"));
        assertEquals("Sensitive validate() valid", "acDE1", sensitive.validate("ac-DE-1"));
        assertEquals("Sensitive validate() invalid", null, sensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() valid", "ABde1", insensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() invalid", null, insensitive.validate("ABd-de-1"));
        sensitive.match("ac-DE-1");
        checkArray(
                "Sensitive match() valid",
                new String[] {"ac", "DE", "1"},
                sensitive.match("ac-DE-1"));
        sensitive.match("AB-de-1");
        checkArray("Sensitive match() invalid", null, sensitive.match("AB-de-1"));
        insensitive.match("AB-de-1");
        checkArray(
                "Insensitive match() valid",
                new String[] {"AB", "de", "1"},
                insensitive.match("AB-de-1"));
        insensitive.match("ABd-de-1");
        checkArray("Insensitive match() invalid", null, insensitive.match("ABd-de-1"));
        RegexValidator.RegexValidator3("^([A-Z]*)$");
        assertEquals(
                "validate one",
                "ABC",
                (RegexValidator.RegexValidator3("^([A-Z]*)$")).validate("ABC"));
        RegexValidator.RegexValidator3("^([A-Z]*)$");
        (RegexValidator.RegexValidator3("^([A-Z]*)$")).match("ABC");
    }

    @Test
    public void testSingle_test16_decomposed()  {
        RegexValidator sensitive = RegexValidator.RegexValidator3(REGEX);
        RegexValidator insensitive = RegexValidator.RegexValidator2(REGEX, false);
        assertEquals("Sensitive isValid() valid", true, sensitive.isValid("ac-DE-1"));
        assertEquals("Sensitive isValid() invalid", false, sensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() valid", true, insensitive.isValid("AB-de-1"));
        assertEquals("Insensitive isValid() invalid", false, insensitive.isValid("ABd-de-1"));
        assertEquals("Sensitive validate() valid", "acDE1", sensitive.validate("ac-DE-1"));
        assertEquals("Sensitive validate() invalid", null, sensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() valid", "ABde1", insensitive.validate("AB-de-1"));
        assertEquals("Insensitive validate() invalid", null, insensitive.validate("ABd-de-1"));
        sensitive.match("ac-DE-1");
        checkArray(
                "Sensitive match() valid",
                new String[] {"ac", "DE", "1"},
                sensitive.match("ac-DE-1"));
        sensitive.match("AB-de-1");
        checkArray("Sensitive match() invalid", null, sensitive.match("AB-de-1"));
        insensitive.match("AB-de-1");
        checkArray(
                "Insensitive match() valid",
                new String[] {"AB", "de", "1"},
                insensitive.match("AB-de-1"));
        insensitive.match("ABd-de-1");
        checkArray("Insensitive match() invalid", null, insensitive.match("ABd-de-1"));
        RegexValidator.RegexValidator3("^([A-Z]*)$");
        assertEquals(
                "validate one",
                "ABC",
                (RegexValidator.RegexValidator3("^([A-Z]*)$")).validate("ABC"));
        RegexValidator.RegexValidator3("^([A-Z]*)$");
        (RegexValidator.RegexValidator3("^([A-Z]*)$")).match("ABC");
        checkArray(
                "match one",
                new String[] {"ABC"},
                (RegexValidator.RegexValidator3("^([A-Z]*)$")).match("ABC"));
    }

    @Test
    public void testMultipleSensitive_test0_decomposed()  {
        RegexValidator multiple = RegexValidator.RegexValidator1(MULTIPLE_REGEX);
    }

    @Test
    public void testMultipleSensitive_test1_decomposed()  {
        RegexValidator multiple = RegexValidator.RegexValidator1(MULTIPLE_REGEX);
        RegexValidator single1 = RegexValidator.RegexValidator3(REGEX_1);
        RegexValidator single2 = RegexValidator.RegexValidator3(REGEX_2);
        RegexValidator single3 = RegexValidator.RegexValidator3(REGEX_3);
    }

    @Test
    public void testMultipleSensitive_test2_decomposed()  {
        RegexValidator multiple = RegexValidator.RegexValidator1(MULTIPLE_REGEX);
        RegexValidator single1 = RegexValidator.RegexValidator3(REGEX_1);
        RegexValidator single2 = RegexValidator.RegexValidator3(REGEX_2);
        RegexValidator single3 = RegexValidator.RegexValidator3(REGEX_3);
        String value = "aac FDE 321";
        String expect = "aacFDE321";
        String[] array = new String[] {"aac", "FDE", "321"};
        assertEquals("Sensitive isValid() Multiple", true, multiple.isValid(value));
    }

    @Test
    public void testMultipleSensitive_test3_decomposed()  {
        RegexValidator multiple = RegexValidator.RegexValidator1(MULTIPLE_REGEX);
        RegexValidator single1 = RegexValidator.RegexValidator3(REGEX_1);
        RegexValidator single2 = RegexValidator.RegexValidator3(REGEX_2);
        RegexValidator single3 = RegexValidator.RegexValidator3(REGEX_3);
        String value = "aac FDE 321";
        String expect = "aacFDE321";
        String[] array = new String[] {"aac", "FDE", "321"};
        assertEquals("Sensitive isValid() Multiple", true, multiple.isValid(value));
        assertEquals("Sensitive isValid() 1st", false, single1.isValid(value));
        assertEquals("Sensitive isValid() 2nd", true, single2.isValid(value));
        assertEquals("Sensitive isValid() 3rd", false, single3.isValid(value));
    }

    @Test
    public void testMultipleSensitive_test4_decomposed()  {
        RegexValidator multiple = RegexValidator.RegexValidator1(MULTIPLE_REGEX);
        RegexValidator single1 = RegexValidator.RegexValidator3(REGEX_1);
        RegexValidator single2 = RegexValidator.RegexValidator3(REGEX_2);
        RegexValidator single3 = RegexValidator.RegexValidator3(REGEX_3);
        String value = "aac FDE 321";
        String expect = "aacFDE321";
        String[] array = new String[] {"aac", "FDE", "321"};
        assertEquals("Sensitive isValid() Multiple", true, multiple.isValid(value));
        assertEquals("Sensitive isValid() 1st", false, single1.isValid(value));
        assertEquals("Sensitive isValid() 2nd", true, single2.isValid(value));
        assertEquals("Sensitive isValid() 3rd", false, single3.isValid(value));
        assertEquals("Sensitive validate() Multiple", expect, multiple.validate(value));
        assertEquals("Sensitive validate() 1st", null, single1.validate(value));
        assertEquals("Sensitive validate() 2nd", expect, single2.validate(value));
        assertEquals("Sensitive validate() 3rd", null, single3.validate(value));
    }

    @Test
    public void testMultipleSensitive_test5_decomposed()  {
        RegexValidator multiple = RegexValidator.RegexValidator1(MULTIPLE_REGEX);
        RegexValidator single1 = RegexValidator.RegexValidator3(REGEX_1);
        RegexValidator single2 = RegexValidator.RegexValidator3(REGEX_2);
        RegexValidator single3 = RegexValidator.RegexValidator3(REGEX_3);
        String value = "aac FDE 321";
        String expect = "aacFDE321";
        String[] array = new String[] {"aac", "FDE", "321"};
        assertEquals("Sensitive isValid() Multiple", true, multiple.isValid(value));
        assertEquals("Sensitive isValid() 1st", false, single1.isValid(value));
        assertEquals("Sensitive isValid() 2nd", true, single2.isValid(value));
        assertEquals("Sensitive isValid() 3rd", false, single3.isValid(value));
        assertEquals("Sensitive validate() Multiple", expect, multiple.validate(value));
        assertEquals("Sensitive validate() 1st", null, single1.validate(value));
        assertEquals("Sensitive validate() 2nd", expect, single2.validate(value));
        assertEquals("Sensitive validate() 3rd", null, single3.validate(value));
        multiple.match(value);
    }

    @Test
    public void testMultipleSensitive_test6_decomposed()  {
        RegexValidator multiple = RegexValidator.RegexValidator1(MULTIPLE_REGEX);
        RegexValidator single1 = RegexValidator.RegexValidator3(REGEX_1);
        RegexValidator single2 = RegexValidator.RegexValidator3(REGEX_2);
        RegexValidator single3 = RegexValidator.RegexValidator3(REGEX_3);
        String value = "aac FDE 321";
        String expect = "aacFDE321";
        String[] array = new String[] {"aac", "FDE", "321"};
        assertEquals("Sensitive isValid() Multiple", true, multiple.isValid(value));
        assertEquals("Sensitive isValid() 1st", false, single1.isValid(value));
        assertEquals("Sensitive isValid() 2nd", true, single2.isValid(value));
        assertEquals("Sensitive isValid() 3rd", false, single3.isValid(value));
        assertEquals("Sensitive validate() Multiple", expect, multiple.validate(value));
        assertEquals("Sensitive validate() 1st", null, single1.validate(value));
        assertEquals("Sensitive validate() 2nd", expect, single2.validate(value));
        assertEquals("Sensitive validate() 3rd", null, single3.validate(value));
        multiple.match(value);
        checkArray("Sensitive match() Multiple", array, multiple.match(value));
    }

    @Test
    public void testMultipleSensitive_test7_decomposed()  {
        RegexValidator multiple = RegexValidator.RegexValidator1(MULTIPLE_REGEX);
        RegexValidator single1 = RegexValidator.RegexValidator3(REGEX_1);
        RegexValidator single2 = RegexValidator.RegexValidator3(REGEX_2);
        RegexValidator single3 = RegexValidator.RegexValidator3(REGEX_3);
        String value = "aac FDE 321";
        String expect = "aacFDE321";
        String[] array = new String[] {"aac", "FDE", "321"};
        assertEquals("Sensitive isValid() Multiple", true, multiple.isValid(value));
        assertEquals("Sensitive isValid() 1st", false, single1.isValid(value));
        assertEquals("Sensitive isValid() 2nd", true, single2.isValid(value));
        assertEquals("Sensitive isValid() 3rd", false, single3.isValid(value));
        assertEquals("Sensitive validate() Multiple", expect, multiple.validate(value));
        assertEquals("Sensitive validate() 1st", null, single1.validate(value));
        assertEquals("Sensitive validate() 2nd", expect, single2.validate(value));
        assertEquals("Sensitive validate() 3rd", null, single3.validate(value));
        multiple.match(value);
        checkArray("Sensitive match() Multiple", array, multiple.match(value));
        single1.match(value);
    }

    @Test
    public void testMultipleSensitive_test8_decomposed()  {
        RegexValidator multiple = RegexValidator.RegexValidator1(MULTIPLE_REGEX);
        RegexValidator single1 = RegexValidator.RegexValidator3(REGEX_1);
        RegexValidator single2 = RegexValidator.RegexValidator3(REGEX_2);
        RegexValidator single3 = RegexValidator.RegexValidator3(REGEX_3);
        String value = "aac FDE 321";
        String expect = "aacFDE321";
        String[] array = new String[] {"aac", "FDE", "321"};
        assertEquals("Sensitive isValid() Multiple", true, multiple.isValid(value));
        assertEquals("Sensitive isValid() 1st", false, single1.isValid(value));
        assertEquals("Sensitive isValid() 2nd", true, single2.isValid(value));
        assertEquals("Sensitive isValid() 3rd", false, single3.isValid(value));
        assertEquals("Sensitive validate() Multiple", expect, multiple.validate(value));
        assertEquals("Sensitive validate() 1st", null, single1.validate(value));
        assertEquals("Sensitive validate() 2nd", expect, single2.validate(value));
        assertEquals("Sensitive validate() 3rd", null, single3.validate(value));
        multiple.match(value);
        checkArray("Sensitive match() Multiple", array, multiple.match(value));
        single1.match(value);
        checkArray("Sensitive match() 1st", null, single1.match(value));
    }

    @Test
    public void testMultipleSensitive_test9_decomposed()  {
        RegexValidator multiple = RegexValidator.RegexValidator1(MULTIPLE_REGEX);
        RegexValidator single1 = RegexValidator.RegexValidator3(REGEX_1);
        RegexValidator single2 = RegexValidator.RegexValidator3(REGEX_2);
        RegexValidator single3 = RegexValidator.RegexValidator3(REGEX_3);
        String value = "aac FDE 321";
        String expect = "aacFDE321";
        String[] array = new String[] {"aac", "FDE", "321"};
        assertEquals("Sensitive isValid() Multiple", true, multiple.isValid(value));
        assertEquals("Sensitive isValid() 1st", false, single1.isValid(value));
        assertEquals("Sensitive isValid() 2nd", true, single2.isValid(value));
        assertEquals("Sensitive isValid() 3rd", false, single3.isValid(value));
        assertEquals("Sensitive validate() Multiple", expect, multiple.validate(value));
        assertEquals("Sensitive validate() 1st", null, single1.validate(value));
        assertEquals("Sensitive validate() 2nd", expect, single2.validate(value));
        assertEquals("Sensitive validate() 3rd", null, single3.validate(value));
        multiple.match(value);
        checkArray("Sensitive match() Multiple", array, multiple.match(value));
        single1.match(value);
        checkArray("Sensitive match() 1st", null, single1.match(value));
        single2.match(value);
    }

    @Test
    public void testMultipleSensitive_test10_decomposed()  {
        RegexValidator multiple = RegexValidator.RegexValidator1(MULTIPLE_REGEX);
        RegexValidator single1 = RegexValidator.RegexValidator3(REGEX_1);
        RegexValidator single2 = RegexValidator.RegexValidator3(REGEX_2);
        RegexValidator single3 = RegexValidator.RegexValidator3(REGEX_3);
        String value = "aac FDE 321";
        String expect = "aacFDE321";
        String[] array = new String[] {"aac", "FDE", "321"};
        assertEquals("Sensitive isValid() Multiple", true, multiple.isValid(value));
        assertEquals("Sensitive isValid() 1st", false, single1.isValid(value));
        assertEquals("Sensitive isValid() 2nd", true, single2.isValid(value));
        assertEquals("Sensitive isValid() 3rd", false, single3.isValid(value));
        assertEquals("Sensitive validate() Multiple", expect, multiple.validate(value));
        assertEquals("Sensitive validate() 1st", null, single1.validate(value));
        assertEquals("Sensitive validate() 2nd", expect, single2.validate(value));
        assertEquals("Sensitive validate() 3rd", null, single3.validate(value));
        multiple.match(value);
        checkArray("Sensitive match() Multiple", array, multiple.match(value));
        single1.match(value);
        checkArray("Sensitive match() 1st", null, single1.match(value));
        single2.match(value);
        checkArray("Sensitive match() 2nd", array, single2.match(value));
    }

    @Test
    public void testMultipleSensitive_test11_decomposed()  {
        RegexValidator multiple = RegexValidator.RegexValidator1(MULTIPLE_REGEX);
        RegexValidator single1 = RegexValidator.RegexValidator3(REGEX_1);
        RegexValidator single2 = RegexValidator.RegexValidator3(REGEX_2);
        RegexValidator single3 = RegexValidator.RegexValidator3(REGEX_3);
        String value = "aac FDE 321";
        String expect = "aacFDE321";
        String[] array = new String[] {"aac", "FDE", "321"};
        assertEquals("Sensitive isValid() Multiple", true, multiple.isValid(value));
        assertEquals("Sensitive isValid() 1st", false, single1.isValid(value));
        assertEquals("Sensitive isValid() 2nd", true, single2.isValid(value));
        assertEquals("Sensitive isValid() 3rd", false, single3.isValid(value));
        assertEquals("Sensitive validate() Multiple", expect, multiple.validate(value));
        assertEquals("Sensitive validate() 1st", null, single1.validate(value));
        assertEquals("Sensitive validate() 2nd", expect, single2.validate(value));
        assertEquals("Sensitive validate() 3rd", null, single3.validate(value));
        multiple.match(value);
        checkArray("Sensitive match() Multiple", array, multiple.match(value));
        single1.match(value);
        checkArray("Sensitive match() 1st", null, single1.match(value));
        single2.match(value);
        checkArray("Sensitive match() 2nd", array, single2.match(value));
        single3.match(value);
    }

    @Test
    public void testMultipleSensitive_test12_decomposed()  {
        RegexValidator multiple = RegexValidator.RegexValidator1(MULTIPLE_REGEX);
        RegexValidator single1 = RegexValidator.RegexValidator3(REGEX_1);
        RegexValidator single2 = RegexValidator.RegexValidator3(REGEX_2);
        RegexValidator single3 = RegexValidator.RegexValidator3(REGEX_3);
        String value = "aac FDE 321";
        String expect = "aacFDE321";
        String[] array = new String[] {"aac", "FDE", "321"};
        assertEquals("Sensitive isValid() Multiple", true, multiple.isValid(value));
        assertEquals("Sensitive isValid() 1st", false, single1.isValid(value));
        assertEquals("Sensitive isValid() 2nd", true, single2.isValid(value));
        assertEquals("Sensitive isValid() 3rd", false, single3.isValid(value));
        assertEquals("Sensitive validate() Multiple", expect, multiple.validate(value));
        assertEquals("Sensitive validate() 1st", null, single1.validate(value));
        assertEquals("Sensitive validate() 2nd", expect, single2.validate(value));
        assertEquals("Sensitive validate() 3rd", null, single3.validate(value));
        multiple.match(value);
        checkArray("Sensitive match() Multiple", array, multiple.match(value));
        single1.match(value);
        checkArray("Sensitive match() 1st", null, single1.match(value));
        single2.match(value);
        checkArray("Sensitive match() 2nd", array, single2.match(value));
        single3.match(value);
        checkArray("Sensitive match() 3rd", null, single3.match(value));
    }

    @Test
    public void testMultipleSensitive_test13_decomposed()  {
        RegexValidator multiple = RegexValidator.RegexValidator1(MULTIPLE_REGEX);
        RegexValidator single1 = RegexValidator.RegexValidator3(REGEX_1);
        RegexValidator single2 = RegexValidator.RegexValidator3(REGEX_2);
        RegexValidator single3 = RegexValidator.RegexValidator3(REGEX_3);
        String value = "aac FDE 321";
        String expect = "aacFDE321";
        String[] array = new String[] {"aac", "FDE", "321"};
        assertEquals("Sensitive isValid() Multiple", true, multiple.isValid(value));
        assertEquals("Sensitive isValid() 1st", false, single1.isValid(value));
        assertEquals("Sensitive isValid() 2nd", true, single2.isValid(value));
        assertEquals("Sensitive isValid() 3rd", false, single3.isValid(value));
        assertEquals("Sensitive validate() Multiple", expect, multiple.validate(value));
        assertEquals("Sensitive validate() 1st", null, single1.validate(value));
        assertEquals("Sensitive validate() 2nd", expect, single2.validate(value));
        assertEquals("Sensitive validate() 3rd", null, single3.validate(value));
        multiple.match(value);
        checkArray("Sensitive match() Multiple", array, multiple.match(value));
        single1.match(value);
        checkArray("Sensitive match() 1st", null, single1.match(value));
        single2.match(value);
        checkArray("Sensitive match() 2nd", array, single2.match(value));
        single3.match(value);
        checkArray("Sensitive match() 3rd", null, single3.match(value));
        value = "AAC*FDE*321";
        assertEquals("isValid() Invalid", false, multiple.isValid(value));
    }

    @Test
    public void testMultipleSensitive_test14_decomposed()  {
        RegexValidator multiple = RegexValidator.RegexValidator1(MULTIPLE_REGEX);
        RegexValidator single1 = RegexValidator.RegexValidator3(REGEX_1);
        RegexValidator single2 = RegexValidator.RegexValidator3(REGEX_2);
        RegexValidator single3 = RegexValidator.RegexValidator3(REGEX_3);
        String value = "aac FDE 321";
        String expect = "aacFDE321";
        String[] array = new String[] {"aac", "FDE", "321"};
        assertEquals("Sensitive isValid() Multiple", true, multiple.isValid(value));
        assertEquals("Sensitive isValid() 1st", false, single1.isValid(value));
        assertEquals("Sensitive isValid() 2nd", true, single2.isValid(value));
        assertEquals("Sensitive isValid() 3rd", false, single3.isValid(value));
        assertEquals("Sensitive validate() Multiple", expect, multiple.validate(value));
        assertEquals("Sensitive validate() 1st", null, single1.validate(value));
        assertEquals("Sensitive validate() 2nd", expect, single2.validate(value));
        assertEquals("Sensitive validate() 3rd", null, single3.validate(value));
        multiple.match(value);
        checkArray("Sensitive match() Multiple", array, multiple.match(value));
        single1.match(value);
        checkArray("Sensitive match() 1st", null, single1.match(value));
        single2.match(value);
        checkArray("Sensitive match() 2nd", array, single2.match(value));
        single3.match(value);
        checkArray("Sensitive match() 3rd", null, single3.match(value));
        value = "AAC*FDE*321";
        assertEquals("isValid() Invalid", false, multiple.isValid(value));
        assertEquals("validate() Invalid", null, multiple.validate(value));
    }

    @Test
    public void testMultipleSensitive_test15_decomposed()  {
        RegexValidator multiple = RegexValidator.RegexValidator1(MULTIPLE_REGEX);
        RegexValidator single1 = RegexValidator.RegexValidator3(REGEX_1);
        RegexValidator single2 = RegexValidator.RegexValidator3(REGEX_2);
        RegexValidator single3 = RegexValidator.RegexValidator3(REGEX_3);
        String value = "aac FDE 321";
        String expect = "aacFDE321";
        String[] array = new String[] {"aac", "FDE", "321"};
        assertEquals("Sensitive isValid() Multiple", true, multiple.isValid(value));
        assertEquals("Sensitive isValid() 1st", false, single1.isValid(value));
        assertEquals("Sensitive isValid() 2nd", true, single2.isValid(value));
        assertEquals("Sensitive isValid() 3rd", false, single3.isValid(value));
        assertEquals("Sensitive validate() Multiple", expect, multiple.validate(value));
        assertEquals("Sensitive validate() 1st", null, single1.validate(value));
        assertEquals("Sensitive validate() 2nd", expect, single2.validate(value));
        assertEquals("Sensitive validate() 3rd", null, single3.validate(value));
        multiple.match(value);
        checkArray("Sensitive match() Multiple", array, multiple.match(value));
        single1.match(value);
        checkArray("Sensitive match() 1st", null, single1.match(value));
        single2.match(value);
        checkArray("Sensitive match() 2nd", array, single2.match(value));
        single3.match(value);
        checkArray("Sensitive match() 3rd", null, single3.match(value));
        value = "AAC*FDE*321";
        assertEquals("isValid() Invalid", false, multiple.isValid(value));
        assertEquals("validate() Invalid", null, multiple.validate(value));
        assertEquals("match() Multiple", null, multiple.match(value));
    }

    @Test
    public void testMultipleInsensitive_test0_decomposed()  {
        RegexValidator multiple = new RegexValidator(MULTIPLE_REGEX, false);
    }

    @Test
    public void testMultipleInsensitive_test1_decomposed()  {
        RegexValidator multiple = new RegexValidator(MULTIPLE_REGEX, false);
        RegexValidator single1 = RegexValidator.RegexValidator2(REGEX_1, false);
        RegexValidator single2 = RegexValidator.RegexValidator2(REGEX_2, false);
        RegexValidator single3 = RegexValidator.RegexValidator2(REGEX_3, false);
    }

    @Test
    public void testMultipleInsensitive_test2_decomposed()  {
        RegexValidator multiple = new RegexValidator(MULTIPLE_REGEX, false);
        RegexValidator single1 = RegexValidator.RegexValidator2(REGEX_1, false);
        RegexValidator single2 = RegexValidator.RegexValidator2(REGEX_2, false);
        RegexValidator single3 = RegexValidator.RegexValidator2(REGEX_3, false);
        String value = "AAC FDE 321";
        String expect = "AACFDE321";
        String[] array = new String[] {"AAC", "FDE", "321"};
        assertEquals("isValid() Multiple", true, multiple.isValid(value));
    }

    @Test
    public void testMultipleInsensitive_test3_decomposed()  {
        RegexValidator multiple = new RegexValidator(MULTIPLE_REGEX, false);
        RegexValidator single1 = RegexValidator.RegexValidator2(REGEX_1, false);
        RegexValidator single2 = RegexValidator.RegexValidator2(REGEX_2, false);
        RegexValidator single3 = RegexValidator.RegexValidator2(REGEX_3, false);
        String value = "AAC FDE 321";
        String expect = "AACFDE321";
        String[] array = new String[] {"AAC", "FDE", "321"};
        assertEquals("isValid() Multiple", true, multiple.isValid(value));
        assertEquals("isValid() 1st", false, single1.isValid(value));
        assertEquals("isValid() 2nd", true, single2.isValid(value));
        assertEquals("isValid() 3rd", false, single3.isValid(value));
    }

    @Test
    public void testMultipleInsensitive_test4_decomposed()  {
        RegexValidator multiple = new RegexValidator(MULTIPLE_REGEX, false);
        RegexValidator single1 = RegexValidator.RegexValidator2(REGEX_1, false);
        RegexValidator single2 = RegexValidator.RegexValidator2(REGEX_2, false);
        RegexValidator single3 = RegexValidator.RegexValidator2(REGEX_3, false);
        String value = "AAC FDE 321";
        String expect = "AACFDE321";
        String[] array = new String[] {"AAC", "FDE", "321"};
        assertEquals("isValid() Multiple", true, multiple.isValid(value));
        assertEquals("isValid() 1st", false, single1.isValid(value));
        assertEquals("isValid() 2nd", true, single2.isValid(value));
        assertEquals("isValid() 3rd", false, single3.isValid(value));
        assertEquals("validate() Multiple", expect, multiple.validate(value));
        assertEquals("validate() 1st", null, single1.validate(value));
        assertEquals("validate() 2nd", expect, single2.validate(value));
        assertEquals("validate() 3rd", null, single3.validate(value));
    }

    @Test
    public void testMultipleInsensitive_test5_decomposed()  {
        RegexValidator multiple = new RegexValidator(MULTIPLE_REGEX, false);
        RegexValidator single1 = RegexValidator.RegexValidator2(REGEX_1, false);
        RegexValidator single2 = RegexValidator.RegexValidator2(REGEX_2, false);
        RegexValidator single3 = RegexValidator.RegexValidator2(REGEX_3, false);
        String value = "AAC FDE 321";
        String expect = "AACFDE321";
        String[] array = new String[] {"AAC", "FDE", "321"};
        assertEquals("isValid() Multiple", true, multiple.isValid(value));
        assertEquals("isValid() 1st", false, single1.isValid(value));
        assertEquals("isValid() 2nd", true, single2.isValid(value));
        assertEquals("isValid() 3rd", false, single3.isValid(value));
        assertEquals("validate() Multiple", expect, multiple.validate(value));
        assertEquals("validate() 1st", null, single1.validate(value));
        assertEquals("validate() 2nd", expect, single2.validate(value));
        assertEquals("validate() 3rd", null, single3.validate(value));
        multiple.match(value);
    }

    @Test
    public void testMultipleInsensitive_test6_decomposed()  {
        RegexValidator multiple = new RegexValidator(MULTIPLE_REGEX, false);
        RegexValidator single1 = RegexValidator.RegexValidator2(REGEX_1, false);
        RegexValidator single2 = RegexValidator.RegexValidator2(REGEX_2, false);
        RegexValidator single3 = RegexValidator.RegexValidator2(REGEX_3, false);
        String value = "AAC FDE 321";
        String expect = "AACFDE321";
        String[] array = new String[] {"AAC", "FDE", "321"};
        assertEquals("isValid() Multiple", true, multiple.isValid(value));
        assertEquals("isValid() 1st", false, single1.isValid(value));
        assertEquals("isValid() 2nd", true, single2.isValid(value));
        assertEquals("isValid() 3rd", false, single3.isValid(value));
        assertEquals("validate() Multiple", expect, multiple.validate(value));
        assertEquals("validate() 1st", null, single1.validate(value));
        assertEquals("validate() 2nd", expect, single2.validate(value));
        assertEquals("validate() 3rd", null, single3.validate(value));
        multiple.match(value);
        checkArray("match() Multiple", array, multiple.match(value));
    }

    @Test
    public void testMultipleInsensitive_test7_decomposed()  {
        RegexValidator multiple = new RegexValidator(MULTIPLE_REGEX, false);
        RegexValidator single1 = RegexValidator.RegexValidator2(REGEX_1, false);
        RegexValidator single2 = RegexValidator.RegexValidator2(REGEX_2, false);
        RegexValidator single3 = RegexValidator.RegexValidator2(REGEX_3, false);
        String value = "AAC FDE 321";
        String expect = "AACFDE321";
        String[] array = new String[] {"AAC", "FDE", "321"};
        assertEquals("isValid() Multiple", true, multiple.isValid(value));
        assertEquals("isValid() 1st", false, single1.isValid(value));
        assertEquals("isValid() 2nd", true, single2.isValid(value));
        assertEquals("isValid() 3rd", false, single3.isValid(value));
        assertEquals("validate() Multiple", expect, multiple.validate(value));
        assertEquals("validate() 1st", null, single1.validate(value));
        assertEquals("validate() 2nd", expect, single2.validate(value));
        assertEquals("validate() 3rd", null, single3.validate(value));
        multiple.match(value);
        checkArray("match() Multiple", array, multiple.match(value));
        single1.match(value);
    }

    @Test
    public void testMultipleInsensitive_test8_decomposed()  {
        RegexValidator multiple = new RegexValidator(MULTIPLE_REGEX, false);
        RegexValidator single1 = RegexValidator.RegexValidator2(REGEX_1, false);
        RegexValidator single2 = RegexValidator.RegexValidator2(REGEX_2, false);
        RegexValidator single3 = RegexValidator.RegexValidator2(REGEX_3, false);
        String value = "AAC FDE 321";
        String expect = "AACFDE321";
        String[] array = new String[] {"AAC", "FDE", "321"};
        assertEquals("isValid() Multiple", true, multiple.isValid(value));
        assertEquals("isValid() 1st", false, single1.isValid(value));
        assertEquals("isValid() 2nd", true, single2.isValid(value));
        assertEquals("isValid() 3rd", false, single3.isValid(value));
        assertEquals("validate() Multiple", expect, multiple.validate(value));
        assertEquals("validate() 1st", null, single1.validate(value));
        assertEquals("validate() 2nd", expect, single2.validate(value));
        assertEquals("validate() 3rd", null, single3.validate(value));
        multiple.match(value);
        checkArray("match() Multiple", array, multiple.match(value));
        single1.match(value);
        checkArray("match() 1st", null, single1.match(value));
    }

    @Test
    public void testMultipleInsensitive_test9_decomposed()  {
        RegexValidator multiple = new RegexValidator(MULTIPLE_REGEX, false);
        RegexValidator single1 = RegexValidator.RegexValidator2(REGEX_1, false);
        RegexValidator single2 = RegexValidator.RegexValidator2(REGEX_2, false);
        RegexValidator single3 = RegexValidator.RegexValidator2(REGEX_3, false);
        String value = "AAC FDE 321";
        String expect = "AACFDE321";
        String[] array = new String[] {"AAC", "FDE", "321"};
        assertEquals("isValid() Multiple", true, multiple.isValid(value));
        assertEquals("isValid() 1st", false, single1.isValid(value));
        assertEquals("isValid() 2nd", true, single2.isValid(value));
        assertEquals("isValid() 3rd", false, single3.isValid(value));
        assertEquals("validate() Multiple", expect, multiple.validate(value));
        assertEquals("validate() 1st", null, single1.validate(value));
        assertEquals("validate() 2nd", expect, single2.validate(value));
        assertEquals("validate() 3rd", null, single3.validate(value));
        multiple.match(value);
        checkArray("match() Multiple", array, multiple.match(value));
        single1.match(value);
        checkArray("match() 1st", null, single1.match(value));
        single2.match(value);
    }

    @Test
    public void testMultipleInsensitive_test10_decomposed()  {
        RegexValidator multiple = new RegexValidator(MULTIPLE_REGEX, false);
        RegexValidator single1 = RegexValidator.RegexValidator2(REGEX_1, false);
        RegexValidator single2 = RegexValidator.RegexValidator2(REGEX_2, false);
        RegexValidator single3 = RegexValidator.RegexValidator2(REGEX_3, false);
        String value = "AAC FDE 321";
        String expect = "AACFDE321";
        String[] array = new String[] {"AAC", "FDE", "321"};
        assertEquals("isValid() Multiple", true, multiple.isValid(value));
        assertEquals("isValid() 1st", false, single1.isValid(value));
        assertEquals("isValid() 2nd", true, single2.isValid(value));
        assertEquals("isValid() 3rd", false, single3.isValid(value));
        assertEquals("validate() Multiple", expect, multiple.validate(value));
        assertEquals("validate() 1st", null, single1.validate(value));
        assertEquals("validate() 2nd", expect, single2.validate(value));
        assertEquals("validate() 3rd", null, single3.validate(value));
        multiple.match(value);
        checkArray("match() Multiple", array, multiple.match(value));
        single1.match(value);
        checkArray("match() 1st", null, single1.match(value));
        single2.match(value);
        checkArray("match() 2nd", array, single2.match(value));
    }

    @Test
    public void testMultipleInsensitive_test11_decomposed()  {
        RegexValidator multiple = new RegexValidator(MULTIPLE_REGEX, false);
        RegexValidator single1 = RegexValidator.RegexValidator2(REGEX_1, false);
        RegexValidator single2 = RegexValidator.RegexValidator2(REGEX_2, false);
        RegexValidator single3 = RegexValidator.RegexValidator2(REGEX_3, false);
        String value = "AAC FDE 321";
        String expect = "AACFDE321";
        String[] array = new String[] {"AAC", "FDE", "321"};
        assertEquals("isValid() Multiple", true, multiple.isValid(value));
        assertEquals("isValid() 1st", false, single1.isValid(value));
        assertEquals("isValid() 2nd", true, single2.isValid(value));
        assertEquals("isValid() 3rd", false, single3.isValid(value));
        assertEquals("validate() Multiple", expect, multiple.validate(value));
        assertEquals("validate() 1st", null, single1.validate(value));
        assertEquals("validate() 2nd", expect, single2.validate(value));
        assertEquals("validate() 3rd", null, single3.validate(value));
        multiple.match(value);
        checkArray("match() Multiple", array, multiple.match(value));
        single1.match(value);
        checkArray("match() 1st", null, single1.match(value));
        single2.match(value);
        checkArray("match() 2nd", array, single2.match(value));
        single3.match(value);
    }

    @Test
    public void testMultipleInsensitive_test12_decomposed()  {
        RegexValidator multiple = new RegexValidator(MULTIPLE_REGEX, false);
        RegexValidator single1 = RegexValidator.RegexValidator2(REGEX_1, false);
        RegexValidator single2 = RegexValidator.RegexValidator2(REGEX_2, false);
        RegexValidator single3 = RegexValidator.RegexValidator2(REGEX_3, false);
        String value = "AAC FDE 321";
        String expect = "AACFDE321";
        String[] array = new String[] {"AAC", "FDE", "321"};
        assertEquals("isValid() Multiple", true, multiple.isValid(value));
        assertEquals("isValid() 1st", false, single1.isValid(value));
        assertEquals("isValid() 2nd", true, single2.isValid(value));
        assertEquals("isValid() 3rd", false, single3.isValid(value));
        assertEquals("validate() Multiple", expect, multiple.validate(value));
        assertEquals("validate() 1st", null, single1.validate(value));
        assertEquals("validate() 2nd", expect, single2.validate(value));
        assertEquals("validate() 3rd", null, single3.validate(value));
        multiple.match(value);
        checkArray("match() Multiple", array, multiple.match(value));
        single1.match(value);
        checkArray("match() 1st", null, single1.match(value));
        single2.match(value);
        checkArray("match() 2nd", array, single2.match(value));
        single3.match(value);
        checkArray("match() 3rd", null, single3.match(value));
    }

    @Test
    public void testMultipleInsensitive_test13_decomposed()  {
        RegexValidator multiple = new RegexValidator(MULTIPLE_REGEX, false);
        RegexValidator single1 = RegexValidator.RegexValidator2(REGEX_1, false);
        RegexValidator single2 = RegexValidator.RegexValidator2(REGEX_2, false);
        RegexValidator single3 = RegexValidator.RegexValidator2(REGEX_3, false);
        String value = "AAC FDE 321";
        String expect = "AACFDE321";
        String[] array = new String[] {"AAC", "FDE", "321"};
        assertEquals("isValid() Multiple", true, multiple.isValid(value));
        assertEquals("isValid() 1st", false, single1.isValid(value));
        assertEquals("isValid() 2nd", true, single2.isValid(value));
        assertEquals("isValid() 3rd", false, single3.isValid(value));
        assertEquals("validate() Multiple", expect, multiple.validate(value));
        assertEquals("validate() 1st", null, single1.validate(value));
        assertEquals("validate() 2nd", expect, single2.validate(value));
        assertEquals("validate() 3rd", null, single3.validate(value));
        multiple.match(value);
        checkArray("match() Multiple", array, multiple.match(value));
        single1.match(value);
        checkArray("match() 1st", null, single1.match(value));
        single2.match(value);
        checkArray("match() 2nd", array, single2.match(value));
        single3.match(value);
        checkArray("match() 3rd", null, single3.match(value));
        value = "AAC*FDE*321";
        assertEquals("isValid() Invalid", false, multiple.isValid(value));
    }

    @Test
    public void testMultipleInsensitive_test14_decomposed()  {
        RegexValidator multiple = new RegexValidator(MULTIPLE_REGEX, false);
        RegexValidator single1 = RegexValidator.RegexValidator2(REGEX_1, false);
        RegexValidator single2 = RegexValidator.RegexValidator2(REGEX_2, false);
        RegexValidator single3 = RegexValidator.RegexValidator2(REGEX_3, false);
        String value = "AAC FDE 321";
        String expect = "AACFDE321";
        String[] array = new String[] {"AAC", "FDE", "321"};
        assertEquals("isValid() Multiple", true, multiple.isValid(value));
        assertEquals("isValid() 1st", false, single1.isValid(value));
        assertEquals("isValid() 2nd", true, single2.isValid(value));
        assertEquals("isValid() 3rd", false, single3.isValid(value));
        assertEquals("validate() Multiple", expect, multiple.validate(value));
        assertEquals("validate() 1st", null, single1.validate(value));
        assertEquals("validate() 2nd", expect, single2.validate(value));
        assertEquals("validate() 3rd", null, single3.validate(value));
        multiple.match(value);
        checkArray("match() Multiple", array, multiple.match(value));
        single1.match(value);
        checkArray("match() 1st", null, single1.match(value));
        single2.match(value);
        checkArray("match() 2nd", array, single2.match(value));
        single3.match(value);
        checkArray("match() 3rd", null, single3.match(value));
        value = "AAC*FDE*321";
        assertEquals("isValid() Invalid", false, multiple.isValid(value));
        assertEquals("validate() Invalid", null, multiple.validate(value));
    }

    @Test
    public void testMultipleInsensitive_test15_decomposed()  {
        RegexValidator multiple = new RegexValidator(MULTIPLE_REGEX, false);
        RegexValidator single1 = RegexValidator.RegexValidator2(REGEX_1, false);
        RegexValidator single2 = RegexValidator.RegexValidator2(REGEX_2, false);
        RegexValidator single3 = RegexValidator.RegexValidator2(REGEX_3, false);
        String value = "AAC FDE 321";
        String expect = "AACFDE321";
        String[] array = new String[] {"AAC", "FDE", "321"};
        assertEquals("isValid() Multiple", true, multiple.isValid(value));
        assertEquals("isValid() 1st", false, single1.isValid(value));
        assertEquals("isValid() 2nd", true, single2.isValid(value));
        assertEquals("isValid() 3rd", false, single3.isValid(value));
        assertEquals("validate() Multiple", expect, multiple.validate(value));
        assertEquals("validate() 1st", null, single1.validate(value));
        assertEquals("validate() 2nd", expect, single2.validate(value));
        assertEquals("validate() 3rd", null, single3.validate(value));
        multiple.match(value);
        checkArray("match() Multiple", array, multiple.match(value));
        single1.match(value);
        checkArray("match() 1st", null, single1.match(value));
        single2.match(value);
        checkArray("match() 2nd", array, single2.match(value));
        single3.match(value);
        checkArray("match() 3rd", null, single3.match(value));
        value = "AAC*FDE*321";
        assertEquals("isValid() Invalid", false, multiple.isValid(value));
        assertEquals("validate() Invalid", null, multiple.validate(value));
        assertEquals("match() Multiple", null, multiple.match(value));
    }

    @Test
    public void testNullValue_test0_decomposed()  {
        RegexValidator validator = RegexValidator.RegexValidator3(REGEX);
    }

    @Test
    public void testNullValue_test1_decomposed()  {
        RegexValidator validator = RegexValidator.RegexValidator3(REGEX);
        assertEquals("Instance isValid()", false, validator.isValid(null));
    }

    @Test
    public void testNullValue_test2_decomposed()  {
        RegexValidator validator = RegexValidator.RegexValidator3(REGEX);
        assertEquals("Instance isValid()", false, validator.isValid(null));
        assertEquals("Instance validate()", null, validator.validate(null));
    }

    @Test
    public void testNullValue_test3_decomposed()  {
        RegexValidator validator = RegexValidator.RegexValidator3(REGEX);
        assertEquals("Instance isValid()", false, validator.isValid(null));
        assertEquals("Instance validate()", null, validator.validate(null));
        assertEquals("Instance match()", null, validator.match(null));
    }

    @Test
    public void testMissingRegex_test0_decomposed()  {
        try {
            RegexValidator.RegexValidator3((String) null);
            fail("Single Null - expected IllegalArgumentException");
        } catch (IllegalArgumentException e) {
            assertEquals("Single Null", "Regular expression[0] is missing", e.getMessage());
        }
        try {
            RegexValidator.RegexValidator3("");
            fail("Single Zero Length - expected IllegalArgumentException");
        } catch (IllegalArgumentException e) {
            assertEquals("Single Zero Length", "Regular expression[0] is missing", e.getMessage());
        }
    }

    @Test
    public void testMissingRegex_test1_decomposed()  {
        try {
            RegexValidator.RegexValidator3((String) null);
            fail("Single Null - expected IllegalArgumentException");
        } catch (IllegalArgumentException e) {
            assertEquals("Single Null", "Regular expression[0] is missing", e.getMessage());
        }
        try {
            RegexValidator.RegexValidator3("");
            fail("Single Zero Length - expected IllegalArgumentException");
        } catch (IllegalArgumentException e) {
            assertEquals("Single Zero Length", "Regular expression[0] is missing", e.getMessage());
        }
        try {
            RegexValidator.RegexValidator1((String[]) null);
            fail("Null Array - expected IllegalArgumentException");
        } catch (IllegalArgumentException e) {
            assertEquals("Null Array", "Regular expressions are missing", e.getMessage());
        }
        try {
            RegexValidator.RegexValidator1(new String[0]);
            fail("Zero Length Array - expected IllegalArgumentException");
        } catch (IllegalArgumentException e) {
            assertEquals("Zero Length Array", "Regular expressions are missing", e.getMessage());
        }
    }

    @Test
    public void testMissingRegex_test2_decomposed()  {
        try {
            RegexValidator.RegexValidator3((String) null);
            fail("Single Null - expected IllegalArgumentException");
        } catch (IllegalArgumentException e) {
            assertEquals("Single Null", "Regular expression[0] is missing", e.getMessage());
        }
        try {
            RegexValidator.RegexValidator3("");
            fail("Single Zero Length - expected IllegalArgumentException");
        } catch (IllegalArgumentException e) {
            assertEquals("Single Zero Length", "Regular expression[0] is missing", e.getMessage());
        }
        try {
            RegexValidator.RegexValidator1((String[]) null);
            fail("Null Array - expected IllegalArgumentException");
        } catch (IllegalArgumentException e) {
            assertEquals("Null Array", "Regular expressions are missing", e.getMessage());
        }
        try {
            RegexValidator.RegexValidator1(new String[0]);
            fail("Zero Length Array - expected IllegalArgumentException");
        } catch (IllegalArgumentException e) {
            assertEquals("Zero Length Array", "Regular expressions are missing", e.getMessage());
        }
        String[] expressions = new String[] {"ABC", null};
        try {
            RegexValidator.RegexValidator1(expressions);
            fail("Array has Null - expected IllegalArgumentException");
        } catch (IllegalArgumentException e) {
            assertEquals("Array has Null", "Regular expression[1] is missing", e.getMessage());
        }
    }

    @Test
    public void testMissingRegex_test3_decomposed()  {
        try {
            RegexValidator.RegexValidator3((String) null);
            fail("Single Null - expected IllegalArgumentException");
        } catch (IllegalArgumentException e) {
            assertEquals("Single Null", "Regular expression[0] is missing", e.getMessage());
        }
        try {
            RegexValidator.RegexValidator3("");
            fail("Single Zero Length - expected IllegalArgumentException");
        } catch (IllegalArgumentException e) {
            assertEquals("Single Zero Length", "Regular expression[0] is missing", e.getMessage());
        }
        try {
            RegexValidator.RegexValidator1((String[]) null);
            fail("Null Array - expected IllegalArgumentException");
        } catch (IllegalArgumentException e) {
            assertEquals("Null Array", "Regular expressions are missing", e.getMessage());
        }
        try {
            RegexValidator.RegexValidator1(new String[0]);
            fail("Zero Length Array - expected IllegalArgumentException");
        } catch (IllegalArgumentException e) {
            assertEquals("Zero Length Array", "Regular expressions are missing", e.getMessage());
        }
        String[] expressions = new String[] {"ABC", null};
        try {
            RegexValidator.RegexValidator1(expressions);
            fail("Array has Null - expected IllegalArgumentException");
        } catch (IllegalArgumentException e) {
            assertEquals("Array has Null", "Regular expression[1] is missing", e.getMessage());
        }
        expressions = new String[] {"", "ABC"};
        try {
            RegexValidator.RegexValidator1(expressions);
            fail("Array has Zero Length - expected IllegalArgumentException");
        } catch (IllegalArgumentException e) {
            assertEquals(
                    "Array has Zero Length", "Regular expression[0] is missing", e.getMessage());
        }
    }

    @Test
    public void testExceptions_test0_decomposed()  {
        String invalidRegex = "^([abCD12]*$";
        try {
            RegexValidator.RegexValidator3(invalidRegex);
        } catch (PatternSyntaxException e) {
        }
    }

    @Test
    public void testToString_test0_decomposed()  {
        RegexValidator single = RegexValidator.RegexValidator3(REGEX);
    }

    @Test
    public void testToString_test1_decomposed()  {
        RegexValidator single = RegexValidator.RegexValidator3(REGEX);
        assertEquals("Single", "RegexValidator{" + REGEX + "}", single.toString());
    }

    @Test
    public void testToString_test2_decomposed()  {
        RegexValidator single = RegexValidator.RegexValidator3(REGEX);
        assertEquals("Single", "RegexValidator{" + REGEX + "}", single.toString());
        RegexValidator multiple = RegexValidator.RegexValidator1(new String[] {REGEX, REGEX});
    }

    @Test
    public void testToString_test3_decomposed()  {
        RegexValidator single = RegexValidator.RegexValidator3(REGEX);
        assertEquals("Single", "RegexValidator{" + REGEX + "}", single.toString());
        RegexValidator multiple = RegexValidator.RegexValidator1(new String[] {REGEX, REGEX});
        assertEquals(
                "Multiple", "RegexValidator{" + REGEX + "," + REGEX + "}", multiple.toString());
    }
}