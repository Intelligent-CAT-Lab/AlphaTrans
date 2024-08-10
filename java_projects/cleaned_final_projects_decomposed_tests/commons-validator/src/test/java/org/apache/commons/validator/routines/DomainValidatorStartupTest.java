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

import static org.junit.Assert.*;

import org.apache.commons.validator.routines.DomainValidator.ArrayType;
import org.bitstrings.test.junit.runner.ClassLoaderPerTestRunner;
import org.junit.Test;
import org.junit.runner.RunWith;

import java.util.ArrayList;
import java.util.List;

/**
 * Startup Tests for the DomainValidator.
 *
 * @version $Revision$
 */
@RunWith(ClassLoaderPerTestRunner.class)
public class DomainValidatorStartupTest {

    @Test(expected = IllegalArgumentException.class)
    public void testUpdateBaseArrayCC_test0_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_RO, new String[] {"com"});
    }

    @Test(expected = IllegalArgumentException.class)
    public void testUpdateBaseArrayGeneric_test0_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_RO, new String[] {"com"});
    }

    @Test(expected = IllegalArgumentException.class)
    public void testUpdateBaseArrayInfra_test0_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.INFRASTRUCTURE_RO, new String[] {"com"});
    }

    @Test(expected = IllegalArgumentException.class)
    public void testUpdateBaseArrayLocal_test0_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.LOCAL_RO, new String[] {"com"});
    }

    @Test
    public void testUpdateCountryCode1a_test0_decomposed()  {
        DomainValidator validator = DomainValidator.getInstance0();
    }

    @Test
    public void testUpdateCountryCode1a_test1_decomposed()  {
        DomainValidator validator = DomainValidator.getInstance0();
        assertFalse(validator.isValidCountryCodeTld("com"));
    }

    @Test
    public void testUpdateCountryCode1b_test0_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_PLUS, new String[] {"com"});
    }

    @Test
    public void testUpdateCountryCode1b_test1_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_PLUS, new String[] {"com"});
        DomainValidator validator = DomainValidator.getInstance0();
    }

    @Test
    public void testUpdateCountryCode1b_test2_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_PLUS, new String[] {"com"});
        DomainValidator validator = DomainValidator.getInstance0();
        assertTrue(validator.isValidCountryCodeTld("com"));
    }

    @Test
    public void testUpdateCountryCode2_test0_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_PLUS, new String[] {"com"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"com"});
    }

    @Test
    public void testUpdateCountryCode2_test1_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_PLUS, new String[] {"com"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"com"});
        DomainValidator validator = DomainValidator.getInstance0();
    }

    @Test
    public void testUpdateCountryCode2_test2_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_PLUS, new String[] {"com"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"com"});
        DomainValidator validator = DomainValidator.getInstance0();
        assertFalse(validator.isValidCountryCodeTld("com"));
    }

    @Test
    public void testUpdateCountryCode3a_test0_decomposed()  {
        DomainValidator validator = DomainValidator.getInstance0();
    }

    @Test
    public void testUpdateCountryCode3a_test1_decomposed()  {
        DomainValidator validator = DomainValidator.getInstance0();
        assertTrue(validator.isValidCountryCodeTld("ch"));
    }

    @Test
    public void testUpdateCountryCode3b_test0_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"ch"});
    }

    @Test
    public void testUpdateCountryCode3b_test1_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"ch"});
        DomainValidator validator = DomainValidator.getInstance0();
    }

    @Test
    public void testUpdateCountryCode3b_test2_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"ch"});
        DomainValidator validator = DomainValidator.getInstance0();
        assertFalse(validator.isValidCountryCodeTld("ch"));
    }

    @Test
    public void testUpdateCountryCode3c_test0_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"ch"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"xx"});
    }

    @Test
    public void testUpdateCountryCode3c_test1_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"ch"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"xx"});
        DomainValidator validator = DomainValidator.getInstance0();
    }

    @Test
    public void testUpdateCountryCode3c_test2_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"ch"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"xx"});
        DomainValidator validator = DomainValidator.getInstance0();
        assertTrue(validator.isValidCountryCodeTld("ch"));
    }

    @Test
    public void testUpdateGeneric1_test0_decomposed()  {
        DomainValidator validator = DomainValidator.getInstance0();
    }

    @Test
    public void testUpdateGeneric1_test1_decomposed()  {
        DomainValidator validator = DomainValidator.getInstance0();
        assertFalse(validator.isValidGenericTld("ch"));
    }

    @Test
    public void testUpdateGeneric2_test0_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"ch"});
    }

    @Test
    public void testUpdateGeneric2_test1_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"ch"});
        DomainValidator validator = DomainValidator.getInstance0();
    }

    @Test
    public void testUpdateGeneric2_test2_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"ch"});
        DomainValidator validator = DomainValidator.getInstance0();
        assertTrue(validator.isValidGenericTld("ch"));
    }

    @Test
    public void testUpdateGeneric3_test0_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"ch"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"ch"});
    }

    @Test
    public void testUpdateGeneric3_test1_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"ch"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"ch"});
        DomainValidator validator = DomainValidator.getInstance0();
    }

    @Test
    public void testUpdateGeneric3_test2_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"ch"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"ch"});
        DomainValidator validator = DomainValidator.getInstance0();
        assertFalse(validator.isValidGenericTld("ch"));
        assertTrue(validator.isValidGenericTld("com"));
    }

    @Test
    public void testUpdateGeneric4_test0_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"ch"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"ch"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"com"});
    }

    @Test
    public void testUpdateGeneric4_test1_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"ch"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"ch"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"com"});
        DomainValidator validator = DomainValidator.getInstance0();
    }

    @Test
    public void testUpdateGeneric4_test2_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"ch"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"ch"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"com"});
        DomainValidator validator = DomainValidator.getInstance0();
        assertFalse(validator.isValidGenericTld("com"));
    }

    @Test
    public void testUpdateGeneric5_test0_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"ch"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"ch"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"com"});
        DomainValidator.updateTLDOverride(
                ArrayType.GENERIC_MINUS, new String[] {"xx"});
    }

    @Test
    public void testUpdateGeneric5_test1_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"ch"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"ch"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"com"});
        DomainValidator.updateTLDOverride(
                ArrayType.GENERIC_MINUS, new String[] {"xx"});
        DomainValidator validator = DomainValidator.getInstance0();
    }

    @Test
    public void testUpdateGeneric5_test2_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"ch"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"ch"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"com"});
        DomainValidator.updateTLDOverride(
                ArrayType.GENERIC_MINUS, new String[] {"xx"});
        DomainValidator validator = DomainValidator.getInstance0();
        assertTrue(validator.isValidGenericTld("com"));
    }

    @Test
    public void testVALIDATOR_412a_test0_decomposed()  {
        DomainValidator validator = DomainValidator.getInstance0();
    }

    @Test
    public void testVALIDATOR_412a_test1_decomposed()  {
        DomainValidator validator = DomainValidator.getInstance0();
        assertFalse(validator.isValidGenericTld("local"));
    }

    @Test
    public void testVALIDATOR_412a_test2_decomposed()  {
        DomainValidator validator = DomainValidator.getInstance0();
        assertFalse(validator.isValidGenericTld("local"));
        assertFalse(validator.isValid("abc.local"));
    }

    @Test
    public void testVALIDATOR_412a_test3_decomposed()  {
        DomainValidator validator = DomainValidator.getInstance0();
        assertFalse(validator.isValidGenericTld("local"));
        assertFalse(validator.isValid("abc.local"));
        assertFalse(validator.isValidGenericTld("pvt"));
    }

    @Test
    public void testVALIDATOR_412a_test4_decomposed()  {
        DomainValidator validator = DomainValidator.getInstance0();
        assertFalse(validator.isValidGenericTld("local"));
        assertFalse(validator.isValid("abc.local"));
        assertFalse(validator.isValidGenericTld("pvt"));
        assertFalse(validator.isValid("abc.pvt"));
    }

    @Test
    public void testVALIDATOR_412b_test0_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"local", "pvt"});
    }

    @Test
    public void testVALIDATOR_412b_test1_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"local", "pvt"});
        DomainValidator validator = DomainValidator.getInstance0();
    }

    @Test
    public void testVALIDATOR_412b_test2_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"local", "pvt"});
        DomainValidator validator = DomainValidator.getInstance0();
        assertTrue(validator.isValidGenericTld("local"));
    }

    @Test
    public void testVALIDATOR_412b_test3_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"local", "pvt"});
        DomainValidator validator = DomainValidator.getInstance0();
        assertTrue(validator.isValidGenericTld("local"));
        assertTrue(validator.isValid("abc.local"));
    }

    @Test
    public void testVALIDATOR_412b_test4_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"local", "pvt"});
        DomainValidator validator = DomainValidator.getInstance0();
        assertTrue(validator.isValidGenericTld("local"));
        assertTrue(validator.isValid("abc.local"));
        assertTrue(validator.isValidGenericTld("pvt"));
    }

    @Test
    public void testVALIDATOR_412b_test5_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"local", "pvt"});
        DomainValidator validator = DomainValidator.getInstance0();
        assertTrue(validator.isValidGenericTld("local"));
        assertTrue(validator.isValid("abc.local"));
        assertTrue(validator.isValidGenericTld("pvt"));
        assertTrue(validator.isValid("abc.pvt"));
    }

    @Test
    public void testVALIDATOR_412c_test0_decomposed()  {
        DomainValidator validator = DomainValidator.getInstance1(true);
    }

    @Test
    public void testVALIDATOR_412c_test1_decomposed()  {
        DomainValidator validator = DomainValidator.getInstance1(true);
        assertFalse(validator.isValidLocalTld("local"));
    }

    @Test
    public void testVALIDATOR_412c_test2_decomposed()  {
        DomainValidator validator = DomainValidator.getInstance1(true);
        assertFalse(validator.isValidLocalTld("local"));
        assertFalse(validator.isValid("abc.local"));
    }

    @Test
    public void testVALIDATOR_412c_test3_decomposed()  {
        DomainValidator validator = DomainValidator.getInstance1(true);
        assertFalse(validator.isValidLocalTld("local"));
        assertFalse(validator.isValid("abc.local"));
        assertFalse(validator.isValidLocalTld("pvt"));
    }

    @Test
    public void testVALIDATOR_412c_test4_decomposed()  {
        DomainValidator validator = DomainValidator.getInstance1(true);
        assertFalse(validator.isValidLocalTld("local"));
        assertFalse(validator.isValid("abc.local"));
        assertFalse(validator.isValidLocalTld("pvt"));
        assertFalse(validator.isValid("abc.pvt"));
    }

    @Test
    public void testVALIDATOR_412d_test0_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.LOCAL_PLUS, new String[] {"local", "pvt"});
    }

    @Test
    public void testVALIDATOR_412d_test1_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.LOCAL_PLUS, new String[] {"local", "pvt"});
        DomainValidator validator = DomainValidator.getInstance1(true);
    }

    @Test
    public void testVALIDATOR_412d_test2_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.LOCAL_PLUS, new String[] {"local", "pvt"});
        DomainValidator validator = DomainValidator.getInstance1(true);
        assertTrue(validator.isValidLocalTld("local"));
        assertTrue(validator.isValidLocalTld("pvt"));
    }

    @Test
    public void testVALIDATOR_412d_test3_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.LOCAL_PLUS, new String[] {"local", "pvt"});
        DomainValidator validator = DomainValidator.getInstance1(true);
        assertTrue(validator.isValidLocalTld("local"));
        assertTrue(validator.isValidLocalTld("pvt"));
        assertTrue(validator.isValid("abc.local"));
        assertTrue(validator.isValid("abc.pvt"));
    }

    @Test
    public void testCannotUpdate_test0_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"ch"});
    }

    @Test
    public void testCannotUpdate_test1_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"ch"});
        DomainValidator dv = DomainValidator.getInstance0();
    }

    @Test
    public void testCannotUpdate_test2_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"ch"});
        DomainValidator dv = DomainValidator.getInstance0();
        assertNotNull(dv);
        try {
            DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"ch"});
            fail("Expected IllegalStateException");
        } catch (IllegalStateException ise) {
        }
    }

    @Test
    public void testInstanceOverride_test0_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"gp"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"com"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_PLUS, new String[] {"cp"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"ch"});
    }

    @Test
    public void testInstanceOverride_test1_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"gp"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"com"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_PLUS, new String[] {"cp"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"ch"});
        DomainValidator validator = DomainValidator.getInstance1(false);
    }

    @Test
    public void testInstanceOverride_test2_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"gp"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"com"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_PLUS, new String[] {"cp"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"ch"});
        DomainValidator validator = DomainValidator.getInstance1(false);
        assertTrue(validator.isValidGenericTld("gp"));
        assertFalse(validator.isValidGenericTld("com"));
    }

    @Test
    public void testInstanceOverride_test3_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"gp"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"com"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_PLUS, new String[] {"cp"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"ch"});
        DomainValidator validator = DomainValidator.getInstance1(false);
        assertTrue(validator.isValidGenericTld("gp"));
        assertFalse(validator.isValidGenericTld("com"));
        assertTrue(validator.isValidCountryCodeTld("cp"));
        assertFalse(validator.isValidCountryCodeTld("ch"));
    }

    @Test
    public void testInstanceOverride_test4_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"gp"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"com"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_PLUS, new String[] {"cp"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"ch"});
        DomainValidator validator = DomainValidator.getInstance1(false);
        assertTrue(validator.isValidGenericTld("gp"));
        assertFalse(validator.isValidGenericTld("com"));
        assertTrue(validator.isValidCountryCodeTld("cp"));
        assertFalse(validator.isValidCountryCodeTld("ch"));
        List<DomainValidator.Item> items = new ArrayList<>();
        items.add(new DomainValidator.Item(ArrayType.GENERIC_MINUS, new String[] {""}));
    }

    @Test
    public void testInstanceOverride_test5_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"gp"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"com"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_PLUS, new String[] {"cp"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"ch"});
        DomainValidator validator = DomainValidator.getInstance1(false);
        assertTrue(validator.isValidGenericTld("gp"));
        assertFalse(validator.isValidGenericTld("com"));
        assertTrue(validator.isValidCountryCodeTld("cp"));
        assertFalse(validator.isValidCountryCodeTld("ch"));
        List<DomainValidator.Item> items = new ArrayList<>();
        items.add(new DomainValidator.Item(ArrayType.GENERIC_MINUS, new String[] {""}));
        items.add(new DomainValidator.Item(ArrayType.COUNTRY_CODE_MINUS, new String[] {""}));
    }

    @Test
    public void testInstanceOverride_test6_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"gp"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"com"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_PLUS, new String[] {"cp"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"ch"});
        DomainValidator validator = DomainValidator.getInstance1(false);
        assertTrue(validator.isValidGenericTld("gp"));
        assertFalse(validator.isValidGenericTld("com"));
        assertTrue(validator.isValidCountryCodeTld("cp"));
        assertFalse(validator.isValidCountryCodeTld("ch"));
        List<DomainValidator.Item> items = new ArrayList<>();
        items.add(new DomainValidator.Item(ArrayType.GENERIC_MINUS, new String[] {""}));
        items.add(new DomainValidator.Item(ArrayType.COUNTRY_CODE_MINUS, new String[] {""}));
        validator = DomainValidator.getInstance2(false, items);
    }

    @Test
    public void testInstanceOverride_test7_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"gp"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"com"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_PLUS, new String[] {"cp"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"ch"});
        DomainValidator validator = DomainValidator.getInstance1(false);
        assertTrue(validator.isValidGenericTld("gp"));
        assertFalse(validator.isValidGenericTld("com"));
        assertTrue(validator.isValidCountryCodeTld("cp"));
        assertFalse(validator.isValidCountryCodeTld("ch"));
        List<DomainValidator.Item> items = new ArrayList<>();
        items.add(new DomainValidator.Item(ArrayType.GENERIC_MINUS, new String[] {""}));
        items.add(new DomainValidator.Item(ArrayType.COUNTRY_CODE_MINUS, new String[] {""}));
        validator = DomainValidator.getInstance2(false, items);
        assertTrue(validator.isValidGenericTld("gp"));
        assertTrue(validator.isValidGenericTld("com"));
    }

    @Test
    public void testInstanceOverride_test8_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"gp"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"com"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_PLUS, new String[] {"cp"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"ch"});
        DomainValidator validator = DomainValidator.getInstance1(false);
        assertTrue(validator.isValidGenericTld("gp"));
        assertFalse(validator.isValidGenericTld("com"));
        assertTrue(validator.isValidCountryCodeTld("cp"));
        assertFalse(validator.isValidCountryCodeTld("ch"));
        List<DomainValidator.Item> items = new ArrayList<>();
        items.add(new DomainValidator.Item(ArrayType.GENERIC_MINUS, new String[] {""}));
        items.add(new DomainValidator.Item(ArrayType.COUNTRY_CODE_MINUS, new String[] {""}));
        validator = DomainValidator.getInstance2(false, items);
        assertTrue(validator.isValidGenericTld("gp"));
        assertTrue(validator.isValidGenericTld("com"));
        assertTrue(validator.isValidCountryCodeTld("cp"));
        assertTrue(validator.isValidCountryCodeTld("ch"));
    }

    @Test
    public void testInstanceOverride_test9_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"gp"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"com"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_PLUS, new String[] {"cp"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"ch"});
        DomainValidator validator = DomainValidator.getInstance1(false);
        assertTrue(validator.isValidGenericTld("gp"));
        assertFalse(validator.isValidGenericTld("com"));
        assertTrue(validator.isValidCountryCodeTld("cp"));
        assertFalse(validator.isValidCountryCodeTld("ch"));
        List<DomainValidator.Item> items = new ArrayList<>();
        items.add(new DomainValidator.Item(ArrayType.GENERIC_MINUS, new String[] {""}));
        items.add(new DomainValidator.Item(ArrayType.COUNTRY_CODE_MINUS, new String[] {""}));
        validator = DomainValidator.getInstance2(false, items);
        assertTrue(validator.isValidGenericTld("gp"));
        assertTrue(validator.isValidGenericTld("com"));
        assertTrue(validator.isValidCountryCodeTld("cp"));
        assertTrue(validator.isValidCountryCodeTld("ch"));
        validator = DomainValidator.getInstance1(false);
    }

    @Test
    public void testInstanceOverride_test10_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"gp"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"com"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_PLUS, new String[] {"cp"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"ch"});
        DomainValidator validator = DomainValidator.getInstance1(false);
        assertTrue(validator.isValidGenericTld("gp"));
        assertFalse(validator.isValidGenericTld("com"));
        assertTrue(validator.isValidCountryCodeTld("cp"));
        assertFalse(validator.isValidCountryCodeTld("ch"));
        List<DomainValidator.Item> items = new ArrayList<>();
        items.add(new DomainValidator.Item(ArrayType.GENERIC_MINUS, new String[] {""}));
        items.add(new DomainValidator.Item(ArrayType.COUNTRY_CODE_MINUS, new String[] {""}));
        validator = DomainValidator.getInstance2(false, items);
        assertTrue(validator.isValidGenericTld("gp"));
        assertTrue(validator.isValidGenericTld("com"));
        assertTrue(validator.isValidCountryCodeTld("cp"));
        assertTrue(validator.isValidCountryCodeTld("ch"));
        validator = DomainValidator.getInstance1(false);
        assertTrue(validator.isValidGenericTld("gp"));
        assertFalse(validator.isValidGenericTld("com"));
    }

    @Test
    public void testInstanceOverride_test11_decomposed()  {
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, new String[] {"gp"});
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, new String[] {"com"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_PLUS, new String[] {"cp"});
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, new String[] {"ch"});
        DomainValidator validator = DomainValidator.getInstance1(false);
        assertTrue(validator.isValidGenericTld("gp"));
        assertFalse(validator.isValidGenericTld("com"));
        assertTrue(validator.isValidCountryCodeTld("cp"));
        assertFalse(validator.isValidCountryCodeTld("ch"));
        List<DomainValidator.Item> items = new ArrayList<>();
        items.add(new DomainValidator.Item(ArrayType.GENERIC_MINUS, new String[] {""}));
        items.add(new DomainValidator.Item(ArrayType.COUNTRY_CODE_MINUS, new String[] {""}));
        validator = DomainValidator.getInstance2(false, items);
        assertTrue(validator.isValidGenericTld("gp"));
        assertTrue(validator.isValidGenericTld("com"));
        assertTrue(validator.isValidCountryCodeTld("cp"));
        assertTrue(validator.isValidCountryCodeTld("ch"));
        validator = DomainValidator.getInstance1(false);
        assertTrue(validator.isValidGenericTld("gp"));
        assertFalse(validator.isValidGenericTld("com"));
        assertTrue(validator.isValidCountryCodeTld("cp"));
        assertFalse(validator.isValidCountryCodeTld("ch"));
    }
}