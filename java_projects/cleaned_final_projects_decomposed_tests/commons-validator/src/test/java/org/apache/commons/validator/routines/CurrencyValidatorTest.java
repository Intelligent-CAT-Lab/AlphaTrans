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

import java.math.BigDecimal;
import java.text.DecimalFormatSymbols;
import java.util.Locale;

/**
 * Test Case for CurrencyValidator.
 *
 * @version $Revision$
 */
public class CurrencyValidatorTest extends TestCase {

    private static final char CURRENCY_SYMBOL = '\u00A4';

    private String US_DOLLAR;
    private String UK_POUND;

    /**
     * Constructor
     *
     * @param name test name
     */
    public CurrencyValidatorTest(String name) {
        super(name);
    }

    @Override
    protected void setUp() throws Exception {
        super.setUp();
        US_DOLLAR = (new DecimalFormatSymbols(Locale.US)).getCurrencySymbol();
        UK_POUND = (new DecimalFormatSymbols(Locale.UK)).getCurrencySymbol();
    }

    /**
     * Tear down
     *
     * @throws Exception
     */
    @Override
    protected void tearDown() throws Exception {
        super.tearDown();
    }

    /** Test Format Type */
    

    /** Test Valid currency values */
    

    /** Test Invalid currency values */
    

    /** Test Valid integer (non-decimal) currency values */
    

    /** Test Invalid integer (non decimal) currency values */
    

    /** Test currency values with a pattern */

    @Test
    public void testFormatType_test0_decomposed()  {
        CurrencyValidator.getInstance();
    }

    @Test
    public void testFormatType_test1_decomposed()  {
        CurrencyValidator.getInstance();
        assertEquals("Format Type A", 1, CurrencyValidator.getInstance().getFormatType());
    }

    @Test
    public void testFormatType_test2_decomposed()  {
        CurrencyValidator.getInstance();
        assertEquals("Format Type A", 1, CurrencyValidator.getInstance().getFormatType());
        CurrencyValidator.getInstance();
    }

    @Test
    public void testFormatType_test3_decomposed()  {
        CurrencyValidator.getInstance();
        assertEquals("Format Type A", 1, CurrencyValidator.getInstance().getFormatType());
        CurrencyValidator.getInstance();
        assertEquals(
                "Format Type B",
                AbstractNumberValidator.CURRENCY_FORMAT,
                CurrencyValidator.getInstance().getFormatType());
    }

    @Test
    public void testValid_test0_decomposed()  {
        Locale origDefault = Locale.getDefault();
        Locale.setDefault(Locale.UK);
        BigDecimalValidator validator = CurrencyValidator.getInstance();
    }

    @Test
    public void testValid_test1_decomposed()  {
        Locale origDefault = Locale.getDefault();
        Locale.setDefault(Locale.UK);
        BigDecimalValidator validator = CurrencyValidator.getInstance();
        BigDecimal expected = new BigDecimal("1234.56");
        BigDecimal negative = new BigDecimal("-1234.56");
        BigDecimal noDecimal = new BigDecimal("1234.00");
        BigDecimal oneDecimal = new BigDecimal("1234.50");
        assertEquals("Default locale", expected, validator.validate0(UK_POUND + "1,234.56"));
    }

