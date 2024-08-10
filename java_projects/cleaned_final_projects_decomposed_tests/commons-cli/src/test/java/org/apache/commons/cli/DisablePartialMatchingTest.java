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

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class DisablePartialMatchingTest {

    @Test
    public void testDisablePartialMatching_test0_decomposed() throws Exception {
        final CommandLineParser parser = new DefaultParser(0, false, null);
    }

    @Test
    public void testDisablePartialMatching_test1_decomposed() throws Exception {
        final CommandLineParser parser = new DefaultParser(0, false, null);
        final Options options = new Options();
    }

    @Test
    public void testDisablePartialMatching_test2_decomposed() throws Exception {
        final CommandLineParser parser = new DefaultParser(0, false, null);
        final Options options = new Options();
        options.addOption0(new Option(0, "d", "debug", "Turn on debug.", false, null));
    }

    @Test
    public void testDisablePartialMatching_test3_decomposed() throws Exception {
        final CommandLineParser parser = new DefaultParser(0, false, null);
        final Options options = new Options();
        options.addOption0(new Option(0, "d", "debug", "Turn on debug.", false, null));
        options.addOption0(new Option(0, "e", "extract", "Turn on extract.", false, null));
    }

    @Test
    public void testDisablePartialMatching_test4_decomposed() throws Exception {
        final CommandLineParser parser = new DefaultParser(0, false, null);
        final Options options = new Options();
        options.addOption0(new Option(0, "d", "debug", "Turn on debug.", false, null));
        options.addOption0(new Option(0, "e", "extract", "Turn on extract.", false, null));
        options.addOption0(
                new Option(0, "o", "option", "Turn on option with argument.", true, null));
    }

    @Test
    public void testDisablePartialMatching_test5_decomposed() throws Exception {
        final CommandLineParser parser = new DefaultParser(0, false, null);
        final Options options = new Options();
        options.addOption0(new Option(0, "d", "debug", "Turn on debug.", false, null));
        options.addOption0(new Option(0, "e", "extract", "Turn on extract.", false, null));
        options.addOption0(
                new Option(0, "o", "option", "Turn on option with argument.", true, null));
        final CommandLine line = parser.parse0(options, new String[] {"-de", "--option=foobar"});
    }

    @Test
    public void testDisablePartialMatching_test6_decomposed() throws Exception {
        final CommandLineParser parser = new DefaultParser(0, false, null);
        final Options options = new Options();
        options.addOption0(new Option(0, "d", "debug", "Turn on debug.", false, null));
        options.addOption0(new Option(0, "e", "extract", "Turn on extract.", false, null));
        options.addOption0(
                new Option(0, "o", "option", "Turn on option with argument.", true, null));
        final CommandLine line = parser.parse0(options, new String[] {"-de", "--option=foobar"});
        assertTrue("There should be an option debug in any case...", line.hasOption2("debug"));
        assertTrue(
                "There should be an extract option because partial matching is off",
                line.hasOption2("extract"));
        assertTrue(
                "There should be an option option with a argument value",
                line.hasOption2("option"));
    }

    @Test
    public void testRegularPartialMatching_test0_decomposed() throws Exception {
        final CommandLineParser parser = new DefaultParser(2, false, null);
    }

    @Test
    public void testRegularPartialMatching_test1_decomposed() throws Exception {
        final CommandLineParser parser = new DefaultParser(2, false, null);
        final Options options = new Options();
    }

    @Test
    public void testRegularPartialMatching_test2_decomposed() throws Exception {
        final CommandLineParser parser = new DefaultParser(2, false, null);
        final Options options = new Options();
        options.addOption0(new Option(0, "d", "debug", "Turn on debug.", false, null));
    }

    @Test
    public void testRegularPartialMatching_test3_decomposed() throws Exception {
        final CommandLineParser parser = new DefaultParser(2, false, null);
        final Options options = new Options();
        options.addOption0(new Option(0, "d", "debug", "Turn on debug.", false, null));
        options.addOption0(new Option(0, "e", "extract", "Turn on extract.", false, null));
    }

    @Test
    public void testRegularPartialMatching_test4_decomposed() throws Exception {
        final CommandLineParser parser = new DefaultParser(2, false, null);
        final Options options = new Options();
        options.addOption0(new Option(0, "d", "debug", "Turn on debug.", false, null));
        options.addOption0(new Option(0, "e", "extract", "Turn on extract.", false, null));
        options.addOption0(
                new Option(0, "o", "option", "Turn on option with argument.", true, null));
    }

    @Test
    public void testRegularPartialMatching_test5_decomposed() throws Exception {
        final CommandLineParser parser = new DefaultParser(2, false, null);
        final Options options = new Options();
        options.addOption0(new Option(0, "d", "debug", "Turn on debug.", false, null));
        options.addOption0(new Option(0, "e", "extract", "Turn on extract.", false, null));
        options.addOption0(
                new Option(0, "o", "option", "Turn on option with argument.", true, null));
        final CommandLine line = parser.parse0(options, new String[] {"-de", "--option=foobar"});
    }

    @Test
    public void testRegularPartialMatching_test6_decomposed() throws Exception {
        final CommandLineParser parser = new DefaultParser(2, false, null);
        final Options options = new Options();
        options.addOption0(new Option(0, "d", "debug", "Turn on debug.", false, null));
        options.addOption0(new Option(0, "e", "extract", "Turn on extract.", false, null));
        options.addOption0(
                new Option(0, "o", "option", "Turn on option with argument.", true, null));
        final CommandLine line = parser.parse0(options, new String[] {"-de", "--option=foobar"});
        assertTrue("There should be an option debug in any case...", line.hasOption2("debug"));
        assertFalse(
                "There should not be an extract option because partial matching only selects debug",
                line.hasOption2("extract"));
        assertTrue(
                "There should be an option option with a argument value",
                line.hasOption2("option"));
    }
}