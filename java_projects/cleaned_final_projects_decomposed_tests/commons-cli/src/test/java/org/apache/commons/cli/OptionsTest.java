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
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import org.junit.Test;

import java.util.ArrayList;
import java.util.Collection;

@SuppressWarnings("deprecation") // tests some deprecated classes
public class OptionsTest {

    @Test
    public void testDuplicateLong_test0_decomposed()  {
        final Options opts = new Options();
    }

    @Test
    public void testDuplicateLong_test1_decomposed()  {
        final Options opts = new Options();
        opts.addOption3("a", "--a", false, "toggle -a");
        opts.addOption3("a", "--a", false, "toggle -a*");
    }

    @Test
    public void testDuplicateLong_test2_decomposed()  {
        final Options opts = new Options();
        opts.addOption3("a", "--a", false, "toggle -a");
        opts.addOption3("a", "--a", false, "toggle -a*");
        opts.getOption("a");
    }

    @Test
    public void testDuplicateLong_test3_decomposed()  {
        final Options opts = new Options();
        opts.addOption3("a", "--a", false, "toggle -a");
        opts.addOption3("a", "--a", false, "toggle -a*");
        opts.getOption("a");
        assertEquals("last one in wins", "toggle -a*", opts.getOption("a").getDescription());
    }

    @Test
    public void testDuplicateSimple_test0_decomposed()  {
        final Options opts = new Options();
    }

    @Test
    public void testDuplicateSimple_test1_decomposed()  {
        final Options opts = new Options();
        opts.addOption1("a", false, "toggle -a");
        opts.addOption1("a", true, "toggle -a*");
    }

    @Test
    public void testDuplicateSimple_test2_decomposed()  {
        final Options opts = new Options();
        opts.addOption1("a", false, "toggle -a");
        opts.addOption1("a", true, "toggle -a*");
        opts.getOption("a");
    }

    @Test
    public void testDuplicateSimple_test3_decomposed()  {
        final Options opts = new Options();
        opts.addOption1("a", false, "toggle -a");
        opts.addOption1("a", true, "toggle -a*");
        opts.getOption("a");
        assertEquals("last one in wins", "toggle -a*", opts.getOption("a").getDescription());
    }

    @Test
    public void testGetMatchingOpts_test0_decomposed()  {
        final Options options = new Options();
    }

    @Test
    public void testGetMatchingOpts_test1_decomposed()  {
        final Options options = new Options();
        OptionBuilder.withLongOpt("version");
    }

    @Test
    public void testGetMatchingOpts_test2_decomposed()  {
        final Options options = new Options();
        OptionBuilder.withLongOpt("version");
        OptionBuilder.withLongOpt("version").create0();
    }

    @Test
    public void testGetMatchingOpts_test3_decomposed()  {
        final Options options = new Options();
        OptionBuilder.withLongOpt("version");
        OptionBuilder.withLongOpt("version").create0();
        options.addOption0(OptionBuilder.withLongOpt("version").create0());
    }

    @Test
    public void testGetMatchingOpts_test4_decomposed()  {
        final Options options = new Options();
        OptionBuilder.withLongOpt("version");
        OptionBuilder.withLongOpt("version").create0();
        options.addOption0(OptionBuilder.withLongOpt("version").create0());
        OptionBuilder.withLongOpt("verbose");
    }

    @Test
    public void testGetMatchingOpts_test5_decomposed()  {
        final Options options = new Options();
        OptionBuilder.withLongOpt("version");
        OptionBuilder.withLongOpt("version").create0();
        options.addOption0(OptionBuilder.withLongOpt("version").create0());
        OptionBuilder.withLongOpt("verbose");
        OptionBuilder.withLongOpt("verbose").create0();
    }

    @Test
    public void testGetMatchingOpts_test6_decomposed()  {
        final Options options = new Options();
        OptionBuilder.withLongOpt("version");
        OptionBuilder.withLongOpt("version").create0();
        options.addOption0(OptionBuilder.withLongOpt("version").create0());
        OptionBuilder.withLongOpt("verbose");
        OptionBuilder.withLongOpt("verbose").create0();
        options.addOption0(OptionBuilder.withLongOpt("verbose").create0());
    }

