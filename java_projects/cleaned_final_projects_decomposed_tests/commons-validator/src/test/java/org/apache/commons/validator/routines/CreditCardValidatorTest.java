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

import org.apache.commons.validator.routines.CreditCardValidator.CreditCardRange;
import org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit;

/**
 * Test the CreditCardValidator class.
 *
 * @version $Revision$
 */
public class CreditCardValidatorTest extends TestCase {

    private static final String VALID_VISA = "4417123456789113"; // 16
    private static final String ERROR_VISA = "4417123456789112";
    private static final String VALID_SHORT_VISA = "4222222222222"; // 13
    private static final String ERROR_SHORT_VISA = "4222222222229";
    private static final String VALID_AMEX = "378282246310005"; // 15
    private static final String ERROR_AMEX = "378282246310001";
    private static final String VALID_MASTERCARD = "5105105105105100";
    private static final String ERROR_MASTERCARD = "5105105105105105";
    private static final String VALID_DISCOVER = "6011000990139424";
    private static final String ERROR_DISCOVER = "6011000990139421";
    private static final String VALID_DISCOVER65 =
            "6534567890123458"; // FIXME need verified test data for Discover with "65" prefix
    private static final String ERROR_DISCOVER65 =
            "6534567890123450"; // FIXME need verified test data for Discover with "65" prefix
    private static final String VALID_DINERS = "30569309025904"; // 14
    private static final String ERROR_DINERS = "30569309025901";
    private static final String VALID_VPAY = "4370000000000061"; // 16
    private static final String VALID_VPAY2 = "4370000000000012";
    private static final String ERROR_VPAY = "4370000000000069";

    private static final String[] VALID_CARDS = {
        VALID_VISA,
        VALID_SHORT_VISA,
        VALID_AMEX,
        VALID_MASTERCARD,
        VALID_DISCOVER,
        VALID_DISCOVER65,
        VALID_DINERS,
        VALID_VPAY,
        VALID_VPAY2,
        "60115564485789458", // VALIDATOR-403
    };

    private static final String[] ERROR_CARDS = {
        ERROR_VISA,
        ERROR_SHORT_VISA,
        ERROR_AMEX,
        ERROR_MASTERCARD,
        ERROR_DISCOVER,
        ERROR_DISCOVER65,
        ERROR_DINERS,
        ERROR_VPAY,
        "",
        "12345678901", // too short (11)
        "12345678901234567890", // too long (20)
        "4417123456789112", // invalid check digit
    };

    /** Constructor for CreditCardValidatorTest. */
    public CreditCardValidatorTest(String name) {
        super(name);
    }

    

    

    /** Test the CodeValidator array constructor */
    

    /** Test the Amex Card validator */
    

    /** Test the Amex Card option */
    

    /** Test the Diners Card validator */
    

    /** Test the Diners Card option */
    

    /** Test the Discover Card validator */
    

    /** Test the Discover Card option */
    

    /** Test the Mastercard Card validator */
    

    /** Test the Mastercard Card option */
    

    /** Test the Visa Card validator */
    

    /** Test the Visa Card option */
    

    

    /** Test using separators */

    @Test
    public void testIsValid_test0_decomposed()  {
        CreditCardValidator ccv = CreditCardValidator.CreditCardValidator0();
    }

    @Test
    public void testIsValid_test1_decomposed()  {
        CreditCardValidator ccv = CreditCardValidator.CreditCardValidator0();
        assertNull(ccv.validate(null));
    }

    @Test
    public void testIsValid_test2_decomposed()  {
        CreditCardValidator ccv = CreditCardValidator.CreditCardValidator0();
        assertNull(ccv.validate(null));
        assertFalse(ccv.isValid(null));
        assertFalse(ccv.isValid(""));
        assertFalse(ccv.isValid("123456789012"));
        assertFalse(ccv.isValid("12345678901234567890"));
        assertFalse(ccv.isValid("4417123456789112"));
        assertFalse(ccv.isValid("4417q23456w89113"));
        assertTrue(ccv.isValid(VALID_VISA));
        assertTrue(ccv.isValid(VALID_SHORT_VISA));
        assertTrue(ccv.isValid(VALID_AMEX));
        assertTrue(ccv.isValid(VALID_MASTERCARD));
        assertTrue(ccv.isValid(VALID_DISCOVER));
        assertTrue(ccv.isValid(VALID_DISCOVER65));
        assertFalse(ccv.isValid(ERROR_VISA));
        assertFalse(ccv.isValid(ERROR_SHORT_VISA));
        assertFalse(ccv.isValid(ERROR_AMEX));
        assertFalse(ccv.isValid(ERROR_MASTERCARD));
        assertFalse(ccv.isValid(ERROR_DISCOVER));
        assertFalse(ccv.isValid(ERROR_DISCOVER65));
    }

    @Test
    public void testIsValid_test3_decomposed()  {
        CreditCardValidator ccv = CreditCardValidator.CreditCardValidator0();
        assertNull(ccv.validate(null));
        assertFalse(ccv.isValid(null));
        assertFalse(ccv.isValid(""));
        assertFalse(ccv.isValid("123456789012"));
        assertFalse(ccv.isValid("12345678901234567890"));
        assertFalse(ccv.isValid("4417123456789112"));
        assertFalse(ccv.isValid("4417q23456w89113"));
        assertTrue(ccv.isValid(VALID_VISA));
        assertTrue(ccv.isValid(VALID_SHORT_VISA));
        assertTrue(ccv.isValid(VALID_AMEX));
        assertTrue(ccv.isValid(VALID_MASTERCARD));
        assertTrue(ccv.isValid(VALID_DISCOVER));
        assertTrue(ccv.isValid(VALID_DISCOVER65));
        assertFalse(ccv.isValid(ERROR_VISA));
        assertFalse(ccv.isValid(ERROR_SHORT_VISA));
        assertFalse(ccv.isValid(ERROR_AMEX));
        assertFalse(ccv.isValid(ERROR_MASTERCARD));
        assertFalse(ccv.isValid(ERROR_DISCOVER));
        assertFalse(ccv.isValid(ERROR_DISCOVER65));
        ccv = new CreditCardValidator(0, CreditCardValidator.AMEX, null, null);
    }

    @Test
    public void testIsValid_test4_decomposed()  {
        CreditCardValidator ccv = CreditCardValidator.CreditCardValidator0();
        assertNull(ccv.validate(null));
        assertFalse(ccv.isValid(null));
        assertFalse(ccv.isValid(""));
        assertFalse(ccv.isValid("123456789012"));
        assertFalse(ccv.isValid("12345678901234567890"));
        assertFalse(ccv.isValid("4417123456789112"));
        assertFalse(ccv.isValid("4417q23456w89113"));
        assertTrue(ccv.isValid(VALID_VISA));
        assertTrue(ccv.isValid(VALID_SHORT_VISA));
        assertTrue(ccv.isValid(VALID_AMEX));
        assertTrue(ccv.isValid(VALID_MASTERCARD));
        assertTrue(ccv.isValid(VALID_DISCOVER));
        assertTrue(ccv.isValid(VALID_DISCOVER65));
        assertFalse(ccv.isValid(ERROR_VISA));
        assertFalse(ccv.isValid(ERROR_SHORT_VISA));
        assertFalse(ccv.isValid(ERROR_AMEX));
        assertFalse(ccv.isValid(ERROR_MASTERCARD));
        assertFalse(ccv.isValid(ERROR_DISCOVER));
        assertFalse(ccv.isValid(ERROR_DISCOVER65));
        ccv = new CreditCardValidator(0, CreditCardValidator.AMEX, null, null);
        assertFalse(ccv.isValid("4417123456789113"));
    }

    @Test
    public void testAddAllowedCardType_test0_decomposed()  {
        CreditCardValidator ccv = new CreditCardValidator(0, CreditCardValidator.NONE, null, null);
    }

    @Test
    public void testAddAllowedCardType_test1_decomposed()  {
        CreditCardValidator ccv = new CreditCardValidator(0, CreditCardValidator.NONE, null, null);
        assertFalse(ccv.isValid(VALID_VISA));
        assertFalse(ccv.isValid(VALID_AMEX));
        assertFalse(ccv.isValid(VALID_MASTERCARD));
        assertFalse(ccv.isValid(VALID_DISCOVER));
        assertFalse(ccv.isValid(VALID_DINERS));
    }

    @Test
    public void testArrayConstructor_test0_decomposed()  {
        CreditCardValidator ccv =
                new CreditCardValidator(
                        1,
                        0,
                        null,
                        new CodeValidator[] {
                            CreditCardValidator.VISA_VALIDATOR, CreditCardValidator.AMEX_VALIDATOR
                        });
    }

    @Test
    public void testArrayConstructor_test1_decomposed()  {
        CreditCardValidator ccv =
                new CreditCardValidator(
                        1,
                        0,
                        null,
                        new CodeValidator[] {
                            CreditCardValidator.VISA_VALIDATOR, CreditCardValidator.AMEX_VALIDATOR
                        });
        assertTrue(ccv.isValid(VALID_VISA));
        assertTrue(ccv.isValid(VALID_SHORT_VISA));
        assertTrue(ccv.isValid(VALID_AMEX));
        assertFalse(ccv.isValid(VALID_MASTERCARD));
        assertFalse(ccv.isValid(VALID_DISCOVER));
        assertFalse(ccv.isValid(ERROR_VISA));
        assertFalse(ccv.isValid(ERROR_SHORT_VISA));
        assertFalse(ccv.isValid(ERROR_AMEX));
        assertFalse(ccv.isValid(ERROR_MASTERCARD));
        assertFalse(ccv.isValid(ERROR_DISCOVER));
    }

    @Test
    public void testArrayConstructor_test2_decomposed()  {
        CreditCardValidator ccv =
                new CreditCardValidator(
                        1,
                        0,
                        null,
                        new CodeValidator[] {
                            CreditCardValidator.VISA_VALIDATOR, CreditCardValidator.AMEX_VALIDATOR
                        });
        assertTrue(ccv.isValid(VALID_VISA));
        assertTrue(ccv.isValid(VALID_SHORT_VISA));
        assertTrue(ccv.isValid(VALID_AMEX));
        assertFalse(ccv.isValid(VALID_MASTERCARD));
        assertFalse(ccv.isValid(VALID_DISCOVER));
        assertFalse(ccv.isValid(ERROR_VISA));
        assertFalse(ccv.isValid(ERROR_SHORT_VISA));
        assertFalse(ccv.isValid(ERROR_AMEX));
        assertFalse(ccv.isValid(ERROR_MASTERCARD));
        assertFalse(ccv.isValid(ERROR_DISCOVER));
        try {
            new CreditCardValidator(1, 0, null, (CodeValidator[]) null);
            fail("Expected IllegalArgumentException");
        } catch (IllegalArgumentException iae) {
        }
    }