    @Test
    public void testValid_test2_decomposed()  {
        Locale origDefault = Locale.getDefault();
        Locale.setDefault(Locale.UK);
        BigDecimalValidator validator = CurrencyValidator.getInstance();
        BigDecimal expected = new BigDecimal("1234.56");
        BigDecimal negative = new BigDecimal("-1234.56");
        BigDecimal noDecimal = new BigDecimal("1234.00");
        BigDecimal oneDecimal = new BigDecimal("1234.50");
        assertEquals("Default locale", expected, validator.validate0(UK_POUND + "1,234.56"));
        assertEquals("UK locale", expected, validator.validate2(UK_POUND + "1,234.56", Locale.UK));
        assertEquals(
                "UK negative",
                negative,
                validator.validate2("-" + UK_POUND + "1,234.56", Locale.UK));
        assertEquals(
                "UK no decimal", noDecimal, validator.validate2(UK_POUND + "1,234", Locale.UK));
        assertEquals(
                "UK 1 decimal", oneDecimal, validator.validate2(UK_POUND + "1,234.5", Locale.UK));
        assertEquals(
                "UK 3 decimal", expected, validator.validate2(UK_POUND + "1,234.567", Locale.UK));
        assertEquals("UK no symbol", expected, validator.validate2("1,234.56", Locale.UK));
        assertEquals("US locale", expected, validator.validate2(US_DOLLAR + "1,234.56", Locale.US));
        assertEquals(
                "US negative",
                negative,
                validator.validate2("(" + US_DOLLAR + "1,234.56)", Locale.US));
        assertEquals(
                "US no decimal", noDecimal, validator.validate2(US_DOLLAR + "1,234", Locale.US));
        assertEquals(
                "US 1 decimal", oneDecimal, validator.validate2(US_DOLLAR + "1,234.5", Locale.US));
        assertEquals(
                "US 3 decimal", expected, validator.validate2(US_DOLLAR + "1,234.567", Locale.US));
        assertEquals("US no symbol", expected, validator.validate2("1,234.56", Locale.US));
    }

    @Test
    public void testValid_test3_decomposed()  {
        Locale origDefault = Locale.getDefault();
        Locale.setDefault(Locale.UK);
        BigDecimalValidator validator = CurrencyValidator.getInstance();
        BigDecimal expected = new BigDecimal("1234.56");
        BigDecimal negative = new BigDecimal("-1234.56");
        BigDecimal noDecimal = new BigDecimal("1234.00");
        BigDecimal oneDecimal = new BigDecimal("1234.50");
        assertEquals("Default locale", expected, validator.validate0(UK_POUND + "1,234.56"));
        assertEquals("UK locale", expected, validator.validate2(UK_POUND + "1,234.56", Locale.UK));
        assertEquals(
                "UK negative",
                negative,
                validator.validate2("-" + UK_POUND + "1,234.56", Locale.UK));
        assertEquals(
                "UK no decimal", noDecimal, validator.validate2(UK_POUND + "1,234", Locale.UK));
        assertEquals(
                "UK 1 decimal", oneDecimal, validator.validate2(UK_POUND + "1,234.5", Locale.UK));
        assertEquals(
                "UK 3 decimal", expected, validator.validate2(UK_POUND + "1,234.567", Locale.UK));
        assertEquals("UK no symbol", expected, validator.validate2("1,234.56", Locale.UK));
        assertEquals("US locale", expected, validator.validate2(US_DOLLAR + "1,234.56", Locale.US));
        assertEquals(
                "US negative",
                negative,
                validator.validate2("(" + US_DOLLAR + "1,234.56)", Locale.US));
        assertEquals(
                "US no decimal", noDecimal, validator.validate2(US_DOLLAR + "1,234", Locale.US));
        assertEquals(
                "US 1 decimal", oneDecimal, validator.validate2(US_DOLLAR + "1,234.5", Locale.US));
        assertEquals(
                "US 3 decimal", expected, validator.validate2(US_DOLLAR + "1,234.567", Locale.US));
        assertEquals("US no symbol", expected, validator.validate2("1,234.56", Locale.US));
        Locale.setDefault(origDefault);
    }

    @Test
    public void testInvalid_test0_decomposed()  {
        BigDecimalValidator validator = CurrencyValidator.getInstance();
    }

    @Test
    public void testInvalid_test1_decomposed()  {
        BigDecimalValidator validator = CurrencyValidator.getInstance();
        assertFalse("isValid() Null Value", validator.isValid0(null));
        assertFalse("isValid() Empty Value", validator.isValid0(""));
    }

    @Test
    public void testInvalid_test2_decomposed()  {
        BigDecimalValidator validator = CurrencyValidator.getInstance();
        assertFalse("isValid() Null Value", validator.isValid0(null));
        assertFalse("isValid() Empty Value", validator.isValid0(""));
        assertNull("validate() Null Value", validator.validate0(null));
        assertNull("validate() Empty Value", validator.validate0(""));
    }