    @Test
    public void testGetMatchingOpts_test7_decomposed()  {
        final Options options = new Options();
        OptionBuilder.withLongOpt("version");
        OptionBuilder.withLongOpt("version").create0();
        options.addOption0(OptionBuilder.withLongOpt("version").create0());
        OptionBuilder.withLongOpt("verbose");
        OptionBuilder.withLongOpt("verbose").create0();
        options.addOption0(OptionBuilder.withLongOpt("verbose").create0());
        assertTrue(options.getMatchingOptions("foo").isEmpty());
        assertEquals(1, options.getMatchingOptions("version").size());
        assertEquals(2, options.getMatchingOptions("ver").size());
    }

    @Test
    public void testGetOptionsGroups_test0_decomposed()  {
        final Options options = new Options();
    }

    @Test
    public void testGetOptionsGroups_test1_decomposed()  {
        final Options options = new Options();
        final OptionGroup group1 = new OptionGroup();
    }

    @Test
    public void testGetOptionsGroups_test2_decomposed()  {
        final Options options = new Options();
        final OptionGroup group1 = new OptionGroup();
        OptionBuilder.create1('a');
    }

    @Test
    public void testGetOptionsGroups_test3_decomposed()  {
        final Options options = new Options();
        final OptionGroup group1 = new OptionGroup();
        OptionBuilder.create1('a');
        group1.addOption(OptionBuilder.create1('a'));
    }

    @Test
    public void testGetOptionsGroups_test4_decomposed()  {
        final Options options = new Options();
        final OptionGroup group1 = new OptionGroup();
        OptionBuilder.create1('a');
        group1.addOption(OptionBuilder.create1('a'));
        OptionBuilder.create1('b');
    }

    @Test
    public void testGetOptionsGroups_test5_decomposed()  {
        final Options options = new Options();
        final OptionGroup group1 = new OptionGroup();
        OptionBuilder.create1('a');
        group1.addOption(OptionBuilder.create1('a'));
        OptionBuilder.create1('b');
        group1.addOption(OptionBuilder.create1('b'));
    }

    @Test
    public void testGetOptionsGroups_test6_decomposed()  {
        final Options options = new Options();
        final OptionGroup group1 = new OptionGroup();
        OptionBuilder.create1('a');
        group1.addOption(OptionBuilder.create1('a'));
        OptionBuilder.create1('b');
        group1.addOption(OptionBuilder.create1('b'));
        final OptionGroup group2 = new OptionGroup();
    }

    @Test
    public void testGetOptionsGroups_test7_decomposed()  {
        final Options options = new Options();
        final OptionGroup group1 = new OptionGroup();
        OptionBuilder.create1('a');
        group1.addOption(OptionBuilder.create1('a'));
        OptionBuilder.create1('b');
        group1.addOption(OptionBuilder.create1('b'));
        final OptionGroup group2 = new OptionGroup();
        OptionBuilder.create1('x');
    }

    @Test
    public void testGetOptionsGroups_test8_decomposed()  {
        final Options options = new Options();
        final OptionGroup group1 = new OptionGroup();
        OptionBuilder.create1('a');
        group1.addOption(OptionBuilder.create1('a'));
        OptionBuilder.create1('b');
        group1.addOption(OptionBuilder.create1('b'));
        final OptionGroup group2 = new OptionGroup();
        OptionBuilder.create1('x');
        group2.addOption(OptionBuilder.create1('x'));
    }

    @Test
    public void testGetOptionsGroups_test9_decomposed()  {
        final Options options = new Options();
        final OptionGroup group1 = new OptionGroup();
        OptionBuilder.create1('a');
        group1.addOption(OptionBuilder.create1('a'));
        OptionBuilder.create1('b');
        group1.addOption(OptionBuilder.create1('b'));
        final OptionGroup group2 = new OptionGroup();
        OptionBuilder.create1('x');
        group2.addOption(OptionBuilder.create1('x'));
        OptionBuilder.create1('y');
    }

