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

import org.apache.commons.validator.routines.checkdigit.CheckDigit;
import org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit;

/**
 * CodeValidatorTest.java.
 *
 * @version $Revision$
 * @since Validator 1.4
 */
public class CodeValidatorTest extends TestCase {

    /**
     * Construct a test with the specified name.
     *
     * @param name The name of the test
     */
    public CodeValidatorTest(String name) {
        super(name);
    }

    /**
     * @see junit.framework.TestCase#setUp()
     */
    @Override
    protected void setUp() throws Exception {
        super.setUp();
    }

    /**
     * @see junit.framework.TestCase#tearDown()
     */
    @Override
    protected void tearDown() throws Exception {
        super.tearDown();
    }

    /** Test Check Digit. */
    

    /** Test the minimum/maximum length */
    

    /** Test Regular Expression. */
    

    /** Test Regular Expression. */
    

    

    

    /** Test Regular Expression. */

    @Test
    public void testCheckDigit_test0_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
    }

    @Test
    public void testCheckDigit_test1_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String invalidEAN = "9781930110992";
        String validEAN = "9781930110991";
        assertNull("No CheckDigit", validator.getCheckDigit());
    }

    @Test
    public void testCheckDigit_test2_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String invalidEAN = "9781930110992";
        String validEAN = "9781930110991";
        assertNull("No CheckDigit", validator.getCheckDigit());
        assertEquals("No CheckDigit invalid", invalidEAN, validator.validate(invalidEAN));
        assertEquals("No CheckDigit valid", validEAN, validator.validate(validEAN));
    }

    @Test
    public void testCheckDigit_test3_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String invalidEAN = "9781930110992";
        String validEAN = "9781930110991";
        assertNull("No CheckDigit", validator.getCheckDigit());
        assertEquals("No CheckDigit invalid", invalidEAN, validator.validate(invalidEAN));
        assertEquals("No CheckDigit valid", validEAN, validator.validate(validEAN));
        assertEquals("No CheckDigit (is) invalid", true, validator.isValid(invalidEAN));
        assertEquals("No CheckDigit (is) valid", true, validator.isValid(validEAN));
    }

    @Test
    public void testCheckDigit_test4_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String invalidEAN = "9781930110992";
        String validEAN = "9781930110991";
        assertNull("No CheckDigit", validator.getCheckDigit());
        assertEquals("No CheckDigit invalid", invalidEAN, validator.validate(invalidEAN));
        assertEquals("No CheckDigit valid", validEAN, validator.validate(validEAN));
        assertEquals("No CheckDigit (is) invalid", true, validator.isValid(invalidEAN));
        assertEquals("No CheckDigit (is) valid", true, validator.isValid(validEAN));
        validator =
                CodeValidator.CodeValidator4((String) null, -1, EAN13CheckDigit.EAN13_CHECK_DIGIT);
    }

    @Test
    public void testCheckDigit_test5_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String invalidEAN = "9781930110992";
        String validEAN = "9781930110991";
        assertNull("No CheckDigit", validator.getCheckDigit());
        assertEquals("No CheckDigit invalid", invalidEAN, validator.validate(invalidEAN));
        assertEquals("No CheckDigit valid", validEAN, validator.validate(validEAN));
        assertEquals("No CheckDigit (is) invalid", true, validator.isValid(invalidEAN));
        assertEquals("No CheckDigit (is) valid", true, validator.isValid(validEAN));
        validator =
                CodeValidator.CodeValidator4((String) null, -1, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertNotNull("EAN CheckDigit", validator.getCheckDigit());
    }

    @Test
    public void testCheckDigit_test6_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String invalidEAN = "9781930110992";
        String validEAN = "9781930110991";
        assertNull("No CheckDigit", validator.getCheckDigit());
        assertEquals("No CheckDigit invalid", invalidEAN, validator.validate(invalidEAN));
        assertEquals("No CheckDigit valid", validEAN, validator.validate(validEAN));
        assertEquals("No CheckDigit (is) invalid", true, validator.isValid(invalidEAN));
        assertEquals("No CheckDigit (is) valid", true, validator.isValid(validEAN));
        validator =
                CodeValidator.CodeValidator4((String) null, -1, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertNotNull("EAN CheckDigit", validator.getCheckDigit());
        assertEquals("EAN CheckDigit invalid", null, validator.validate(invalidEAN));
        assertEquals("EAN CheckDigit valid", validEAN, validator.validate(validEAN));
    }

    @Test
    public void testCheckDigit_test7_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String invalidEAN = "9781930110992";
        String validEAN = "9781930110991";
        assertNull("No CheckDigit", validator.getCheckDigit());
        assertEquals("No CheckDigit invalid", invalidEAN, validator.validate(invalidEAN));
        assertEquals("No CheckDigit valid", validEAN, validator.validate(validEAN));
        assertEquals("No CheckDigit (is) invalid", true, validator.isValid(invalidEAN));
        assertEquals("No CheckDigit (is) valid", true, validator.isValid(validEAN));
        validator =
                CodeValidator.CodeValidator4((String) null, -1, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertNotNull("EAN CheckDigit", validator.getCheckDigit());
        assertEquals("EAN CheckDigit invalid", null, validator.validate(invalidEAN));
        assertEquals("EAN CheckDigit valid", validEAN, validator.validate(validEAN));
        assertEquals("EAN CheckDigit (is) invalid", false, validator.isValid(invalidEAN));
        assertEquals("EAN CheckDigit (is) valid", true, validator.isValid(validEAN));
    }

    @Test
    public void testCheckDigit_test8_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String invalidEAN = "9781930110992";
        String validEAN = "9781930110991";
        assertNull("No CheckDigit", validator.getCheckDigit());
        assertEquals("No CheckDigit invalid", invalidEAN, validator.validate(invalidEAN));
        assertEquals("No CheckDigit valid", validEAN, validator.validate(validEAN));
        assertEquals("No CheckDigit (is) invalid", true, validator.isValid(invalidEAN));
        assertEquals("No CheckDigit (is) valid", true, validator.isValid(validEAN));
        validator =
                CodeValidator.CodeValidator4((String) null, -1, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertNotNull("EAN CheckDigit", validator.getCheckDigit());
        assertEquals("EAN CheckDigit invalid", null, validator.validate(invalidEAN));
        assertEquals("EAN CheckDigit valid", validEAN, validator.validate(validEAN));
        assertEquals("EAN CheckDigit (is) invalid", false, validator.isValid(invalidEAN));
        assertEquals("EAN CheckDigit (is) valid", true, validator.isValid(validEAN));
        assertEquals("EAN CheckDigit ex", null, validator.validate("978193011099X"));
    }

    @Test
    public void testLength_test0_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
    }

    @Test
    public void testLength_test1_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String length_10 = "1234567890";
        String length_11 = "12345678901";
        String length_12 = "123456789012";
        String length_20 = "12345678901234567890";
        String length_21 = "123456789012345678901";
        String length_22 = "1234567890123456789012";
        assertEquals("No min", -1, validator.getMinLength());
    }

    @Test
    public void testLength_test2_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String length_10 = "1234567890";
        String length_11 = "12345678901";
        String length_12 = "123456789012";
        String length_20 = "12345678901234567890";
        String length_21 = "123456789012345678901";
        String length_22 = "1234567890123456789012";
        assertEquals("No min", -1, validator.getMinLength());
        assertEquals("No max", -1, validator.getMaxLength());
    }

    @Test
    public void testLength_test3_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String length_10 = "1234567890";
        String length_11 = "12345678901";
        String length_12 = "123456789012";
        String length_20 = "12345678901234567890";
        String length_21 = "123456789012345678901";
        String length_22 = "1234567890123456789012";
        assertEquals("No min", -1, validator.getMinLength());
        assertEquals("No max", -1, validator.getMaxLength());
        assertEquals("No Length 10", length_10, validator.validate(length_10));
        assertEquals("No Length 11", length_11, validator.validate(length_11));
        assertEquals("No Length 12", length_12, validator.validate(length_12));
        assertEquals("No Length 20", length_20, validator.validate(length_20));
        assertEquals("No Length 21", length_21, validator.validate(length_21));
        assertEquals("No Length 22", length_22, validator.validate(length_22));
    }

    @Test
    public void testLength_test4_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String length_10 = "1234567890";
        String length_11 = "12345678901";
        String length_12 = "123456789012";
        String length_20 = "12345678901234567890";
        String length_21 = "123456789012345678901";
        String length_22 = "1234567890123456789012";
        assertEquals("No min", -1, validator.getMinLength());
        assertEquals("No max", -1, validator.getMaxLength());
        assertEquals("No Length 10", length_10, validator.validate(length_10));
        assertEquals("No Length 11", length_11, validator.validate(length_11));
        assertEquals("No Length 12", length_12, validator.validate(length_12));
        assertEquals("No Length 20", length_20, validator.validate(length_20));
        assertEquals("No Length 21", length_21, validator.validate(length_21));
        assertEquals("No Length 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, 11, (String) null);
    }

    @Test
    public void testLength_test5_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String length_10 = "1234567890";
        String length_11 = "12345678901";
        String length_12 = "123456789012";
        String length_20 = "12345678901234567890";
        String length_21 = "123456789012345678901";
        String length_22 = "1234567890123456789012";
        assertEquals("No min", -1, validator.getMinLength());
        assertEquals("No max", -1, validator.getMaxLength());
        assertEquals("No Length 10", length_10, validator.validate(length_10));
        assertEquals("No Length 11", length_11, validator.validate(length_11));
        assertEquals("No Length 12", length_12, validator.validate(length_12));
        assertEquals("No Length 20", length_20, validator.validate(length_20));
        assertEquals("No Length 21", length_21, validator.validate(length_21));
        assertEquals("No Length 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, 11, (String) null);
        assertEquals("Min 11 - min", 11, validator.getMinLength());
    }

    @Test
    public void testLength_test6_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String length_10 = "1234567890";
        String length_11 = "12345678901";
        String length_12 = "123456789012";
        String length_20 = "12345678901234567890";
        String length_21 = "123456789012345678901";
        String length_22 = "1234567890123456789012";
        assertEquals("No min", -1, validator.getMinLength());
        assertEquals("No max", -1, validator.getMaxLength());
        assertEquals("No Length 10", length_10, validator.validate(length_10));
        assertEquals("No Length 11", length_11, validator.validate(length_11));
        assertEquals("No Length 12", length_12, validator.validate(length_12));
        assertEquals("No Length 20", length_20, validator.validate(length_20));
        assertEquals("No Length 21", length_21, validator.validate(length_21));
        assertEquals("No Length 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, 11, (String) null);
        assertEquals("Min 11 - min", 11, validator.getMinLength());
        assertEquals("Min 11 - max", -1, validator.getMaxLength());
    }

    @Test
    public void testLength_test7_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String length_10 = "1234567890";
        String length_11 = "12345678901";
        String length_12 = "123456789012";
        String length_20 = "12345678901234567890";
        String length_21 = "123456789012345678901";
        String length_22 = "1234567890123456789012";
        assertEquals("No min", -1, validator.getMinLength());
        assertEquals("No max", -1, validator.getMaxLength());
        assertEquals("No Length 10", length_10, validator.validate(length_10));
        assertEquals("No Length 11", length_11, validator.validate(length_11));
        assertEquals("No Length 12", length_12, validator.validate(length_12));
        assertEquals("No Length 20", length_20, validator.validate(length_20));
        assertEquals("No Length 21", length_21, validator.validate(length_21));
        assertEquals("No Length 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, 11, (String) null);
        assertEquals("Min 11 - min", 11, validator.getMinLength());
        assertEquals("Min 11 - max", -1, validator.getMaxLength());
        assertEquals("Min 11 - 10", null, validator.validate(length_10));
        assertEquals("Min 11 - 11", length_11, validator.validate(length_11));
        assertEquals("Min 11 - 12", length_12, validator.validate(length_12));
        assertEquals("Min 11 - 20", length_20, validator.validate(length_20));
        assertEquals("Min 11 - 21", length_21, validator.validate(length_21));
        assertEquals("Min 11 - 22", length_22, validator.validate(length_22));
    }

    @Test
    public void testLength_test8_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String length_10 = "1234567890";
        String length_11 = "12345678901";
        String length_12 = "123456789012";
        String length_20 = "12345678901234567890";
        String length_21 = "123456789012345678901";
        String length_22 = "1234567890123456789012";
        assertEquals("No min", -1, validator.getMinLength());
        assertEquals("No max", -1, validator.getMaxLength());
        assertEquals("No Length 10", length_10, validator.validate(length_10));
        assertEquals("No Length 11", length_11, validator.validate(length_11));
        assertEquals("No Length 12", length_12, validator.validate(length_12));
        assertEquals("No Length 20", length_20, validator.validate(length_20));
        assertEquals("No Length 21", length_21, validator.validate(length_21));
        assertEquals("No Length 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, 11, (String) null);
        assertEquals("Min 11 - min", 11, validator.getMinLength());
        assertEquals("Min 11 - max", -1, validator.getMaxLength());
        assertEquals("Min 11 - 10", null, validator.validate(length_10));
        assertEquals("Min 11 - 11", length_11, validator.validate(length_11));
        assertEquals("Min 11 - 12", length_12, validator.validate(length_12));
        assertEquals("Min 11 - 20", length_20, validator.validate(length_20));
        assertEquals("Min 11 - 21", length_21, validator.validate(length_21));
        assertEquals("Min 11 - 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 21, null, -1, (String) null);
    }

    @Test
    public void testLength_test9_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String length_10 = "1234567890";
        String length_11 = "12345678901";
        String length_12 = "123456789012";
        String length_20 = "12345678901234567890";
        String length_21 = "123456789012345678901";
        String length_22 = "1234567890123456789012";
        assertEquals("No min", -1, validator.getMinLength());
        assertEquals("No max", -1, validator.getMaxLength());
        assertEquals("No Length 10", length_10, validator.validate(length_10));
        assertEquals("No Length 11", length_11, validator.validate(length_11));
        assertEquals("No Length 12", length_12, validator.validate(length_12));
        assertEquals("No Length 20", length_20, validator.validate(length_20));
        assertEquals("No Length 21", length_21, validator.validate(length_21));
        assertEquals("No Length 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, 11, (String) null);
        assertEquals("Min 11 - min", 11, validator.getMinLength());
        assertEquals("Min 11 - max", -1, validator.getMaxLength());
        assertEquals("Min 11 - 10", null, validator.validate(length_10));
        assertEquals("Min 11 - 11", length_11, validator.validate(length_11));
        assertEquals("Min 11 - 12", length_12, validator.validate(length_12));
        assertEquals("Min 11 - 20", length_20, validator.validate(length_20));
        assertEquals("Min 11 - 21", length_21, validator.validate(length_21));
        assertEquals("Min 11 - 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 21, null, -1, (String) null);
        assertEquals("Max 21 - min", -1, validator.getMinLength());
    }

    @Test
    public void testLength_test10_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String length_10 = "1234567890";
        String length_11 = "12345678901";
        String length_12 = "123456789012";
        String length_20 = "12345678901234567890";
        String length_21 = "123456789012345678901";
        String length_22 = "1234567890123456789012";
        assertEquals("No min", -1, validator.getMinLength());
        assertEquals("No max", -1, validator.getMaxLength());
        assertEquals("No Length 10", length_10, validator.validate(length_10));
        assertEquals("No Length 11", length_11, validator.validate(length_11));
        assertEquals("No Length 12", length_12, validator.validate(length_12));
        assertEquals("No Length 20", length_20, validator.validate(length_20));
        assertEquals("No Length 21", length_21, validator.validate(length_21));
        assertEquals("No Length 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, 11, (String) null);
        assertEquals("Min 11 - min", 11, validator.getMinLength());
        assertEquals("Min 11 - max", -1, validator.getMaxLength());
        assertEquals("Min 11 - 10", null, validator.validate(length_10));
        assertEquals("Min 11 - 11", length_11, validator.validate(length_11));
        assertEquals("Min 11 - 12", length_12, validator.validate(length_12));
        assertEquals("Min 11 - 20", length_20, validator.validate(length_20));
        assertEquals("Min 11 - 21", length_21, validator.validate(length_21));
        assertEquals("Min 11 - 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 21, null, -1, (String) null);
        assertEquals("Max 21 - min", -1, validator.getMinLength());
        assertEquals("Max 21 - max", 21, validator.getMaxLength());
    }

    @Test
    public void testLength_test11_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String length_10 = "1234567890";
        String length_11 = "12345678901";
        String length_12 = "123456789012";
        String length_20 = "12345678901234567890";
        String length_21 = "123456789012345678901";
        String length_22 = "1234567890123456789012";
        assertEquals("No min", -1, validator.getMinLength());
        assertEquals("No max", -1, validator.getMaxLength());
        assertEquals("No Length 10", length_10, validator.validate(length_10));
        assertEquals("No Length 11", length_11, validator.validate(length_11));
        assertEquals("No Length 12", length_12, validator.validate(length_12));
        assertEquals("No Length 20", length_20, validator.validate(length_20));
        assertEquals("No Length 21", length_21, validator.validate(length_21));
        assertEquals("No Length 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, 11, (String) null);
        assertEquals("Min 11 - min", 11, validator.getMinLength());
        assertEquals("Min 11 - max", -1, validator.getMaxLength());
        assertEquals("Min 11 - 10", null, validator.validate(length_10));
        assertEquals("Min 11 - 11", length_11, validator.validate(length_11));
        assertEquals("Min 11 - 12", length_12, validator.validate(length_12));
        assertEquals("Min 11 - 20", length_20, validator.validate(length_20));
        assertEquals("Min 11 - 21", length_21, validator.validate(length_21));
        assertEquals("Min 11 - 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 21, null, -1, (String) null);
        assertEquals("Max 21 - min", -1, validator.getMinLength());
        assertEquals("Max 21 - max", 21, validator.getMaxLength());
        assertEquals("Max 21 - 10", length_10, validator.validate(length_10));
        assertEquals("Max 21 - 11", length_11, validator.validate(length_11));
        assertEquals("Max 21 - 12", length_12, validator.validate(length_12));
        assertEquals("Max 21 - 20", length_20, validator.validate(length_20));
        assertEquals("Max 21 - 21", length_21, validator.validate(length_21));
        assertEquals("Max 21 - 22", null, validator.validate(length_22));
    }

    @Test
    public void testLength_test12_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String length_10 = "1234567890";
        String length_11 = "12345678901";
        String length_12 = "123456789012";
        String length_20 = "12345678901234567890";
        String length_21 = "123456789012345678901";
        String length_22 = "1234567890123456789012";
        assertEquals("No min", -1, validator.getMinLength());
        assertEquals("No max", -1, validator.getMaxLength());
        assertEquals("No Length 10", length_10, validator.validate(length_10));
        assertEquals("No Length 11", length_11, validator.validate(length_11));
        assertEquals("No Length 12", length_12, validator.validate(length_12));
        assertEquals("No Length 20", length_20, validator.validate(length_20));
        assertEquals("No Length 21", length_21, validator.validate(length_21));
        assertEquals("No Length 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, 11, (String) null);
        assertEquals("Min 11 - min", 11, validator.getMinLength());
        assertEquals("Min 11 - max", -1, validator.getMaxLength());
        assertEquals("Min 11 - 10", null, validator.validate(length_10));
        assertEquals("Min 11 - 11", length_11, validator.validate(length_11));
        assertEquals("Min 11 - 12", length_12, validator.validate(length_12));
        assertEquals("Min 11 - 20", length_20, validator.validate(length_20));
        assertEquals("Min 11 - 21", length_21, validator.validate(length_21));
        assertEquals("Min 11 - 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 21, null, -1, (String) null);
        assertEquals("Max 21 - min", -1, validator.getMinLength());
        assertEquals("Max 21 - max", 21, validator.getMaxLength());
        assertEquals("Max 21 - 10", length_10, validator.validate(length_10));
        assertEquals("Max 21 - 11", length_11, validator.validate(length_11));
        assertEquals("Max 21 - 12", length_12, validator.validate(length_12));
        assertEquals("Max 21 - 20", length_20, validator.validate(length_20));
        assertEquals("Max 21 - 21", length_21, validator.validate(length_21));
        assertEquals("Max 21 - 22", null, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 21, null, 11, (String) null);
    }

    @Test
    public void testLength_test13_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String length_10 = "1234567890";
        String length_11 = "12345678901";
        String length_12 = "123456789012";
        String length_20 = "12345678901234567890";
        String length_21 = "123456789012345678901";
        String length_22 = "1234567890123456789012";
        assertEquals("No min", -1, validator.getMinLength());
        assertEquals("No max", -1, validator.getMaxLength());
        assertEquals("No Length 10", length_10, validator.validate(length_10));
        assertEquals("No Length 11", length_11, validator.validate(length_11));
        assertEquals("No Length 12", length_12, validator.validate(length_12));
        assertEquals("No Length 20", length_20, validator.validate(length_20));
        assertEquals("No Length 21", length_21, validator.validate(length_21));
        assertEquals("No Length 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, 11, (String) null);
        assertEquals("Min 11 - min", 11, validator.getMinLength());
        assertEquals("Min 11 - max", -1, validator.getMaxLength());
        assertEquals("Min 11 - 10", null, validator.validate(length_10));
        assertEquals("Min 11 - 11", length_11, validator.validate(length_11));
        assertEquals("Min 11 - 12", length_12, validator.validate(length_12));
        assertEquals("Min 11 - 20", length_20, validator.validate(length_20));
        assertEquals("Min 11 - 21", length_21, validator.validate(length_21));
        assertEquals("Min 11 - 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 21, null, -1, (String) null);
        assertEquals("Max 21 - min", -1, validator.getMinLength());
        assertEquals("Max 21 - max", 21, validator.getMaxLength());
        assertEquals("Max 21 - 10", length_10, validator.validate(length_10));
        assertEquals("Max 21 - 11", length_11, validator.validate(length_11));
        assertEquals("Max 21 - 12", length_12, validator.validate(length_12));
        assertEquals("Max 21 - 20", length_20, validator.validate(length_20));
        assertEquals("Max 21 - 21", length_21, validator.validate(length_21));
        assertEquals("Max 21 - 22", null, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 21, null, 11, (String) null);
        assertEquals("Min 11 / Max 21 - min", 11, validator.getMinLength());
    }

    @Test
    public void testLength_test14_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String length_10 = "1234567890";
        String length_11 = "12345678901";
        String length_12 = "123456789012";
        String length_20 = "12345678901234567890";
        String length_21 = "123456789012345678901";
        String length_22 = "1234567890123456789012";
        assertEquals("No min", -1, validator.getMinLength());
        assertEquals("No max", -1, validator.getMaxLength());
        assertEquals("No Length 10", length_10, validator.validate(length_10));
        assertEquals("No Length 11", length_11, validator.validate(length_11));
        assertEquals("No Length 12", length_12, validator.validate(length_12));
        assertEquals("No Length 20", length_20, validator.validate(length_20));
        assertEquals("No Length 21", length_21, validator.validate(length_21));
        assertEquals("No Length 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, 11, (String) null);
        assertEquals("Min 11 - min", 11, validator.getMinLength());
        assertEquals("Min 11 - max", -1, validator.getMaxLength());
        assertEquals("Min 11 - 10", null, validator.validate(length_10));
        assertEquals("Min 11 - 11", length_11, validator.validate(length_11));
        assertEquals("Min 11 - 12", length_12, validator.validate(length_12));
        assertEquals("Min 11 - 20", length_20, validator.validate(length_20));
        assertEquals("Min 11 - 21", length_21, validator.validate(length_21));
        assertEquals("Min 11 - 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 21, null, -1, (String) null);
        assertEquals("Max 21 - min", -1, validator.getMinLength());
        assertEquals("Max 21 - max", 21, validator.getMaxLength());
        assertEquals("Max 21 - 10", length_10, validator.validate(length_10));
        assertEquals("Max 21 - 11", length_11, validator.validate(length_11));
        assertEquals("Max 21 - 12", length_12, validator.validate(length_12));
        assertEquals("Max 21 - 20", length_20, validator.validate(length_20));
        assertEquals("Max 21 - 21", length_21, validator.validate(length_21));
        assertEquals("Max 21 - 22", null, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 21, null, 11, (String) null);
        assertEquals("Min 11 / Max 21 - min", 11, validator.getMinLength());
        assertEquals("Min 11 / Max 21 - max", 21, validator.getMaxLength());
    }

    @Test
    public void testLength_test15_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String length_10 = "1234567890";
        String length_11 = "12345678901";
        String length_12 = "123456789012";
        String length_20 = "12345678901234567890";
        String length_21 = "123456789012345678901";
        String length_22 = "1234567890123456789012";
        assertEquals("No min", -1, validator.getMinLength());
        assertEquals("No max", -1, validator.getMaxLength());
        assertEquals("No Length 10", length_10, validator.validate(length_10));
        assertEquals("No Length 11", length_11, validator.validate(length_11));
        assertEquals("No Length 12", length_12, validator.validate(length_12));
        assertEquals("No Length 20", length_20, validator.validate(length_20));
        assertEquals("No Length 21", length_21, validator.validate(length_21));
        assertEquals("No Length 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, 11, (String) null);
        assertEquals("Min 11 - min", 11, validator.getMinLength());
        assertEquals("Min 11 - max", -1, validator.getMaxLength());
        assertEquals("Min 11 - 10", null, validator.validate(length_10));
        assertEquals("Min 11 - 11", length_11, validator.validate(length_11));
        assertEquals("Min 11 - 12", length_12, validator.validate(length_12));
        assertEquals("Min 11 - 20", length_20, validator.validate(length_20));
        assertEquals("Min 11 - 21", length_21, validator.validate(length_21));
        assertEquals("Min 11 - 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 21, null, -1, (String) null);
        assertEquals("Max 21 - min", -1, validator.getMinLength());
        assertEquals("Max 21 - max", 21, validator.getMaxLength());
        assertEquals("Max 21 - 10", length_10, validator.validate(length_10));
        assertEquals("Max 21 - 11", length_11, validator.validate(length_11));
        assertEquals("Max 21 - 12", length_12, validator.validate(length_12));
        assertEquals("Max 21 - 20", length_20, validator.validate(length_20));
        assertEquals("Max 21 - 21", length_21, validator.validate(length_21));
        assertEquals("Max 21 - 22", null, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 21, null, 11, (String) null);
        assertEquals("Min 11 / Max 21 - min", 11, validator.getMinLength());
        assertEquals("Min 11 / Max 21 - max", 21, validator.getMaxLength());
        assertEquals("Min 11 / Max 21 - 10", null, validator.validate(length_10));
        assertEquals("Min 11 / Max 21 - 11", length_11, validator.validate(length_11));
        assertEquals("Min 11 / Max 21 - 12", length_12, validator.validate(length_12));
        assertEquals("Min 11 / Max 21 - 20", length_20, validator.validate(length_20));
        assertEquals("Min 11 / Max 21 - 21", length_21, validator.validate(length_21));
        assertEquals("Min 11 / Max 21 - 22", null, validator.validate(length_22));
    }

    @Test
    public void testLength_test16_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String length_10 = "1234567890";
        String length_11 = "12345678901";
        String length_12 = "123456789012";
        String length_20 = "12345678901234567890";
        String length_21 = "123456789012345678901";
        String length_22 = "1234567890123456789012";
        assertEquals("No min", -1, validator.getMinLength());
        assertEquals("No max", -1, validator.getMaxLength());
        assertEquals("No Length 10", length_10, validator.validate(length_10));
        assertEquals("No Length 11", length_11, validator.validate(length_11));
        assertEquals("No Length 12", length_12, validator.validate(length_12));
        assertEquals("No Length 20", length_20, validator.validate(length_20));
        assertEquals("No Length 21", length_21, validator.validate(length_21));
        assertEquals("No Length 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, 11, (String) null);
        assertEquals("Min 11 - min", 11, validator.getMinLength());
        assertEquals("Min 11 - max", -1, validator.getMaxLength());
        assertEquals("Min 11 - 10", null, validator.validate(length_10));
        assertEquals("Min 11 - 11", length_11, validator.validate(length_11));
        assertEquals("Min 11 - 12", length_12, validator.validate(length_12));
        assertEquals("Min 11 - 20", length_20, validator.validate(length_20));
        assertEquals("Min 11 - 21", length_21, validator.validate(length_21));
        assertEquals("Min 11 - 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 21, null, -1, (String) null);
        assertEquals("Max 21 - min", -1, validator.getMinLength());
        assertEquals("Max 21 - max", 21, validator.getMaxLength());
        assertEquals("Max 21 - 10", length_10, validator.validate(length_10));
        assertEquals("Max 21 - 11", length_11, validator.validate(length_11));
        assertEquals("Max 21 - 12", length_12, validator.validate(length_12));
        assertEquals("Max 21 - 20", length_20, validator.validate(length_20));
        assertEquals("Max 21 - 21", length_21, validator.validate(length_21));
        assertEquals("Max 21 - 22", null, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 21, null, 11, (String) null);
        assertEquals("Min 11 / Max 21 - min", 11, validator.getMinLength());
        assertEquals("Min 11 / Max 21 - max", 21, validator.getMaxLength());
        assertEquals("Min 11 / Max 21 - 10", null, validator.validate(length_10));
        assertEquals("Min 11 / Max 21 - 11", length_11, validator.validate(length_11));
        assertEquals("Min 11 / Max 21 - 12", length_12, validator.validate(length_12));
        assertEquals("Min 11 / Max 21 - 20", length_20, validator.validate(length_20));
        assertEquals("Min 11 / Max 21 - 21", length_21, validator.validate(length_21));
        assertEquals("Min 11 / Max 21 - 22", null, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 11, null, 11, (String) null);
    }

    @Test
    public void testLength_test17_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String length_10 = "1234567890";
        String length_11 = "12345678901";
        String length_12 = "123456789012";
        String length_20 = "12345678901234567890";
        String length_21 = "123456789012345678901";
        String length_22 = "1234567890123456789012";
        assertEquals("No min", -1, validator.getMinLength());
        assertEquals("No max", -1, validator.getMaxLength());
        assertEquals("No Length 10", length_10, validator.validate(length_10));
        assertEquals("No Length 11", length_11, validator.validate(length_11));
        assertEquals("No Length 12", length_12, validator.validate(length_12));
        assertEquals("No Length 20", length_20, validator.validate(length_20));
        assertEquals("No Length 21", length_21, validator.validate(length_21));
        assertEquals("No Length 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, 11, (String) null);
        assertEquals("Min 11 - min", 11, validator.getMinLength());
        assertEquals("Min 11 - max", -1, validator.getMaxLength());
        assertEquals("Min 11 - 10", null, validator.validate(length_10));
        assertEquals("Min 11 - 11", length_11, validator.validate(length_11));
        assertEquals("Min 11 - 12", length_12, validator.validate(length_12));
        assertEquals("Min 11 - 20", length_20, validator.validate(length_20));
        assertEquals("Min 11 - 21", length_21, validator.validate(length_21));
        assertEquals("Min 11 - 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 21, null, -1, (String) null);
        assertEquals("Max 21 - min", -1, validator.getMinLength());
        assertEquals("Max 21 - max", 21, validator.getMaxLength());
        assertEquals("Max 21 - 10", length_10, validator.validate(length_10));
        assertEquals("Max 21 - 11", length_11, validator.validate(length_11));
        assertEquals("Max 21 - 12", length_12, validator.validate(length_12));
        assertEquals("Max 21 - 20", length_20, validator.validate(length_20));
        assertEquals("Max 21 - 21", length_21, validator.validate(length_21));
        assertEquals("Max 21 - 22", null, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 21, null, 11, (String) null);
        assertEquals("Min 11 / Max 21 - min", 11, validator.getMinLength());
        assertEquals("Min 11 / Max 21 - max", 21, validator.getMaxLength());
        assertEquals("Min 11 / Max 21 - 10", null, validator.validate(length_10));
        assertEquals("Min 11 / Max 21 - 11", length_11, validator.validate(length_11));
        assertEquals("Min 11 / Max 21 - 12", length_12, validator.validate(length_12));
        assertEquals("Min 11 / Max 21 - 20", length_20, validator.validate(length_20));
        assertEquals("Min 11 / Max 21 - 21", length_21, validator.validate(length_21));
        assertEquals("Min 11 / Max 21 - 22", null, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 11, null, 11, (String) null);
        assertEquals("Exact 11 - min", 11, validator.getMinLength());
    }

    @Test
    public void testLength_test18_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String length_10 = "1234567890";
        String length_11 = "12345678901";
        String length_12 = "123456789012";
        String length_20 = "12345678901234567890";
        String length_21 = "123456789012345678901";
        String length_22 = "1234567890123456789012";
        assertEquals("No min", -1, validator.getMinLength());
        assertEquals("No max", -1, validator.getMaxLength());
        assertEquals("No Length 10", length_10, validator.validate(length_10));
        assertEquals("No Length 11", length_11, validator.validate(length_11));
        assertEquals("No Length 12", length_12, validator.validate(length_12));
        assertEquals("No Length 20", length_20, validator.validate(length_20));
        assertEquals("No Length 21", length_21, validator.validate(length_21));
        assertEquals("No Length 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, 11, (String) null);
        assertEquals("Min 11 - min", 11, validator.getMinLength());
        assertEquals("Min 11 - max", -1, validator.getMaxLength());
        assertEquals("Min 11 - 10", null, validator.validate(length_10));
        assertEquals("Min 11 - 11", length_11, validator.validate(length_11));
        assertEquals("Min 11 - 12", length_12, validator.validate(length_12));
        assertEquals("Min 11 - 20", length_20, validator.validate(length_20));
        assertEquals("Min 11 - 21", length_21, validator.validate(length_21));
        assertEquals("Min 11 - 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 21, null, -1, (String) null);
        assertEquals("Max 21 - min", -1, validator.getMinLength());
        assertEquals("Max 21 - max", 21, validator.getMaxLength());
        assertEquals("Max 21 - 10", length_10, validator.validate(length_10));
        assertEquals("Max 21 - 11", length_11, validator.validate(length_11));
        assertEquals("Max 21 - 12", length_12, validator.validate(length_12));
        assertEquals("Max 21 - 20", length_20, validator.validate(length_20));
        assertEquals("Max 21 - 21", length_21, validator.validate(length_21));
        assertEquals("Max 21 - 22", null, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 21, null, 11, (String) null);
        assertEquals("Min 11 / Max 21 - min", 11, validator.getMinLength());
        assertEquals("Min 11 / Max 21 - max", 21, validator.getMaxLength());
        assertEquals("Min 11 / Max 21 - 10", null, validator.validate(length_10));
        assertEquals("Min 11 / Max 21 - 11", length_11, validator.validate(length_11));
        assertEquals("Min 11 / Max 21 - 12", length_12, validator.validate(length_12));
        assertEquals("Min 11 / Max 21 - 20", length_20, validator.validate(length_20));
        assertEquals("Min 11 / Max 21 - 21", length_21, validator.validate(length_21));
        assertEquals("Min 11 / Max 21 - 22", null, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 11, null, 11, (String) null);
        assertEquals("Exact 11 - min", 11, validator.getMinLength());
        assertEquals("Exact 11 - max", 11, validator.getMaxLength());
    }

    @Test
    public void testLength_test19_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String length_10 = "1234567890";
        String length_11 = "12345678901";
        String length_12 = "123456789012";
        String length_20 = "12345678901234567890";
        String length_21 = "123456789012345678901";
        String length_22 = "1234567890123456789012";
        assertEquals("No min", -1, validator.getMinLength());
        assertEquals("No max", -1, validator.getMaxLength());
        assertEquals("No Length 10", length_10, validator.validate(length_10));
        assertEquals("No Length 11", length_11, validator.validate(length_11));
        assertEquals("No Length 12", length_12, validator.validate(length_12));
        assertEquals("No Length 20", length_20, validator.validate(length_20));
        assertEquals("No Length 21", length_21, validator.validate(length_21));
        assertEquals("No Length 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, 11, (String) null);
        assertEquals("Min 11 - min", 11, validator.getMinLength());
        assertEquals("Min 11 - max", -1, validator.getMaxLength());
        assertEquals("Min 11 - 10", null, validator.validate(length_10));
        assertEquals("Min 11 - 11", length_11, validator.validate(length_11));
        assertEquals("Min 11 - 12", length_12, validator.validate(length_12));
        assertEquals("Min 11 - 20", length_20, validator.validate(length_20));
        assertEquals("Min 11 - 21", length_21, validator.validate(length_21));
        assertEquals("Min 11 - 22", length_22, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 21, null, -1, (String) null);
        assertEquals("Max 21 - min", -1, validator.getMinLength());
        assertEquals("Max 21 - max", 21, validator.getMaxLength());
        assertEquals("Max 21 - 10", length_10, validator.validate(length_10));
        assertEquals("Max 21 - 11", length_11, validator.validate(length_11));
        assertEquals("Max 21 - 12", length_12, validator.validate(length_12));
        assertEquals("Max 21 - 20", length_20, validator.validate(length_20));
        assertEquals("Max 21 - 21", length_21, validator.validate(length_21));
        assertEquals("Max 21 - 22", null, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 21, null, 11, (String) null);
        assertEquals("Min 11 / Max 21 - min", 11, validator.getMinLength());
        assertEquals("Min 11 / Max 21 - max", 21, validator.getMaxLength());
        assertEquals("Min 11 / Max 21 - 10", null, validator.validate(length_10));
        assertEquals("Min 11 / Max 21 - 11", length_11, validator.validate(length_11));
        assertEquals("Min 11 / Max 21 - 12", length_12, validator.validate(length_12));
        assertEquals("Min 11 / Max 21 - 20", length_20, validator.validate(length_20));
        assertEquals("Min 11 / Max 21 - 21", length_21, validator.validate(length_21));
        assertEquals("Min 11 / Max 21 - 22", null, validator.validate(length_22));
        validator = new CodeValidator(3, (CheckDigit) null, 11, null, 11, (String) null);
        assertEquals("Exact 11 - min", 11, validator.getMinLength());
        assertEquals("Exact 11 - max", 11, validator.getMaxLength());
        assertEquals("Exact 11 - 10", null, validator.validate(length_10));
        assertEquals("Exact 11 - 11", length_11, validator.validate(length_11));
        assertEquals("Exact 11 - 12", null, validator.validate(length_12));
    }

    @Test
    public void testRegex_test0_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
    }

    @Test
    public void testRegex_test1_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String value2 = "12";
        String value3 = "123";
        String value4 = "1234";
        String value5 = "12345";
        String invalid = "12a4";
        assertNull("No Regex", validator.getRegexValidator());
    }

    @Test
    public void testRegex_test2_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String value2 = "12";
        String value3 = "123";
        String value4 = "1234";
        String value5 = "12345";
        String invalid = "12a4";
        assertNull("No Regex", validator.getRegexValidator());
        assertEquals("No Regex 2", value2, validator.validate(value2));
        assertEquals("No Regex 3", value3, validator.validate(value3));
        assertEquals("No Regex 4", value4, validator.validate(value4));
        assertEquals("No Regex 5", value5, validator.validate(value5));
        assertEquals("No Regex invalid", invalid, validator.validate(invalid));
    }

    @Test
    public void testRegex_test3_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String value2 = "12";
        String value3 = "123";
        String value4 = "1234";
        String value5 = "12345";
        String invalid = "12a4";
        assertNull("No Regex", validator.getRegexValidator());
        assertEquals("No Regex 2", value2, validator.validate(value2));
        assertEquals("No Regex 3", value3, validator.validate(value3));
        assertEquals("No Regex 4", value4, validator.validate(value4));
        assertEquals("No Regex 5", value5, validator.validate(value5));
        assertEquals("No Regex invalid", invalid, validator.validate(invalid));
        String regex = "^([0-9]{3,4})$";
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, -1, regex);
    }

    @Test
    public void testRegex_test4_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String value2 = "12";
        String value3 = "123";
        String value4 = "1234";
        String value5 = "12345";
        String invalid = "12a4";
        assertNull("No Regex", validator.getRegexValidator());
        assertEquals("No Regex 2", value2, validator.validate(value2));
        assertEquals("No Regex 3", value3, validator.validate(value3));
        assertEquals("No Regex 4", value4, validator.validate(value4));
        assertEquals("No Regex 5", value5, validator.validate(value5));
        assertEquals("No Regex invalid", invalid, validator.validate(invalid));
        String regex = "^([0-9]{3,4})$";
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, -1, regex);
        assertNotNull("No Regex", validator.getRegexValidator());
    }

    @Test
    public void testRegex_test5_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String value2 = "12";
        String value3 = "123";
        String value4 = "1234";
        String value5 = "12345";
        String invalid = "12a4";
        assertNull("No Regex", validator.getRegexValidator());
        assertEquals("No Regex 2", value2, validator.validate(value2));
        assertEquals("No Regex 3", value3, validator.validate(value3));
        assertEquals("No Regex 4", value4, validator.validate(value4));
        assertEquals("No Regex 5", value5, validator.validate(value5));
        assertEquals("No Regex invalid", invalid, validator.validate(invalid));
        String regex = "^([0-9]{3,4})$";
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, -1, regex);
        assertNotNull("No Regex", validator.getRegexValidator());
        assertEquals("Regex 2", null, validator.validate(value2));
        assertEquals("Regex 3", value3, validator.validate(value3));
        assertEquals("Regex 4", value4, validator.validate(value4));
        assertEquals("Regex 5", null, validator.validate(value5));
        assertEquals("Regex invalid", null, validator.validate(invalid));
    }

    @Test
    public void testRegex_test6_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String value2 = "12";
        String value3 = "123";
        String value4 = "1234";
        String value5 = "12345";
        String invalid = "12a4";
        assertNull("No Regex", validator.getRegexValidator());
        assertEquals("No Regex 2", value2, validator.validate(value2));
        assertEquals("No Regex 3", value3, validator.validate(value3));
        assertEquals("No Regex 4", value4, validator.validate(value4));
        assertEquals("No Regex 5", value5, validator.validate(value5));
        assertEquals("No Regex invalid", invalid, validator.validate(invalid));
        String regex = "^([0-9]{3,4})$";
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, -1, regex);
        assertNotNull("No Regex", validator.getRegexValidator());
        assertEquals("Regex 2", null, validator.validate(value2));
        assertEquals("Regex 3", value3, validator.validate(value3));
        assertEquals("Regex 4", value4, validator.validate(value4));
        assertEquals("Regex 5", null, validator.validate(value5));
        assertEquals("Regex invalid", null, validator.validate(invalid));
        regex = "^([0-9]{3})(?:[-\\s])([0-9]{3})$";
        RegexValidator.RegexValidator3(regex);
    }

    @Test
    public void testRegex_test7_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String value2 = "12";
        String value3 = "123";
        String value4 = "1234";
        String value5 = "12345";
        String invalid = "12a4";
        assertNull("No Regex", validator.getRegexValidator());
        assertEquals("No Regex 2", value2, validator.validate(value2));
        assertEquals("No Regex 3", value3, validator.validate(value3));
        assertEquals("No Regex 4", value4, validator.validate(value4));
        assertEquals("No Regex 5", value5, validator.validate(value5));
        assertEquals("No Regex invalid", invalid, validator.validate(invalid));
        String regex = "^([0-9]{3,4})$";
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, -1, regex);
        assertNotNull("No Regex", validator.getRegexValidator());
        assertEquals("Regex 2", null, validator.validate(value2));
        assertEquals("Regex 3", value3, validator.validate(value3));
        assertEquals("Regex 4", value4, validator.validate(value4));
        assertEquals("Regex 5", null, validator.validate(value5));
        assertEquals("Regex invalid", null, validator.validate(invalid));
        regex = "^([0-9]{3})(?:[-\\s])([0-9]{3})$";
        RegexValidator.RegexValidator3(regex);
        validator =
                CodeValidator.CodeValidator1(
                        RegexValidator.RegexValidator3(regex), 6, (CheckDigit) null);
    }

    @Test
    public void testRegex_test8_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String value2 = "12";
        String value3 = "123";
        String value4 = "1234";
        String value5 = "12345";
        String invalid = "12a4";
        assertNull("No Regex", validator.getRegexValidator());
        assertEquals("No Regex 2", value2, validator.validate(value2));
        assertEquals("No Regex 3", value3, validator.validate(value3));
        assertEquals("No Regex 4", value4, validator.validate(value4));
        assertEquals("No Regex 5", value5, validator.validate(value5));
        assertEquals("No Regex invalid", invalid, validator.validate(invalid));
        String regex = "^([0-9]{3,4})$";
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, -1, regex);
        assertNotNull("No Regex", validator.getRegexValidator());
        assertEquals("Regex 2", null, validator.validate(value2));
        assertEquals("Regex 3", value3, validator.validate(value3));
        assertEquals("Regex 4", value4, validator.validate(value4));
        assertEquals("Regex 5", null, validator.validate(value5));
        assertEquals("Regex invalid", null, validator.validate(invalid));
        regex = "^([0-9]{3})(?:[-\\s])([0-9]{3})$";
        RegexValidator.RegexValidator3(regex);
        validator =
                CodeValidator.CodeValidator1(
                        RegexValidator.RegexValidator3(regex), 6, (CheckDigit) null);
        assertEquals("Reformat 123-456", "123456", validator.validate("123-456"));
        assertEquals("Reformat 123 456", "123456", validator.validate("123 456"));
        assertEquals("Reformat 123456", null, validator.validate("123456"));
        assertEquals("Reformat 123.456", null, validator.validate("123.456"));
    }

    @Test
    public void testRegex_test9_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String value2 = "12";
        String value3 = "123";
        String value4 = "1234";
        String value5 = "12345";
        String invalid = "12a4";
        assertNull("No Regex", validator.getRegexValidator());
        assertEquals("No Regex 2", value2, validator.validate(value2));
        assertEquals("No Regex 3", value3, validator.validate(value3));
        assertEquals("No Regex 4", value4, validator.validate(value4));
        assertEquals("No Regex 5", value5, validator.validate(value5));
        assertEquals("No Regex invalid", invalid, validator.validate(invalid));
        String regex = "^([0-9]{3,4})$";
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, -1, regex);
        assertNotNull("No Regex", validator.getRegexValidator());
        assertEquals("Regex 2", null, validator.validate(value2));
        assertEquals("Regex 3", value3, validator.validate(value3));
        assertEquals("Regex 4", value4, validator.validate(value4));
        assertEquals("Regex 5", null, validator.validate(value5));
        assertEquals("Regex invalid", null, validator.validate(invalid));
        regex = "^([0-9]{3})(?:[-\\s])([0-9]{3})$";
        RegexValidator.RegexValidator3(regex);
        validator =
                CodeValidator.CodeValidator1(
                        RegexValidator.RegexValidator3(regex), 6, (CheckDigit) null);
        assertEquals("Reformat 123-456", "123456", validator.validate("123-456"));
        assertEquals("Reformat 123 456", "123456", validator.validate("123 456"));
        assertEquals("Reformat 123456", null, validator.validate("123456"));
        assertEquals("Reformat 123.456", null, validator.validate("123.456"));
        regex = "^(?:([0-9]{3})(?:[-\\s])([0-9]{3}))|([0-9]{6})$";
        RegexValidator.RegexValidator3(regex);
    }

    @Test
    public void testRegex_test10_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String value2 = "12";
        String value3 = "123";
        String value4 = "1234";
        String value5 = "12345";
        String invalid = "12a4";
        assertNull("No Regex", validator.getRegexValidator());
        assertEquals("No Regex 2", value2, validator.validate(value2));
        assertEquals("No Regex 3", value3, validator.validate(value3));
        assertEquals("No Regex 4", value4, validator.validate(value4));
        assertEquals("No Regex 5", value5, validator.validate(value5));
        assertEquals("No Regex invalid", invalid, validator.validate(invalid));
        String regex = "^([0-9]{3,4})$";
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, -1, regex);
        assertNotNull("No Regex", validator.getRegexValidator());
        assertEquals("Regex 2", null, validator.validate(value2));
        assertEquals("Regex 3", value3, validator.validate(value3));
        assertEquals("Regex 4", value4, validator.validate(value4));
        assertEquals("Regex 5", null, validator.validate(value5));
        assertEquals("Regex invalid", null, validator.validate(invalid));
        regex = "^([0-9]{3})(?:[-\\s])([0-9]{3})$";
        RegexValidator.RegexValidator3(regex);
        validator =
                CodeValidator.CodeValidator1(
                        RegexValidator.RegexValidator3(regex), 6, (CheckDigit) null);
        assertEquals("Reformat 123-456", "123456", validator.validate("123-456"));
        assertEquals("Reformat 123 456", "123456", validator.validate("123 456"));
        assertEquals("Reformat 123456", null, validator.validate("123456"));
        assertEquals("Reformat 123.456", null, validator.validate("123.456"));
        regex = "^(?:([0-9]{3})(?:[-\\s])([0-9]{3}))|([0-9]{6})$";
        RegexValidator.RegexValidator3(regex);
        validator =
                CodeValidator.CodeValidator1(
                        RegexValidator.RegexValidator3(regex), 6, (CheckDigit) null);
    }

    @Test
    public void testRegex_test11_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String value2 = "12";
        String value3 = "123";
        String value4 = "1234";
        String value5 = "12345";
        String invalid = "12a4";
        assertNull("No Regex", validator.getRegexValidator());
        assertEquals("No Regex 2", value2, validator.validate(value2));
        assertEquals("No Regex 3", value3, validator.validate(value3));
        assertEquals("No Regex 4", value4, validator.validate(value4));
        assertEquals("No Regex 5", value5, validator.validate(value5));
        assertEquals("No Regex invalid", invalid, validator.validate(invalid));
        String regex = "^([0-9]{3,4})$";
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, -1, regex);
        assertNotNull("No Regex", validator.getRegexValidator());
        assertEquals("Regex 2", null, validator.validate(value2));
        assertEquals("Regex 3", value3, validator.validate(value3));
        assertEquals("Regex 4", value4, validator.validate(value4));
        assertEquals("Regex 5", null, validator.validate(value5));
        assertEquals("Regex invalid", null, validator.validate(invalid));
        regex = "^([0-9]{3})(?:[-\\s])([0-9]{3})$";
        RegexValidator.RegexValidator3(regex);
        validator =
                CodeValidator.CodeValidator1(
                        RegexValidator.RegexValidator3(regex), 6, (CheckDigit) null);
        assertEquals("Reformat 123-456", "123456", validator.validate("123-456"));
        assertEquals("Reformat 123 456", "123456", validator.validate("123 456"));
        assertEquals("Reformat 123456", null, validator.validate("123456"));
        assertEquals("Reformat 123.456", null, validator.validate("123.456"));
        regex = "^(?:([0-9]{3})(?:[-\\s])([0-9]{3}))|([0-9]{6})$";
        RegexValidator.RegexValidator3(regex);
        validator =
                CodeValidator.CodeValidator1(
                        RegexValidator.RegexValidator3(regex), 6, (CheckDigit) null);
        validator.getRegexValidator();
    }

    @Test
    public void testRegex_test12_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String value2 = "12";
        String value3 = "123";
        String value4 = "1234";
        String value5 = "12345";
        String invalid = "12a4";
        assertNull("No Regex", validator.getRegexValidator());
        assertEquals("No Regex 2", value2, validator.validate(value2));
        assertEquals("No Regex 3", value3, validator.validate(value3));
        assertEquals("No Regex 4", value4, validator.validate(value4));
        assertEquals("No Regex 5", value5, validator.validate(value5));
        assertEquals("No Regex invalid", invalid, validator.validate(invalid));
        String regex = "^([0-9]{3,4})$";
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, -1, regex);
        assertNotNull("No Regex", validator.getRegexValidator());
        assertEquals("Regex 2", null, validator.validate(value2));
        assertEquals("Regex 3", value3, validator.validate(value3));
        assertEquals("Regex 4", value4, validator.validate(value4));
        assertEquals("Regex 5", null, validator.validate(value5));
        assertEquals("Regex invalid", null, validator.validate(invalid));
        regex = "^([0-9]{3})(?:[-\\s])([0-9]{3})$";
        RegexValidator.RegexValidator3(regex);
        validator =
                CodeValidator.CodeValidator1(
                        RegexValidator.RegexValidator3(regex), 6, (CheckDigit) null);
        assertEquals("Reformat 123-456", "123456", validator.validate("123-456"));
        assertEquals("Reformat 123 456", "123456", validator.validate("123 456"));
        assertEquals("Reformat 123456", null, validator.validate("123456"));
        assertEquals("Reformat 123.456", null, validator.validate("123.456"));
        regex = "^(?:([0-9]{3})(?:[-\\s])([0-9]{3}))|([0-9]{6})$";
        RegexValidator.RegexValidator3(regex);
        validator =
                CodeValidator.CodeValidator1(
                        RegexValidator.RegexValidator3(regex), 6, (CheckDigit) null);
        validator.getRegexValidator();
        assertEquals(
                "Reformat 2 Regex",
                "RegexValidator{" + regex + "}",
                validator.getRegexValidator().toString());
    }

    @Test
    public void testRegex_test13_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        String value2 = "12";
        String value3 = "123";
        String value4 = "1234";
        String value5 = "12345";
        String invalid = "12a4";
        assertNull("No Regex", validator.getRegexValidator());
        assertEquals("No Regex 2", value2, validator.validate(value2));
        assertEquals("No Regex 3", value3, validator.validate(value3));
        assertEquals("No Regex 4", value4, validator.validate(value4));
        assertEquals("No Regex 5", value5, validator.validate(value5));
        assertEquals("No Regex invalid", invalid, validator.validate(invalid));
        String regex = "^([0-9]{3,4})$";
        validator = new CodeValidator(3, (CheckDigit) null, -1, null, -1, regex);
        assertNotNull("No Regex", validator.getRegexValidator());
        assertEquals("Regex 2", null, validator.validate(value2));
        assertEquals("Regex 3", value3, validator.validate(value3));
        assertEquals("Regex 4", value4, validator.validate(value4));
        assertEquals("Regex 5", null, validator.validate(value5));
        assertEquals("Regex invalid", null, validator.validate(invalid));
        regex = "^([0-9]{3})(?:[-\\s])([0-9]{3})$";
        RegexValidator.RegexValidator3(regex);
        validator =
                CodeValidator.CodeValidator1(
                        RegexValidator.RegexValidator3(regex), 6, (CheckDigit) null);
        assertEquals("Reformat 123-456", "123456", validator.validate("123-456"));
        assertEquals("Reformat 123 456", "123456", validator.validate("123 456"));
        assertEquals("Reformat 123456", null, validator.validate("123456"));
        assertEquals("Reformat 123.456", null, validator.validate("123.456"));
        regex = "^(?:([0-9]{3})(?:[-\\s])([0-9]{3}))|([0-9]{6})$";
        RegexValidator.RegexValidator3(regex);
        validator =
                CodeValidator.CodeValidator1(
                        RegexValidator.RegexValidator3(regex), 6, (CheckDigit) null);
        validator.getRegexValidator();
        assertEquals(
                "Reformat 2 Regex",
                "RegexValidator{" + regex + "}",
                validator.getRegexValidator().toString());
        assertEquals("Reformat 2 123-456", "123456", validator.validate("123-456"));
        assertEquals("Reformat 2 123 456", "123456", validator.validate("123 456"));
        assertEquals("Reformat 2 123456", "123456", validator.validate("123456"));
    }

    @Test
    public void testNoInput_test0_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
    }

    @Test
    public void testNoInput_test1_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, -1, (String) null);
        assertEquals("Null", null, validator.validate(null));
        assertEquals("Zero Length", null, validator.validate(""));
        assertEquals("Spaces", null, validator.validate("   "));
        assertEquals("Trimmed", "A", validator.validate(" A  "));
    }

    @Test
    public void testValidator294_1_test0_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, 0, (String) null);
    }

    @Test
    public void testValidator294_1_test1_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, 0, (String) null);
        assertEquals("Null", null, validator.validate(null));
    }

    @Test
    public void testValidator294_1_test2_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, 0, (String) null);
        assertEquals("Null", null, validator.validate(null));
        validator = new CodeValidator(3, (CheckDigit) null, 0, null, -1, (String) null);
    }

    @Test
    public void testValidator294_1_test3_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, -1, null, 0, (String) null);
        assertEquals("Null", null, validator.validate(null));
        validator = new CodeValidator(3, (CheckDigit) null, 0, null, -1, (String) null);
        assertEquals("Null", null, validator.validate(null));
    }

    @Test
    public void testValidator294_2_test0_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, 0, null, -1, (String) null);
    }

    @Test
    public void testValidator294_2_test1_decomposed()  {
        CodeValidator validator =
                new CodeValidator(3, (CheckDigit) null, 0, null, -1, (String) null);
        assertEquals("Null", null, validator.validate(null));
    }

    @Test
    public void testConstructors_test0_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
    }

    @Test
    public void testConstructors_test1_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
    }

    @Test
    public void testConstructors_test2_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
    }

    @Test
    public void testConstructors_test3_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
    }

    @Test
    public void testConstructors_test4_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
    }

    @Test
    public void testConstructors_test5_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
    }

    @Test
    public void testConstructors_test6_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
    }

    @Test
    public void testConstructors_test7_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
    }

    @Test
    public void testConstructors_test8_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
    }

    @Test
    public void testConstructors_test9_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
    }

    @Test
    public void testConstructors_test10_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
    }

    @Test
    public void testConstructors_test11_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = new CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, null);
    }

    @Test
    public void testConstructors_test12_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = new CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, null);
        assertEquals("Constructor 3 - regex", regex, validator.getRegexValidator());
    }

    @Test
    public void testConstructors_test13_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = new CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, null);
        assertEquals("Constructor 3 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 3 - min length", 10, validator.getMinLength());
    }

    @Test
    public void testConstructors_test14_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = new CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, null);
        assertEquals("Constructor 3 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 3 - min length", 10, validator.getMinLength());
        assertEquals("Constructor 3 - max length", 20, validator.getMaxLength());
    }

    @Test
    public void testConstructors_test15_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = new CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, null);
        assertEquals("Constructor 3 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 3 - min length", 10, validator.getMinLength());
        assertEquals("Constructor 3 - max length", 20, validator.getMaxLength());
        assertEquals(
                "Constructor 3 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
    }

    @Test
    public void testConstructors_test16_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = new CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, null);
        assertEquals("Constructor 3 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 3 - min length", 10, validator.getMinLength());
        assertEquals("Constructor 3 - max length", 20, validator.getMaxLength());
        assertEquals(
                "Constructor 3 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator5("^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT);
    }

    @Test
    public void testConstructors_test17_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = new CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, null);
        assertEquals("Constructor 3 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 3 - min length", 10, validator.getMinLength());
        assertEquals("Constructor 3 - max length", 20, validator.getMaxLength());
        assertEquals(
                "Constructor 3 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator5("^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
    }

    @Test
    public void testConstructors_test18_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = new CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, null);
        assertEquals("Constructor 3 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 3 - min length", 10, validator.getMinLength());
        assertEquals("Constructor 3 - max length", 20, validator.getMaxLength());
        assertEquals(
                "Constructor 3 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator5("^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 4 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
    }

    @Test
    public void testConstructors_test19_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = new CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, null);
        assertEquals("Constructor 3 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 3 - min length", 10, validator.getMinLength());
        assertEquals("Constructor 3 - max length", 20, validator.getMaxLength());
        assertEquals(
                "Constructor 3 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator5("^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 4 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 4 - min length", -1, validator.getMinLength());
    }

    @Test
    public void testConstructors_test20_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = new CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, null);
        assertEquals("Constructor 3 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 3 - min length", 10, validator.getMinLength());
        assertEquals("Constructor 3 - max length", 20, validator.getMaxLength());
        assertEquals(
                "Constructor 3 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator5("^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 4 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 4 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 4 - max length", -1, validator.getMaxLength());
    }

    @Test
    public void testConstructors_test21_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = new CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, null);
        assertEquals("Constructor 3 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 3 - min length", 10, validator.getMinLength());
        assertEquals("Constructor 3 - max length", 20, validator.getMaxLength());
        assertEquals(
                "Constructor 3 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator5("^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 4 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 4 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 4 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 4 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
    }

    @Test
    public void testConstructors_test22_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = new CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, null);
        assertEquals("Constructor 3 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 3 - min length", 10, validator.getMinLength());
        assertEquals("Constructor 3 - max length", 20, validator.getMaxLength());
        assertEquals(
                "Constructor 3 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator5("^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 4 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 4 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 4 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 4 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator4("^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
    }

    @Test
    public void testConstructors_test23_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = new CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, null);
        assertEquals("Constructor 3 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 3 - min length", 10, validator.getMinLength());
        assertEquals("Constructor 3 - max length", 20, validator.getMaxLength());
        assertEquals(
                "Constructor 3 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator5("^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 4 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 4 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 4 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 4 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator4("^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
    }

    @Test
    public void testConstructors_test24_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = new CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, null);
        assertEquals("Constructor 3 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 3 - min length", 10, validator.getMinLength());
        assertEquals("Constructor 3 - max length", 20, validator.getMaxLength());
        assertEquals(
                "Constructor 3 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator5("^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 4 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 4 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 4 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 4 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator4("^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 5 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
    }

    @Test
    public void testConstructors_test25_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = new CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, null);
        assertEquals("Constructor 3 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 3 - min length", 10, validator.getMinLength());
        assertEquals("Constructor 3 - max length", 20, validator.getMaxLength());
        assertEquals(
                "Constructor 3 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator5("^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 4 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 4 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 4 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 4 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator4("^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 5 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 5 - min length", 13, validator.getMinLength());
    }

    @Test
    public void testConstructors_test26_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = new CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, null);
        assertEquals("Constructor 3 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 3 - min length", 10, validator.getMinLength());
        assertEquals("Constructor 3 - max length", 20, validator.getMaxLength());
        assertEquals(
                "Constructor 3 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator5("^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 4 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 4 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 4 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 4 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator4("^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 5 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 5 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 5 - max length", 13, validator.getMaxLength());
    }

    @Test
    public void testConstructors_test27_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = new CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, null);
        assertEquals("Constructor 3 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 3 - min length", 10, validator.getMinLength());
        assertEquals("Constructor 3 - max length", 20, validator.getMaxLength());
        assertEquals(
                "Constructor 3 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator5("^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 4 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 4 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 4 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 4 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator4("^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 5 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 5 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 5 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 5 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
    }

    @Test
    public void testConstructors_test28_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = new CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, null);
        assertEquals("Constructor 3 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 3 - min length", 10, validator.getMinLength());
        assertEquals("Constructor 3 - max length", 20, validator.getMaxLength());
        assertEquals(
                "Constructor 3 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator5("^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 4 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 4 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 4 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 4 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator4("^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 5 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 5 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 5 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 5 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator =
                new CodeValidator(3, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, null, 10, "^[0-9]*$");
    }

    @Test
    public void testConstructors_test29_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = new CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, null);
        assertEquals("Constructor 3 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 3 - min length", 10, validator.getMinLength());
        assertEquals("Constructor 3 - max length", 20, validator.getMaxLength());
        assertEquals(
                "Constructor 3 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator5("^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 4 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 4 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 4 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 4 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator4("^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 5 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 5 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 5 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 5 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator =
                new CodeValidator(3, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, null, 10, "^[0-9]*$");
        validator.getRegexValidator();
    }

    @Test
    public void testConstructors_test30_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = new CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, null);
        assertEquals("Constructor 3 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 3 - min length", 10, validator.getMinLength());
        assertEquals("Constructor 3 - max length", 20, validator.getMaxLength());
        assertEquals(
                "Constructor 3 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator5("^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 4 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 4 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 4 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 4 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator4("^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 5 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 5 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 5 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 5 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator =
                new CodeValidator(3, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, null, 10, "^[0-9]*$");
        validator.getRegexValidator();
        assertEquals(
                "Constructor 6 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
    }

    @Test
    public void testConstructors_test31_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = new CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, null);
        assertEquals("Constructor 3 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 3 - min length", 10, validator.getMinLength());
        assertEquals("Constructor 3 - max length", 20, validator.getMaxLength());
        assertEquals(
                "Constructor 3 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator5("^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 4 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 4 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 4 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 4 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator4("^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 5 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 5 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 5 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 5 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator =
                new CodeValidator(3, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, null, 10, "^[0-9]*$");
        validator.getRegexValidator();
        assertEquals(
                "Constructor 6 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 6 - min length", 10, validator.getMinLength());
    }

    @Test
    public void testConstructors_test32_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = new CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, null);
        assertEquals("Constructor 3 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 3 - min length", 10, validator.getMinLength());
        assertEquals("Constructor 3 - max length", 20, validator.getMaxLength());
        assertEquals(
                "Constructor 3 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator5("^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 4 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 4 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 4 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 4 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator4("^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 5 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 5 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 5 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 5 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator =
                new CodeValidator(3, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, null, 10, "^[0-9]*$");
        validator.getRegexValidator();
        assertEquals(
                "Constructor 6 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 6 - min length", 10, validator.getMinLength());
        assertEquals("Constructor 6 - max length", 20, validator.getMaxLength());
    }

    @Test
    public void testConstructors_test33_decomposed()  {
        CodeValidator validator = null;
        RegexValidator regex = RegexValidator.RegexValidator3("^[0-9]*$");
        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 1 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 1 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 1 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 1 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        assertEquals("Constructor 2 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 2 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 2 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 2 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = new CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, null);
        assertEquals("Constructor 3 - regex", regex, validator.getRegexValidator());
        assertEquals("Constructor 3 - min length", 10, validator.getMinLength());
        assertEquals("Constructor 3 - max length", 20, validator.getMaxLength());
        assertEquals(
                "Constructor 3 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator5("^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 4 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 4 - min length", -1, validator.getMinLength());
        assertEquals("Constructor 4 - max length", -1, validator.getMaxLength());
        assertEquals(
                "Constructor 4 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator = CodeValidator.CodeValidator4("^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
        validator.getRegexValidator();
        assertEquals(
                "Constructor 5 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 5 - min length", 13, validator.getMinLength());
        assertEquals("Constructor 5 - max length", 13, validator.getMaxLength());
        assertEquals(
                "Constructor 5 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
        validator =
                new CodeValidator(3, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, null, 10, "^[0-9]*$");
        validator.getRegexValidator();
        assertEquals(
                "Constructor 6 - regex",
                "RegexValidator{^[0-9]*$}",
                validator.getRegexValidator().toString());
        assertEquals("Constructor 6 - min length", 10, validator.getMinLength());
        assertEquals("Constructor 6 - max length", 20, validator.getMaxLength());
        assertEquals(
                "Constructor 6 - check digit",
                EAN13CheckDigit.EAN13_CHECK_DIGIT,
                validator.getCheckDigit());
    }
}