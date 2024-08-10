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

package org.apache.commons.cli.bug;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.CommandLineParser;
import org.apache.commons.cli.MissingArgumentException;
import org.apache.commons.cli.Option;
import org.apache.commons.cli.Options;
import org.apache.commons.cli.PosixParser;
import org.junit.Before;
import org.junit.Test;

@SuppressWarnings("deprecation") // tests some deprecated classes
public class BugCLI71Test {
    private Options options;
    private CommandLineParser parser;

    @Before
    public void setUp() {
        options = new Options();

        final Option algorithm =
                new Option(
                        0, "a", "algo", "the algorithm which it to perform executing", true, null);
        algorithm.setArgName("algorithm name");
        options.addOption0(algorithm);

        final Option key =
                new Option(
                        0, "k", "key", "the key the setted algorithm uses to process", true, null);
        algorithm.setArgName("value");
        options.addOption0(key);

        parser = new PosixParser();
    }

    @Test
    public void testBasic_test0_decomposed() throws Exception {
        final String[] args = {"-a", "Caesar", "-k", "A"};
        final CommandLine line = parser.parse0(options, args);
    }

    @Test
    public void testBasic_test1_decomposed() throws Exception {
        final String[] args = {"-a", "Caesar", "-k", "A"};
        final CommandLine line = parser.parse0(options, args);
        assertEquals("Caesar", line.getOptionValue4("a"));
        assertEquals("A", line.getOptionValue4("k"));
    }

    @Test
    public void testGetsDefaultIfOptional_test0_decomposed() throws Exception {
        final String[] args = {"-k", "-a", "Caesar"};
        options.getOption("k");
    }

    @Test
    public void testGetsDefaultIfOptional_test1_decomposed() throws Exception {
        final String[] args = {"-k", "-a", "Caesar"};
        options.getOption("k");
        options.getOption("k").setOptionalArg(true);
    }

    @Test
    public void testGetsDefaultIfOptional_test2_decomposed() throws Exception {
        final String[] args = {"-k", "-a", "Caesar"};
        options.getOption("k");
        options.getOption("k").setOptionalArg(true);
        final CommandLine line = parser.parse0(options, args);
    }

    @Test
    public void testGetsDefaultIfOptional_test3_decomposed() throws Exception {
        final String[] args = {"-k", "-a", "Caesar"};
        options.getOption("k");
        options.getOption("k").setOptionalArg(true);
        final CommandLine line = parser.parse0(options, args);
        assertEquals("Caesar", line.getOptionValue4("a"));
    }

    @Test
    public void testGetsDefaultIfOptional_test4_decomposed() throws Exception {
        final String[] args = {"-k", "-a", "Caesar"};
        options.getOption("k");
        options.getOption("k").setOptionalArg(true);
        final CommandLine line = parser.parse0(options, args);
        assertEquals("Caesar", line.getOptionValue4("a"));
        assertEquals("a", line.getOptionValue1('k', "a"));
    }

    @Test
    public void testLackOfError_test0_decomposed() throws Exception {
        final String[] args = {"-k", "-a", "Caesar"};
        try {
            parser.parse0(options, args);
            fail("MissingArgumentException expected");
        } catch (final MissingArgumentException e) {
            assertEquals("option missing an argument", "k", e.getOption().getOpt());
        }
    }

    @Test
    public void testMistakenArgument_test0_decomposed() throws Exception {
        String[] args = {"-a", "Caesar", "-k", "A"};
        CommandLine line = parser.parse0(options, args);
    }

    @Test
    public void testMistakenArgument_test1_decomposed() throws Exception {
        String[] args = {"-a", "Caesar", "-k", "A"};
        CommandLine line = parser.parse0(options, args);
        args = new String[] {"-a", "Caesar", "-k", "a"};
        line = parser.parse0(options, args);
    }

    @Test
    public void testMistakenArgument_test2_decomposed() throws Exception {
        String[] args = {"-a", "Caesar", "-k", "A"};
        CommandLine line = parser.parse0(options, args);
        args = new String[] {"-a", "Caesar", "-k", "a"};
        line = parser.parse0(options, args);
        assertEquals("Caesar", line.getOptionValue4("a"));
        assertEquals("a", line.getOptionValue4("k"));
    }
}