    @Test
    public void testGetOptionsGroups_test10_decomposed()  {
        final Options options = new Options();
        final OptionGroup group1 = new OptionGroup();
        OptionBuilder.create1('a');
        group1.addOption(OptionBuilder.create1('a'));
        OptionBuilder.create1('b');
        group1.addOption(OptionBuilder.create1('b'));
        final OptionGroup group2 = new OptionGroup();
        OptionBuilder.create1('x');
        group2.addOption(OptionBuilder.create1('x'));
        OptionBuilder.create1('y');
        group2.addOption(OptionBuilder.create1('y'));
    }

    @Test
    public void testGetOptionsGroups_test11_decomposed()  {
        final Options options = new Options();
        final OptionGroup group1 = new OptionGroup();
        OptionBuilder.create1('a');
        group1.addOption(OptionBuilder.create1('a'));
        OptionBuilder.create1('b');
        group1.addOption(OptionBuilder.create1('b'));
        final OptionGroup group2 = new OptionGroup();
        OptionBuilder.create1('x');
        group2.addOption(OptionBuilder.create1('x'));
        OptionBuilder.create1('y');
        group2.addOption(OptionBuilder.create1('y'));
        options.addOptionGroup(group1);
        options.addOptionGroup(group2);
    }

    @Test
    public void testGetOptionsGroups_test12_decomposed()  {
        final Options options = new Options();
        final OptionGroup group1 = new OptionGroup();
        OptionBuilder.create1('a');
        group1.addOption(OptionBuilder.create1('a'));
        OptionBuilder.create1('b');
        group1.addOption(OptionBuilder.create1('b'));
        final OptionGroup group2 = new OptionGroup();
        OptionBuilder.create1('x');
        group2.addOption(OptionBuilder.create1('x'));
        OptionBuilder.create1('y');
        group2.addOption(OptionBuilder.create1('y'));
        options.addOptionGroup(group1);
        options.addOptionGroup(group2);
        assertNotNull(options.getOptionGroups());
        assertEquals(2, options.getOptionGroups().size());
    }

    @Test
    public void testHelpOptions_test0_decomposed()  {
        OptionBuilder.withLongOpt("long-only1");
    }

    @Test
    public void testHelpOptions_test1_decomposed()  {
        OptionBuilder.withLongOpt("long-only1");
        final Option longOnly1 = OptionBuilder.withLongOpt("long-only1").create0();
    }

    @Test
    public void testHelpOptions_test2_decomposed()  {
        OptionBuilder.withLongOpt("long-only1");
        final Option longOnly1 = OptionBuilder.withLongOpt("long-only1").create0();
        OptionBuilder.withLongOpt("long-only2");
    }

    @Test
    public void testHelpOptions_test3_decomposed()  {
        OptionBuilder.withLongOpt("long-only1");
        final Option longOnly1 = OptionBuilder.withLongOpt("long-only1").create0();
        OptionBuilder.withLongOpt("long-only2");
        final Option longOnly2 = OptionBuilder.withLongOpt("long-only2").create0();
    }

    @Test
    public void testHelpOptions_test4_decomposed()  {
        OptionBuilder.withLongOpt("long-only1");
        final Option longOnly1 = OptionBuilder.withLongOpt("long-only1").create0();
        OptionBuilder.withLongOpt("long-only2");
        final Option longOnly2 = OptionBuilder.withLongOpt("long-only2").create0();
        final Option shortOnly1 = OptionBuilder.create2("1");
        final Option shortOnly2 = OptionBuilder.create2("2");
    }