    @Test
    public void testAmexValidator_test0_decomposed()  {
        CodeValidator validator = CreditCardValidator.AMEX_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
    }

    @Test
    public void testAmexValidator_test1_decomposed()  {
        CodeValidator validator = CreditCardValidator.AMEX_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
        assertFalse("Length 12", regex.isValid("343456789012"));
        assertFalse("Length 13", regex.isValid("3434567890123"));
        assertFalse("Length 14", regex.isValid("34345678901234"));
        assertTrue("Length 15", regex.isValid("343456789012345"));
        assertFalse("Length 16", regex.isValid("3434567890123456"));
        assertFalse("Length 17", regex.isValid("34345678901234567"));
        assertFalse("Length 18", regex.isValid("343456789012345678"));
        assertFalse("Prefix 33", regex.isValid("333456789012345"));
        assertTrue("Prefix 34", regex.isValid("343456789012345"));
        assertFalse("Prefix 35", regex.isValid("353456789012345"));
        assertFalse("Prefix 36", regex.isValid("363456789012345"));
        assertTrue("Prefix 37", regex.isValid("373456789012345"));
        assertFalse("Prefix 38", regex.isValid("383456789012345"));
        assertFalse("Prefix 41", regex.isValid("413456789012345"));
        assertFalse("Invalid Char", regex.isValid("3434567x9012345"));
        assertTrue("Valid regex", regex.isValid(ERROR_AMEX));
        assertFalse("Invalid", validator.isValid(ERROR_AMEX));
    }

    @Test
    public void testAmexValidator_test2_decomposed()  {
        CodeValidator validator = CreditCardValidator.AMEX_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
        assertFalse("Length 12", regex.isValid("343456789012"));
        assertFalse("Length 13", regex.isValid("3434567890123"));
        assertFalse("Length 14", regex.isValid("34345678901234"));
        assertTrue("Length 15", regex.isValid("343456789012345"));
        assertFalse("Length 16", regex.isValid("3434567890123456"));
        assertFalse("Length 17", regex.isValid("34345678901234567"));
        assertFalse("Length 18", regex.isValid("343456789012345678"));
        assertFalse("Prefix 33", regex.isValid("333456789012345"));
        assertTrue("Prefix 34", regex.isValid("343456789012345"));
        assertFalse("Prefix 35", regex.isValid("353456789012345"));
        assertFalse("Prefix 36", regex.isValid("363456789012345"));
        assertTrue("Prefix 37", regex.isValid("373456789012345"));
        assertFalse("Prefix 38", regex.isValid("383456789012345"));
        assertFalse("Prefix 41", regex.isValid("413456789012345"));
        assertFalse("Invalid Char", regex.isValid("3434567x9012345"));
        assertTrue("Valid regex", regex.isValid(ERROR_AMEX));
        assertFalse("Invalid", validator.isValid(ERROR_AMEX));
        assertNull("validate()", validator.validate(ERROR_AMEX));
        assertEquals(VALID_AMEX, validator.validate(VALID_AMEX));
    }

    @Test
    public void testAmexValidator_test3_decomposed()  {
        CodeValidator validator = CreditCardValidator.AMEX_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
        assertFalse("Length 12", regex.isValid("343456789012"));
        assertFalse("Length 13", regex.isValid("3434567890123"));
        assertFalse("Length 14", regex.isValid("34345678901234"));
        assertTrue("Length 15", regex.isValid("343456789012345"));
        assertFalse("Length 16", regex.isValid("3434567890123456"));
        assertFalse("Length 17", regex.isValid("34345678901234567"));
        assertFalse("Length 18", regex.isValid("343456789012345678"));
        assertFalse("Prefix 33", regex.isValid("333456789012345"));
        assertTrue("Prefix 34", regex.isValid("343456789012345"));
        assertFalse("Prefix 35", regex.isValid("353456789012345"));
        assertFalse("Prefix 36", regex.isValid("363456789012345"));
        assertTrue("Prefix 37", regex.isValid("373456789012345"));
        assertFalse("Prefix 38", regex.isValid("383456789012345"));
        assertFalse("Prefix 41", regex.isValid("413456789012345"));
        assertFalse("Invalid Char", regex.isValid("3434567x9012345"));
        assertTrue("Valid regex", regex.isValid(ERROR_AMEX));
        assertFalse("Invalid", validator.isValid(ERROR_AMEX));
        assertNull("validate()", validator.validate(ERROR_AMEX));
        assertEquals(VALID_AMEX, validator.validate(VALID_AMEX));
        assertTrue("Amex", validator.isValid(VALID_AMEX));
        assertFalse("Diners", validator.isValid(VALID_DINERS));
        assertFalse("Discover", validator.isValid(VALID_DISCOVER));
        assertFalse("Mastercard", validator.isValid(VALID_MASTERCARD));
        assertFalse("Visa", validator.isValid(VALID_VISA));
        assertFalse("Visa Short", validator.isValid(VALID_SHORT_VISA));
        assertTrue("Valid-A", validator.isValid("371449635398431"));
        assertTrue("Valid-B", validator.isValid("340000000000009"));
        assertTrue("Valid-C", validator.isValid("370000000000002"));
        assertTrue("Valid-D", validator.isValid("378734493671000"));
    }

