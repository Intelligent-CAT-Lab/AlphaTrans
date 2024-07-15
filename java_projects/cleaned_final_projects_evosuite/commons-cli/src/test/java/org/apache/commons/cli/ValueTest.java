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
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;

import org.junit.Before;
import org.junit.Test;

@SuppressWarnings("deprecation") // tests some deprecated classes
public class ValueTest {
    private CommandLine cl;
    private final Options opts = new Options();

    @Before
    public void setUp() throws Exception {
        opts.addOption1("a", false, "toggle -a");
        opts.addOption1("b", true, "set -b");
        opts.addOption3("c", "c", false, "toggle -c");
        opts.addOption3("d", "d", true, "set -d");

        opts.addOption0(OptionBuilder.hasOptionalArg().create1('e'));
        opts.addOption0(OptionBuilder.hasOptionalArg().withLongOpt("fish").create0());
        opts.addOption0(OptionBuilder.hasOptionalArgs0().withLongOpt("gravy").create0());
        opts.addOption0(OptionBuilder.hasOptionalArgs1(2).withLongOpt("hide").create0());
        opts.addOption0(OptionBuilder.hasOptionalArgs1(2).create1('i'));
        opts.addOption0(OptionBuilder.hasOptionalArgs0().create1('j'));

        final String[] args = {"-a", "-b", "foo", "--c", "--d", "bar"};

        final Parser parser = new PosixParser();
        cl = parser.parse0(opts, args);
    }

    @Test
    public void testLongNoArg() {
        assertTrue(cl.hasOption2("c"));
        assertNull(cl.getOptionValue4("c"));
    }

    @Test
    public void testLongNoArgWithOption() {
        assertTrue(cl.hasOption1(opts.getOption("c")));
        assertNull(cl.getOptionValue2(opts.getOption("c")));
    }