    @Test
    public void testHelpOptions_test5_decomposed()  {
        OptionBuilder.withLongOpt("long-only1");
        final Option longOnly1 = OptionBuilder.withLongOpt("long-only1").create0();
        OptionBuilder.withLongOpt("long-only2");
        final Option longOnly2 = OptionBuilder.withLongOpt("long-only2").create0();
        final Option shortOnly1 = OptionBuilder.create2("1");
        final Option shortOnly2 = OptionBuilder.create2("2");
        OptionBuilder.withLongOpt("bothA");
    }

    @Test
    public void testHelpOptions_test6_decomposed()  {
        OptionBuilder.withLongOpt("long-only1");
        final Option longOnly1 = OptionBuilder.withLongOpt("long-only1").create0();
        OptionBuilder.withLongOpt("long-only2");
        final Option longOnly2 = OptionBuilder.withLongOpt("long-only2").create0();
        final Option shortOnly1 = OptionBuilder.create2("1");
        final Option shortOnly2 = OptionBuilder.create2("2");
        OptionBuilder.withLongOpt("bothA");
        final Option bothA = OptionBuilder.withLongOpt("bothA").create2("a");
    }

    @Test
    public void testHelpOptions_test7_decomposed()  {
        OptionBuilder.withLongOpt("long-only1");
        final Option longOnly1 = OptionBuilder.withLongOpt("long-only1").create0();
        OptionBuilder.withLongOpt("long-only2");
        final Option longOnly2 = OptionBuilder.withLongOpt("long-only2").create0();
        final Option shortOnly1 = OptionBuilder.create2("1");
        final Option shortOnly2 = OptionBuilder.create2("2");
        OptionBuilder.withLongOpt("bothA");
        final Option bothA = OptionBuilder.withLongOpt("bothA").create2("a");
        OptionBuilder.withLongOpt("bothB");
    }

    @Test
    public void testHelpOptions_test8_decomposed()  {
        OptionBuilder.withLongOpt("long-only1");
        final Option longOnly1 = OptionBuilder.withLongOpt("long-only1").create0();
        OptionBuilder.withLongOpt("long-only2");
        final Option longOnly2 = OptionBuilder.withLongOpt("long-only2").create0();
        final Option shortOnly1 = OptionBuilder.create2("1");
        final Option shortOnly2 = OptionBuilder.create2("2");
        OptionBuilder.withLongOpt("bothA");
        final Option bothA = OptionBuilder.withLongOpt("bothA").create2("a");
        OptionBuilder.withLongOpt("bothB");
        final Option bothB = OptionBuilder.withLongOpt("bothB").create2("b");
    }

    @Test
    public void testHelpOptions_test9_decomposed()  {
        OptionBuilder.withLongOpt("long-only1");
        final Option longOnly1 = OptionBuilder.withLongOpt("long-only1").create0();
        OptionBuilder.withLongOpt("long-only2");
        final Option longOnly2 = OptionBuilder.withLongOpt("long-only2").create0();
        final Option shortOnly1 = OptionBuilder.create2("1");
        final Option shortOnly2 = OptionBuilder.create2("2");
        OptionBuilder.withLongOpt("bothA");
        final Option bothA = OptionBuilder.withLongOpt("bothA").create2("a");
        OptionBuilder.withLongOpt("bothB");
        final Option bothB = OptionBuilder.withLongOpt("bothB").create2("b");
        final Options options = new Options();
    }

    @Test
    public void testHelpOptions_test10_decomposed()  {
        OptionBuilder.withLongOpt("long-only1");
        final Option longOnly1 = OptionBuilder.withLongOpt("long-only1").create0();
        OptionBuilder.withLongOpt("long-only2");
        final Option longOnly2 = OptionBuilder.withLongOpt("long-only2").create0();
        final Option shortOnly1 = OptionBuilder.create2("1");
        final Option shortOnly2 = OptionBuilder.create2("2");
        OptionBuilder.withLongOpt("bothA");
        final Option bothA = OptionBuilder.withLongOpt("bothA").create2("a");
        OptionBuilder.withLongOpt("bothB");
        final Option bothB = OptionBuilder.withLongOpt("bothB").create2("b");
        final Options options = new Options();
        options.addOption0(longOnly1);
        options.addOption0(longOnly2);
        options.addOption0(shortOnly1);
        options.addOption0(shortOnly2);
        options.addOption0(bothA);
        options.addOption0(bothB);
    }

