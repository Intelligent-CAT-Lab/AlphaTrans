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
    public void testDuplicateLong() {
        final Options opts = new Options();
        opts.addOption3("a", "--a", false, "toggle -a");
        opts.addOption3("a", "--a", false, "toggle -a*");
        assertEquals("last one in wins", "toggle -a*", opts.getOption("a").getDescription());
    }

    @Test
    public void testDuplicateSimple() {
        final Options opts = new Options();
        opts.addOption1("a", false, "toggle -a");
        opts.addOption1("a", true, "toggle -a*");

        assertEquals("last one in wins", "toggle -a*", opts.getOption("a").getDescription());
    }

    @Test
    public void testGetMatchingOpts() {
        final Options options = new Options();
        options.addOption0(OptionBuilder.withLongOpt("version").create0());
        options.addOption0(OptionBuilder.withLongOpt("verbose").create0());

        assertTrue(options.getMatchingOptions("foo").isEmpty());
        assertEquals(1, options.getMatchingOptions("version").size());
        assertEquals(2, options.getMatchingOptions("ver").size());
    }

    @Test
    public void testGetOptionsGroups() {
        final Options options = new Options();

        final OptionGroup group1 = new OptionGroup();
        group1.addOption(OptionBuilder.create1('a'));
        group1.addOption(OptionBuilder.create1('b'));

        final OptionGroup group2 = new OptionGroup();
        group2.addOption(OptionBuilder.create1('x'));
        group2.addOption(OptionBuilder.create1('y'));

        options.addOptionGroup(group1);
        options.addOptionGroup(group2);

        assertNotNull(options.getOptionGroups());
        assertEquals(2, options.getOptionGroups().size());
    }

    @Test
    public void testHelpOptions() {
        final Option longOnly1 = OptionBuilder.withLongOpt("long-only1").create0();
        final Option longOnly2 = OptionBuilder.withLongOpt("long-only2").create0();
        final Option shortOnly1 = OptionBuilder.create2("1");
        final Option shortOnly2 = OptionBuilder.create2("2");
        final Option bothA = OptionBuilder.withLongOpt("bothA").create2("a");
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
    public void testLong() {
        final Options opts = new Options();

        opts.addOption3("a", "--a", false, "toggle -a");
        opts.addOption3("b", "--b", true, "set -b");

        assertTrue(opts.hasOption("a"));
        assertTrue(opts.hasOption("b"));
    }

    @Test
    public void testMissingOptionException() throws ParseException {
        final Options options = new Options();
        options.addOption0(OptionBuilder.isRequired0().create2("f"));
        try {
            new PosixParser().parse0(options, new String[0]);
            fail("Expected MissingOptionException to be thrown");
        } catch (final MissingOptionException e) {
            assertEquals("Missing required option: f", e.getMessage());
        }
    }

    @Test
    public void testMissingOptionsException() throws ParseException {
        final Options options = new Options();
        options.addOption0(OptionBuilder.isRequired0().create2("f"));
        options.addOption0(OptionBuilder.isRequired0().create2("x"));
        try {
            new PosixParser().parse0(options, new String[0]);
            fail("Expected MissingOptionException to be thrown");
        } catch (final MissingOptionException e) {
            assertEquals("Missing required options: f, x", e.getMessage());
        }
    }

    @Test
    public void testSimple() {
        final Options opts = new Options();

        opts.addOption1("a", false, "toggle -a");
        opts.addOption1("b", true, "toggle -b");

        assertTrue(opts.hasOption("a"));
        assertTrue(opts.hasOption("b"));
    }

    @Test
    public void testToString() {
        final Options options = new Options();
        options.addOption3("f", "foo", true, "Foo");
        options.addOption3("b", "bar", false, "Bar");

        final String s = options.toString();
        assertNotNull("null string returned", s);
        assertTrue("foo option missing", s.toLowerCase().contains("foo"));
        assertTrue("bar option missing", s.toLowerCase().contains("bar"));
    }
}
