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

package org.apache.commons.codec.binary;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import org.junit.Assert;
import org.junit.Test;

/**
 * Tests {@link org.apache.commons.codec.binary.CharSequenceUtils}.
 *
 * <p>Tests copied from Apache Commons Lang 3.11. The implementation in codec is based on an earlier
 * version of Lang and some tests fail. The CharSequenceUtils class is public but the method is
 * package private. The failing tests have been commented out and the implementation left unchanged.
 */
public class CharSequenceUtilsTest {

    static class TestData {
        final String source;
        final boolean ignoreCase;
        final int toffset;
        final String other;
        final int ooffset;
        final int len;
        final boolean expected;
        final Class<? extends Throwable> throwable;

        public TestData(
                int constructorId,
                final boolean expected,
                final int ooffset,
                final String source,
                final Class<? extends Throwable> throwable,
                final int toffset,
                final boolean ignoreCase,
                final String other,
                final int len) {
            if (constructorId == 0) {
                this.source = source;
                this.ignoreCase = ignoreCase;
                this.toffset = toffset;
                this.other = other;
                this.ooffset = ooffset;
                this.len = len;
                this.expected = false;
                this.throwable = throwable;
            } else {
                this.source = source;
                this.ignoreCase = ignoreCase;
                this.toffset = toffset;
                this.other = other;
                this.ooffset = ooffset;
                this.len = len;
                this.expected = expected;
                this.throwable = null;
            }
        }

        @Override
        public String toString() {
            final StringBuilder sb = new StringBuilder();
            sb.append(source).append("[").append(toffset).append("]");
            sb.append(ignoreCase ? " caseblind " : " samecase ");
            sb.append(other).append("[").append(ooffset).append("]");
            sb.append(" ").append(len).append(" => ");
            if (throwable != null) {
                sb.append(throwable);
            } else {
                sb.append(expected);
            }
            return sb.toString();
        }
    }

    private static final TestData[] TEST_DATA = {
        new TestData(1, true, 0, "a", null, 0, true, "abc", 0),
        new TestData(1, true, 0, "a", null, 0, true, "abc", 1),
        new TestData(1, true, 0, "Abc", null, 0, true, "abc", 3),
        new TestData(1, false, 0, "Abc", null, 0, false, "abc", 3),
        new TestData(1, true, 1, "Abc", null, 1, true, "abc", 2),
        new TestData(1, true, 1, "Abc", null, 1, false, "abc", 2),
        new TestData(1, true, 1, "Abcd", null, 1, true, "abcD", 2),
        new TestData(1, true, 1, "Abcd", null, 1, false, "abcD", 2),
    };

    private abstract static class RunTest {

        abstract boolean invoke();

        void run(final TestData data, final String id) {
            if (data.throwable != null) {
                final String msg = id + " Expected " + data.throwable;
                try {
                    invoke();
                    Assert.fail(msg + " but nothing was thrown.");
                } catch (final Exception ex) {
                    assertTrue(
                            msg + " but was " + ex.getClass().getSimpleName(),
                            data.throwable.isAssignableFrom(ex.getClass()));
                }
            } else {
                final boolean stringCheck = invoke();
                assertEquals(id + " Failed test " + data, data.expected, stringCheck);
            }
        }
    }

    

    /**
     * Test the constructor exists. This is here for code coverage. The class ideally should be
     * package private, marked as final and have a private constructor to prevent instances.
     */

    @Test
    public void testRegionMatches_test0_decomposed()  {
        for (final TestData data : TEST_DATA) {
            new RunTest() {
                @Override
                boolean invoke() {
                    return data.source.regionMatches(
                            data.ignoreCase, data.toffset, data.other, data.ooffset, data.len);
                }
            }.run(data, "String");
            new RunTest() {
                @Override
                boolean invoke() {
                    return CharSequenceUtils.regionMatches(
                            data.source,
                            data.ignoreCase,
                            data.toffset,
                            data.other,
                            data.ooffset,
                            data.len);
                }
            }.run(data, "CSString");
            new RunTest() {
                @Override
                boolean invoke() {
                    return CharSequenceUtils.regionMatches(
                            new StringBuilder(data.source),
                            data.ignoreCase,
                            data.toffset,
                            data.other,
                            data.ooffset,
                            data.len);
                }
            }.run(data, "CSNonString");
        }
    }

    @Test
    public void testConstructor_test0_decomposed()  {
        new CharSequenceUtils();
    }
}