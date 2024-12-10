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
    public void testLongNoArg_test0_decomposed()  {
        assertTrue(cl.hasOption2("c"));
    }

    @Test
    public void testLongNoArg_test1_decomposed()  {
        assertTrue(cl.hasOption2("c"));
        assertNull(cl.getOptionValue4("c"));
    }

    @Test
    public void testLongNoArgWithOption_test0_decomposed()  {
        opts.getOption("c");
    }

    @Test
    public void testLongNoArgWithOption_test1_decomposed()  {
        opts.getOption("c");
        assertTrue(cl.hasOption1(opts.getOption("c")));
    }

    @Test
    public void testLongNoArgWithOption_test2_decomposed()  {
        opts.getOption("c");
        assertTrue(cl.hasOption1(opts.getOption("c")));
        opts.getOption("c");
    }

    @Test
    public void testLongNoArgWithOption_test3_decomposed()  {
        opts.getOption("c");
        assertTrue(cl.hasOption1(opts.getOption("c")));
        opts.getOption("c");
        assertNull(cl.getOptionValue2(opts.getOption("c")));
    }

    @Test
    public void testLongOptionalArgValue_test0_decomposed() throws Exception {
        final String[] args = {"--fish", "face"};
        final Parser parser = new PosixParser();
    }

    @Test
    public void testLongOptionalArgValue_test1_decomposed() throws Exception {
        final String[] args = {"--fish", "face"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
    }

    @Test
    public void testLongOptionalArgValue_test2_decomposed() throws Exception {
        final String[] args = {"--fish", "face"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("fish"));
    }

    @Test
    public void testLongOptionalArgValue_test3_decomposed() throws Exception {
        final String[] args = {"--fish", "face"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("fish"));
        assertEquals("face", cmd.getOptionValue4("fish"));
    }

    @Test
    public void testLongOptionalArgValues_test0_decomposed() throws Exception {
        final String[] args = {"--gravy", "gold", "garden"};
        final Parser parser = new PosixParser();
    }

    @Test
    public void testLongOptionalArgValues_test1_decomposed() throws Exception {
        final String[] args = {"--gravy", "gold", "garden"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
    }

    @Test
    public void testLongOptionalArgValues_test2_decomposed() throws Exception {
        final String[] args = {"--gravy", "gold", "garden"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("gravy"));
    }

    @Test
    public void testLongOptionalArgValues_test3_decomposed() throws Exception {
        final String[] args = {"--gravy", "gold", "garden"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("gravy"));
        assertEquals("gold", cmd.getOptionValue4("gravy"));
    }

    @Test
    public void testLongOptionalArgValues_test4_decomposed() throws Exception {
        final String[] args = {"--gravy", "gold", "garden"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("gravy"));
        assertEquals("gold", cmd.getOptionValue4("gravy"));
        assertEquals("gold", cmd.getOptionValues2("gravy")[0]);
        assertEquals("garden", cmd.getOptionValues2("gravy")[1]);
    }

    @Test
    public void testLongOptionalArgValues_test5_decomposed() throws Exception {
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
    public void testLongOptionalArgValuesWithOption_test0_decomposed() throws Exception {
        final String[] args = {"--gravy", "gold", "garden"};
        final Parser parser = new PosixParser();
    }

    @Test
    public void testLongOptionalArgValuesWithOption_test1_decomposed() throws Exception {
        final String[] args = {"--gravy", "gold", "garden"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
    }

    @Test
    public void testLongOptionalArgValuesWithOption_test2_decomposed() throws Exception {
        final String[] args = {"--gravy", "gold", "garden"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("gravy");
    }

    @Test
    public void testLongOptionalArgValuesWithOption_test3_decomposed() throws Exception {
        final String[] args = {"--gravy", "gold", "garden"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("gravy");
        assertTrue(cmd.hasOption1(opts.getOption("gravy")));
    }

    @Test
    public void testLongOptionalArgValuesWithOption_test4_decomposed() throws Exception {
        final String[] args = {"--gravy", "gold", "garden"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("gravy");
        assertTrue(cmd.hasOption1(opts.getOption("gravy")));
        opts.getOption("gravy");
    }

    @Test
    public void testLongOptionalArgValuesWithOption_test5_decomposed() throws Exception {
        final String[] args = {"--gravy", "gold", "garden"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("gravy");
        assertTrue(cmd.hasOption1(opts.getOption("gravy")));
        opts.getOption("gravy");
        assertEquals("gold", cmd.getOptionValue2(opts.getOption("gravy")));
    }

    @Test
    public void testLongOptionalArgValuesWithOption_test6_decomposed() throws Exception {
        final String[] args = {"--gravy", "gold", "garden"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("gravy");
        assertTrue(cmd.hasOption1(opts.getOption("gravy")));
        opts.getOption("gravy");
        assertEquals("gold", cmd.getOptionValue2(opts.getOption("gravy")));
        opts.getOption("gravy");
    }

    @Test
    public void testLongOptionalArgValuesWithOption_test7_decomposed() throws Exception {
        final String[] args = {"--gravy", "gold", "garden"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("gravy");
        assertTrue(cmd.hasOption1(opts.getOption("gravy")));
        opts.getOption("gravy");
        assertEquals("gold", cmd.getOptionValue2(opts.getOption("gravy")));
        opts.getOption("gravy");
        assertEquals("gold", cmd.getOptionValues1(opts.getOption("gravy"))[0]);
    }

    @Test
    public void testLongOptionalArgValuesWithOption_test8_decomposed() throws Exception {
        final String[] args = {"--gravy", "gold", "garden"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("gravy");
        assertTrue(cmd.hasOption1(opts.getOption("gravy")));
        opts.getOption("gravy");
        assertEquals("gold", cmd.getOptionValue2(opts.getOption("gravy")));
        opts.getOption("gravy");
        assertEquals("gold", cmd.getOptionValues1(opts.getOption("gravy"))[0]);
        opts.getOption("gravy");
    }

    @Test
    public void testLongOptionalArgValuesWithOption_test9_decomposed() throws Exception {
        final String[] args = {"--gravy", "gold", "garden"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("gravy");
        assertTrue(cmd.hasOption1(opts.getOption("gravy")));
        opts.getOption("gravy");
        assertEquals("gold", cmd.getOptionValue2(opts.getOption("gravy")));
        opts.getOption("gravy");
        assertEquals("gold", cmd.getOptionValues1(opts.getOption("gravy"))[0]);
        opts.getOption("gravy");
        assertEquals("garden", cmd.getOptionValues1(opts.getOption("gravy"))[1]);
    }

    @Test
    public void testLongOptionalArgValuesWithOption_test10_decomposed() throws Exception {
        final String[] args = {"--gravy", "gold", "garden"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("gravy");
        assertTrue(cmd.hasOption1(opts.getOption("gravy")));
        opts.getOption("gravy");
        assertEquals("gold", cmd.getOptionValue2(opts.getOption("gravy")));
        opts.getOption("gravy");
        assertEquals("gold", cmd.getOptionValues1(opts.getOption("gravy"))[0]);
        opts.getOption("gravy");
        assertEquals("garden", cmd.getOptionValues1(opts.getOption("gravy"))[1]);
        assertEquals(cmd.getArgs().length, 0);
    }

    @Test
    public void testLongOptionalArgValueWithOption_test0_decomposed() throws Exception {
        final String[] args = {"--fish", "face"};
        final Parser parser = new PosixParser();
    }

    @Test
    public void testLongOptionalArgValueWithOption_test1_decomposed() throws Exception {
        final String[] args = {"--fish", "face"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
    }

    @Test
    public void testLongOptionalArgValueWithOption_test2_decomposed() throws Exception {
        final String[] args = {"--fish", "face"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("fish");
    }

    @Test
    public void testLongOptionalArgValueWithOption_test3_decomposed() throws Exception {
        final String[] args = {"--fish", "face"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("fish");
        assertTrue(cmd.hasOption1(opts.getOption("fish")));
    }

    @Test
    public void testLongOptionalArgValueWithOption_test4_decomposed() throws Exception {
        final String[] args = {"--fish", "face"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("fish");
        assertTrue(cmd.hasOption1(opts.getOption("fish")));
        opts.getOption("fish");
    }

    @Test
    public void testLongOptionalArgValueWithOption_test5_decomposed() throws Exception {
        final String[] args = {"--fish", "face"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("fish");
        assertTrue(cmd.hasOption1(opts.getOption("fish")));
        opts.getOption("fish");
        assertEquals("face", cmd.getOptionValue2(opts.getOption("fish")));
    }

    @Test
    public void testLongOptionalNArgValues_test0_decomposed() throws Exception {
        final String[] args = {"--hide", "house", "hair", "head"};
        final Parser parser = new PosixParser();
    }

    @Test
    public void testLongOptionalNArgValues_test1_decomposed() throws Exception {
        final String[] args = {"--hide", "house", "hair", "head"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
    }

    @Test
    public void testLongOptionalNArgValues_test2_decomposed() throws Exception {
        final String[] args = {"--hide", "house", "hair", "head"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("hide"));
    }

    @Test
    public void testLongOptionalNArgValues_test3_decomposed() throws Exception {
        final String[] args = {"--hide", "house", "hair", "head"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("hide"));
        assertEquals("house", cmd.getOptionValue4("hide"));
    }

    @Test
    public void testLongOptionalNArgValues_test4_decomposed() throws Exception {
        final String[] args = {"--hide", "house", "hair", "head"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("hide"));
        assertEquals("house", cmd.getOptionValue4("hide"));
        assertEquals("house", cmd.getOptionValues2("hide")[0]);
        assertEquals("hair", cmd.getOptionValues2("hide")[1]);
    }

    @Test
    public void testLongOptionalNArgValues_test5_decomposed() throws Exception {
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
    public void testLongOptionalNArgValuesWithOption_test0_decomposed() throws Exception {
        final String[] args = {"--hide", "house", "hair", "head"};
        final Parser parser = new PosixParser();
    }

    @Test
    public void testLongOptionalNArgValuesWithOption_test1_decomposed() throws Exception {
        final String[] args = {"--hide", "house", "hair", "head"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
    }

    @Test
    public void testLongOptionalNArgValuesWithOption_test2_decomposed() throws Exception {
        final String[] args = {"--hide", "house", "hair", "head"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("hide");
    }

    @Test
    public void testLongOptionalNArgValuesWithOption_test3_decomposed() throws Exception {
        final String[] args = {"--hide", "house", "hair", "head"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("hide");
        assertTrue(cmd.hasOption1(opts.getOption("hide")));
    }

    @Test
    public void testLongOptionalNArgValuesWithOption_test4_decomposed() throws Exception {
        final String[] args = {"--hide", "house", "hair", "head"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("hide");
        assertTrue(cmd.hasOption1(opts.getOption("hide")));
        opts.getOption("hide");
    }

    @Test
    public void testLongOptionalNArgValuesWithOption_test5_decomposed() throws Exception {
        final String[] args = {"--hide", "house", "hair", "head"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("hide");
        assertTrue(cmd.hasOption1(opts.getOption("hide")));
        opts.getOption("hide");
        assertEquals("house", cmd.getOptionValue2(opts.getOption("hide")));
    }

    @Test
    public void testLongOptionalNArgValuesWithOption_test6_decomposed() throws Exception {
        final String[] args = {"--hide", "house", "hair", "head"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("hide");
        assertTrue(cmd.hasOption1(opts.getOption("hide")));
        opts.getOption("hide");
        assertEquals("house", cmd.getOptionValue2(opts.getOption("hide")));
        opts.getOption("hide");
    }

    @Test
    public void testLongOptionalNArgValuesWithOption_test7_decomposed() throws Exception {
        final String[] args = {"--hide", "house", "hair", "head"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("hide");
        assertTrue(cmd.hasOption1(opts.getOption("hide")));
        opts.getOption("hide");
        assertEquals("house", cmd.getOptionValue2(opts.getOption("hide")));
        opts.getOption("hide");
        assertEquals("house", cmd.getOptionValues1(opts.getOption("hide"))[0]);
    }

    @Test
    public void testLongOptionalNArgValuesWithOption_test8_decomposed() throws Exception {
        final String[] args = {"--hide", "house", "hair", "head"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("hide");
        assertTrue(cmd.hasOption1(opts.getOption("hide")));
        opts.getOption("hide");
        assertEquals("house", cmd.getOptionValue2(opts.getOption("hide")));
        opts.getOption("hide");
        assertEquals("house", cmd.getOptionValues1(opts.getOption("hide"))[0]);
        opts.getOption("hide");
    }

    @Test
    public void testLongOptionalNArgValuesWithOption_test9_decomposed() throws Exception {
        final String[] args = {"--hide", "house", "hair", "head"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("hide");
        assertTrue(cmd.hasOption1(opts.getOption("hide")));
        opts.getOption("hide");
        assertEquals("house", cmd.getOptionValue2(opts.getOption("hide")));
        opts.getOption("hide");
        assertEquals("house", cmd.getOptionValues1(opts.getOption("hide"))[0]);
        opts.getOption("hide");
        assertEquals("hair", cmd.getOptionValues1(opts.getOption("hide"))[1]);
    }

    @Test
    public void testLongOptionalNArgValuesWithOption_test10_decomposed() throws Exception {
        final String[] args = {"--hide", "house", "hair", "head"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("hide");
        assertTrue(cmd.hasOption1(opts.getOption("hide")));
        opts.getOption("hide");
        assertEquals("house", cmd.getOptionValue2(opts.getOption("hide")));
        opts.getOption("hide");
        assertEquals("house", cmd.getOptionValues1(opts.getOption("hide"))[0]);
        opts.getOption("hide");
        assertEquals("hair", cmd.getOptionValues1(opts.getOption("hide"))[1]);
        assertEquals(cmd.getArgs().length, 1);
        assertEquals("head", cmd.getArgs()[0]);
    }

    @Test
    public void testLongOptionalNoValue_test0_decomposed() throws Exception {
        final String[] args = {"--fish"};
        final Parser parser = new PosixParser();
    }

    @Test
    public void testLongOptionalNoValue_test1_decomposed() throws Exception {
        final String[] args = {"--fish"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
    }

    @Test
    public void testLongOptionalNoValue_test2_decomposed() throws Exception {
        final String[] args = {"--fish"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("fish"));
    }

    @Test
    public void testLongOptionalNoValue_test3_decomposed() throws Exception {
        final String[] args = {"--fish"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("fish"));
        assertNull(cmd.getOptionValue4("fish"));
    }

    @Test
    public void testLongOptionalNoValueWithOption_test0_decomposed() throws Exception {
        final String[] args = {"--fish"};
        final Parser parser = new PosixParser();
    }

    @Test
    public void testLongOptionalNoValueWithOption_test1_decomposed() throws Exception {
        final String[] args = {"--fish"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
    }

    @Test
    public void testLongOptionalNoValueWithOption_test2_decomposed() throws Exception {
        final String[] args = {"--fish"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("fish");
    }

    @Test
    public void testLongOptionalNoValueWithOption_test3_decomposed() throws Exception {
        final String[] args = {"--fish"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("fish");
        assertTrue(cmd.hasOption1(opts.getOption("fish")));
    }

    @Test
    public void testLongOptionalNoValueWithOption_test4_decomposed() throws Exception {
        final String[] args = {"--fish"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("fish");
        assertTrue(cmd.hasOption1(opts.getOption("fish")));
        opts.getOption("fish");
    }

    @Test
    public void testLongOptionalNoValueWithOption_test5_decomposed() throws Exception {
        final String[] args = {"--fish"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("fish");
        assertTrue(cmd.hasOption1(opts.getOption("fish")));
        opts.getOption("fish");
        assertNull(cmd.getOptionValue2(opts.getOption("fish")));
    }

    @Test
    public void testLongWithArg_test0_decomposed()  {
        assertTrue(cl.hasOption2("d"));
    }

    @Test
    public void testLongWithArg_test1_decomposed()  {
        assertTrue(cl.hasOption2("d"));
        assertNotNull(cl.getOptionValue4("d"));
        assertEquals(cl.getOptionValue4("d"), "bar");
    }

    @Test
    public void testLongWithArgWithOption_test0_decomposed()  {
        opts.getOption("d");
    }

    @Test
    public void testLongWithArgWithOption_test1_decomposed()  {
        opts.getOption("d");
        assertTrue(cl.hasOption1(opts.getOption("d")));
    }

    @Test
    public void testLongWithArgWithOption_test2_decomposed()  {
        opts.getOption("d");
        assertTrue(cl.hasOption1(opts.getOption("d")));
        opts.getOption("d");
    }

    @Test
    public void testLongWithArgWithOption_test3_decomposed()  {
        opts.getOption("d");
        assertTrue(cl.hasOption1(opts.getOption("d")));
        opts.getOption("d");
        assertNotNull(cl.getOptionValue2(opts.getOption("d")));
    }

    @Test
    public void testLongWithArgWithOption_test4_decomposed()  {
        opts.getOption("d");
        assertTrue(cl.hasOption1(opts.getOption("d")));
        opts.getOption("d");
        assertNotNull(cl.getOptionValue2(opts.getOption("d")));
        opts.getOption("d");
    }

    @Test
    public void testLongWithArgWithOption_test5_decomposed()  {
        opts.getOption("d");
        assertTrue(cl.hasOption1(opts.getOption("d")));
        opts.getOption("d");
        assertNotNull(cl.getOptionValue2(opts.getOption("d")));
        opts.getOption("d");
        assertEquals(cl.getOptionValue2(opts.getOption("d")), "bar");
    }

    @Test
    public void testShortNoArg_test0_decomposed()  {
        assertTrue(cl.hasOption2("a"));
    }

    @Test
    public void testShortNoArg_test1_decomposed()  {
        assertTrue(cl.hasOption2("a"));
        assertNull(cl.getOptionValue4("a"));
    }

    @Test
    public void testShortNoArgWithOption_test0_decomposed()  {
        opts.getOption("a");
    }

    @Test
    public void testShortNoArgWithOption_test1_decomposed()  {
        opts.getOption("a");
        assertTrue(cl.hasOption1(opts.getOption("a")));
    }

    @Test
    public void testShortNoArgWithOption_test2_decomposed()  {
        opts.getOption("a");
        assertTrue(cl.hasOption1(opts.getOption("a")));
        opts.getOption("a");
    }

    @Test
    public void testShortNoArgWithOption_test3_decomposed()  {
        opts.getOption("a");
        assertTrue(cl.hasOption1(opts.getOption("a")));
        opts.getOption("a");
        assertNull(cl.getOptionValue2(opts.getOption("a")));
    }

    @Test
    public void testShortOptionalArgNoValue_test0_decomposed() throws Exception {
        final String[] args = {"-e"};
        final Parser parser = new PosixParser();
    }

    @Test
    public void testShortOptionalArgNoValue_test1_decomposed() throws Exception {
        final String[] args = {"-e"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
    }

    @Test
    public void testShortOptionalArgNoValue_test2_decomposed() throws Exception {
        final String[] args = {"-e"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("e"));
    }

    @Test
    public void testShortOptionalArgNoValue_test3_decomposed() throws Exception {
        final String[] args = {"-e"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("e"));
        assertNull(cmd.getOptionValue4("e"));
    }

    @Test
    public void testShortOptionalArgNoValueWithOption_test0_decomposed() throws Exception {
        final String[] args = {"-e"};
        final Parser parser = new PosixParser();
    }

    @Test
    public void testShortOptionalArgNoValueWithOption_test1_decomposed() throws Exception {
        final String[] args = {"-e"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
    }

    @Test
    public void testShortOptionalArgNoValueWithOption_test2_decomposed() throws Exception {
        final String[] args = {"-e"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("e");
    }

    @Test
    public void testShortOptionalArgNoValueWithOption_test3_decomposed() throws Exception {
        final String[] args = {"-e"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("e");
        assertTrue(cmd.hasOption1(opts.getOption("e")));
    }

    @Test
    public void testShortOptionalArgNoValueWithOption_test4_decomposed() throws Exception {
        final String[] args = {"-e"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("e");
        assertTrue(cmd.hasOption1(opts.getOption("e")));
        opts.getOption("e");
    }

    @Test
    public void testShortOptionalArgNoValueWithOption_test5_decomposed() throws Exception {
        final String[] args = {"-e"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("e");
        assertTrue(cmd.hasOption1(opts.getOption("e")));
        opts.getOption("e");
        assertNull(cmd.getOptionValue2(opts.getOption("e")));
    }

    @Test
    public void testShortOptionalArgValue_test0_decomposed() throws Exception {
        final String[] args = {"-e", "everything"};
        final Parser parser = new PosixParser();
    }

    @Test
    public void testShortOptionalArgValue_test1_decomposed() throws Exception {
        final String[] args = {"-e", "everything"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
    }

    @Test
    public void testShortOptionalArgValue_test2_decomposed() throws Exception {
        final String[] args = {"-e", "everything"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("e"));
    }

    @Test
    public void testShortOptionalArgValue_test3_decomposed() throws Exception {
        final String[] args = {"-e", "everything"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("e"));
        assertEquals("everything", cmd.getOptionValue4("e"));
    }

    @Test
    public void testShortOptionalArgValues_test0_decomposed() throws Exception {
        final String[] args = {"-j", "ink", "idea"};
        final Parser parser = new PosixParser();
    }

    @Test
    public void testShortOptionalArgValues_test1_decomposed() throws Exception {
        final String[] args = {"-j", "ink", "idea"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
    }

    @Test
    public void testShortOptionalArgValues_test2_decomposed() throws Exception {
        final String[] args = {"-j", "ink", "idea"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("j"));
    }

    @Test
    public void testShortOptionalArgValues_test3_decomposed() throws Exception {
        final String[] args = {"-j", "ink", "idea"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("j"));
        assertEquals("ink", cmd.getOptionValue4("j"));
    }

    @Test
    public void testShortOptionalArgValues_test4_decomposed() throws Exception {
        final String[] args = {"-j", "ink", "idea"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("j"));
        assertEquals("ink", cmd.getOptionValue4("j"));
        assertEquals("ink", cmd.getOptionValues2("j")[0]);
        assertEquals("idea", cmd.getOptionValues2("j")[1]);
    }

    @Test
    public void testShortOptionalArgValues_test5_decomposed() throws Exception {
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
    public void testShortOptionalArgValuesWithOption_test0_decomposed() throws Exception {
        final String[] args = {"-j", "ink", "idea"};
        final Parser parser = new PosixParser();
    }

    @Test
    public void testShortOptionalArgValuesWithOption_test1_decomposed() throws Exception {
        final String[] args = {"-j", "ink", "idea"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
    }

    @Test
    public void testShortOptionalArgValuesWithOption_test2_decomposed() throws Exception {
        final String[] args = {"-j", "ink", "idea"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("j");
    }

    @Test
    public void testShortOptionalArgValuesWithOption_test3_decomposed() throws Exception {
        final String[] args = {"-j", "ink", "idea"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("j");
        assertTrue(cmd.hasOption1(opts.getOption("j")));
    }

    @Test
    public void testShortOptionalArgValuesWithOption_test4_decomposed() throws Exception {
        final String[] args = {"-j", "ink", "idea"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("j");
        assertTrue(cmd.hasOption1(opts.getOption("j")));
        opts.getOption("j");
    }

    @Test
    public void testShortOptionalArgValuesWithOption_test5_decomposed() throws Exception {
        final String[] args = {"-j", "ink", "idea"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("j");
        assertTrue(cmd.hasOption1(opts.getOption("j")));
        opts.getOption("j");
        assertEquals("ink", cmd.getOptionValue2(opts.getOption("j")));
    }

    @Test
    public void testShortOptionalArgValuesWithOption_test6_decomposed() throws Exception {
        final String[] args = {"-j", "ink", "idea"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("j");
        assertTrue(cmd.hasOption1(opts.getOption("j")));
        opts.getOption("j");
        assertEquals("ink", cmd.getOptionValue2(opts.getOption("j")));
        opts.getOption("j");
    }

    @Test
    public void testShortOptionalArgValuesWithOption_test7_decomposed() throws Exception {
        final String[] args = {"-j", "ink", "idea"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("j");
        assertTrue(cmd.hasOption1(opts.getOption("j")));
        opts.getOption("j");
        assertEquals("ink", cmd.getOptionValue2(opts.getOption("j")));
        opts.getOption("j");
        assertEquals("ink", cmd.getOptionValues1(opts.getOption("j"))[0]);
    }

    @Test
    public void testShortOptionalArgValuesWithOption_test8_decomposed() throws Exception {
        final String[] args = {"-j", "ink", "idea"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("j");
        assertTrue(cmd.hasOption1(opts.getOption("j")));
        opts.getOption("j");
        assertEquals("ink", cmd.getOptionValue2(opts.getOption("j")));
        opts.getOption("j");
        assertEquals("ink", cmd.getOptionValues1(opts.getOption("j"))[0]);
        opts.getOption("j");
    }

    @Test
    public void testShortOptionalArgValuesWithOption_test9_decomposed() throws Exception {
        final String[] args = {"-j", "ink", "idea"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("j");
        assertTrue(cmd.hasOption1(opts.getOption("j")));
        opts.getOption("j");
        assertEquals("ink", cmd.getOptionValue2(opts.getOption("j")));
        opts.getOption("j");
        assertEquals("ink", cmd.getOptionValues1(opts.getOption("j"))[0]);
        opts.getOption("j");
        assertEquals("idea", cmd.getOptionValues1(opts.getOption("j"))[1]);
    }

    @Test
    public void testShortOptionalArgValuesWithOption_test10_decomposed() throws Exception {
        final String[] args = {"-j", "ink", "idea"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("j");
        assertTrue(cmd.hasOption1(opts.getOption("j")));
        opts.getOption("j");
        assertEquals("ink", cmd.getOptionValue2(opts.getOption("j")));
        opts.getOption("j");
        assertEquals("ink", cmd.getOptionValues1(opts.getOption("j"))[0]);
        opts.getOption("j");
        assertEquals("idea", cmd.getOptionValues1(opts.getOption("j"))[1]);
        assertEquals(cmd.getArgs().length, 0);
    }

    @Test
    public void testShortOptionalArgValueWithOption_test0_decomposed() throws Exception {
        final String[] args = {"-e", "everything"};
        final Parser parser = new PosixParser();
    }

    @Test
    public void testShortOptionalArgValueWithOption_test1_decomposed() throws Exception {
        final String[] args = {"-e", "everything"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
    }

    @Test
    public void testShortOptionalArgValueWithOption_test2_decomposed() throws Exception {
        final String[] args = {"-e", "everything"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("e");
    }

    @Test
    public void testShortOptionalArgValueWithOption_test3_decomposed() throws Exception {
        final String[] args = {"-e", "everything"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("e");
        assertTrue(cmd.hasOption1(opts.getOption("e")));
    }

    @Test
    public void testShortOptionalArgValueWithOption_test4_decomposed() throws Exception {
        final String[] args = {"-e", "everything"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("e");
        assertTrue(cmd.hasOption1(opts.getOption("e")));
        opts.getOption("e");
    }

    @Test
    public void testShortOptionalArgValueWithOption_test5_decomposed() throws Exception {
        final String[] args = {"-e", "everything"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        opts.getOption("e");
        assertTrue(cmd.hasOption1(opts.getOption("e")));
        opts.getOption("e");
        assertEquals("everything", cmd.getOptionValue2(opts.getOption("e")));
    }

    @Test
    public void testShortOptionalNArgValues_test0_decomposed() throws Exception {
        final String[] args = {"-i", "ink", "idea", "isotope", "ice"};
        final Parser parser = new PosixParser();
    }

    @Test
    public void testShortOptionalNArgValues_test1_decomposed() throws Exception {
        final String[] args = {"-i", "ink", "idea", "isotope", "ice"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
    }

    @Test
    public void testShortOptionalNArgValues_test2_decomposed() throws Exception {
        final String[] args = {"-i", "ink", "idea", "isotope", "ice"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("i"));
    }

    @Test
    public void testShortOptionalNArgValues_test3_decomposed() throws Exception {
        final String[] args = {"-i", "ink", "idea", "isotope", "ice"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("i"));
        assertEquals("ink", cmd.getOptionValue4("i"));
    }

    @Test
    public void testShortOptionalNArgValues_test4_decomposed() throws Exception {
        final String[] args = {"-i", "ink", "idea", "isotope", "ice"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("i"));
        assertEquals("ink", cmd.getOptionValue4("i"));
        assertEquals("ink", cmd.getOptionValues2("i")[0]);
        assertEquals("idea", cmd.getOptionValues2("i")[1]);
    }

    @Test
    public void testShortOptionalNArgValues_test5_decomposed() throws Exception {
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
    public void testShortOptionalNArgValuesWithOption_test0_decomposed() throws Exception {
        final String[] args = {"-i", "ink", "idea", "isotope", "ice"};
        final Parser parser = new PosixParser();
    }

    @Test
    public void testShortOptionalNArgValuesWithOption_test1_decomposed() throws Exception {
        final String[] args = {"-i", "ink", "idea", "isotope", "ice"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
    }

    @Test
    public void testShortOptionalNArgValuesWithOption_test2_decomposed() throws Exception {
        final String[] args = {"-i", "ink", "idea", "isotope", "ice"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("i"));
    }

    @Test
    public void testShortOptionalNArgValuesWithOption_test3_decomposed() throws Exception {
        final String[] args = {"-i", "ink", "idea", "isotope", "ice"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("i"));
        opts.getOption("i");
    }

    @Test
    public void testShortOptionalNArgValuesWithOption_test4_decomposed() throws Exception {
        final String[] args = {"-i", "ink", "idea", "isotope", "ice"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("i"));
        opts.getOption("i");
        assertEquals("ink", cmd.getOptionValue2(opts.getOption("i")));
    }

    @Test
    public void testShortOptionalNArgValuesWithOption_test5_decomposed() throws Exception {
        final String[] args = {"-i", "ink", "idea", "isotope", "ice"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("i"));
        opts.getOption("i");
        assertEquals("ink", cmd.getOptionValue2(opts.getOption("i")));
        opts.getOption("i");
    }

    @Test
    public void testShortOptionalNArgValuesWithOption_test6_decomposed() throws Exception {
        final String[] args = {"-i", "ink", "idea", "isotope", "ice"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("i"));
        opts.getOption("i");
        assertEquals("ink", cmd.getOptionValue2(opts.getOption("i")));
        opts.getOption("i");
        assertEquals("ink", cmd.getOptionValues1(opts.getOption("i"))[0]);
    }

    @Test
    public void testShortOptionalNArgValuesWithOption_test7_decomposed() throws Exception {
        final String[] args = {"-i", "ink", "idea", "isotope", "ice"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("i"));
        opts.getOption("i");
        assertEquals("ink", cmd.getOptionValue2(opts.getOption("i")));
        opts.getOption("i");
        assertEquals("ink", cmd.getOptionValues1(opts.getOption("i"))[0]);
        opts.getOption("i");
    }

    @Test
    public void testShortOptionalNArgValuesWithOption_test8_decomposed() throws Exception {
        final String[] args = {"-i", "ink", "idea", "isotope", "ice"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("i"));
        opts.getOption("i");
        assertEquals("ink", cmd.getOptionValue2(opts.getOption("i")));
        opts.getOption("i");
        assertEquals("ink", cmd.getOptionValues1(opts.getOption("i"))[0]);
        opts.getOption("i");
        assertEquals("idea", cmd.getOptionValues1(opts.getOption("i"))[1]);
    }

    @Test
    public void testShortOptionalNArgValuesWithOption_test9_decomposed() throws Exception {
        final String[] args = {"-i", "ink", "idea", "isotope", "ice"};
        final Parser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(opts, args);
        assertTrue(cmd.hasOption2("i"));
        opts.getOption("i");
        assertEquals("ink", cmd.getOptionValue2(opts.getOption("i")));
        opts.getOption("i");
        assertEquals("ink", cmd.getOptionValues1(opts.getOption("i"))[0]);
        opts.getOption("i");
        assertEquals("idea", cmd.getOptionValues1(opts.getOption("i"))[1]);
        assertEquals(cmd.getArgs().length, 2);
        assertEquals("isotope", cmd.getArgs()[0]);
        assertEquals("ice", cmd.getArgs()[1]);
    }

    @Test
    public void testShortWithArg_test0_decomposed()  {
        assertTrue(cl.hasOption2("b"));
    }

    @Test
    public void testShortWithArg_test1_decomposed()  {
        assertTrue(cl.hasOption2("b"));
        assertNotNull(cl.getOptionValue4("b"));
        assertEquals(cl.getOptionValue4("b"), "foo");
    }

    @Test
    public void testShortWithArgWithOption_test0_decomposed()  {
        opts.getOption("b");
    }

    @Test
    public void testShortWithArgWithOption_test1_decomposed()  {
        opts.getOption("b");
        assertTrue(cl.hasOption1(opts.getOption("b")));
    }

    @Test
    public void testShortWithArgWithOption_test2_decomposed()  {
        opts.getOption("b");
        assertTrue(cl.hasOption1(opts.getOption("b")));
        opts.getOption("b");
    }

    @Test
    public void testShortWithArgWithOption_test3_decomposed()  {
        opts.getOption("b");
        assertTrue(cl.hasOption1(opts.getOption("b")));
        opts.getOption("b");
        assertNotNull(cl.getOptionValue2(opts.getOption("b")));
    }

    @Test
    public void testShortWithArgWithOption_test4_decomposed()  {
        opts.getOption("b");
        assertTrue(cl.hasOption1(opts.getOption("b")));
        opts.getOption("b");
        assertNotNull(cl.getOptionValue2(opts.getOption("b")));
        opts.getOption("b");
    }

    @Test
    public void testShortWithArgWithOption_test5_decomposed()  {
        opts.getOption("b");
        assertTrue(cl.hasOption1(opts.getOption("b")));
        opts.getOption("b");
        assertNotNull(cl.getOptionValue2(opts.getOption("b")));
        opts.getOption("b");
        assertEquals(cl.getOptionValue2(opts.getOption("b")), "foo");
    }
}