    @Test
    public void testLongOptionalArgValue() throws Exception {
        final String[] args = {"--fish", "face"};

        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("fish"));
        assertEquals("face", cmd.getOptionValue4("fish"));
    }

    @Test
    public void testLongOptionalArgValues() throws Exception {
        final String[] args = {"--gravy", "gold", "garden"};

        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("gravy"));
        assertEquals("gold", cmd.getOptionValue4("gravy"));
        assertEquals("gold", cmd.getOptionValues2("gravy")[0]);
        assertEquals("garden", cmd.getOptionValues2("gravy")[1]);
        assertEquals(cmd.getArgs().length, 0);
    }

    @Test
    public void testLongOptionalArgValuesWithOption() throws Exception {
        final String[] args = {"--gravy", "gold", "garden"};

        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption1(opts.getOption("gravy")));
        assertEquals("gold", cmd.getOptionValue2(opts.getOption("gravy")));
        assertEquals("gold", cmd.getOptionValues1(opts.getOption("gravy"))[0]);
        assertEquals("garden", cmd.getOptionValues1(opts.getOption("gravy"))[1]);
        assertEquals(cmd.getArgs().length, 0);
    }

    @Test
    public void testLongOptionalArgValueWithOption() throws Exception {
        final String[] args = {"--fish", "face"};

        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption1(opts.getOption("fish")));
        assertEquals("face", cmd.getOptionValue2(opts.getOption("fish")));
    }

    @Test
    public void testLongOptionalNArgValues() throws Exception {
        final String[] args = {"--hide", "house", "hair", "head"};

        final Parser parser = new PosixParser();

        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("hide"));
        assertEquals("house", cmd.getOptionValue4("hide"));
        assertEquals("house", cmd.getOptionValues2("hide")[0]);
        assertEquals("hair", cmd.getOptionValues2("hide")[1]);
        assertEquals(cmd.getArgs().length, 1);
        assertEquals("head", cmd.getArgs()[0]);
    }

    @Test
    public void testLongOptionalNArgValuesWithOption() throws Exception {
        final String[] args = {"--hide", "house", "hair", "head"};

        final Parser parser = new PosixParser();

        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption1(opts.getOption("hide")));
        assertEquals("house", cmd.getOptionValue2(opts.getOption("hide")));
        assertEquals("house", cmd.getOptionValues1(opts.getOption("hide"))[0]);
        assertEquals("hair", cmd.getOptionValues1(opts.getOption("hide"))[1]);
        assertEquals(cmd.getArgs().length, 1);
        assertEquals("head", cmd.getArgs()[0]);
    }

    @Test
    public void testLongOptionalNoValue() throws Exception {
        final String[] args = {"--fish"};

        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("fish"));
        assertNull(cmd.getOptionValue4("fish"));
    }

    @Test
    public void testLongOptionalNoValueWithOption() throws Exception {
        final String[] args = {"--fish"};

        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption1(opts.getOption("fish")));
        assertNull(cmd.getOptionValue2(opts.getOption("fish")));
    }

    @Test
    public void testLongWithArg() {
        assertTrue(cl.hasOption2("d"));
        assertNotNull(cl.getOptionValue4("d"));
        assertEquals(cl.getOptionValue4("d"), "bar");
    }

    @Test
    public void testLongWithArgWithOption() {
        assertTrue(cl.hasOption1(opts.getOption("d")));
        assertNotNull(cl.getOptionValue2(opts.getOption("d")));
        assertEquals(cl.getOptionValue2(opts.getOption("d")), "bar");
    }

    @Test
    public void testShortNoArg() {
        assertTrue(cl.hasOption2("a"));
        assertNull(cl.getOptionValue4("a"));
    }

    @Test
    public void testShortNoArgWithOption() {
        assertTrue(cl.hasOption1(opts.getOption("a")));
        assertNull(cl.getOptionValue2(opts.getOption("a")));
    }

    @Test
    public void testShortOptionalArgNoValue() throws Exception {
        final String[] args = {"-e"};

        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("e"));
        assertNull(cmd.getOptionValue4("e"));
    }

    @Test
    public void testShortOptionalArgNoValueWithOption() throws Exception {
        final String[] args = {"-e"};

        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption1(opts.getOption("e")));
        assertNull(cmd.getOptionValue2(opts.getOption("e")));
    }

    @Test
    public void testShortOptionalArgValue() throws Exception {
        final String[] args = {"-e", "everything"};

        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("e"));
        assertEquals("everything", cmd.getOptionValue4("e"));
    }

    @Test
    public void testShortOptionalArgValues() throws Exception {
        final String[] args = {"-j", "ink", "idea"};

        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("j"));
        assertEquals("ink", cmd.getOptionValue4("j"));
        assertEquals("ink", cmd.getOptionValues2("j")[0]);
        assertEquals("idea", cmd.getOptionValues2("j")[1]);
        assertEquals(cmd.getArgs().length, 0);
    }

    @Test
    public void testShortOptionalArgValuesWithOption() throws Exception {
        final String[] args = {"-j", "ink", "idea"};

        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption1(opts.getOption("j")));
        assertEquals("ink", cmd.getOptionValue2(opts.getOption("j")));
        assertEquals("ink", cmd.getOptionValues1(opts.getOption("j"))[0]);
        assertEquals("idea", cmd.getOptionValues1(opts.getOption("j"))[1]);
        assertEquals(cmd.getArgs().length, 0);
    }

    @Test
    public void testShortOptionalArgValueWithOption() throws Exception {
        final String[] args = {"-e", "everything"};

        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption1(opts.getOption("e")));
        assertEquals("everything", cmd.getOptionValue2(opts.getOption("e")));
    }

    @Test
    public void testShortOptionalNArgValues() throws Exception {
        final String[] args = {"-i", "ink", "idea", "isotope", "ice"};

        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("i"));
        assertEquals("ink", cmd.getOptionValue4("i"));
        assertEquals("ink", cmd.getOptionValues2("i")[0]);
        assertEquals("idea", cmd.getOptionValues2("i")[1]);
        assertEquals(cmd.getArgs().length, 2);
        assertEquals("isotope", cmd.getArgs()[0]);
        assertEquals("ice", cmd.getArgs()[1]);
    }

    @Test
    public void testShortOptionalNArgValuesWithOption() throws Exception {
        final String[] args = {"-i", "ink", "idea", "isotope", "ice"};

        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("i"));
        assertEquals("ink", cmd.getOptionValue2(opts.getOption("i")));
        assertEquals("ink", cmd.getOptionValues1(opts.getOption("i"))[0]);
        assertEquals("idea", cmd.getOptionValues1(opts.getOption("i"))[1]);
        assertEquals(cmd.getArgs().length, 2);
        assertEquals("isotope", cmd.getArgs()[0]);
        assertEquals("ice", cmd.getArgs()[1]);
    }

    @Test
    public void testShortWithArg() {
        assertTrue(cl.hasOption2("b"));
        assertNotNull(cl.getOptionValue4("b"));
        assertEquals(cl.getOptionValue4("b"), "foo");
    }

    @Test
    public void testShortWithArgWithOption() {
        assertTrue(cl.hasOption1(opts.getOption("b")));
        assertNotNull(cl.getOptionValue2(opts.getOption("b")));
        assertEquals(cl.getOptionValue2(opts.getOption("b")), "foo");
    }
}
