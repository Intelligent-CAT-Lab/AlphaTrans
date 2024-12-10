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
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import org.junit.Before;
import org.junit.Test;

import java.util.Properties;

@SuppressWarnings("deprecation") // tests some deprecated classes
public class OptionGroupTest {
    private Options options;
    private final Parser parser = new PosixParser();

    @Before
    public void setUp() {
        final Option file = new Option(0, "f", "file", "file to process", false, null);
        final Option dir = new Option(0, "d", "directory", "directory to process", false, null);
        final OptionGroup group = new OptionGroup();
        group.addOption(file);
        group.addOption(dir);
        options = new Options().addOptionGroup(group);

        final Option section = new Option(0, "s", "section", "section to process", false, null);
        final Option chapter = new Option(0, "c", "chapter", "chapter to process", false, null);
        final OptionGroup group2 = new OptionGroup();
        group2.addOption(section);
        group2.addOption(chapter);

        options.addOptionGroup(group2);

        final Option importOpt = new Option(0, null, "import", "section to process", false, null);
        final Option exportOpt = new Option(0, null, "export", "chapter to process", false, null);
        final OptionGroup group3 = new OptionGroup();
        group3.addOption(importOpt);
        group3.addOption(exportOpt);
        options.addOptionGroup(group3);

        options.addOption3("r", "revision", false, "revision number");
    }

    @Test
    public void testGetNames_test0_decomposed()  {
        final OptionGroup group = new OptionGroup();
    }

    @Test
    public void testGetNames_test1_decomposed()  {
        final OptionGroup group = new OptionGroup();
        OptionBuilder.create1('a');
    }

    @Test
    public void testGetNames_test2_decomposed()  {
        final OptionGroup group = new OptionGroup();
        OptionBuilder.create1('a');
        group.addOption(OptionBuilder.create1('a'));
    }

    @Test
    public void testGetNames_test3_decomposed()  {
        final OptionGroup group = new OptionGroup();
        OptionBuilder.create1('a');
        group.addOption(OptionBuilder.create1('a'));
        OptionBuilder.create1('b');
    }

    @Test
    public void testGetNames_test4_decomposed()  {
        final OptionGroup group = new OptionGroup();
        OptionBuilder.create1('a');
        group.addOption(OptionBuilder.create1('a'));
        OptionBuilder.create1('b');
        group.addOption(OptionBuilder.create1('b'));
    }

    @Test
    public void testGetNames_test5_decomposed()  {
        final OptionGroup group = new OptionGroup();
        OptionBuilder.create1('a');
        group.addOption(OptionBuilder.create1('a'));
        OptionBuilder.create1('b');
        group.addOption(OptionBuilder.create1('b'));
        assertNotNull("null names", group.getNames());
        assertEquals(2, group.getNames().size());
        assertTrue(group.getNames().contains("a"));
        assertTrue(group.getNames().contains("b"));
    }

    @Test
    public void testNoOptionsExtraArgs_test0_decomposed() throws Exception {
        final String[] args = {"arg1", "arg2"};
        final CommandLine cl = parser.parse0(options, args);
    }

    @Test
    public void testNoOptionsExtraArgs_test1_decomposed() throws Exception {
        final String[] args = {"arg1", "arg2"};
        final CommandLine cl = parser.parse0(options, args);
        assertFalse("Confirm -r is NOT set", cl.hasOption2("r"));
        assertFalse("Confirm -f is NOT set", cl.hasOption2("f"));
        assertFalse("Confirm -d is NOT set", cl.hasOption2("d"));
        assertFalse("Confirm -s is NOT set", cl.hasOption2("s"));
        assertFalse("Confirm -c is NOT set", cl.hasOption2("c"));
    }

    @Test
    public void testNoOptionsExtraArgs_test2_decomposed() throws Exception {
        final String[] args = {"arg1", "arg2"};
        final CommandLine cl = parser.parse0(options, args);
        assertFalse("Confirm -r is NOT set", cl.hasOption2("r"));
        assertFalse("Confirm -f is NOT set", cl.hasOption2("f"));
        assertFalse("Confirm -d is NOT set", cl.hasOption2("d"));
        assertFalse("Confirm -s is NOT set", cl.hasOption2("s"));
        assertFalse("Confirm -c is NOT set", cl.hasOption2("c"));
        assertEquals("Confirm TWO extra args", 2, cl.getArgList().size());
    }

    @Test
    public void testSingleLongOption_test0_decomposed() throws Exception {
        final String[] args = {"--file"};
        final CommandLine cl = parser.parse0(options, args);
    }