    @Test
    public void testAmexOption_test0_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.AMEX, null, null);
    }

    @Test
    public void testAmexOption_test1_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.AMEX, null, null);
        assertFalse("Invalid", validator.isValid(ERROR_AMEX));
    }

    @Test
    public void testAmexOption_test2_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.AMEX, null, null);
        assertFalse("Invalid", validator.isValid(ERROR_AMEX));
        assertNull("validate()", validator.validate(ERROR_AMEX));
        assertEquals(VALID_AMEX, validator.validate(VALID_AMEX));
    }

    @Test
    public void testAmexOption_test3_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.AMEX, null, null);
        assertFalse("Invalid", validator.isValid(ERROR_AMEX));
        assertNull("validate()", validator.validate(ERROR_AMEX));
        assertEquals(VALID_AMEX, validator.validate(VALID_AMEX));
        assertTrue("Amex", validator.isValid(VALID_AMEX));
        assertFalse("Diners", validator.isValid(VALID_DINERS));
        assertFalse("Discover", validator.isValid(VALID_DISCOVER));
        assertFalse("Mastercard", validator.isValid(VALID_MASTERCARD));
        assertFalse("Visa", validator.isValid(VALID_VISA));
        assertFalse("Visa Short", validator.isValid(VALID_SHORT_VISA));
    }

    @Test
    public void testDinersValidator_test0_decomposed()  {
        CodeValidator validator = CreditCardValidator.DINERS_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
    }

    @Test
    public void testDinersValidator_test1_decomposed()  {
        CodeValidator validator = CreditCardValidator.DINERS_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
        assertFalse("Length 12-300", regex.isValid("300456789012"));
        assertFalse("Length 12-36", regex.isValid("363456789012"));
        assertFalse("Length 13-300", regex.isValid("3004567890123"));
        assertFalse("Length 13-36", regex.isValid("3634567890123"));
        assertTrue("Length 14-300", regex.isValid("30045678901234"));
        assertTrue("Length 14-36", regex.isValid("36345678901234"));
        assertFalse("Length 15-300", regex.isValid("300456789012345"));
        assertFalse("Length 15-36", regex.isValid("363456789012345"));
        assertFalse("Length 16-300", regex.isValid("3004567890123456"));
        assertFalse("Length 16-36", regex.isValid("3634567890123456"));
        assertFalse("Length 17-300", regex.isValid("30045678901234567"));
        assertFalse("Length 17-36", regex.isValid("36345678901234567"));
        assertFalse("Length 18-300", regex.isValid("300456789012345678"));
        assertFalse("Length 18-36", regex.isValid("363456789012345678"));
        assertTrue("Prefix 300", regex.isValid("30045678901234"));
        assertTrue("Prefix 301", regex.isValid("30145678901234"));
        assertTrue("Prefix 302", regex.isValid("30245678901234"));
        assertTrue("Prefix 303", regex.isValid("30345678901234"));
        assertTrue("Prefix 304", regex.isValid("30445678901234"));
        assertTrue("Prefix 305", regex.isValid("30545678901234"));
        assertFalse("Prefix 306", regex.isValid("30645678901234"));
        assertFalse("Prefix 3094", regex.isValid("30945678901234"));
        assertTrue("Prefix 3095", regex.isValid("30955678901234"));
        assertFalse("Prefix 3096", regex.isValid("30965678901234"));
        assertFalse("Prefix 35", regex.isValid("35345678901234"));
        assertTrue("Prefix 36", regex.isValid("36345678901234"));
        assertFalse("Prefix 37", regex.isValid("37345678901234"));
        assertTrue("Prefix 38", regex.isValid("38345678901234"));
        assertTrue("Prefix 39", regex.isValid("39345678901234"));
        assertFalse("Invalid Char-A", regex.isValid("3004567x901234"));
        assertFalse("Invalid Char-B", regex.isValid("3634567x901234"));
        assertTrue("Valid regex", regex.isValid(ERROR_DINERS));
        assertFalse("Invalid", validator.isValid(ERROR_DINERS));
    }

    @Test
    public void testDinersValidator_test2_decomposed()  {
        CodeValidator validator = CreditCardValidator.DINERS_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
        assertFalse("Length 12-300", regex.isValid("300456789012"));
        assertFalse("Length 12-36", regex.isValid("363456789012"));
        assertFalse("Length 13-300", regex.isValid("3004567890123"));
        assertFalse("Length 13-36", regex.isValid("3634567890123"));
        assertTrue("Length 14-300", regex.isValid("30045678901234"));
        assertTrue("Length 14-36", regex.isValid("36345678901234"));
        assertFalse("Length 15-300", regex.isValid("300456789012345"));
        assertFalse("Length 15-36", regex.isValid("363456789012345"));
        assertFalse("Length 16-300", regex.isValid("3004567890123456"));
        assertFalse("Length 16-36", regex.isValid("3634567890123456"));
        assertFalse("Length 17-300", regex.isValid("30045678901234567"));
        assertFalse("Length 17-36", regex.isValid("36345678901234567"));
        assertFalse("Length 18-300", regex.isValid("300456789012345678"));
        assertFalse("Length 18-36", regex.isValid("363456789012345678"));
        assertTrue("Prefix 300", regex.isValid("30045678901234"));
        assertTrue("Prefix 301", regex.isValid("30145678901234"));
        assertTrue("Prefix 302", regex.isValid("30245678901234"));
        assertTrue("Prefix 303", regex.isValid("30345678901234"));
        assertTrue("Prefix 304", regex.isValid("30445678901234"));
        assertTrue("Prefix 305", regex.isValid("30545678901234"));
        assertFalse("Prefix 306", regex.isValid("30645678901234"));
        assertFalse("Prefix 3094", regex.isValid("30945678901234"));
        assertTrue("Prefix 3095", regex.isValid("30955678901234"));
        assertFalse("Prefix 3096", regex.isValid("30965678901234"));
        assertFalse("Prefix 35", regex.isValid("35345678901234"));
        assertTrue("Prefix 36", regex.isValid("36345678901234"));
        assertFalse("Prefix 37", regex.isValid("37345678901234"));
        assertTrue("Prefix 38", regex.isValid("38345678901234"));
        assertTrue("Prefix 39", regex.isValid("39345678901234"));
        assertFalse("Invalid Char-A", regex.isValid("3004567x901234"));
        assertFalse("Invalid Char-B", regex.isValid("3634567x901234"));
        assertTrue("Valid regex", regex.isValid(ERROR_DINERS));
        assertFalse("Invalid", validator.isValid(ERROR_DINERS));
        assertNull("validate()", validator.validate(ERROR_DINERS));
        assertEquals(VALID_DINERS, validator.validate(VALID_DINERS));
    }

    @Test
    public void testDinersValidator_test3_decomposed()  {
        CodeValidator validator = CreditCardValidator.DINERS_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
        assertFalse("Length 12-300", regex.isValid("300456789012"));
        assertFalse("Length 12-36", regex.isValid("363456789012"));
        assertFalse("Length 13-300", regex.isValid("3004567890123"));
        assertFalse("Length 13-36", regex.isValid("3634567890123"));
        assertTrue("Length 14-300", regex.isValid("30045678901234"));
        assertTrue("Length 14-36", regex.isValid("36345678901234"));
        assertFalse("Length 15-300", regex.isValid("300456789012345"));
        assertFalse("Length 15-36", regex.isValid("363456789012345"));
        assertFalse("Length 16-300", regex.isValid("3004567890123456"));
        assertFalse("Length 16-36", regex.isValid("3634567890123456"));
        assertFalse("Length 17-300", regex.isValid("30045678901234567"));
        assertFalse("Length 17-36", regex.isValid("36345678901234567"));
        assertFalse("Length 18-300", regex.isValid("300456789012345678"));
        assertFalse("Length 18-36", regex.isValid("363456789012345678"));
        assertTrue("Prefix 300", regex.isValid("30045678901234"));
        assertTrue("Prefix 301", regex.isValid("30145678901234"));
        assertTrue("Prefix 302", regex.isValid("30245678901234"));
        assertTrue("Prefix 303", regex.isValid("30345678901234"));
        assertTrue("Prefix 304", regex.isValid("30445678901234"));
        assertTrue("Prefix 305", regex.isValid("30545678901234"));
        assertFalse("Prefix 306", regex.isValid("30645678901234"));
        assertFalse("Prefix 3094", regex.isValid("30945678901234"));
        assertTrue("Prefix 3095", regex.isValid("30955678901234"));
        assertFalse("Prefix 3096", regex.isValid("30965678901234"));
        assertFalse("Prefix 35", regex.isValid("35345678901234"));
        assertTrue("Prefix 36", regex.isValid("36345678901234"));
        assertFalse("Prefix 37", regex.isValid("37345678901234"));
        assertTrue("Prefix 38", regex.isValid("38345678901234"));
        assertTrue("Prefix 39", regex.isValid("39345678901234"));
        assertFalse("Invalid Char-A", regex.isValid("3004567x901234"));
        assertFalse("Invalid Char-B", regex.isValid("3634567x901234"));
        assertTrue("Valid regex", regex.isValid(ERROR_DINERS));
        assertFalse("Invalid", validator.isValid(ERROR_DINERS));
        assertNull("validate()", validator.validate(ERROR_DINERS));
        assertEquals(VALID_DINERS, validator.validate(VALID_DINERS));
        assertFalse("Amex", validator.isValid(VALID_AMEX));
        assertTrue("Diners", validator.isValid(VALID_DINERS));
        assertFalse("Discover", validator.isValid(VALID_DISCOVER));
        assertFalse("Mastercard", validator.isValid(VALID_MASTERCARD));
        assertFalse("Visa", validator.isValid(VALID_VISA));
        assertFalse("Visa Short", validator.isValid(VALID_SHORT_VISA));
        assertTrue("Valid-A", validator.isValid("30000000000004"));
        assertTrue("Valid-B", validator.isValid("30123456789019"));
        assertTrue("Valid-C", validator.isValid("36432685260294"));
    }

    @Test
    public void testDinersOption_test0_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.DINERS, null, null);
    }

    @Test
    public void testDinersOption_test1_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.DINERS, null, null);
        assertFalse("Invalid", validator.isValid(ERROR_DINERS));
    }

    @Test
    public void testDinersOption_test2_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.DINERS, null, null);
        assertFalse("Invalid", validator.isValid(ERROR_DINERS));
        assertNull("validate()", validator.validate(ERROR_DINERS));
        assertEquals(VALID_DINERS, validator.validate(VALID_DINERS));
    }

    @Test
    public void testDinersOption_test3_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.DINERS, null, null);
        assertFalse("Invalid", validator.isValid(ERROR_DINERS));
        assertNull("validate()", validator.validate(ERROR_DINERS));
        assertEquals(VALID_DINERS, validator.validate(VALID_DINERS));
        assertFalse("Amex", validator.isValid(VALID_AMEX));
        assertTrue("Diners", validator.isValid(VALID_DINERS));
        assertFalse("Discover", validator.isValid(VALID_DISCOVER));
        assertFalse("Mastercard", validator.isValid(VALID_MASTERCARD));
        assertFalse("Visa", validator.isValid(VALID_VISA));
        assertFalse("Visa Short", validator.isValid(VALID_SHORT_VISA));
    }

    @Test
    public void testDiscoverValidator_test0_decomposed()  {
        CodeValidator validator = CreditCardValidator.DISCOVER_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
    }

    @Test
    public void testDiscoverValidator_test1_decomposed()  {
        CodeValidator validator = CreditCardValidator.DISCOVER_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
        assertFalse("Length 12-6011", regex.isValid("601156789012"));
        assertFalse("Length 12-65", regex.isValid("653456789012"));
        assertFalse("Length 13-6011", regex.isValid("6011567890123"));
        assertFalse("Length 13-65", regex.isValid("6534567890123"));
        assertFalse("Length 14-6011", regex.isValid("60115678901234"));
        assertFalse("Length 14-65", regex.isValid("65345678901234"));
        assertFalse("Length 15-6011", regex.isValid("601156789012345"));
        assertFalse("Length 15-65", regex.isValid("653456789012345"));
        assertTrue("Length 16-6011", regex.isValid("6011567890123456"));
        assertTrue("Length 16-644", regex.isValid("6444567890123456"));
        assertTrue("Length 16-648", regex.isValid("6484567890123456"));
        assertTrue("Length 16-65", regex.isValid("6534567890123456"));
        assertFalse("Length 17-65", regex.isValid("65345678901234567"));
        assertFalse("Length 18-6011", regex.isValid("601156789012345678"));
        assertFalse("Length 18-65", regex.isValid("653456789012345678"));
        assertFalse("Prefix 640", regex.isValid("6404567890123456"));
        assertFalse("Prefix 641", regex.isValid("6414567890123456"));
        assertFalse("Prefix 642", regex.isValid("6424567890123456"));
        assertFalse("Prefix 643", regex.isValid("6434567890123456"));
        assertFalse("Prefix 6010", regex.isValid("6010567890123456"));
        assertFalse("Prefix 6012", regex.isValid("6012567890123456"));
        assertFalse("Invalid Char", regex.isValid("6011567x90123456"));
        assertTrue("Valid regex", regex.isValid(ERROR_DISCOVER));
        assertTrue("Valid regex65", regex.isValid(ERROR_DISCOVER65));
        assertFalse("Invalid", validator.isValid(ERROR_DISCOVER));
        assertFalse("Invalid65", validator.isValid(ERROR_DISCOVER65));
    }

    @Test
    public void testDiscoverValidator_test2_decomposed()  {
        CodeValidator validator = CreditCardValidator.DISCOVER_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
        assertFalse("Length 12-6011", regex.isValid("601156789012"));
        assertFalse("Length 12-65", regex.isValid("653456789012"));
        assertFalse("Length 13-6011", regex.isValid("6011567890123"));
        assertFalse("Length 13-65", regex.isValid("6534567890123"));
        assertFalse("Length 14-6011", regex.isValid("60115678901234"));
        assertFalse("Length 14-65", regex.isValid("65345678901234"));
        assertFalse("Length 15-6011", regex.isValid("601156789012345"));
        assertFalse("Length 15-65", regex.isValid("653456789012345"));
        assertTrue("Length 16-6011", regex.isValid("6011567890123456"));
        assertTrue("Length 16-644", regex.isValid("6444567890123456"));
        assertTrue("Length 16-648", regex.isValid("6484567890123456"));
        assertTrue("Length 16-65", regex.isValid("6534567890123456"));
        assertFalse("Length 17-65", regex.isValid("65345678901234567"));
        assertFalse("Length 18-6011", regex.isValid("601156789012345678"));
        assertFalse("Length 18-65", regex.isValid("653456789012345678"));
        assertFalse("Prefix 640", regex.isValid("6404567890123456"));
        assertFalse("Prefix 641", regex.isValid("6414567890123456"));
        assertFalse("Prefix 642", regex.isValid("6424567890123456"));
        assertFalse("Prefix 643", regex.isValid("6434567890123456"));
        assertFalse("Prefix 6010", regex.isValid("6010567890123456"));
        assertFalse("Prefix 6012", regex.isValid("6012567890123456"));
        assertFalse("Invalid Char", regex.isValid("6011567x90123456"));
        assertTrue("Valid regex", regex.isValid(ERROR_DISCOVER));
        assertTrue("Valid regex65", regex.isValid(ERROR_DISCOVER65));
        assertFalse("Invalid", validator.isValid(ERROR_DISCOVER));
        assertFalse("Invalid65", validator.isValid(ERROR_DISCOVER65));
        assertNull("validate()", validator.validate(ERROR_DISCOVER));
        assertEquals(VALID_DISCOVER, validator.validate(VALID_DISCOVER));
        assertEquals(VALID_DISCOVER65, validator.validate(VALID_DISCOVER65));
    }

    @Test
    public void testDiscoverValidator_test3_decomposed()  {
        CodeValidator validator = CreditCardValidator.DISCOVER_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
        assertFalse("Length 12-6011", regex.isValid("601156789012"));
        assertFalse("Length 12-65", regex.isValid("653456789012"));
        assertFalse("Length 13-6011", regex.isValid("6011567890123"));
        assertFalse("Length 13-65", regex.isValid("6534567890123"));
        assertFalse("Length 14-6011", regex.isValid("60115678901234"));
        assertFalse("Length 14-65", regex.isValid("65345678901234"));
        assertFalse("Length 15-6011", regex.isValid("601156789012345"));
        assertFalse("Length 15-65", regex.isValid("653456789012345"));
        assertTrue("Length 16-6011", regex.isValid("6011567890123456"));
        assertTrue("Length 16-644", regex.isValid("6444567890123456"));
        assertTrue("Length 16-648", regex.isValid("6484567890123456"));
        assertTrue("Length 16-65", regex.isValid("6534567890123456"));
        assertFalse("Length 17-65", regex.isValid("65345678901234567"));
        assertFalse("Length 18-6011", regex.isValid("601156789012345678"));
        assertFalse("Length 18-65", regex.isValid("653456789012345678"));
        assertFalse("Prefix 640", regex.isValid("6404567890123456"));
        assertFalse("Prefix 641", regex.isValid("6414567890123456"));
        assertFalse("Prefix 642", regex.isValid("6424567890123456"));
        assertFalse("Prefix 643", regex.isValid("6434567890123456"));
        assertFalse("Prefix 6010", regex.isValid("6010567890123456"));
        assertFalse("Prefix 6012", regex.isValid("6012567890123456"));
        assertFalse("Invalid Char", regex.isValid("6011567x90123456"));
        assertTrue("Valid regex", regex.isValid(ERROR_DISCOVER));
        assertTrue("Valid regex65", regex.isValid(ERROR_DISCOVER65));
        assertFalse("Invalid", validator.isValid(ERROR_DISCOVER));
        assertFalse("Invalid65", validator.isValid(ERROR_DISCOVER65));
        assertNull("validate()", validator.validate(ERROR_DISCOVER));
        assertEquals(VALID_DISCOVER, validator.validate(VALID_DISCOVER));
        assertEquals(VALID_DISCOVER65, validator.validate(VALID_DISCOVER65));
        assertFalse("Amex", validator.isValid(VALID_AMEX));
        assertFalse("Diners", validator.isValid(VALID_DINERS));
        assertTrue("Discover", validator.isValid(VALID_DISCOVER));
        assertTrue("Discover", validator.isValid(VALID_DISCOVER65));
        assertFalse("Mastercard", validator.isValid(VALID_MASTERCARD));
        assertFalse("Visa", validator.isValid(VALID_VISA));
        assertFalse("Visa Short", validator.isValid(VALID_SHORT_VISA));
        assertTrue("Valid-A", validator.isValid("6011111111111117"));
        assertTrue("Valid-B", validator.isValid("6011000000000004"));
        assertTrue("Valid-C", validator.isValid("6011000000000012"));
    }

    @Test
    public void testDiscoverOption_test0_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.DISCOVER, null, null);
    }

    @Test
    public void testDiscoverOption_test1_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.DISCOVER, null, null);
        assertFalse("Invalid", validator.isValid(ERROR_DISCOVER));
        assertFalse("Invalid65", validator.isValid(ERROR_DISCOVER65));
    }

    @Test
    public void testDiscoverOption_test2_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.DISCOVER, null, null);
        assertFalse("Invalid", validator.isValid(ERROR_DISCOVER));
        assertFalse("Invalid65", validator.isValid(ERROR_DISCOVER65));
        assertNull("validate()", validator.validate(ERROR_DISCOVER));
        assertEquals(VALID_DISCOVER, validator.validate(VALID_DISCOVER));
        assertEquals(VALID_DISCOVER65, validator.validate(VALID_DISCOVER65));
    }

    @Test
    public void testDiscoverOption_test3_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.DISCOVER, null, null);
        assertFalse("Invalid", validator.isValid(ERROR_DISCOVER));
        assertFalse("Invalid65", validator.isValid(ERROR_DISCOVER65));
        assertNull("validate()", validator.validate(ERROR_DISCOVER));
        assertEquals(VALID_DISCOVER, validator.validate(VALID_DISCOVER));
        assertEquals(VALID_DISCOVER65, validator.validate(VALID_DISCOVER65));
        assertFalse("Amex", validator.isValid(VALID_AMEX));
        assertFalse("Diners", validator.isValid(VALID_DINERS));
        assertTrue("Discover", validator.isValid(VALID_DISCOVER));
        assertTrue("Discover", validator.isValid(VALID_DISCOVER65));
        assertFalse("Mastercard", validator.isValid(VALID_MASTERCARD));
        assertFalse("Visa", validator.isValid(VALID_VISA));
        assertFalse("Visa Short", validator.isValid(VALID_SHORT_VISA));
    }

    @Test
    public void testMastercardValidator_test0_decomposed()  {
        CodeValidator validator = CreditCardValidator.MASTERCARD_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
    }

    @Test
    public void testMastercardValidator_test1_decomposed()  {
        CodeValidator validator = CreditCardValidator.MASTERCARD_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
        assertFalse("Length 12", regex.isValid("513456789012"));
        assertFalse("Length 13", regex.isValid("5134567890123"));
        assertFalse("Length 14", regex.isValid("51345678901234"));
        assertFalse("Length 15", regex.isValid("513456789012345"));
        assertTrue("Length 16", regex.isValid("5134567890123456"));
        assertFalse("Length 17", regex.isValid("51345678901234567"));
        assertFalse("Length 18", regex.isValid("513456789012345678"));
        assertFalse("Prefix 41", regex.isValid("4134567890123456"));
        assertFalse("Prefix 50", regex.isValid("5034567890123456"));
        assertTrue("Prefix 51", regex.isValid("5134567890123456"));
        assertTrue("Prefix 52", regex.isValid("5234567890123456"));
        assertTrue("Prefix 53", regex.isValid("5334567890123456"));
        assertTrue("Prefix 54", regex.isValid("5434567890123456"));
        assertTrue("Prefix 55", regex.isValid("5534567890123456"));
        assertFalse("Prefix 56", regex.isValid("5634567890123456"));
        assertFalse("Prefix 61", regex.isValid("6134567890123456"));
        assertFalse("Invalid Char", regex.isValid("5134567x90123456"));
        assertTrue("Valid regex", regex.isValid(ERROR_MASTERCARD));
        assertFalse("Invalid", validator.isValid(ERROR_MASTERCARD));
    }

    @Test
    public void testMastercardValidator_test2_decomposed()  {
        CodeValidator validator = CreditCardValidator.MASTERCARD_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
        assertFalse("Length 12", regex.isValid("513456789012"));
        assertFalse("Length 13", regex.isValid("5134567890123"));
        assertFalse("Length 14", regex.isValid("51345678901234"));
        assertFalse("Length 15", regex.isValid("513456789012345"));
        assertTrue("Length 16", regex.isValid("5134567890123456"));
        assertFalse("Length 17", regex.isValid("51345678901234567"));
        assertFalse("Length 18", regex.isValid("513456789012345678"));
        assertFalse("Prefix 41", regex.isValid("4134567890123456"));
        assertFalse("Prefix 50", regex.isValid("5034567890123456"));
        assertTrue("Prefix 51", regex.isValid("5134567890123456"));
        assertTrue("Prefix 52", regex.isValid("5234567890123456"));
        assertTrue("Prefix 53", regex.isValid("5334567890123456"));
        assertTrue("Prefix 54", regex.isValid("5434567890123456"));
        assertTrue("Prefix 55", regex.isValid("5534567890123456"));
        assertFalse("Prefix 56", regex.isValid("5634567890123456"));
        assertFalse("Prefix 61", regex.isValid("6134567890123456"));
        assertFalse("Invalid Char", regex.isValid("5134567x90123456"));
        assertTrue("Valid regex", regex.isValid(ERROR_MASTERCARD));
        assertFalse("Invalid", validator.isValid(ERROR_MASTERCARD));
        assertNull("validate()", validator.validate(ERROR_MASTERCARD));
        assertEquals(VALID_MASTERCARD, validator.validate(VALID_MASTERCARD));
    }

    @Test
    public void testMastercardValidator_test3_decomposed()  {
        CodeValidator validator = CreditCardValidator.MASTERCARD_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
        assertFalse("Length 12", regex.isValid("513456789012"));
        assertFalse("Length 13", regex.isValid("5134567890123"));
        assertFalse("Length 14", regex.isValid("51345678901234"));
        assertFalse("Length 15", regex.isValid("513456789012345"));
        assertTrue("Length 16", regex.isValid("5134567890123456"));
        assertFalse("Length 17", regex.isValid("51345678901234567"));
        assertFalse("Length 18", regex.isValid("513456789012345678"));
        assertFalse("Prefix 41", regex.isValid("4134567890123456"));
        assertFalse("Prefix 50", regex.isValid("5034567890123456"));
        assertTrue("Prefix 51", regex.isValid("5134567890123456"));
        assertTrue("Prefix 52", regex.isValid("5234567890123456"));
        assertTrue("Prefix 53", regex.isValid("5334567890123456"));
        assertTrue("Prefix 54", regex.isValid("5434567890123456"));
        assertTrue("Prefix 55", regex.isValid("5534567890123456"));
        assertFalse("Prefix 56", regex.isValid("5634567890123456"));
        assertFalse("Prefix 61", regex.isValid("6134567890123456"));
        assertFalse("Invalid Char", regex.isValid("5134567x90123456"));
        assertTrue("Valid regex", regex.isValid(ERROR_MASTERCARD));
        assertFalse("Invalid", validator.isValid(ERROR_MASTERCARD));
        assertNull("validate()", validator.validate(ERROR_MASTERCARD));
        assertEquals(VALID_MASTERCARD, validator.validate(VALID_MASTERCARD));
        assertFalse("Amex", validator.isValid(VALID_AMEX));
        assertFalse("Diners", validator.isValid(VALID_DINERS));
        assertFalse("Discover", validator.isValid(VALID_DISCOVER));
        assertTrue("Mastercard", validator.isValid(VALID_MASTERCARD));
        assertFalse("Visa", validator.isValid(VALID_VISA));
        assertFalse("Visa Short", validator.isValid(VALID_SHORT_VISA));
        assertTrue("Valid-A", validator.isValid("5500000000000004"));
        assertTrue("Valid-B", validator.isValid("5424000000000015"));
        assertTrue("Valid-C", validator.isValid("5301250070000191"));
        assertTrue("Valid-D", validator.isValid("5123456789012346"));
        assertTrue("Valid-E", validator.isValid("5555555555554444"));
    }

    @Test
    public void testMastercardValidator_test4_decomposed()  {
        CodeValidator validator = CreditCardValidator.MASTERCARD_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
        assertFalse("Length 12", regex.isValid("513456789012"));
        assertFalse("Length 13", regex.isValid("5134567890123"));
        assertFalse("Length 14", regex.isValid("51345678901234"));
        assertFalse("Length 15", regex.isValid("513456789012345"));
        assertTrue("Length 16", regex.isValid("5134567890123456"));
        assertFalse("Length 17", regex.isValid("51345678901234567"));
        assertFalse("Length 18", regex.isValid("513456789012345678"));
        assertFalse("Prefix 41", regex.isValid("4134567890123456"));
        assertFalse("Prefix 50", regex.isValid("5034567890123456"));
        assertTrue("Prefix 51", regex.isValid("5134567890123456"));
        assertTrue("Prefix 52", regex.isValid("5234567890123456"));
        assertTrue("Prefix 53", regex.isValid("5334567890123456"));
        assertTrue("Prefix 54", regex.isValid("5434567890123456"));
        assertTrue("Prefix 55", regex.isValid("5534567890123456"));
        assertFalse("Prefix 56", regex.isValid("5634567890123456"));
        assertFalse("Prefix 61", regex.isValid("6134567890123456"));
        assertFalse("Invalid Char", regex.isValid("5134567x90123456"));
        assertTrue("Valid regex", regex.isValid(ERROR_MASTERCARD));
        assertFalse("Invalid", validator.isValid(ERROR_MASTERCARD));
        assertNull("validate()", validator.validate(ERROR_MASTERCARD));
        assertEquals(VALID_MASTERCARD, validator.validate(VALID_MASTERCARD));
        assertFalse("Amex", validator.isValid(VALID_AMEX));
        assertFalse("Diners", validator.isValid(VALID_DINERS));
        assertFalse("Discover", validator.isValid(VALID_DISCOVER));
        assertTrue("Mastercard", validator.isValid(VALID_MASTERCARD));
        assertFalse("Visa", validator.isValid(VALID_VISA));
        assertFalse("Visa Short", validator.isValid(VALID_SHORT_VISA));
        assertTrue("Valid-A", validator.isValid("5500000000000004"));
        assertTrue("Valid-B", validator.isValid("5424000000000015"));
        assertTrue("Valid-C", validator.isValid("5301250070000191"));
        assertTrue("Valid-D", validator.isValid("5123456789012346"));
        assertTrue("Valid-E", validator.isValid("5555555555554444"));
        RegexValidator rev = validator.getRegexValidator();
    }

    @Test
    public void testMastercardValidator_test5_decomposed()  {
        CodeValidator validator = CreditCardValidator.MASTERCARD_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
        assertFalse("Length 12", regex.isValid("513456789012"));
        assertFalse("Length 13", regex.isValid("5134567890123"));
        assertFalse("Length 14", regex.isValid("51345678901234"));
        assertFalse("Length 15", regex.isValid("513456789012345"));
        assertTrue("Length 16", regex.isValid("5134567890123456"));
        assertFalse("Length 17", regex.isValid("51345678901234567"));
        assertFalse("Length 18", regex.isValid("513456789012345678"));
        assertFalse("Prefix 41", regex.isValid("4134567890123456"));
        assertFalse("Prefix 50", regex.isValid("5034567890123456"));
        assertTrue("Prefix 51", regex.isValid("5134567890123456"));
        assertTrue("Prefix 52", regex.isValid("5234567890123456"));
        assertTrue("Prefix 53", regex.isValid("5334567890123456"));
        assertTrue("Prefix 54", regex.isValid("5434567890123456"));
        assertTrue("Prefix 55", regex.isValid("5534567890123456"));
        assertFalse("Prefix 56", regex.isValid("5634567890123456"));
        assertFalse("Prefix 61", regex.isValid("6134567890123456"));
        assertFalse("Invalid Char", regex.isValid("5134567x90123456"));
        assertTrue("Valid regex", regex.isValid(ERROR_MASTERCARD));
        assertFalse("Invalid", validator.isValid(ERROR_MASTERCARD));
        assertNull("validate()", validator.validate(ERROR_MASTERCARD));
        assertEquals(VALID_MASTERCARD, validator.validate(VALID_MASTERCARD));
        assertFalse("Amex", validator.isValid(VALID_AMEX));
        assertFalse("Diners", validator.isValid(VALID_DINERS));
        assertFalse("Discover", validator.isValid(VALID_DISCOVER));
        assertTrue("Mastercard", validator.isValid(VALID_MASTERCARD));
        assertFalse("Visa", validator.isValid(VALID_VISA));
        assertFalse("Visa Short", validator.isValid(VALID_SHORT_VISA));
        assertTrue("Valid-A", validator.isValid("5500000000000004"));
        assertTrue("Valid-B", validator.isValid("5424000000000015"));
        assertTrue("Valid-C", validator.isValid("5301250070000191"));
        assertTrue("Valid-D", validator.isValid("5123456789012346"));
        assertTrue("Valid-E", validator.isValid("5555555555554444"));
        RegexValidator rev = validator.getRegexValidator();
        final String PAD = "0000000000";
        assertFalse("222099", rev.isValid("222099" + PAD));
    }

    @Test
    public void testMastercardValidator_test6_decomposed()  {
        CodeValidator validator = CreditCardValidator.MASTERCARD_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
        assertFalse("Length 12", regex.isValid("513456789012"));
        assertFalse("Length 13", regex.isValid("5134567890123"));
        assertFalse("Length 14", regex.isValid("51345678901234"));
        assertFalse("Length 15", regex.isValid("513456789012345"));
        assertTrue("Length 16", regex.isValid("5134567890123456"));
        assertFalse("Length 17", regex.isValid("51345678901234567"));
        assertFalse("Length 18", regex.isValid("513456789012345678"));
        assertFalse("Prefix 41", regex.isValid("4134567890123456"));
        assertFalse("Prefix 50", regex.isValid("5034567890123456"));
        assertTrue("Prefix 51", regex.isValid("5134567890123456"));
        assertTrue("Prefix 52", regex.isValid("5234567890123456"));
        assertTrue("Prefix 53", regex.isValid("5334567890123456"));
        assertTrue("Prefix 54", regex.isValid("5434567890123456"));
        assertTrue("Prefix 55", regex.isValid("5534567890123456"));
        assertFalse("Prefix 56", regex.isValid("5634567890123456"));
        assertFalse("Prefix 61", regex.isValid("6134567890123456"));
        assertFalse("Invalid Char", regex.isValid("5134567x90123456"));
        assertTrue("Valid regex", regex.isValid(ERROR_MASTERCARD));
        assertFalse("Invalid", validator.isValid(ERROR_MASTERCARD));
        assertNull("validate()", validator.validate(ERROR_MASTERCARD));
        assertEquals(VALID_MASTERCARD, validator.validate(VALID_MASTERCARD));
        assertFalse("Amex", validator.isValid(VALID_AMEX));
        assertFalse("Diners", validator.isValid(VALID_DINERS));
        assertFalse("Discover", validator.isValid(VALID_DISCOVER));
        assertTrue("Mastercard", validator.isValid(VALID_MASTERCARD));
        assertFalse("Visa", validator.isValid(VALID_VISA));
        assertFalse("Visa Short", validator.isValid(VALID_SHORT_VISA));
        assertTrue("Valid-A", validator.isValid("5500000000000004"));
        assertTrue("Valid-B", validator.isValid("5424000000000015"));
        assertTrue("Valid-C", validator.isValid("5301250070000191"));
        assertTrue("Valid-D", validator.isValid("5123456789012346"));
        assertTrue("Valid-E", validator.isValid("5555555555554444"));
        RegexValidator rev = validator.getRegexValidator();
        final String PAD = "0000000000";
        assertFalse("222099", rev.isValid("222099" + PAD));
        for (int i = 222100; i <= 272099; i++) {
            String j = Integer.toString(i) + PAD;
            assertTrue(j, rev.isValid(j));
        }
    }

    @Test
    public void testMastercardValidator_test7_decomposed()  {
        CodeValidator validator = CreditCardValidator.MASTERCARD_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
        assertFalse("Length 12", regex.isValid("513456789012"));
        assertFalse("Length 13", regex.isValid("5134567890123"));
        assertFalse("Length 14", regex.isValid("51345678901234"));
        assertFalse("Length 15", regex.isValid("513456789012345"));
        assertTrue("Length 16", regex.isValid("5134567890123456"));
        assertFalse("Length 17", regex.isValid("51345678901234567"));
        assertFalse("Length 18", regex.isValid("513456789012345678"));
        assertFalse("Prefix 41", regex.isValid("4134567890123456"));
        assertFalse("Prefix 50", regex.isValid("5034567890123456"));
        assertTrue("Prefix 51", regex.isValid("5134567890123456"));
        assertTrue("Prefix 52", regex.isValid("5234567890123456"));
        assertTrue("Prefix 53", regex.isValid("5334567890123456"));
        assertTrue("Prefix 54", regex.isValid("5434567890123456"));
        assertTrue("Prefix 55", regex.isValid("5534567890123456"));
        assertFalse("Prefix 56", regex.isValid("5634567890123456"));
        assertFalse("Prefix 61", regex.isValid("6134567890123456"));
        assertFalse("Invalid Char", regex.isValid("5134567x90123456"));
        assertTrue("Valid regex", regex.isValid(ERROR_MASTERCARD));
        assertFalse("Invalid", validator.isValid(ERROR_MASTERCARD));
        assertNull("validate()", validator.validate(ERROR_MASTERCARD));
        assertEquals(VALID_MASTERCARD, validator.validate(VALID_MASTERCARD));
        assertFalse("Amex", validator.isValid(VALID_AMEX));
        assertFalse("Diners", validator.isValid(VALID_DINERS));
        assertFalse("Discover", validator.isValid(VALID_DISCOVER));
        assertTrue("Mastercard", validator.isValid(VALID_MASTERCARD));
        assertFalse("Visa", validator.isValid(VALID_VISA));
        assertFalse("Visa Short", validator.isValid(VALID_SHORT_VISA));
        assertTrue("Valid-A", validator.isValid("5500000000000004"));
        assertTrue("Valid-B", validator.isValid("5424000000000015"));
        assertTrue("Valid-C", validator.isValid("5301250070000191"));
        assertTrue("Valid-D", validator.isValid("5123456789012346"));
        assertTrue("Valid-E", validator.isValid("5555555555554444"));
        RegexValidator rev = validator.getRegexValidator();
        final String PAD = "0000000000";
        assertFalse("222099", rev.isValid("222099" + PAD));
        for (int i = 222100; i <= 272099; i++) {
            String j = Integer.toString(i) + PAD;
            assertTrue(j, rev.isValid(j));
        }
        assertFalse("272100", rev.isValid("272100" + PAD));
    }

    @Test
    public void testMastercardOption_test0_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.MASTERCARD, null, null);
    }

    @Test
    public void testMastercardOption_test1_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.MASTERCARD, null, null);
        assertFalse("Invalid", validator.isValid(ERROR_MASTERCARD));
    }

    @Test
    public void testMastercardOption_test2_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.MASTERCARD, null, null);
        assertFalse("Invalid", validator.isValid(ERROR_MASTERCARD));
        assertNull("validate()", validator.validate(ERROR_MASTERCARD));
        assertEquals(VALID_MASTERCARD, validator.validate(VALID_MASTERCARD));
    }

    @Test
    public void testMastercardOption_test3_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.MASTERCARD, null, null);
        assertFalse("Invalid", validator.isValid(ERROR_MASTERCARD));
        assertNull("validate()", validator.validate(ERROR_MASTERCARD));
        assertEquals(VALID_MASTERCARD, validator.validate(VALID_MASTERCARD));
        assertFalse("Amex", validator.isValid(VALID_AMEX));
        assertFalse("Diners", validator.isValid(VALID_DINERS));
        assertFalse("Discover", validator.isValid(VALID_DISCOVER));
        assertTrue("Mastercard", validator.isValid(VALID_MASTERCARD));
        assertFalse("Visa", validator.isValid(VALID_VISA));
        assertFalse("Visa Short", validator.isValid(VALID_SHORT_VISA));
    }

    @Test
    public void testVisaValidator_test0_decomposed()  {
        CodeValidator validator = CreditCardValidator.VISA_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
    }

    @Test
    public void testVisaValidator_test1_decomposed()  {
        CodeValidator validator = CreditCardValidator.VISA_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
        assertFalse("Length 12", regex.isValid("423456789012"));
        assertTrue("Length 13", regex.isValid("4234567890123"));
        assertFalse("Length 14", regex.isValid("42345678901234"));
        assertFalse("Length 15", regex.isValid("423456789012345"));
        assertTrue("Length 16", regex.isValid("4234567890123456"));
        assertFalse("Length 17", regex.isValid("42345678901234567"));
        assertFalse("Length 18", regex.isValid("423456789012345678"));
        assertFalse("Invalid Pref-A", regex.isValid("3234567890123"));
        assertFalse("Invalid Pref-B", regex.isValid("3234567890123456"));
        assertFalse("Invalid Char-A", regex.isValid("4234567x90123"));
        assertFalse("Invalid Char-B", regex.isValid("4234567x90123456"));
        assertTrue("Valid regex", regex.isValid(ERROR_VISA));
        assertTrue("Valid regex-S", regex.isValid(ERROR_SHORT_VISA));
        assertFalse("Invalid", validator.isValid(ERROR_VISA));
        assertFalse("Invalid-S", validator.isValid(ERROR_SHORT_VISA));
    }

    @Test
    public void testVisaValidator_test2_decomposed()  {
        CodeValidator validator = CreditCardValidator.VISA_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
        assertFalse("Length 12", regex.isValid("423456789012"));
        assertTrue("Length 13", regex.isValid("4234567890123"));
        assertFalse("Length 14", regex.isValid("42345678901234"));
        assertFalse("Length 15", regex.isValid("423456789012345"));
        assertTrue("Length 16", regex.isValid("4234567890123456"));
        assertFalse("Length 17", regex.isValid("42345678901234567"));
        assertFalse("Length 18", regex.isValid("423456789012345678"));
        assertFalse("Invalid Pref-A", regex.isValid("3234567890123"));
        assertFalse("Invalid Pref-B", regex.isValid("3234567890123456"));
        assertFalse("Invalid Char-A", regex.isValid("4234567x90123"));
        assertFalse("Invalid Char-B", regex.isValid("4234567x90123456"));
        assertTrue("Valid regex", regex.isValid(ERROR_VISA));
        assertTrue("Valid regex-S", regex.isValid(ERROR_SHORT_VISA));
        assertFalse("Invalid", validator.isValid(ERROR_VISA));
        assertFalse("Invalid-S", validator.isValid(ERROR_SHORT_VISA));
        assertNull("validate()", validator.validate(ERROR_VISA));
        assertEquals(VALID_VISA, validator.validate(VALID_VISA));
        assertEquals(VALID_SHORT_VISA, validator.validate(VALID_SHORT_VISA));
    }

    @Test
    public void testVisaValidator_test3_decomposed()  {
        CodeValidator validator = CreditCardValidator.VISA_VALIDATOR;
        RegexValidator regex = validator.getRegexValidator();
        assertFalse("Length 12", regex.isValid("423456789012"));
        assertTrue("Length 13", regex.isValid("4234567890123"));
        assertFalse("Length 14", regex.isValid("42345678901234"));
        assertFalse("Length 15", regex.isValid("423456789012345"));
        assertTrue("Length 16", regex.isValid("4234567890123456"));
        assertFalse("Length 17", regex.isValid("42345678901234567"));
        assertFalse("Length 18", regex.isValid("423456789012345678"));
        assertFalse("Invalid Pref-A", regex.isValid("3234567890123"));
        assertFalse("Invalid Pref-B", regex.isValid("3234567890123456"));
        assertFalse("Invalid Char-A", regex.isValid("4234567x90123"));
        assertFalse("Invalid Char-B", regex.isValid("4234567x90123456"));
        assertTrue("Valid regex", regex.isValid(ERROR_VISA));
        assertTrue("Valid regex-S", regex.isValid(ERROR_SHORT_VISA));
        assertFalse("Invalid", validator.isValid(ERROR_VISA));
        assertFalse("Invalid-S", validator.isValid(ERROR_SHORT_VISA));
        assertNull("validate()", validator.validate(ERROR_VISA));
        assertEquals(VALID_VISA, validator.validate(VALID_VISA));
        assertEquals(VALID_SHORT_VISA, validator.validate(VALID_SHORT_VISA));
        assertFalse("Amex", validator.isValid(VALID_AMEX));
        assertFalse("Diners", validator.isValid(VALID_DINERS));
        assertFalse("Discover", validator.isValid(VALID_DISCOVER));
        assertFalse("Mastercard", validator.isValid(VALID_MASTERCARD));
        assertTrue("Visa", validator.isValid(VALID_VISA));
        assertTrue("Visa Short", validator.isValid(VALID_SHORT_VISA));
        assertTrue("Valid-A", validator.isValid("4111111111111111"));
        assertTrue("Valid-C", validator.isValid("4543059999999982"));
        assertTrue("Valid-B", validator.isValid("4462000000000003"));
        assertTrue("Valid-D", validator.isValid("4508750000000009"));
        assertTrue("Valid-E", validator.isValid("4012888888881881"));
    }

    @Test
    public void testVisaOption_test0_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.VISA, null, null);
    }

    @Test
    public void testVisaOption_test1_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.VISA, null, null);
        assertFalse("Invalid", validator.isValid(ERROR_VISA));
        assertFalse("Invalid-S", validator.isValid(ERROR_SHORT_VISA));
    }

    @Test
    public void testVisaOption_test2_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.VISA, null, null);
        assertFalse("Invalid", validator.isValid(ERROR_VISA));
        assertFalse("Invalid-S", validator.isValid(ERROR_SHORT_VISA));
        assertNull("validate()", validator.validate(ERROR_VISA));
        assertEquals(VALID_VISA, validator.validate(VALID_VISA));
        assertEquals(VALID_SHORT_VISA, validator.validate(VALID_SHORT_VISA));
    }

    @Test
    public void testVisaOption_test3_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.VISA, null, null);
        assertFalse("Invalid", validator.isValid(ERROR_VISA));
        assertFalse("Invalid-S", validator.isValid(ERROR_SHORT_VISA));
        assertNull("validate()", validator.validate(ERROR_VISA));
        assertEquals(VALID_VISA, validator.validate(VALID_VISA));
        assertEquals(VALID_SHORT_VISA, validator.validate(VALID_SHORT_VISA));
        assertFalse("Amex", validator.isValid(VALID_AMEX));
        assertFalse("Diners", validator.isValid(VALID_DINERS));
        assertFalse("Discover", validator.isValid(VALID_DISCOVER));
        assertFalse("Mastercard", validator.isValid(VALID_MASTERCARD));
        assertTrue("Visa", validator.isValid(VALID_VISA));
        assertTrue("Visa Short", validator.isValid(VALID_SHORT_VISA));
    }

    @Test
    public void testVPayOption_test0_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.VPAY, null, null);
    }

    @Test
    public void testVPayOption_test1_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.VPAY, null, null);
        assertTrue("Valid", validator.isValid(VALID_VPAY));
        assertTrue("Valid", validator.isValid(VALID_VPAY2));
        assertFalse("Invalid", validator.isValid(ERROR_VPAY));
    }

    @Test
    public void testVPayOption_test2_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.VPAY, null, null);
        assertTrue("Valid", validator.isValid(VALID_VPAY));
        assertTrue("Valid", validator.isValid(VALID_VPAY2));
        assertFalse("Invalid", validator.isValid(ERROR_VPAY));
        assertEquals(VALID_VPAY, validator.validate(VALID_VPAY));
        assertEquals(VALID_VPAY2, validator.validate(VALID_VPAY2));
    }

    @Test
    public void testVPayOption_test3_decomposed()  {
        CreditCardValidator validator =
                new CreditCardValidator(0, CreditCardValidator.VPAY, null, null);
        assertTrue("Valid", validator.isValid(VALID_VPAY));
        assertTrue("Valid", validator.isValid(VALID_VPAY2));
        assertFalse("Invalid", validator.isValid(ERROR_VPAY));
        assertEquals(VALID_VPAY, validator.validate(VALID_VPAY));
        assertEquals(VALID_VPAY2, validator.validate(VALID_VPAY2));
        assertFalse("Amex", validator.isValid(VALID_AMEX));
        assertFalse("Diners", validator.isValid(VALID_DINERS));
        assertFalse("Discover", validator.isValid(VALID_DISCOVER));
        assertFalse("Mastercard", validator.isValid(VALID_MASTERCARD));
        assertTrue("Visa", validator.isValid(VALID_VISA));
        assertTrue("Visa Short", validator.isValid(VALID_SHORT_VISA));
    }

    @Test
    public void testMastercardUsingSeparators_test0_decomposed()  {
        String MASTERCARD_REGEX_SEP =
                "^(5[1-5]\\d{2})(?:[- ])?(\\d{4})(?:[- ])?(\\d{4})(?:[- ])?(\\d{4})$";
        CodeValidator validator =
                CodeValidator.CodeValidator5(MASTERCARD_REGEX_SEP, LuhnCheckDigit.LUHN_CHECK_DIGIT);
    }

    @Test
    public void testMastercardUsingSeparators_test1_decomposed()  {
        String MASTERCARD_REGEX_SEP =
                "^(5[1-5]\\d{2})(?:[- ])?(\\d{4})(?:[- ])?(\\d{4})(?:[- ])?(\\d{4})$";
        CodeValidator validator =
                CodeValidator.CodeValidator5(MASTERCARD_REGEX_SEP, LuhnCheckDigit.LUHN_CHECK_DIGIT);
        RegexValidator regex = validator.getRegexValidator();
    }

    @Test
    public void testMastercardUsingSeparators_test2_decomposed()  {
        String MASTERCARD_REGEX_SEP =
                "^(5[1-5]\\d{2})(?:[- ])?(\\d{4})(?:[- ])?(\\d{4})(?:[- ])?(\\d{4})$";
        CodeValidator validator =
                CodeValidator.CodeValidator5(MASTERCARD_REGEX_SEP, LuhnCheckDigit.LUHN_CHECK_DIGIT);
        RegexValidator regex = validator.getRegexValidator();
        assertEquals("Number", "5134567890123456", regex.validate("5134567890123456"));
        assertEquals("Hyphen", "5134567890123456", regex.validate("5134-5678-9012-3456"));
        assertEquals("Space", "5134567890123456", regex.validate("5134 5678 9012 3456"));
        assertEquals("MixedA", "5134567890123456", regex.validate("5134-5678 9012-3456"));
        assertEquals("MixedB", "5134567890123456", regex.validate("5134 5678-9012 3456"));
    }

    @Test
    public void testMastercardUsingSeparators_test3_decomposed()  {
        String MASTERCARD_REGEX_SEP =
                "^(5[1-5]\\d{2})(?:[- ])?(\\d{4})(?:[- ])?(\\d{4})(?:[- ])?(\\d{4})$";
        CodeValidator validator =
                CodeValidator.CodeValidator5(MASTERCARD_REGEX_SEP, LuhnCheckDigit.LUHN_CHECK_DIGIT);
        RegexValidator regex = validator.getRegexValidator();
        assertEquals("Number", "5134567890123456", regex.validate("5134567890123456"));
        assertEquals("Hyphen", "5134567890123456", regex.validate("5134-5678-9012-3456"));
        assertEquals("Space", "5134567890123456", regex.validate("5134 5678 9012 3456"));
        assertEquals("MixedA", "5134567890123456", regex.validate("5134-5678 9012-3456"));
        assertEquals("MixedB", "5134567890123456", regex.validate("5134 5678-9012 3456"));
        assertFalse("Invalid Separator A", regex.isValid("5134.5678.9012.3456"));
        assertFalse("Invalid Separator B", regex.isValid("5134_5678_9012_3456"));
        assertFalse("Invalid Grouping A", regex.isValid("513-45678-9012-3456"));
        assertFalse("Invalid Grouping B", regex.isValid("5134-567-89012-3456"));
        assertFalse("Invalid Grouping C", regex.isValid("5134-5678-901-23456"));
    }

    @Test
    public void testMastercardUsingSeparators_test4_decomposed()  {
        String MASTERCARD_REGEX_SEP =
                "^(5[1-5]\\d{2})(?:[- ])?(\\d{4})(?:[- ])?(\\d{4})(?:[- ])?(\\d{4})$";
        CodeValidator validator =
                CodeValidator.CodeValidator5(MASTERCARD_REGEX_SEP, LuhnCheckDigit.LUHN_CHECK_DIGIT);
        RegexValidator regex = validator.getRegexValidator();
        assertEquals("Number", "5134567890123456", regex.validate("5134567890123456"));
        assertEquals("Hyphen", "5134567890123456", regex.validate("5134-5678-9012-3456"));
        assertEquals("Space", "5134567890123456", regex.validate("5134 5678 9012 3456"));
        assertEquals("MixedA", "5134567890123456", regex.validate("5134-5678 9012-3456"));
        assertEquals("MixedB", "5134567890123456", regex.validate("5134 5678-9012 3456"));
        assertFalse("Invalid Separator A", regex.isValid("5134.5678.9012.3456"));
        assertFalse("Invalid Separator B", regex.isValid("5134_5678_9012_3456"));
        assertFalse("Invalid Grouping A", regex.isValid("513-45678-9012-3456"));
        assertFalse("Invalid Grouping B", regex.isValid("5134-567-89012-3456"));
        assertFalse("Invalid Grouping C", regex.isValid("5134-5678-901-23456"));
        assertEquals("Valid-A", "5500000000000004", validator.validate("5500-0000-0000-0004"));
        assertEquals("Valid-B", "5424000000000015", validator.validate("5424 0000 0000 0015"));
        assertEquals("Valid-C", "5301250070000191", validator.validate("5301-250070000191"));
        assertEquals("Valid-D", "5123456789012346", validator.validate("5123456789012346"));
    }

    @Test
    public void testGeneric_test0_decomposed()  {
        CreditCardValidator ccv = CreditCardValidator.genericCreditCardValidator2();
    }

    @Test
    public void testGeneric_test1_decomposed()  {
        CreditCardValidator ccv = CreditCardValidator.genericCreditCardValidator2();
        for (String s : VALID_CARDS) {
            assertTrue(s, ccv.isValid(s));
        }
        for (String s : ERROR_CARDS) {
            assertFalse(s, ccv.isValid(s));
        }
    }

    @Test
    public void testRangeGeneratorNoLuhn_test0_decomposed()  {
        CodeValidator cv =
                CreditCardValidator.createRangeValidator(
                        new CreditCardRange[] {
                            new CreditCardRange(0, "1", null, 6, 7, null),
                            new CreditCardRange(0, "644", "65", 8, 8, null)
                        },
                        null);
    }

    @Test
    public void testRangeGeneratorNoLuhn_test1_decomposed()  {
        CodeValidator cv =
                CreditCardValidator.createRangeValidator(
                        new CreditCardRange[] {
                            new CreditCardRange(0, "1", null, 6, 7, null),
                            new CreditCardRange(0, "644", "65", 8, 8, null)
                        },
                        null);
        assertTrue(cv.isValid("1990000"));
        assertTrue(cv.isValid("199000"));
        assertFalse(cv.isValid("000000"));
        assertFalse(cv.isValid("099999"));
        assertFalse(cv.isValid("200000"));
        assertFalse(cv.isValid("64399999"));
        assertTrue(cv.isValid("64400000"));
        assertTrue(cv.isValid("64900000"));
        assertTrue(cv.isValid("65000000"));
        assertTrue(cv.isValid("65999999"));
        assertFalse(cv.isValid("66000000"));
    }

    @Test
    public void testRangeGenerator_test0_decomposed()  {
        CreditCardValidator ccv =
                new CreditCardValidator(
                        3,
                        0,
                        new CreditCardRange[] {
                            new CreditCardRange(0, "300", "305", 14, 14, null), // Diners
                            new CreditCardRange(0, "3095", null, 14, 14, null), // Diners
                            new CreditCardRange(0, "36", null, 14, 14, null), // Diners
                            new CreditCardRange(0, "38", "39", 14, 14, null), // Diners
                        },
                        new CodeValidator[] {
                            CreditCardValidator.AMEX_VALIDATOR,
                            CreditCardValidator.VISA_VALIDATOR,
                            CreditCardValidator.MASTERCARD_VALIDATOR,
                            CreditCardValidator.DISCOVER_VALIDATOR,
                        });
    }

    @Test
    public void testRangeGenerator_test1_decomposed()  {
        CreditCardValidator ccv =
                new CreditCardValidator(
                        3,
                        0,
                        new CreditCardRange[] {
                            new CreditCardRange(0, "300", "305", 14, 14, null), // Diners
                            new CreditCardRange(0, "3095", null, 14, 14, null), // Diners
                            new CreditCardRange(0, "36", null, 14, 14, null), // Diners
                            new CreditCardRange(0, "38", "39", 14, 14, null), // Diners
                        },
                        new CodeValidator[] {
                            CreditCardValidator.AMEX_VALIDATOR,
                            CreditCardValidator.VISA_VALIDATOR,
                            CreditCardValidator.MASTERCARD_VALIDATOR,
                            CreditCardValidator.DISCOVER_VALIDATOR,
                        });
        for (String s : VALID_CARDS) {
            assertTrue(s, ccv.isValid(s));
        }
        for (String s : ERROR_CARDS) {
            assertFalse(s, ccv.isValid(s));
        }
    }

    @Test
    public void testValidLength_test0_decomposed()  {
        assertTrue(
                CreditCardValidator.validLength(14, new CreditCardRange(0, "", "", 14, 14, null)));
    }

    @Test
    public void testValidLength_test1_decomposed()  {
        assertTrue(
                CreditCardValidator.validLength(14, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(15, new CreditCardRange(0, "", "", 14, 14, null)));
    }

    @Test
    public void testValidLength_test2_decomposed()  {
        assertTrue(
                CreditCardValidator.validLength(14, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(15, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(13, new CreditCardRange(0, "", "", 14, 14, null)));
    }

    @Test
    public void testValidLength_test3_decomposed()  {
        assertTrue(
                CreditCardValidator.validLength(14, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(15, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(13, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(14, new CreditCardRange(0, "", "", 15, 17, null)));
    }

    @Test
    public void testValidLength_test4_decomposed()  {
        assertTrue(
                CreditCardValidator.validLength(14, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(15, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(13, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(14, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(15, new CreditCardRange(0, "", "", 15, 17, null)));
    }

    @Test
    public void testValidLength_test5_decomposed()  {
        assertTrue(
                CreditCardValidator.validLength(14, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(15, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(13, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(14, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(15, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(16, new CreditCardRange(0, "", "", 15, 17, null)));
    }

    @Test
    public void testValidLength_test6_decomposed()  {
        assertTrue(
                CreditCardValidator.validLength(14, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(15, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(13, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(14, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(15, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(16, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(17, new CreditCardRange(0, "", "", 15, 17, null)));
    }

    @Test
    public void testValidLength_test7_decomposed()  {
        assertTrue(
                CreditCardValidator.validLength(14, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(15, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(13, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(14, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(15, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(16, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(17, new CreditCardRange(0, "", "", 15, 17, null)));
        assertFalse(
                CreditCardValidator.validLength(18, new CreditCardRange(0, "", "", 15, 17, null)));
    }

    @Test
    public void testValidLength_test8_decomposed()  {
        assertTrue(
                CreditCardValidator.validLength(14, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(15, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(13, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(14, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(15, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(16, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(17, new CreditCardRange(0, "", "", 15, 17, null)));
        assertFalse(
                CreditCardValidator.validLength(18, new CreditCardRange(0, "", "", 15, 17, null)));
        assertFalse(
                CreditCardValidator.validLength(
                        14, new CreditCardRange(1, "", "", 0, 0, new int[] {15, 17})));
    }

    @Test
    public void testValidLength_test9_decomposed()  {
        assertTrue(
                CreditCardValidator.validLength(14, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(15, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(13, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(14, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(15, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(16, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(17, new CreditCardRange(0, "", "", 15, 17, null)));
        assertFalse(
                CreditCardValidator.validLength(18, new CreditCardRange(0, "", "", 15, 17, null)));
        assertFalse(
                CreditCardValidator.validLength(
                        14, new CreditCardRange(1, "", "", 0, 0, new int[] {15, 17})));
        assertTrue(
                CreditCardValidator.validLength(
                        15, new CreditCardRange(1, "", "", 0, 0, new int[] {15, 17})));
    }

    @Test
    public void testValidLength_test10_decomposed()  {
        assertTrue(
                CreditCardValidator.validLength(14, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(15, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(13, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(14, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(15, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(16, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(17, new CreditCardRange(0, "", "", 15, 17, null)));
        assertFalse(
                CreditCardValidator.validLength(18, new CreditCardRange(0, "", "", 15, 17, null)));
        assertFalse(
                CreditCardValidator.validLength(
                        14, new CreditCardRange(1, "", "", 0, 0, new int[] {15, 17})));
        assertTrue(
                CreditCardValidator.validLength(
                        15, new CreditCardRange(1, "", "", 0, 0, new int[] {15, 17})));
        assertFalse(
                CreditCardValidator.validLength(
                        16, new CreditCardRange(1, "", "", 0, 0, new int[] {15, 17})));
    }

    @Test
    public void testValidLength_test11_decomposed()  {
        assertTrue(
                CreditCardValidator.validLength(14, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(15, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(13, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(14, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(15, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(16, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(17, new CreditCardRange(0, "", "", 15, 17, null)));
        assertFalse(
                CreditCardValidator.validLength(18, new CreditCardRange(0, "", "", 15, 17, null)));
        assertFalse(
                CreditCardValidator.validLength(
                        14, new CreditCardRange(1, "", "", 0, 0, new int[] {15, 17})));
        assertTrue(
                CreditCardValidator.validLength(
                        15, new CreditCardRange(1, "", "", 0, 0, new int[] {15, 17})));
        assertFalse(
                CreditCardValidator.validLength(
                        16, new CreditCardRange(1, "", "", 0, 0, new int[] {15, 17})));
        assertTrue(
                CreditCardValidator.validLength(
                        17, new CreditCardRange(1, "", "", 0, 0, new int[] {15, 17})));
    }

    @Test
    public void testValidLength_test12_decomposed()  {
        assertTrue(
                CreditCardValidator.validLength(14, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(15, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(13, new CreditCardRange(0, "", "", 14, 14, null)));
        assertFalse(
                CreditCardValidator.validLength(14, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(15, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(16, new CreditCardRange(0, "", "", 15, 17, null)));
        assertTrue(
                CreditCardValidator.validLength(17, new CreditCardRange(0, "", "", 15, 17, null)));
        assertFalse(
                CreditCardValidator.validLength(18, new CreditCardRange(0, "", "", 15, 17, null)));
        assertFalse(
                CreditCardValidator.validLength(
                        14, new CreditCardRange(1, "", "", 0, 0, new int[] {15, 17})));
        assertTrue(
                CreditCardValidator.validLength(
                        15, new CreditCardRange(1, "", "", 0, 0, new int[] {15, 17})));
        assertFalse(
                CreditCardValidator.validLength(
                        16, new CreditCardRange(1, "", "", 0, 0, new int[] {15, 17})));
        assertTrue(
                CreditCardValidator.validLength(
                        17, new CreditCardRange(1, "", "", 0, 0, new int[] {15, 17})));
        assertFalse(
                CreditCardValidator.validLength(
                        18, new CreditCardRange(1, "", "", 0, 0, new int[] {15, 17})));
    }

    @Test
    public void testDisjointRange_test0_decomposed()  {
        CreditCardValidator ccv =
                new CreditCardValidator(
                        2,
                        0,
                        new CreditCardRange[] {
                            new CreditCardRange(1, "305", "4", 0, 0, new int[] {13, 16}),
                        },
                        null);
    }

    @Test
    public void testDisjointRange_test1_decomposed()  {
        CreditCardValidator ccv =
                new CreditCardValidator(
                        2,
                        0,
                        new CreditCardRange[] {
                            new CreditCardRange(1, "305", "4", 0, 0, new int[] {13, 16}),
                        },
                        null);
        assertEquals(13, VALID_SHORT_VISA.length());
        assertEquals(16, VALID_VISA.length());
    }

    @Test
    public void testDisjointRange_test2_decomposed()  {
        CreditCardValidator ccv =
                new CreditCardValidator(
                        2,
                        0,
                        new CreditCardRange[] {
                            new CreditCardRange(1, "305", "4", 0, 0, new int[] {13, 16}),
                        },
                        null);
        assertEquals(13, VALID_SHORT_VISA.length());
        assertEquals(16, VALID_VISA.length());
        assertEquals(14, VALID_DINERS.length());
        assertTrue(ccv.isValid(VALID_SHORT_VISA));
    }

    @Test
    public void testDisjointRange_test3_decomposed()  {
        CreditCardValidator ccv =
                new CreditCardValidator(
                        2,
                        0,
                        new CreditCardRange[] {
                            new CreditCardRange(1, "305", "4", 0, 0, new int[] {13, 16}),
                        },
                        null);
        assertEquals(13, VALID_SHORT_VISA.length());
        assertEquals(16, VALID_VISA.length());
        assertEquals(14, VALID_DINERS.length());
        assertTrue(ccv.isValid(VALID_SHORT_VISA));
        assertTrue(ccv.isValid(VALID_VISA));
        assertFalse(ccv.isValid(ERROR_SHORT_VISA));
        assertFalse(ccv.isValid(ERROR_VISA));
        assertFalse(ccv.isValid(VALID_DINERS));
    }

    @Test
    public void testDisjointRange_test4_decomposed()  {
        CreditCardValidator ccv =
                new CreditCardValidator(
                        2,
                        0,
                        new CreditCardRange[] {
                            new CreditCardRange(1, "305", "4", 0, 0, new int[] {13, 16}),
                        },
                        null);
        assertEquals(13, VALID_SHORT_VISA.length());
        assertEquals(16, VALID_VISA.length());
        assertEquals(14, VALID_DINERS.length());
        assertTrue(ccv.isValid(VALID_SHORT_VISA));
        assertTrue(ccv.isValid(VALID_VISA));
        assertFalse(ccv.isValid(ERROR_SHORT_VISA));
        assertFalse(ccv.isValid(ERROR_VISA));
        assertFalse(ccv.isValid(VALID_DINERS));
        ccv =
                new CreditCardValidator(
                        2,
                        0,
                        new CreditCardRange[] {
                            new CreditCardRange(1, "305", "4", 0, 0, new int[] {13, 14, 16}),
                        },
                        null);
    }

    @Test
    public void testDisjointRange_test5_decomposed()  {
        CreditCardValidator ccv =
                new CreditCardValidator(
                        2,
                        0,
                        new CreditCardRange[] {
                            new CreditCardRange(1, "305", "4", 0, 0, new int[] {13, 16}),
                        },
                        null);
        assertEquals(13, VALID_SHORT_VISA.length());
        assertEquals(16, VALID_VISA.length());
        assertEquals(14, VALID_DINERS.length());
        assertTrue(ccv.isValid(VALID_SHORT_VISA));
        assertTrue(ccv.isValid(VALID_VISA));
        assertFalse(ccv.isValid(ERROR_SHORT_VISA));
        assertFalse(ccv.isValid(ERROR_VISA));
        assertFalse(ccv.isValid(VALID_DINERS));
        ccv =
                new CreditCardValidator(
                        2,
                        0,
                        new CreditCardRange[] {
                            new CreditCardRange(1, "305", "4", 0, 0, new int[] {13, 14, 16}),
                        },
                        null);
        assertTrue(ccv.isValid(VALID_DINERS));
    }
}