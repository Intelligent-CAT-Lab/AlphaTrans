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
package org.apache.commons.validator;
import org.junit.Test;

import junit.framework.TestCase;

/**
 * Test the CreditCardValidator class.
 *
 * @version $Revision$
 * @deprecated this test can be removed when the deprecated class is removed
 */
@Deprecated
public class CreditCardValidatorTest extends TestCase {

    private static final String VALID_VISA = "4417123456789113";
    private static final String VALID_SHORT_VISA = "4222222222222";
    private static final String VALID_AMEX = "378282246310005";
    private static final String VALID_MASTERCARD = "5105105105105100";
    private static final String VALID_DISCOVER = "6011000990139424";
    private static final String VALID_DINERS = "30569309025904";

    /** Constructor for CreditCardValidatorTest. */
    public CreditCardValidatorTest(String name) {
        super(name);
    }

    

    

    /** Test a custom implementation of CreditCardType. */
    private class DinersClub implements CreditCardValidator.CreditCardType {
        private static final String PREFIX = "300,301,302,303,304,305,";

        @Override
        public boolean matches(String card) {
            String prefix = card.substring(0, 3) + ",";
            return ((PREFIX.contains(prefix)) && (card.length() == 14));
        }
    }

    @Test
    public void testIsValid_test0_decomposed()  {
        CreditCardValidator ccv = CreditCardValidator.CreditCardValidator1();
    }

    @Test
    public void testIsValid_test1_decomposed()  {
        CreditCardValidator ccv = CreditCardValidator.CreditCardValidator1();
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
    }

    @Test
    public void testIsValid_test2_decomposed()  {
        CreditCardValidator ccv = CreditCardValidator.CreditCardValidator1();
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
        ccv = new CreditCardValidator(CreditCardValidator.AMEX);
    }

    @Test
    public void testIsValid_test3_decomposed()  {
        CreditCardValidator ccv = CreditCardValidator.CreditCardValidator1();
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
        ccv = new CreditCardValidator(CreditCardValidator.AMEX);
        assertFalse(ccv.isValid("4417123456789113"));
    }

    @Test
    public void testAddAllowedCardType_test0_decomposed()  {
        CreditCardValidator ccv = new CreditCardValidator(CreditCardValidator.NONE);
    }

    @Test
    public void testAddAllowedCardType_test1_decomposed()  {
        CreditCardValidator ccv = new CreditCardValidator(CreditCardValidator.NONE);
        assertFalse(ccv.isValid(VALID_VISA));
        assertFalse(ccv.isValid(VALID_AMEX));
        assertFalse(ccv.isValid(VALID_MASTERCARD));
        assertFalse(ccv.isValid(VALID_DISCOVER));
    }

    @Test
    public void testAddAllowedCardType_test2_decomposed()  {
        CreditCardValidator ccv = new CreditCardValidator(CreditCardValidator.NONE);
        assertFalse(ccv.isValid(VALID_VISA));
        assertFalse(ccv.isValid(VALID_AMEX));
        assertFalse(ccv.isValid(VALID_MASTERCARD));
        assertFalse(ccv.isValid(VALID_DISCOVER));
        ccv.addAllowedCardType(new DinersClub());
    }

    @Test
    public void testAddAllowedCardType_test3_decomposed()  {
        CreditCardValidator ccv = new CreditCardValidator(CreditCardValidator.NONE);
        assertFalse(ccv.isValid(VALID_VISA));
        assertFalse(ccv.isValid(VALID_AMEX));
        assertFalse(ccv.isValid(VALID_MASTERCARD));
        assertFalse(ccv.isValid(VALID_DISCOVER));
        ccv.addAllowedCardType(new DinersClub());
        assertTrue(ccv.isValid(VALID_DINERS));
    }
}