    @Test
    public void testSingleLongOption_test1_decomposed() throws Exception {
        final String[] args = {"--file"};
        final CommandLine cl = parser.parse0(options, args);
        assertFalse("Confirm -r is NOT set", cl.hasOption2("r"));
        assertTrue("Confirm -f is set", cl.hasOption2("f"));
        assertFalse("Confirm -d is NOT set", cl.hasOption2("d"));
        assertFalse("Confirm -s is NOT set", cl.hasOption2("s"));
        assertFalse("Confirm -c is NOT set", cl.hasOption2("c"));
    }

    @Test
    public void testSingleLongOption_test2_decomposed() throws Exception {
        final String[] args = {"--file"};
        final CommandLine cl = parser.parse0(options, args);
        assertFalse("Confirm -r is NOT set", cl.hasOption2("r"));
        assertTrue("Confirm -f is set", cl.hasOption2("f"));
        assertFalse("Confirm -d is NOT set", cl.hasOption2("d"));
        assertFalse("Confirm -s is NOT set", cl.hasOption2("s"));
        assertFalse("Confirm -c is NOT set", cl.hasOption2("c"));
        assertTrue("Confirm no extra args", cl.getArgList().isEmpty());
    }

    @Test
    public void testSingleOption_test0_decomposed() throws Exception {
        final String[] args = {"-r"};
        final CommandLine cl = parser.parse0(options, args);
    }

    @Test
    public void testSingleOption_test1_decomposed() throws Exception {
        final String[] args = {"-r"};
        final CommandLine cl = parser.parse0(options, args);
        assertTrue("Confirm -r is set", cl.hasOption2("r"));
        assertFalse("Confirm -f is NOT set", cl.hasOption2("f"));
        assertFalse("Confirm -d is NOT set", cl.hasOption2("d"));
        assertFalse("Confirm -s is NOT set", cl.hasOption2("s"));
        assertFalse("Confirm -c is NOT set", cl.hasOption2("c"));
    }

    @Test
    public void testSingleOption_test2_decomposed() throws Exception {
        final String[] args = {"-r"};
        final CommandLine cl = parser.parse0(options, args);
        assertTrue("Confirm -r is set", cl.hasOption2("r"));
        assertFalse("Confirm -f is NOT set", cl.hasOption2("f"));
        assertFalse("Confirm -d is NOT set", cl.hasOption2("d"));
        assertFalse("Confirm -s is NOT set", cl.hasOption2("s"));
        assertFalse("Confirm -c is NOT set", cl.hasOption2("c"));
        assertTrue("Confirm no extra args", cl.getArgList().isEmpty());
    }

    @Test
    public void testSingleOptionFromGroup_test0_decomposed() throws Exception {
        final String[] args = {"-f"};
        final CommandLine cl = parser.parse0(options, args);
    }

    @Test
    public void testSingleOptionFromGroup_test1_decomposed() throws Exception {
        final String[] args = {"-f"};
        final CommandLine cl = parser.parse0(options, args);
        assertFalse("Confirm -r is NOT set", cl.hasOption2("r"));
        assertTrue("Confirm -f is set", cl.hasOption2("f"));
        assertFalse("Confirm -d is NOT set", cl.hasOption2("d"));
        assertFalse("Confirm -s is NOT set", cl.hasOption2("s"));
        assertFalse("Confirm -c is NOT set", cl.hasOption2("c"));
    }

    @Test
    public void testSingleOptionFromGroup_test2_decomposed() throws Exception {
        final String[] args = {"-f"};
        final CommandLine cl = parser.parse0(options, args);
        assertFalse("Confirm -r is NOT set", cl.hasOption2("r"));
        assertTrue("Confirm -f is set", cl.hasOption2("f"));
        assertFalse("Confirm -d is NOT set", cl.hasOption2("d"));
        assertFalse("Confirm -s is NOT set", cl.hasOption2("s"));
        assertFalse("Confirm -c is NOT set", cl.hasOption2("c"));
        assertTrue("Confirm no extra args", cl.getArgList().isEmpty());
    }

    @Test
    public void testToString_test0_decomposed()  {
        final OptionGroup group1 = new OptionGroup();
    }

    @Test
    public void testToString_test1_decomposed()  {
        final OptionGroup group1 = new OptionGroup();
        group1.addOption(new Option(0, null, "foo", "Foo", false, null));
    }

    @Test
    public void testToString_test2_decomposed()  {
        final OptionGroup group1 = new OptionGroup();
        group1.addOption(new Option(0, null, "foo", "Foo", false, null));
        group1.addOption(new Option(0, null, "bar", "Bar", false, null));
    }

    @Test
    public void testToString_test3_decomposed()  {
        final OptionGroup group1 = new OptionGroup();
        group1.addOption(new Option(0, null, "foo", "Foo", false, null));
        group1.addOption(new Option(0, null, "bar", "Bar", false, null));
        if (!"[--bar Bar, --foo Foo]".equals(group1.toString())) {
            assertEquals("[--foo Foo, --bar Bar]", group1.toString());
        }
    }