    @Test
    public void testInvalid_test3_decomposed()  {
        BigDecimalValidator validator = CurrencyValidator.getInstance();
        assertFalse("isValid() Null Value", validator.isValid0(null));
        assertFalse("isValid() Empty Value", validator.isValid0(""));
        assertNull("validate() Null Value", validator.validate0(null));
        assertNull("validate() Empty Value", validator.validate0(""));
        assertFalse("UK wrong symbol", validator.isValid2(US_DOLLAR + "1,234.56", Locale.UK));
        assertFalse(
                "UK wrong negative", validator.isValid2("(" + UK_POUND + "1,234.56)", Locale.UK));
        assertFalse("US wrong symbol", validator.isValid2(UK_POUND + "1,234.56", Locale.US));
        assertFalse(
                "US wrong negative", validator.isValid2("-" + US_DOLLAR + "1,234.56", Locale.US));
    }

    @Test
    public void testIntegerValid_test0_decomposed()  {
        Locale origDefault = Locale.getDefault();
        Locale.setDefault(Locale.UK);
        CurrencyValidator validator = CurrencyValidator.CurrencyValidator1();
    }

    @Test
    public void testIntegerValid_test1_decomposed()  {
        Locale origDefault = Locale.getDefault();
        Locale.setDefault(Locale.UK);
        CurrencyValidator validator = CurrencyValidator.CurrencyValidator1();
        BigDecimal expected = new BigDecimal("1234.00");
        BigDecimal negative = new BigDecimal("-1234.00");
        assertEquals("Default locale", expected, validator.validate0(UK_POUND + "1,234"));
    }

    @Test
    public void testIntegerValid_test2_decomposed()  {
        Locale origDefault = Locale.getDefault();
        Locale.setDefault(Locale.UK);
        CurrencyValidator validator = CurrencyValidator.CurrencyValidator1();
        BigDecimal expected = new BigDecimal("1234.00");
        BigDecimal negative = new BigDecimal("-1234.00");
        assertEquals("Default locale", expected, validator.validate0(UK_POUND + "1,234"));
        assertEquals("UK locale", expected, validator.validate2(UK_POUND + "1,234", Locale.UK));
        assertEquals(
                "UK negative", negative, validator.validate2("-" + UK_POUND + "1,234", Locale.UK));
        assertEquals("US locale", expected, validator.validate2(US_DOLLAR + "1,234", Locale.US));
        assertEquals(
                "US negative",
                negative,
                validator.validate2("(" + US_DOLLAR + "1,234)", Locale.US));
    }

    @Test
    public void testIntegerValid_test3_decomposed()  {
        Locale origDefault = Locale.getDefault();
        Locale.setDefault(Locale.UK);
        CurrencyValidator validator = CurrencyValidator.CurrencyValidator1();
        BigDecimal expected = new BigDecimal("1234.00");
        BigDecimal negative = new BigDecimal("-1234.00");
        assertEquals("Default locale", expected, validator.validate0(UK_POUND + "1,234"));
        assertEquals("UK locale", expected, validator.validate2(UK_POUND + "1,234", Locale.UK));
        assertEquals(
                "UK negative", negative, validator.validate2("-" + UK_POUND + "1,234", Locale.UK));
        assertEquals("US locale", expected, validator.validate2(US_DOLLAR + "1,234", Locale.US));
        assertEquals(
                "US negative",
                negative,
                validator.validate2("(" + US_DOLLAR + "1,234)", Locale.US));
        Locale.setDefault(origDefault);
    }

    @Test
    public void testIntegerInvalid_test0_decomposed()  {
        CurrencyValidator validator = new CurrencyValidator(true, false);
    }

    @Test
    public void testIntegerInvalid_test1_decomposed()  {
        CurrencyValidator validator = new CurrencyValidator(true, false);
        assertFalse("UK positive", validator.isValid2(UK_POUND + "1,234.56", Locale.UK));
        assertFalse("UK negative", validator.isValid2("-" + UK_POUND + "1,234.56", Locale.UK));
        assertFalse("US positive", validator.isValid2(US_DOLLAR + "1,234.56", Locale.US));
        assertFalse("US negative", validator.isValid2("(" + US_DOLLAR + "1,234.56)", Locale.US));
    }

