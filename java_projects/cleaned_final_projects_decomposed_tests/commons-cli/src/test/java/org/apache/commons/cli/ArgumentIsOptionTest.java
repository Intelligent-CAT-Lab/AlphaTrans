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

package org.apache.commons.cli;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.junit.Before;
import org.junit.Test;

@SuppressWarnings("deprecation") // tests some deprecated classes
public class ArgumentIsOptionTest {

    private Options options;
    private CommandLineParser parser;

    @Before
    public void setUp() {
        options =
                new Options()
                        .addOption1("p", false, "Option p")
                        .addOption1("attr", true, "Option accepts argument");
        parser = new PosixParser();
    }

    @Test
    public void testOption_test0_decomposed() throws Exception {
        final String[] args = {"-p"};
        final CommandLine cl = parser.parse0(options, args);
    }

    @Test
    public void testOption_test1_decomposed() throws Exception {
        final String[] args = {"-p"};
        final CommandLine cl = parser.parse0(options, args);
        assertTrue("Confirm -p is set", cl.hasOption2("p"));
        assertFalse("Confirm -attr is not set", cl.hasOption2("attr"));
    }

    @Test
    public void testOption_test2_decomposed() throws Exception {
        final String[] args = {"-p"};
        final CommandLine cl = parser.parse0(options, args);
        assertTrue("Confirm -p is set", cl.hasOption2("p"));
        assertFalse("Confirm -attr is not set", cl.hasOption2("attr"));
        assertEquals("Confirm all arguments recognized", 0, cl.getArgs().length);
    }

    @Test
    public void testOptionAndOptionWithArgument_test0_decomposed() throws Exception {
        final String[] args = {"-p", "-attr", "p"};
        final CommandLine cl = parser.parse0(options, args);
    }

    @Test
    public void testOptionAndOptionWithArgument_test1_decomposed() throws Exception {
        final String[] args = {"-p", "-attr", "p"};
        final CommandLine cl = parser.parse0(options, args);
        assertTrue("Confirm -p is set", cl.hasOption2("p"));
        assertTrue("Confirm -attr is set", cl.hasOption2("attr"));
    }

    @Test
    public void testOptionAndOptionWithArgument_test2_decomposed() throws Exception {
        final String[] args = {"-p", "-attr", "p"};
        final CommandLine cl = parser.parse0(options, args);
        assertTrue("Confirm -p is set", cl.hasOption2("p"));
        assertTrue("Confirm -attr is set", cl.hasOption2("attr"));
        assertEquals("Confirm arg of -attr", "p", cl.getOptionValue4("attr"));
    }

    @Test
    public void testOptionAndOptionWithArgument_test3_decomposed() throws Exception {
        final String[] args = {"-p", "-attr", "p"};
        final CommandLine cl = parser.parse0(options, args);
        assertTrue("Confirm -p is set", cl.hasOption2("p"));
        assertTrue("Confirm -attr is set", cl.hasOption2("attr"));
        assertEquals("Confirm arg of -attr", "p", cl.getOptionValue4("attr"));
        assertEquals("Confirm all arguments recognized", 0, cl.getArgs().length);
    }

    @Test
    public void testOptionWithArgument_test0_decomposed() throws Exception {
        final String[] args = {"-attr", "p"};
        final CommandLine cl = parser.parse0(options, args);
    }

    @Test
    public void testOptionWithArgument_test1_decomposed() throws Exception {
        final String[] args = {"-attr", "p"};
        final CommandLine cl = parser.parse0(options, args);
        assertFalse("Confirm -p is set", cl.hasOption2("p"));
        assertTrue("Confirm -attr is set", cl.hasOption2("attr"));
    }

    @Test
    public void testOptionWithArgument_test2_decomposed() throws Exception {
        final String[] args = {"-attr", "p"};
        final CommandLine cl = parser.parse0(options, args);
        assertFalse("Confirm -p is set", cl.hasOption2("p"));
        assertTrue("Confirm -attr is set", cl.hasOption2("attr"));
        assertEquals("Confirm arg of -attr", "p", cl.getOptionValue4("attr"));
    }

    @Test
    public void testOptionWithArgument_test3_decomposed() throws Exception {
        final String[] args = {"-attr", "p"};
        final CommandLine cl = parser.parse0(options, args);
        assertFalse("Confirm -p is set", cl.hasOption2("p"));
        assertTrue("Confirm -attr is set", cl.hasOption2("attr"));
        assertEquals("Confirm arg of -attr", "p", cl.getOptionValue4("attr"));
        assertEquals("Confirm all arguments recognized", 0, cl.getArgs().length);
    }
}