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
 * Test the GenericValidator class.
 *
 * @version $Revision$
 */
public class GenericValidatorTest extends TestCase {

    /** Constructor for GenericValidatorTest. */
    public GenericValidatorTest(String name) {
        super(name);
    }

    @Test
    public void testMinLength_test0_decomposed()  {
        assertTrue("Min=5 End=0", GenericValidator.minLength1("12345\n\r", 5, 0));
        assertFalse("Min=6 End=0", GenericValidator.minLength1("12345\n\r", 6, 0));
        assertFalse("Min=7 End=0", GenericValidator.minLength1("12345\n\r", 7, 0));
        assertFalse("Min=8 End=0", GenericValidator.minLength1("12345\n\r", 8, 0));
        assertTrue("Min=5 End=1", GenericValidator.minLength1("12345\n\r", 5, 1));
        assertTrue("Min=6 End=1", GenericValidator.minLength1("12345\n\r", 6, 1));
        assertFalse("Min=7 End=1", GenericValidator.minLength1("12345\n\r", 7, 1));
        assertFalse("Min=8 End=1", GenericValidator.minLength1("12345\n\r", 8, 1));
        assertTrue("Min=5 End=2", GenericValidator.minLength1("12345\n\r", 5, 2));
        assertTrue("Min=6 End=2", GenericValidator.minLength1("12345\n\r", 6, 2));
        assertTrue("Min=7 End=2", GenericValidator.minLength1("12345\n\r", 7, 2));
        assertFalse("Min=8 End=2", GenericValidator.minLength1("12345\n\r", 8, 2));
    }

    @Test
    public void testMaxLength_test0_decomposed()  {
        assertFalse("Max=4 End=0", GenericValidator.maxLength1("12345\n\r", 4, 0));
        assertTrue("Max=5 End=0", GenericValidator.maxLength1("12345\n\r", 5, 0));
        assertTrue("Max=6 End=0", GenericValidator.maxLength1("12345\n\r", 6, 0));
        assertTrue("Max=7 End=0", GenericValidator.maxLength1("12345\n\r", 7, 0));
        assertFalse("Max=4 End=1", GenericValidator.maxLength1("12345\n\r", 4, 1));
        assertFalse("Max=5 End=1", GenericValidator.maxLength1("12345\n\r", 5, 1));
        assertTrue("Max=6 End=1", GenericValidator.maxLength1("12345\n\r", 6, 1));
        assertTrue("Max=7 End=1", GenericValidator.maxLength1("12345\n\r", 7, 1));
        assertFalse("Max=4 End=2", GenericValidator.maxLength1("12345\n\r", 4, 2));
        assertFalse("Max=5 End=2", GenericValidator.maxLength1("12345\n\r", 5, 2));
        assertFalse("Max=6 End=2", GenericValidator.maxLength1("12345\n\r", 6, 2));
        assertTrue("Max=7 End=2", GenericValidator.maxLength1("12345\n\r", 7, 2));
    }
}