    @Test
    public void testPattern_test0_decomposed()  {
        Locale origDefault = Locale.getDefault();
        Locale.setDefault(Locale.UK);
        BigDecimalValidator validator = CurrencyValidator.getInstance();
    }

    @Test
    public void testPattern_test1_decomposed()  {
        Locale origDefault = Locale.getDefault();
        Locale.setDefault(Locale.UK);
        BigDecimalValidator validator = CurrencyValidator.getInstance();
        String basicPattern = CURRENCY_SYMBOL + "#,##0.000";
        String pattern = basicPattern + ";[" + basicPattern + "]";
        BigDecimal expected = new BigDecimal("1234.567");
        BigDecimal negative = new BigDecimal("-1234.567");
        assertEquals("default", expected, validator.validate1(UK_POUND + "1,234.567", pattern));
    }

    @Test
    public void testPattern_test2_decomposed()  {
        Locale origDefault = Locale.getDefault();
        Locale.setDefault(Locale.UK);
        BigDecimalValidator validator = CurrencyValidator.getInstance();
        String basicPattern = CURRENCY_SYMBOL + "#,##0.000";
        String pattern = basicPattern + ";[" + basicPattern + "]";
        BigDecimal expected = new BigDecimal("1234.567");
        BigDecimal negative = new BigDecimal("-1234.567");
        assertEquals("default", expected, validator.validate1(UK_POUND + "1,234.567", pattern));
        assertEquals(
                "negative", negative, validator.validate1("[" + UK_POUND + "1,234.567]", pattern));
        assertEquals("no symbol +ve", expected, validator.validate1("1,234.567", pattern));
        assertEquals("no symbol -ve", negative, validator.validate1("[1,234.567]", pattern));
    }

    @Test
    public void testPattern_test3_decomposed()  {
        Locale origDefault = Locale.getDefault();
        Locale.setDefault(Locale.UK);
        BigDecimalValidator validator = CurrencyValidator.getInstance();
        String basicPattern = CURRENCY_SYMBOL + "#,##0.000";
        String pattern = basicPattern + ";[" + basicPattern + "]";
        BigDecimal expected = new BigDecimal("1234.567");
        BigDecimal negative = new BigDecimal("-1234.567");
        assertEquals("default", expected, validator.validate1(UK_POUND + "1,234.567", pattern));
        assertEquals(
                "negative", negative, validator.validate1("[" + UK_POUND + "1,234.567]", pattern));
        assertEquals("no symbol +ve", expected, validator.validate1("1,234.567", pattern));
        assertEquals("no symbol -ve", negative, validator.validate1("[1,234.567]", pattern));
        assertEquals(
                "default",
                expected,
                validator.validate3(US_DOLLAR + "1,234.567", pattern, Locale.US));
        assertEquals(
                "negative",
                negative,
                validator.validate3("[" + US_DOLLAR + "1,234.567]", pattern, Locale.US));
        assertEquals(
                "no symbol +ve", expected, validator.validate3("1,234.567", pattern, Locale.US));
        assertEquals(
                "no symbol -ve", negative, validator.validate3("[1,234.567]", pattern, Locale.US));
    }

    @Test
    public void testPattern_test4_decomposed()  {
        Locale origDefault = Locale.getDefault();
        Locale.setDefault(Locale.UK);
        BigDecimalValidator validator = CurrencyValidator.getInstance();
        String basicPattern = CURRENCY_SYMBOL + "#,##0.000";
        String pattern = basicPattern + ";[" + basicPattern + "]";
        BigDecimal expected = new BigDecimal("1234.567");
        BigDecimal negative = new BigDecimal("-1234.567");
        assertEquals("default", expected, validator.validate1(UK_POUND + "1,234.567", pattern));
        assertEquals(
                "negative", negative, validator.validate1("[" + UK_POUND + "1,234.567]", pattern));
        assertEquals("no symbol +ve", expected, validator.validate1("1,234.567", pattern));
        assertEquals("no symbol -ve", negative, validator.validate1("[1,234.567]", pattern));
        assertEquals(
                "default",
                expected,
                validator.validate3(US_DOLLAR + "1,234.567", pattern, Locale.US));
        assertEquals(
                "negative",
                negative,
                validator.validate3("[" + US_DOLLAR + "1,234.567]", pattern, Locale.US));
        assertEquals(
                "no symbol +ve", expected, validator.validate3("1,234.567", pattern, Locale.US));
        assertEquals(
                "no symbol -ve", negative, validator.validate3("[1,234.567]", pattern, Locale.US));
        assertFalse("invalid symbol", validator.isValid1(US_DOLLAR + "1,234.567", pattern));
    }

