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

import java.util.Random;

/**
 * ISSNValidator Test Case.
 *
 * @since 1.5.0
 */
public class ISSNValidatorTest extends TestCase {

    private static final ISSNValidator VALIDATOR = ISSNValidator.getInstance();

    private final String[] validFormat =
            new String[] {
                "ISSN 0317-8471",
                "1050-124X",
                "ISSN 1562-6865",
                "1063-7710",
                "1748-7188",
                "ISSN 0264-2875",
                "1750-0095",
                "1188-1534",
                "1911-1479",
                "ISSN 1911-1460",
                "0001-6772",
                "1365-201X",
                "0264-3596",
                "1144-875X",
            };

    private final String[] invalidFormat =
            new String[] {
                "", // empty
                "   ", // empty
                "ISBN 0317-8471", // wrong prefix
                "'1050-124X", // leading garbage
                "ISSN1562-6865", // missing separator
                "10637710", // missing separator
                "1748-7188'", // trailing garbage
                "ISSN  0264-2875", // extra space
                "1750 0095", // invalid separator
                "1188_1534", // invalid separator
                "1911-1478", // invalid checkdigit
            };

    /**
     * Create a test case with the specified name.
     *
     * @param name The name of the test
     */
    public ISSNValidatorTest(String name) {
        super(name);
    }

    /** Test isValid() ISSN codes */
    

    /** Test null values */
    

    /** Test Invalid ISSN codes */
    

    

    

    /** Test isValid() ISSN codes and convert them */
    

    /** Test Invalid EAN-13 ISSN prefix codes Test Input length */
    

    /** Test Invalid EAN-13 ISSN codes */
    

    /** Test valid EAN-13 ISSN codes and extract the ISSN */

    @Test
    public void testIsValidISSN_test0_decomposed()  {
        for (String f : validFormat) {
            assertTrue(f, VALIDATOR.isValid(f));
        }
    }

    @Test
    public void testNull_test0_decomposed()  {
        assertFalse("isValid", VALIDATOR.isValid(null));
    }

    @Test
    public void testInvalid_test0_decomposed()  {
        for (String f : invalidFormat) {
            assertFalse(f, VALIDATOR.isValid(f));
        }
    }

    @Test
    public void testIsValidISSNConvertNull_test0_decomposed()  {
        assertNull(VALIDATOR.convertToEAN13(null, "00"));
    }

    @Test
    public void testIsValidISSNConvertSuffix_test0_decomposed()  {
        try {
            assertNull(VALIDATOR.convertToEAN13(null, null));
            fail("Expected IllegalArgumentException");
        } catch (IllegalArgumentException expected) {

        }
        try {
            assertNull(VALIDATOR.convertToEAN13(null, ""));
            fail("Expected IllegalArgumentException");
        } catch (IllegalArgumentException expected) {

        }
        try {
            assertNull(VALIDATOR.convertToEAN13(null, "0"));
            fail("Expected IllegalArgumentException");
        } catch (IllegalArgumentException expected) {

        }
        try {
            assertNull(VALIDATOR.convertToEAN13(null, "A"));
            fail("Expected IllegalArgumentException");
        } catch (IllegalArgumentException expected) {

        }
        try {
            assertNull(VALIDATOR.convertToEAN13(null, "AA"));
            fail("Expected IllegalArgumentException");
        } catch (IllegalArgumentException expected) {

        }
        try {
            assertNull(VALIDATOR.convertToEAN13(null, "999"));
            fail("Expected IllegalArgumentException");
        } catch (IllegalArgumentException expected) {

        }
    }

    @Test
    public void testIsValidISSNConvert_test0_decomposed()  {
        CheckDigit ean13cd = EAN13CheckDigit.EAN13_CHECK_DIGIT;
        Random r = new Random();
        for (String f : validFormat) {
            String suffix = String.format("%02d", r.nextInt(100));
            String ean13 = VALIDATOR.convertToEAN13(f, suffix);
            assertTrue(ean13, ean13cd.isValid(ean13));
        }
    }

    @Test
    public void testIsValidISSNConvert_test1_decomposed()  {
        CheckDigit ean13cd = EAN13CheckDigit.EAN13_CHECK_DIGIT;
        Random r = new Random();
        for (String f : validFormat) {
            String suffix = String.format("%02d", r.nextInt(100));
            String ean13 = VALIDATOR.convertToEAN13(f, suffix);
            assertTrue(ean13, ean13cd.isValid(ean13));
        }
        assertEquals("9771144875007", VALIDATOR.convertToEAN13("1144-875X", "00"));
        assertEquals("9770264359008", VALIDATOR.convertToEAN13("0264-3596", "00"));
        assertEquals("9771234567003", VALIDATOR.convertToEAN13("1234-5679", "00"));
    }

    @Test
    public void testConversionErrors_test0_decomposed()  {
        String input = null;
        try {
            input = "9780072129519";
            VALIDATOR.extractFromEAN13(input);
            fail("Expected IllegalArgumentException for '" + input + "'");
        } catch (IllegalArgumentException e) {
        }
    }

    @Test
    public void testConversionErrors_test1_decomposed()  {
        String input = null;
        try {
            input = "9780072129519";
            VALIDATOR.extractFromEAN13(input);
            fail("Expected IllegalArgumentException for '" + input + "'");
        } catch (IllegalArgumentException e) {
        }
        try {
            input = "9791090636071";
            VALIDATOR.extractFromEAN13(input);
            fail("Expected IllegalArgumentException for '" + input + "'");
        } catch (IllegalArgumentException e) {
        }
        try {
            input = "03178471";
            VALIDATOR.extractFromEAN13(input);
            fail("Expected IllegalArgumentException for '" + input + "'");
        } catch (IllegalArgumentException e) {
        }
    }

    @Test
    public void testValidCheckDigitEan13_test0_decomposed()  {
        assertNull(VALIDATOR.extractFromEAN13("9771234567001"));
        assertNull(VALIDATOR.extractFromEAN13("9771234567002"));
        assertNotNull(VALIDATOR.extractFromEAN13("9771234567003"));
        assertNull(VALIDATOR.extractFromEAN13("9771234567004"));
        assertNull(VALIDATOR.extractFromEAN13("9771234567005"));
        assertNull(VALIDATOR.extractFromEAN13("9771234567006"));
        assertNull(VALIDATOR.extractFromEAN13("9771234567007"));
        assertNull(VALIDATOR.extractFromEAN13("9771234567008"));
        assertNull(VALIDATOR.extractFromEAN13("9771234567009"));
        assertNull(VALIDATOR.extractFromEAN13("9771234567000"));
    }

    @Test
    public void testIsValidExtract_test0_decomposed()  {
        assertEquals("12345679", VALIDATOR.extractFromEAN13("9771234567003"));
        assertEquals("00014664", VALIDATOR.extractFromEAN13("9770001466006"));
        assertEquals("03178471", VALIDATOR.extractFromEAN13("9770317847001"));
        assertEquals("1144875X", VALIDATOR.extractFromEAN13("9771144875007"));
    }
}