    @Test
    public void testToString_test4_decomposed()  {
        final OptionGroup group1 = new OptionGroup();
        group1.addOption(new Option(0, null, "foo", "Foo", false, null));
        group1.addOption(new Option(0, null, "bar", "Bar", false, null));
        if (!"[--bar Bar, --foo Foo]".equals(group1.toString())) {
            assertEquals("[--foo Foo, --bar Bar]", group1.toString());
        }
        final OptionGroup group2 = new OptionGroup();
    }

    @Test
    public void testToString_test5_decomposed()  {
        final OptionGroup group1 = new OptionGroup();
        group1.addOption(new Option(0, null, "foo", "Foo", false, null));
        group1.addOption(new Option(0, null, "bar", "Bar", false, null));
        if (!"[--bar Bar, --foo Foo]".equals(group1.toString())) {
            assertEquals("[--foo Foo, --bar Bar]", group1.toString());
        }
        final OptionGroup group2 = new OptionGroup();
        group2.addOption(new Option(0, "f", "foo", "Foo", false, null));
    }

    @Test
    public void testToString_test6_decomposed()  {
        final OptionGroup group1 = new OptionGroup();
        group1.addOption(new Option(0, null, "foo", "Foo", false, null));
        group1.addOption(new Option(0, null, "bar", "Bar", false, null));
        if (!"[--bar Bar, --foo Foo]".equals(group1.toString())) {
            assertEquals("[--foo Foo, --bar Bar]", group1.toString());
        }
        final OptionGroup group2 = new OptionGroup();
        group2.addOption(new Option(0, "f", "foo", "Foo", false, null));
        group2.addOption(new Option(0, "b", "bar", "Bar", false, null));
    }

    @Test
    public void testToString_test7_decomposed()  {
        final OptionGroup group1 = new OptionGroup();
        group1.addOption(new Option(0, null, "foo", "Foo", false, null));
        group1.addOption(new Option(0, null, "bar", "Bar", false, null));
        if (!"[--bar Bar, --foo Foo]".equals(group1.toString())) {
            assertEquals("[--foo Foo, --bar Bar]", group1.toString());
        }
        final OptionGroup group2 = new OptionGroup();
        group2.addOption(new Option(0, "f", "foo", "Foo", false, null));
        group2.addOption(new Option(0, "b", "bar", "Bar", false, null));
        if (!"[-b Bar, -f Foo]".equals(group2.toString())) {
            assertEquals("[-f Foo, -b Bar]", group2.toString());
        }
    }

    @Test
    public void testTwoLongOptionsFromGroup_test0_decomposed() throws Exception {
        final String[] args = {"--file", "--directory"};
        try {
            parser.parse0(options, args);
            fail("two arguments from group not allowed");
        } catch (final AlreadySelectedException e) {
            assertNotNull("null option group", e.getOptionGroup());
            assertEquals("selected option", "f", e.getOptionGroup().getSelected());
            assertEquals("option", "d", e.getOption().getOpt());
        }
    }

    @Test
    public void testTwoOptionsFromDifferentGroup_test0_decomposed() throws Exception {
        final String[] args = {"-f", "-s"};
        final CommandLine cl = parser.parse0(options, args);
    }

    @Test
    public void testTwoOptionsFromDifferentGroup_test1_decomposed() throws Exception {
        final String[] args = {"-f", "-s"};
        final CommandLine cl = parser.parse0(options, args);
        assertFalse("Confirm -r is NOT set", cl.hasOption2("r"));
        assertTrue("Confirm -f is set", cl.hasOption2("f"));
        assertFalse("Confirm -d is NOT set", cl.hasOption2("d"));
        assertTrue("Confirm -s is set", cl.hasOption2("s"));
        assertFalse("Confirm -c is NOT set", cl.hasOption2("c"));
    }

    @Test
    public void testTwoOptionsFromDifferentGroup_test2_decomposed() throws Exception {
        final String[] args = {"-f", "-s"};
        final CommandLine cl = parser.parse0(options, args);
        assertFalse("Confirm -r is NOT set", cl.hasOption2("r"));
        assertTrue("Confirm -f is set", cl.hasOption2("f"));
        assertFalse("Confirm -d is NOT set", cl.hasOption2("d"));
        assertTrue("Confirm -s is set", cl.hasOption2("s"));
        assertFalse("Confirm -c is NOT set", cl.hasOption2("c"));
        assertTrue("Confirm NO extra args", cl.getArgList().isEmpty());
    }

    @Test
    public void testTwoOptionsFromGroup_test0_decomposed() throws Exception {
        final String[] args = {"-f", "-d"};
        try {
            parser.parse0(options, args);
            fail("two arguments from group not allowed");
        } catch (final AlreadySelectedException e) {
            assertNotNull("null option group", e.getOptionGroup());
            assertEquals("selected option", "f", e.getOptionGroup().getSelected());
            assertEquals("option", "d", e.getOption().getOpt());
        }
    }