    @Test
    public void testPattern_test5_decomposed()  {
        Locale origDefault = Locale.getDefault();
        Locale.setDefault(Locale.UK);
        BigDecimalValidator validator = CurrencyValidator.getInstance();
        String basicPattern = CURRENCY_SYMBOL + "#,##0.000";
        String pattern = basicPattern + ";[" + basicPattern + "]";
        BigDecimal expected = new BigDecimal("1234.567");
        BigDecimal negative = new BigDecimal("-1234.567");
        assertEquals("default", expected, validator.validate1(UK_POUND + "1,234.567", pattern));
        assertEquals(
                "negative", negative, validator.validate1("[" + UK_POUND + "1,234.567]", pattern));
        assertEquals("no symbol +ve", expected, validator.validate1("1,234.567", pattern));
        assertEquals("no symbol -ve", negative, validator.validate1("[1,234.567]", pattern));
        assertEquals(
                "default",
                expected,
                validator.validate3(US_DOLLAR + "1,234.567", pattern, Locale.US));
        assertEquals(
                "negative",
                negative,
                validator.validate3("[" + US_DOLLAR + "1,234.567]", pattern, Locale.US));
        assertEquals(
                "no symbol +ve", expected, validator.validate3("1,234.567", pattern, Locale.US));
        assertEquals(
                "no symbol -ve", negative, validator.validate3("[1,234.567]", pattern, Locale.US));
        assertFalse("invalid symbol", validator.isValid1(US_DOLLAR + "1,234.567", pattern));
        assertFalse(
                "invalid symbol", validator.isValid3(UK_POUND + "1,234.567", pattern, Locale.US));
    }

    @Test
    public void testPattern_test6_decomposed()  {
        Locale origDefault = Locale.getDefault();
        Locale.setDefault(Locale.UK);
        BigDecimalValidator validator = CurrencyValidator.getInstance();
        String basicPattern = CURRENCY_SYMBOL + "#,##0.000";
        String pattern = basicPattern + ";[" + basicPattern + "]";
        BigDecimal expected = new BigDecimal("1234.567");
        BigDecimal negative = new BigDecimal("-1234.567");
        assertEquals("default", expected, validator.validate1(UK_POUND + "1,234.567", pattern));
        assertEquals(
                "negative", negative, validator.validate1("[" + UK_POUND + "1,234.567]", pattern));
        assertEquals("no symbol +ve", expected, validator.validate1("1,234.567", pattern));
        assertEquals("no symbol -ve", negative, validator.validate1("[1,234.567]", pattern));
        assertEquals(
                "default",
                expected,
                validator.validate3(US_DOLLAR + "1,234.567", pattern, Locale.US));
        assertEquals(
                "negative",
                negative,
                validator.validate3("[" + US_DOLLAR + "1,234.567]", pattern, Locale.US));
        assertEquals(
                "no symbol +ve", expected, validator.validate3("1,234.567", pattern, Locale.US));
        assertEquals(
                "no symbol -ve", negative, validator.validate3("[1,234.567]", pattern, Locale.US));
        assertFalse("invalid symbol", validator.isValid1(US_DOLLAR + "1,234.567", pattern));
        assertFalse(
                "invalid symbol", validator.isValid3(UK_POUND + "1,234.567", pattern, Locale.US));
        Locale.setDefault(origDefault);
    }
}