/*
 *  Copyright 2010-present Stephen Colebourne
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */
package org.joda.convert;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import org.joda.convert.factory.NumericObjectArrayStringConverterFactory;
import org.junit.Test;

import java.util.Arrays;

/** Test NumericObjectArrayStringConverterFactory. */
public class TestNumericObjectArrayStringConverterFactory {

    @Test
    public void test_LongArray() {
        doTest0(new Long[0], "");
        doTest0(new Long[] {5L}, "5");
        doTest0(new Long[] {null}, "-");
        doTest0(new Long[] {-1234L, null, 56789L, null, null, 5L}, "-1234,-,56789,-,-,5");
        doTest0(new Long[] {12345678912345L, 12345678912345L}, "12345678912345,12345678912345");
    }

    private void doTest0(Long[] array, String str) {
        StringConvert test =
                new StringConvert(true, NumericObjectArrayStringConverterFactory.INSTANCE);
        assertEquals(str, test.convertToString0(array));
        assertEquals(str, test.convertToString1(Long[].class, array));
        assertTrue(Arrays.equals(array, test.convertFromString(Long[].class, str)));
    }

    @Test
    public void test_IntegerArray() {
        doTest1(new Integer[0], "");
        doTest1(new Integer[] {5}, "5");
        doTest1(new Integer[] {null}, "-");
        doTest1(new Integer[] {-1234, null, 56789, null, null, 5}, "-1234,-,56789,-,-,5");
    }

    private void doTest1(Integer[] array, String str) {
        StringConvert test =
                new StringConvert(true, NumericObjectArrayStringConverterFactory.INSTANCE);
        assertEquals(str, test.convertToString0(array));
        assertEquals(str, test.convertToString1(Integer[].class, array));
        assertTrue(Arrays.equals(array, test.convertFromString(Integer[].class, str)));
    }

    @Test
    public void test_ShortArray() {
        doTest2(new Short[0], "");
        doTest2(new Short[] {5}, "5");
        doTest2(new Short[] {null}, "-");
        doTest2(new Short[] {-1234, null, 5678, null, null, 5}, "-1234,-,5678,-,-,5");
    }

    private void doTest2(Short[] array, String str) {
        StringConvert test =
                new StringConvert(true, NumericObjectArrayStringConverterFactory.INSTANCE);
        assertEquals(str, test.convertToString0(array));
        assertEquals(str, test.convertToString1(Short[].class, array));
        assertTrue(Arrays.equals(array, test.convertFromString(Short[].class, str)));
    }

    @Test
    public void test_DoubleArray() {
        doTest3(new Double[0], "");
        doTest3(new Double[] {5d}, "5.0");
        doTest3(new Double[] {null}, "-");
        doTest3(new Double[] {5.123456789d}, "5.123456789");
        doTest3(new Double[] {-1234d, null, 5678d, null, null, 5d}, "-1234.0,-,5678.0,-,-,5.0");
        doTest3(
                new Double[] {
                    Double.NaN, Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY, -0.0d, +0.0d, 0d
                },
                "NaN,-Infinity,Infinity,-0.0,0.0,0.0");
        doTest3(new Double[] {0.0000006d, 6000000000d}, "6.0E-7,6.0E9");
    }

    private void doTest3(Double[] array, String str) {
        StringConvert test =
                new StringConvert(true, NumericObjectArrayStringConverterFactory.INSTANCE);
        assertEquals(str, test.convertToString0(array));
        assertEquals(str, test.convertToString1(Double[].class, array));
        assertTrue(Arrays.equals(array, test.convertFromString(Double[].class, str)));
    }

    @Test
    public void test_FloatArray() {
        doTest4(new Float[0], "");
        doTest4(new Float[] {5f}, "5.0");
        doTest4(new Float[] {null}, "-");
        doTest4(new Float[] {5.1234f}, "5.1234");
        doTest4(new Float[] {-1234f, null, 5678f, null, null, 5f}, "-1234.0,-,5678.0,-,-,5.0");
        doTest4(
                new Float[] {
                    Float.NaN, Float.NEGATIVE_INFINITY, Float.POSITIVE_INFINITY, -0.0f, +0.0f, 0f
                },
                "NaN,-Infinity,Infinity,-0.0,0.0,0.0");
        doTest4(new Float[] {0.0000006f, 6000000000f}, "6.0E-7,6.0E9");
    }

    private void doTest4(Float[] array, String str) {
        StringConvert test =
                new StringConvert(true, NumericObjectArrayStringConverterFactory.INSTANCE);
        assertEquals(str, test.convertToString0(array));
        assertEquals(str, test.convertToString1(Float[].class, array));
        assertTrue(Arrays.equals(array, test.convertFromString(Float[].class, str)));
    }
}