    @Test
    public void testHelpOptions_test11_decomposed()  {
        OptionBuilder.withLongOpt("long-only1");
        final Option longOnly1 = OptionBuilder.withLongOpt("long-only1").create0();
        OptionBuilder.withLongOpt("long-only2");
        final Option longOnly2 = OptionBuilder.withLongOpt("long-only2").create0();
        final Option shortOnly1 = OptionBuilder.create2("1");
        final Option shortOnly2 = OptionBuilder.create2("2");
        OptionBuilder.withLongOpt("bothA");
        final Option bothA = OptionBuilder.withLongOpt("bothA").create2("a");
        OptionBuilder.withLongOpt("bothB");
        final Option bothB = OptionBuilder.withLongOpt("bothB").create2("b");
        final Options options = new Options();
        options.addOption0(longOnly1);
        options.addOption0(longOnly2);
        options.addOption0(shortOnly1);
        options.addOption0(shortOnly2);
        options.addOption0(bothA);
        options.addOption0(bothB);
        final Collection<Option> allOptions = new ArrayList<>();
        allOptions.add(longOnly1);
    }

    @Test
    public void testHelpOptions_test12_decomposed()  {
        OptionBuilder.withLongOpt("long-only1");
        final Option longOnly1 = OptionBuilder.withLongOpt("long-only1").create0();
        OptionBuilder.withLongOpt("long-only2");
        final Option longOnly2 = OptionBuilder.withLongOpt("long-only2").create0();
        final Option shortOnly1 = OptionBuilder.create2("1");
        final Option shortOnly2 = OptionBuilder.create2("2");
        OptionBuilder.withLongOpt("bothA");
        final Option bothA = OptionBuilder.withLongOpt("bothA").create2("a");
        OptionBuilder.withLongOpt("bothB");
        final Option bothB = OptionBuilder.withLongOpt("bothB").create2("b");
        final Options options = new Options();
        options.addOption0(longOnly1);
        options.addOption0(longOnly2);
        options.addOption0(shortOnly1);
        options.addOption0(shortOnly2);
        options.addOption0(bothA);
        options.addOption0(bothB);
        final Collection<Option> allOptions = new ArrayList<>();
        allOptions.add(longOnly1);
        allOptions.add(longOnly2);
        allOptions.add(shortOnly1);
        allOptions.add(shortOnly2);
        allOptions.add(bothA);
        allOptions.add(bothB);
    }

    @Test
    public void testHelpOptions_test13_decomposed()  {
        OptionBuilder.withLongOpt("long-only1");
        final Option longOnly1 = OptionBuilder.withLongOpt("long-only1").create0();
        OptionBuilder.withLongOpt("long-only2");
        final Option longOnly2 = OptionBuilder.withLongOpt("long-only2").create0();
        final Option shortOnly1 = OptionBuilder.create2("1");
        final Option shortOnly2 = OptionBuilder.create2("2");
        OptionBuilder.withLongOpt("bothA");
        final Option bothA = OptionBuilder.withLongOpt("bothA").create2("a");
        OptionBuilder.withLongOpt("bothB");
        final Option bothB = OptionBuilder.withLongOpt("bothB").create2("b");
        final Options options = new Options();
        options.addOption0(longOnly1);
        options.addOption0(longOnly2);
        options.addOption0(shortOnly1);
        options.addOption0(shortOnly2);
        options.addOption0(bothA);
        options.addOption0(bothB);
        final Collection<Option> allOptions = new ArrayList<>();
        allOptions.add(longOnly1);
        allOptions.add(longOnly2);
        allOptions.add(shortOnly1);
        allOptions.add(shortOnly2);
        allOptions.add(bothA);
        allOptions.add(bothB);
        final Collection<Option> helpOptions = options.helpOptions();
    }

