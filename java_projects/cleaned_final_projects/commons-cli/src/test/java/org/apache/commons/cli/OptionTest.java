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

package org.apache.commons.cli;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNotEquals;
import static org.junit.Assert.assertNotSame;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class OptionTest {
    private static class DefaultOption extends Option {
        private static final long serialVersionUID = 1L;

        private final String defaultValue;

        DefaultOption(final String opt, final String description, final String defaultValue)
                throws IllegalArgumentException {
            super(-1, null, null, null, false, null);
            this.defaultValue = defaultValue;
        }

        @Override
        public String getValue0() {
            return super.getValue0() != null ? super.getValue0() : defaultValue;
        }
    }

    private static class TestOption extends Option {
        private static final long serialVersionUID = 1L;

        TestOption(final String opt, final boolean hasArg, final String description)
                throws IllegalArgumentException {
            super(-1, opt, null, description, hasArg, null);
        }

        @Override
        public boolean addValue(final String value) {
            addValueForProcessing(value);
            return true;
        }
    }

    private static void checkOption(
            final Option option,
            final String opt,
            final String description,
            final String longOpt,
            final int numArgs,
            final String argName,
            final boolean required,
            final boolean optionalArg,
            final char valueSeparator,
            final Class<?> cls) {
        assertEquals(opt, option.getOpt());
        assertEquals(description, option.getDescription());
        assertEquals(longOpt, option.getLongOpt());
        assertEquals(numArgs, option.getArgs());
        assertEquals(argName, option.getArgName());
        assertEquals(required, option.isRequired());

        assertEquals(optionalArg, option.hasOptionalArg());
        assertEquals(valueSeparator, option.getValueSeparator());
        assertEquals(cls, option.getType());
    }

    @Test(expected = IllegalArgumentException.class)
    public void testBuilderInsufficientParams1() {
        Option.builder0().desc("desc").build();
    }

    @Test(expected = IllegalArgumentException.class)
    public void testBuilderInsufficientParams2() {
        Option.builder1(null).desc("desc").build();
    }

    @Test(expected = IllegalArgumentException.class)
    public void testBuilderInvalidOptionName1() {
        Option.builder0().option("invalid?");
    }

    @Test(expected = IllegalArgumentException.class)
    public void testBuilderInvalidOptionName2() {
        Option.builder0().option("invalid@");
    }

    @Test(expected = IllegalArgumentException.class)
    public void testBuilderInvalidOptionName3() {
        Option.builder1("invalid?");
    }

    @Test(expected = IllegalArgumentException.class)
    public void testBuilderInvalidOptionName4() {
        Option.builder1("invalid@");
    }

    @Test
    public void testBuilderMethods() {
        final char defaultSeparator = (char) 0;

        checkOption(
                Option.builder1("a").desc("desc").build(),
                "a",
                "desc",
                null,
                Option.UNINITIALIZED,
                null,
                false,
                false,
                defaultSeparator,
                String.class);
        checkOption(
                Option.builder1("a").desc("desc").build(),
                "a",
                "desc",
                null,
                Option.UNINITIALIZED,
                null,
                false,
                false,
                defaultSeparator,
                String.class);
        checkOption(
                Option.builder1("a").desc("desc").longOpt("aaa").build(),
                "a",
                "desc",
                "aaa",
                Option.UNINITIALIZED,
                null,
                false,
                false,
                defaultSeparator,
                String.class);
        checkOption(
                Option.builder1("a").desc("desc").hasArg1(true).build(),
                "a",
                "desc",
                null,
                1,
                null,
                false,
                false,
                defaultSeparator,
                String.class);
        checkOption(
                Option.builder1("a").desc("desc").hasArg1(false).build(),
                "a",
                "desc",
                null,
                Option.UNINITIALIZED,
                null,
                false,
                false,
                defaultSeparator,
                String.class);
        checkOption(
                Option.builder1("a").desc("desc").hasArg1(true).build(),
                "a",
                "desc",
                null,
                1,
                null,
                false,
                false,
                defaultSeparator,
                String.class);
        checkOption(
                Option.builder1("a").desc("desc").numberOfArgs(3).build(),
                "a",
                "desc",
                null,
                3,
                null,
                false,
                false,
                defaultSeparator,
                String.class);
        checkOption(
                Option.builder1("a").desc("desc").required1(true).build(),
                "a",
                "desc",
                null,
                Option.UNINITIALIZED,
                null,
                true,
                false,
                defaultSeparator,
                String.class);
        checkOption(
                Option.builder1("a").desc("desc").required1(false).build(),
                "a",
                "desc",
                null,
                Option.UNINITIALIZED,
                null,
                false,
                false,
                defaultSeparator,
                String.class);

        checkOption(
                Option.builder1("a").desc("desc").argName("arg1").build(),
                "a",
                "desc",
                null,
                Option.UNINITIALIZED,
                "arg1",
                false,
                false,
                defaultSeparator,
                String.class);
        checkOption(
                Option.builder1("a").desc("desc").optionalArg(false).build(),
                "a",
                "desc",
                null,
                Option.UNINITIALIZED,
                null,
                false,
                false,
                defaultSeparator,
                String.class);
        checkOption(
                Option.builder1("a").desc("desc").optionalArg(true).build(),
                "a",
                "desc",
                null,
                Option.UNINITIALIZED,
                null,
                false,
                true,
                defaultSeparator,
                String.class);
        checkOption(
                Option.builder1("a").desc("desc").valueSeparator1(':').build(),
                "a",
                "desc",
                null,
                Option.UNINITIALIZED,
                null,
                false,
                false,
                ':',
                String.class);
        checkOption(
                Option.builder1("a").desc("desc").type(Integer.class).build(),
                "a",
                "desc",
                null,
                Option.UNINITIALIZED,
                null,
                false,
                false,
                defaultSeparator,
                Integer.class);
        checkOption(
                Option.builder0().option("a").desc("desc").type(Integer.class).build(),
                "a",
                "desc",
                null,
                Option.UNINITIALIZED,
                null,
                false,
                false,
                defaultSeparator,
                Integer.class);
    }

    @Test
    public void testClear() {
        final TestOption option = new TestOption("x", true, "");
        assertEquals(0, option.getValuesList().size());
        option.addValue("a");
        assertEquals(1, option.getValuesList().size());
        option.clearValues();
        assertEquals(0, option.getValuesList().size());
    }

    @Test
    public void testClone() {
        final TestOption a = new TestOption("a", true, "");
        final TestOption b = (TestOption) a.clone();
        assertEquals(a, b);
        assertNotSame(a, b);
        a.setDescription("a");
        assertEquals("", b.getDescription());
        b.setArgs(2);
        b.addValue("b1");
        b.addValue("b2");
        assertEquals(1, a.getArgs());
        assertEquals(0, a.getValuesList().size());
        assertEquals(2, b.getValues().length);
    }

    @Test
    public void testGetValue() {
        final Option option = Option.Option1("f", null);
        option.setArgs(Option.UNLIMITED_VALUES);

        assertEquals("default", option.getValue2("default"));
        assertNull(option.getValue1(0));

        option.addValueForProcessing("foo");

        assertEquals("foo", option.getValue0());
        assertEquals("foo", option.getValue1(0));
        assertEquals("foo", option.getValue2("default"));
    }

    @Test
    public void testHasArgName() {
        final Option option = Option.Option1("f", null);

        option.setArgName(null);
        assertFalse(option.hasArgName());

        option.setArgName("");
        assertFalse(option.hasArgName());

        option.setArgName("file");
        assertTrue(option.hasArgName());
    }

    @Test
    public void testHasArgs() {
        final Option option = Option.Option1("f", null);

        option.setArgs(0);
        assertFalse(option.hasArgs());

        option.setArgs(1);
        assertFalse(option.hasArgs());

        option.setArgs(10);
        assertTrue(option.hasArgs());

        option.setArgs(Option.UNLIMITED_VALUES);
        assertTrue(option.hasArgs());

        option.setArgs(Option.UNINITIALIZED);
        assertFalse(option.hasArgs());
    }

    @Test
    public void testHashCode() {
        assertNotEquals(
                Option.builder1("test").build().hashCode(),
                Option.builder1("test2").build().hashCode());
        assertNotEquals(
                Option.builder1("test").build().hashCode(),
                Option.builder0().longOpt("test").build().hashCode());
        assertNotEquals(
                Option.builder1("test").build().hashCode(),
                Option.builder1("test").longOpt("long test").build().hashCode());
    }

    @Test
    public void testSubclass() {
        final Option option = new DefaultOption("f", "file", "myfile.txt");
        final Option clone = (Option) option.clone();
        assertEquals("myfile.txt", clone.getValue0());
        assertEquals(DefaultOption.class, clone.getClass());
    }
}
