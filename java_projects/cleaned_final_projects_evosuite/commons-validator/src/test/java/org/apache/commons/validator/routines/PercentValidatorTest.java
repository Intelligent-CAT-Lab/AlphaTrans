
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

package org.apache.commons.validator.routines;

import junit.framework.TestCase;

import java.math.BigDecimal;
import java.util.Locale;

/**
 * Test Case for PercentValidator.
 *
 * @version $Revision$
 */
public class PercentValidatorTest extends TestCase {

    protected PercentValidator validator;

    /**
     * Constructor
     *
     * @param name test name
     */
    public PercentValidatorTest(String name) {
        super(name);
    }

    @Override
    protected void setUp() throws Exception {
        super.setUp();
        validator = PercentValidator.PercentValidator1();
    }

    /**
     * Tear down
     *
     * @throws Exception
     */
    @Override
    protected void tearDown() throws Exception {
        super.tearDown();
        validator = null;
    }

    /** Test Format Type */
    public void testFormatType() {
        assertEquals("Format Type A", 2, PercentValidator.getInstance().getFormatType());
        assertEquals(
                "Format Type B",
                AbstractNumberValidator.PERCENT_FORMAT,
                PercentValidator.getInstance().getFormatType());
    }

    /** Test Valid percentage values */
    public void testValid() {
        Locale origDefault = Locale.getDefault();
        Locale.setDefault(Locale.UK);

        BigDecimalValidator validator = PercentValidator.getInstance();
        BigDecimal expected = new BigDecimal("0.12");
        BigDecimal negative = new BigDecimal("-0.12");
        BigDecimal hundred = new BigDecimal("1.00");

        assertEquals("Default locale", expected, validator.validate0("12%"));
        assertEquals("Default negtve", negative, validator.validate0("-12%"));

        assertEquals("UK locale", expected, validator.validate2("12%", Locale.UK));
        assertEquals("UK negative", negative, validator.validate2("-12%", Locale.UK));
        assertEquals("UK No symbol", expected, validator.validate2("12", Locale.UK));

        assertEquals("US locale", expected, validator.validate2("12%", Locale.US));
        assertEquals("US negative", negative, validator.validate2("-12%", Locale.US));
        assertEquals("US No symbol", expected, validator.validate2("12", Locale.US));

        assertEquals("100%", hundred, validator.validate0("100%"));

        Locale.setDefault(origDefault);
    }

    /** Test Invalid percentage values */
    public void testInvalid() {
        BigDecimalValidator validator = PercentValidator.getInstance();

        assertFalse("isValid() Null Value", validator.isValid0(null));
        assertFalse("isValid() Empty Value", validator.isValid0(""));
        assertNull("validate() Null Value", validator.validate0(null));
        assertNull("validate() Empty Value", validator.validate0(""));

        assertFalse("UK wrong symbol", validator.isValid2("12@", Locale.UK)); // ???
        assertFalse("UK wrong negative", validator.isValid2("(12%)", Locale.UK));

        assertFalse("US wrong symbol", validator.isValid2("12@", Locale.US)); // ???
        assertFalse("US wrong negative", validator.isValid2("(12%)", Locale.US));
    }
}