    @Test
    public void testHelpOptions_test14_decomposed()  {
        OptionBuilder.withLongOpt("long-only1");
        final Option longOnly1 = OptionBuilder.withLongOpt("long-only1").create0();
        OptionBuilder.withLongOpt("long-only2");
        final Option longOnly2 = OptionBuilder.withLongOpt("long-only2").create0();
        final Option shortOnly1 = OptionBuilder.create2("1");
        final Option shortOnly2 = OptionBuilder.create2("2");
        OptionBuilder.withLongOpt("bothA");
        final Option bothA = OptionBuilder.withLongOpt("bothA").create2("a");
        OptionBuilder.withLongOpt("bothB");
        final Option bothB = OptionBuilder.withLongOpt("bothB").create2("b");
        final Options options = new Options();
        options.addOption0(longOnly1);
        options.addOption0(longOnly2);
        options.addOption0(shortOnly1);
        options.addOption0(shortOnly2);
        options.addOption0(bothA);
        options.addOption0(bothB);
        final Collection<Option> allOptions = new ArrayList<>();
        allOptions.add(longOnly1);
        allOptions.add(longOnly2);
        allOptions.add(shortOnly1);
        allOptions.add(shortOnly2);
        allOptions.add(bothA);
        allOptions.add(bothB);
        final Collection<Option> helpOptions = options.helpOptions();
        assertTrue("Everything in all should be in help", helpOptions.containsAll(allOptions));
        assertTrue("Everything in help should be in all", allOptions.containsAll(helpOptions));
    }

    @Test
    public void testLong_test0_decomposed()  {
        final Options opts = new Options();
    }

    @Test
    public void testLong_test1_decomposed()  {
        final Options opts = new Options();
        opts.addOption3("a", "--a", false, "toggle -a");
        opts.addOption3("b", "--b", true, "set -b");
    }

    @Test
    public void testLong_test2_decomposed()  {
        final Options opts = new Options();
        opts.addOption3("a", "--a", false, "toggle -a");
        opts.addOption3("b", "--b", true, "set -b");
        assertTrue(opts.hasOption("a"));
        assertTrue(opts.hasOption("b"));
    }

    @Test
    public void testMissingOptionException_test0_decomposed() throws ParseException {
        final Options options = new Options();
    }

    @Test
    public void testMissingOptionException_test1_decomposed() throws ParseException {
        final Options options = new Options();
        OptionBuilder.isRequired0();
    }

    @Test
    public void testMissingOptionException_test2_decomposed() throws ParseException {
        final Options options = new Options();
        OptionBuilder.isRequired0();
        OptionBuilder.isRequired0().create2("f");
    }

    @Test
    public void testMissingOptionException_test3_decomposed() throws ParseException {
        final Options options = new Options();
        OptionBuilder.isRequired0();
        OptionBuilder.isRequired0().create2("f");
        options.addOption0(OptionBuilder.isRequired0().create2("f"));
    }

    @Test
    public void testMissingOptionException_test4_decomposed() throws ParseException {
        final Options options = new Options();
        OptionBuilder.isRequired0();
        OptionBuilder.isRequired0().create2("f");
        options.addOption0(OptionBuilder.isRequired0().create2("f"));
        try {
            new PosixParser().parse0(options, new String[0]);
            fail("Expected MissingOptionException to be thrown");
        } catch (final MissingOptionException e) {
            assertEquals("Missing required option: f", e.getMessage());
        }
    }

    @Test
    public void testMissingOptionsException_test0_decomposed() throws ParseException {
        final Options options = new Options();
    }

    @Test
    public void testMissingOptionsException_test1_decomposed() throws ParseException {
        final Options options = new Options();
        OptionBuilder.isRequired0();
    }

    @Test
    public void testMissingOptionsException_test2_decomposed() throws ParseException {
        final Options options = new Options();
        OptionBuilder.isRequired0();
        OptionBuilder.isRequired0().create2("f");
    }