    @Test
    public void testTwoOptionsFromGroupWithProperties_test0_decomposed() throws Exception {
        final String[] args = {"-f"};
        final Properties properties = new Properties();
        properties.put("d", "true");
        final CommandLine cl = parser.parse2(options, args, properties);
    }

    @Test
    public void testTwoOptionsFromGroupWithProperties_test1_decomposed() throws Exception {
        final String[] args = {"-f"};
        final Properties properties = new Properties();
        properties.put("d", "true");
        final CommandLine cl = parser.parse2(options, args, properties);
        assertTrue(cl.hasOption2("f"));
        assertFalse(cl.hasOption2("d"));
    }

    @Test
    public void testTwoValidLongOptions_test0_decomposed() throws Exception {
        final String[] args = {"--revision", "--file"};
        final CommandLine cl = parser.parse0(options, args);
    }

    @Test
    public void testTwoValidLongOptions_test1_decomposed() throws Exception {
        final String[] args = {"--revision", "--file"};
        final CommandLine cl = parser.parse0(options, args);
        assertTrue("Confirm -r is set", cl.hasOption2("r"));
        assertTrue("Confirm -f is set", cl.hasOption2("f"));
        assertFalse("Confirm -d is NOT set", cl.hasOption2("d"));
        assertFalse("Confirm -s is NOT set", cl.hasOption2("s"));
        assertFalse("Confirm -c is NOT set", cl.hasOption2("c"));
    }

    @Test
    public void testTwoValidLongOptions_test2_decomposed() throws Exception {
        final String[] args = {"--revision", "--file"};
        final CommandLine cl = parser.parse0(options, args);
        assertTrue("Confirm -r is set", cl.hasOption2("r"));
        assertTrue("Confirm -f is set", cl.hasOption2("f"));
        assertFalse("Confirm -d is NOT set", cl.hasOption2("d"));
        assertFalse("Confirm -s is NOT set", cl.hasOption2("s"));
        assertFalse("Confirm -c is NOT set", cl.hasOption2("c"));
        assertTrue("Confirm no extra args", cl.getArgList().isEmpty());
    }

    @Test
    public void testTwoValidOptions_test0_decomposed() throws Exception {
        final String[] args = {"-r", "-f"};
        final CommandLine cl = parser.parse0(options, args);
    }

    @Test
    public void testTwoValidOptions_test1_decomposed() throws Exception {
        final String[] args = {"-r", "-f"};
        final CommandLine cl = parser.parse0(options, args);
        assertTrue("Confirm -r is set", cl.hasOption2("r"));
        assertTrue("Confirm -f is set", cl.hasOption2("f"));
        assertFalse("Confirm -d is NOT set", cl.hasOption2("d"));
        assertFalse("Confirm -s is NOT set", cl.hasOption2("s"));
        assertFalse("Confirm -c is NOT set", cl.hasOption2("c"));
    }

    @Test
    public void testTwoValidOptions_test2_decomposed() throws Exception {
        final String[] args = {"-r", "-f"};
        final CommandLine cl = parser.parse0(options, args);
        assertTrue("Confirm -r is set", cl.hasOption2("r"));
        assertTrue("Confirm -f is set", cl.hasOption2("f"));
        assertFalse("Confirm -d is NOT set", cl.hasOption2("d"));
        assertFalse("Confirm -s is NOT set", cl.hasOption2("s"));
        assertFalse("Confirm -c is NOT set", cl.hasOption2("c"));
        assertTrue("Confirm no extra args", cl.getArgList().isEmpty());
    }

    @Test
    public void testValidLongOnlyOptions_test0_decomposed() throws Exception {
        final CommandLine cl1 = parser.parse0(options, new String[] {"--export"});
    }

    @Test
    public void testValidLongOnlyOptions_test1_decomposed() throws Exception {
        final CommandLine cl1 = parser.parse0(options, new String[] {"--export"});
        assertTrue("Confirm --export is set", cl1.hasOption2("export"));
    }

    @Test
    public void testValidLongOnlyOptions_test2_decomposed() throws Exception {
        final CommandLine cl1 = parser.parse0(options, new String[] {"--export"});
        assertTrue("Confirm --export is set", cl1.hasOption2("export"));
        final CommandLine cl2 = parser.parse0(options, new String[] {"--import"});
    }

    @Test
    public void testValidLongOnlyOptions_test3_decomposed() throws Exception {
        final CommandLine cl1 = parser.parse0(options, new String[] {"--export"});
        assertTrue("Confirm --export is set", cl1.hasOption2("export"));
        final CommandLine cl2 = parser.parse0(options, new String[] {"--import"});
        assertTrue("Confirm --import is set", cl2.hasOption2("import"));
    }
}