    @Test
    public void testMissingOptionsException_test3_decomposed() throws ParseException {
        final Options options = new Options();
        OptionBuilder.isRequired0();
        OptionBuilder.isRequired0().create2("f");
        options.addOption0(OptionBuilder.isRequired0().create2("f"));
    }

    @Test
    public void testMissingOptionsException_test4_decomposed() throws ParseException {
        final Options options = new Options();
        OptionBuilder.isRequired0();
        OptionBuilder.isRequired0().create2("f");
        options.addOption0(OptionBuilder.isRequired0().create2("f"));
        OptionBuilder.isRequired0();
    }

    @Test
    public void testMissingOptionsException_test5_decomposed() throws ParseException {
        final Options options = new Options();
        OptionBuilder.isRequired0();
        OptionBuilder.isRequired0().create2("f");
        options.addOption0(OptionBuilder.isRequired0().create2("f"));
        OptionBuilder.isRequired0();
        OptionBuilder.isRequired0().create2("x");
    }

    @Test
    public void testMissingOptionsException_test6_decomposed() throws ParseException {
        final Options options = new Options();
        OptionBuilder.isRequired0();
        OptionBuilder.isRequired0().create2("f");
        options.addOption0(OptionBuilder.isRequired0().create2("f"));
        OptionBuilder.isRequired0();
        OptionBuilder.isRequired0().create2("x");
        options.addOption0(OptionBuilder.isRequired0().create2("x"));
    }

    @Test
    public void testMissingOptionsException_test7_decomposed() throws ParseException {
        final Options options = new Options();
        OptionBuilder.isRequired0();
        OptionBuilder.isRequired0().create2("f");
        options.addOption0(OptionBuilder.isRequired0().create2("f"));
        OptionBuilder.isRequired0();
        OptionBuilder.isRequired0().create2("x");
        options.addOption0(OptionBuilder.isRequired0().create2("x"));
        try {
            new PosixParser().parse0(options, new String[0]);
            fail("Expected MissingOptionException to be thrown");
        } catch (final MissingOptionException e) {
            assertEquals("Missing required options: f, x", e.getMessage());
        }
    }

    @Test
    public void testSimple_test0_decomposed()  {
        final Options opts = new Options();
    }

    @Test
    public void testSimple_test1_decomposed()  {
        final Options opts = new Options();
        opts.addOption1("a", false, "toggle -a");
        opts.addOption1("b", true, "toggle -b");
    }

    @Test
    public void testSimple_test2_decomposed()  {
        final Options opts = new Options();
        opts.addOption1("a", false, "toggle -a");
        opts.addOption1("b", true, "toggle -b");
        assertTrue(opts.hasOption("a"));
        assertTrue(opts.hasOption("b"));
    }

    @Test
    public void testToString_test0_decomposed()  {
        final Options options = new Options();
    }

    @Test
    public void testToString_test1_decomposed()  {
        final Options options = new Options();
        options.addOption3("f", "foo", true, "Foo");
        options.addOption3("b", "bar", false, "Bar");
    }

    @Test
    public void testToString_test2_decomposed()  {
        final Options options = new Options();
        options.addOption3("f", "foo", true, "Foo");
        options.addOption3("b", "bar", false, "Bar");
        final String s = options.toString();
    }

    @Test
    public void testToString_test3_decomposed()  {
        final Options options = new Options();
        options.addOption3("f", "foo", true, "Foo");
        options.addOption3("b", "bar", false, "Bar");
        final String s = options.toString();
        assertNotNull("null string returned", s);
        assertTrue("foo option missing", s.toLowerCase().contains("foo"));
    }

    @Test
    public void testToString_test4_decomposed()  {
        final Options options = new Options();
        options.addOption3("f", "foo", true, "Foo");
        options.addOption3("b", "bar", false, "Bar");
        final String s = options.toString();
        assertNotNull("null string returned", s);
        assertTrue("foo option missing", s.toLowerCase().contains("foo"));
        assertTrue("bar option missing", s.toLowerCase().contains("bar"));
    }
}