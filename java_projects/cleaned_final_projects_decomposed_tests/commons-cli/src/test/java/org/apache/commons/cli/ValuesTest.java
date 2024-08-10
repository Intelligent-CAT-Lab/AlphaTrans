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

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;

import org.junit.Before;
import org.junit.Test;

@SuppressWarnings("deprecation") // tests some deprecated classes
public class ValuesTest {
    private CommandLine cmd;

    @Before
    public void setUp() throws Exception {
        final Options options = new Options();

        options.addOption1("a", false, "toggle -a");
        options.addOption1("b", true, "set -b");
        options.addOption3("c", "c", false, "toggle -c");
        options.addOption3("d", "d", true, "set -d");

        options.addOption0(
                OptionBuilder.withLongOpt("e").hasArgs0().withDescription("set -e ").create1('e'));
        options.addOption3("f", "f", false, "jk");
        options.addOption0(
                OptionBuilder.withLongOpt("g").hasArgs1(2).withDescription("set -g").create1('g'));
        options.addOption0(
                OptionBuilder.withLongOpt("h").hasArg0().withDescription("set -h").create1('h'));
        options.addOption0(OptionBuilder.withLongOpt("i").withDescription("set -i").create1('i'));
        options.addOption0(
                OptionBuilder.withLongOpt("j")
                        .hasArgs0()
                        .withDescription("set -j")
                        .withValueSeparator1('=')
                        .create1('j'));
        options.addOption0(
                OptionBuilder.withLongOpt("k")
                        .hasArgs0()
                        .withDescription("set -k")
                        .withValueSeparator1('=')
                        .create1('k'));
        options.addOption0(
                OptionBuilder.withLongOpt("m")
                        .hasArgs0()
                        .withDescription("set -m")
                        .withValueSeparator0()
                        .create1('m'));

        final String[] args = {
            "-a",
            "-b",
            "foo",
            "--c",
            "--d",
            "bar",
            "-e",
            "one",
            "two",
            "-f",
            "arg1",
            "arg2",
            "-g",
            "val1",
            "val2",
            "arg3",
            "-h",
            "val1",
            "-i",
            "-h",
            "val2",
            "-jkey=value",
            "-j",
            "key=value",
            "-kkey1=value1",
            "-kkey2=value2",
            "-mkey=value"
        };

        final CommandLineParser parser = new PosixParser();

        cmd = parser.parse0(options, args);
    }

    

    

    

    

    

    

    

    /**
     * jkeyes - commented out this test as the new architecture breaks this type of functionality. I
     * have left the test here in case I get a brainwave on how to resolve this.
     */
    /*
     * public void testGetValue() { // the 'm' option assertTrue(_option.getValues().length == 2); assertEquals(
     * _option.getValue(), "key"); assertEquals(_option.getValue(0), "key"); assertEquals(_option.getValue(1),
     * "value");
     *
     * try { assertEquals(_option.getValue(2), "key"); fail("IndexOutOfBounds not caught"); } catch(
     * IndexOutOfBoundsException exp) {
     *
     * }
     *
     * try { assertEquals(_option.getValue(-1), "key"); fail("IndexOutOfBounds not caught"); } catch(
     * IndexOutOfBoundsException exp) {
     *
     * } }
     */

    @Test
    public void testCharSeparator_test0_decomposed()  {
        assertTrue("Option j is not set", cmd.hasOption2("j"));
    }

    @Test
    public void testCharSeparator_test1_decomposed()  {
        assertTrue("Option j is not set", cmd.hasOption2("j"));
        assertTrue("Option j is not set", cmd.hasOption0('j'));
    }

    @Test
    public void testCharSeparator_test2_decomposed()  {
        assertTrue("Option j is not set", cmd.hasOption2("j"));
        assertTrue("Option j is not set", cmd.hasOption0('j'));
        assertArrayEquals(new String[] {"key", "value", "key", "value"}, cmd.getOptionValues2("j"));
    }

    @Test
    public void testCharSeparator_test3_decomposed()  {
        assertTrue("Option j is not set", cmd.hasOption2("j"));
        assertTrue("Option j is not set", cmd.hasOption0('j'));
        assertArrayEquals(new String[] {"key", "value", "key", "value"}, cmd.getOptionValues2("j"));
        assertArrayEquals(new String[] {"key", "value", "key", "value"}, cmd.getOptionValues0('j'));
    }

    @Test
    public void testCharSeparator_test4_decomposed()  {
        assertTrue("Option j is not set", cmd.hasOption2("j"));
        assertTrue("Option j is not set", cmd.hasOption0('j'));
        assertArrayEquals(new String[] {"key", "value", "key", "value"}, cmd.getOptionValues2("j"));
        assertArrayEquals(new String[] {"key", "value", "key", "value"}, cmd.getOptionValues0('j'));
        assertTrue("Option k is not set", cmd.hasOption2("k"));
    }

    @Test
    public void testCharSeparator_test5_decomposed()  {
        assertTrue("Option j is not set", cmd.hasOption2("j"));
        assertTrue("Option j is not set", cmd.hasOption0('j'));
        assertArrayEquals(new String[] {"key", "value", "key", "value"}, cmd.getOptionValues2("j"));
        assertArrayEquals(new String[] {"key", "value", "key", "value"}, cmd.getOptionValues0('j'));
        assertTrue("Option k is not set", cmd.hasOption2("k"));
        assertTrue("Option k is not set", cmd.hasOption0('k'));
    }

    @Test
    public void testCharSeparator_test6_decomposed()  {
        assertTrue("Option j is not set", cmd.hasOption2("j"));
        assertTrue("Option j is not set", cmd.hasOption0('j'));
        assertArrayEquals(new String[] {"key", "value", "key", "value"}, cmd.getOptionValues2("j"));
        assertArrayEquals(new String[] {"key", "value", "key", "value"}, cmd.getOptionValues0('j'));
        assertTrue("Option k is not set", cmd.hasOption2("k"));
        assertTrue("Option k is not set", cmd.hasOption0('k'));
        assertArrayEquals(
                new String[] {"key1", "value1", "key2", "value2"}, cmd.getOptionValues2("k"));
    }

    @Test
    public void testCharSeparator_test7_decomposed()  {
        assertTrue("Option j is not set", cmd.hasOption2("j"));
        assertTrue("Option j is not set", cmd.hasOption0('j'));
        assertArrayEquals(new String[] {"key", "value", "key", "value"}, cmd.getOptionValues2("j"));
        assertArrayEquals(new String[] {"key", "value", "key", "value"}, cmd.getOptionValues0('j'));
        assertTrue("Option k is not set", cmd.hasOption2("k"));
        assertTrue("Option k is not set", cmd.hasOption0('k'));
        assertArrayEquals(
                new String[] {"key1", "value1", "key2", "value2"}, cmd.getOptionValues2("k"));
        assertArrayEquals(
                new String[] {"key1", "value1", "key2", "value2"}, cmd.getOptionValues0('k'));
    }

    @Test
    public void testCharSeparator_test8_decomposed()  {
        assertTrue("Option j is not set", cmd.hasOption2("j"));
        assertTrue("Option j is not set", cmd.hasOption0('j'));
        assertArrayEquals(new String[] {"key", "value", "key", "value"}, cmd.getOptionValues2("j"));
        assertArrayEquals(new String[] {"key", "value", "key", "value"}, cmd.getOptionValues0('j'));
        assertTrue("Option k is not set", cmd.hasOption2("k"));
        assertTrue("Option k is not set", cmd.hasOption0('k'));
        assertArrayEquals(
                new String[] {"key1", "value1", "key2", "value2"}, cmd.getOptionValues2("k"));
        assertArrayEquals(
                new String[] {"key1", "value1", "key2", "value2"}, cmd.getOptionValues0('k'));
        assertTrue("Option m is not set", cmd.hasOption2("m"));
    }

    @Test
    public void testCharSeparator_test9_decomposed()  {
        assertTrue("Option j is not set", cmd.hasOption2("j"));
        assertTrue("Option j is not set", cmd.hasOption0('j'));
        assertArrayEquals(new String[] {"key", "value", "key", "value"}, cmd.getOptionValues2("j"));
        assertArrayEquals(new String[] {"key", "value", "key", "value"}, cmd.getOptionValues0('j'));
        assertTrue("Option k is not set", cmd.hasOption2("k"));
        assertTrue("Option k is not set", cmd.hasOption0('k'));
        assertArrayEquals(
                new String[] {"key1", "value1", "key2", "value2"}, cmd.getOptionValues2("k"));
        assertArrayEquals(
                new String[] {"key1", "value1", "key2", "value2"}, cmd.getOptionValues0('k'));
        assertTrue("Option m is not set", cmd.hasOption2("m"));
        assertTrue("Option m is not set", cmd.hasOption0('m'));
    }

    @Test
    public void testCharSeparator_test10_decomposed()  {
        assertTrue("Option j is not set", cmd.hasOption2("j"));
        assertTrue("Option j is not set", cmd.hasOption0('j'));
        assertArrayEquals(new String[] {"key", "value", "key", "value"}, cmd.getOptionValues2("j"));
        assertArrayEquals(new String[] {"key", "value", "key", "value"}, cmd.getOptionValues0('j'));
        assertTrue("Option k is not set", cmd.hasOption2("k"));
        assertTrue("Option k is not set", cmd.hasOption0('k'));
        assertArrayEquals(
                new String[] {"key1", "value1", "key2", "value2"}, cmd.getOptionValues2("k"));
        assertArrayEquals(
                new String[] {"key1", "value1", "key2", "value2"}, cmd.getOptionValues0('k'));
        assertTrue("Option m is not set", cmd.hasOption2("m"));
        assertTrue("Option m is not set", cmd.hasOption0('m'));
        assertArrayEquals(new String[] {"key", "value"}, cmd.getOptionValues2("m"));
    }

    @Test
    public void testCharSeparator_test11_decomposed()  {
        assertTrue("Option j is not set", cmd.hasOption2("j"));
        assertTrue("Option j is not set", cmd.hasOption0('j'));
        assertArrayEquals(new String[] {"key", "value", "key", "value"}, cmd.getOptionValues2("j"));
        assertArrayEquals(new String[] {"key", "value", "key", "value"}, cmd.getOptionValues0('j'));
        assertTrue("Option k is not set", cmd.hasOption2("k"));
        assertTrue("Option k is not set", cmd.hasOption0('k'));
        assertArrayEquals(
                new String[] {"key1", "value1", "key2", "value2"}, cmd.getOptionValues2("k"));
        assertArrayEquals(
                new String[] {"key1", "value1", "key2", "value2"}, cmd.getOptionValues0('k'));
        assertTrue("Option m is not set", cmd.hasOption2("m"));
        assertTrue("Option m is not set", cmd.hasOption0('m'));
        assertArrayEquals(new String[] {"key", "value"}, cmd.getOptionValues2("m"));
        assertArrayEquals(new String[] {"key", "value"}, cmd.getOptionValues0('m'));
    }

    @Test
    public void testComplexValues_test0_decomposed()  {
        assertTrue("Option i is not set", cmd.hasOption2("i"));
        assertTrue("Option h is not set", cmd.hasOption2("h"));
    }

    @Test
    public void testComplexValues_test1_decomposed()  {
        assertTrue("Option i is not set", cmd.hasOption2("i"));
        assertTrue("Option h is not set", cmd.hasOption2("h"));
        assertArrayEquals(new String[] {"val1", "val2"}, cmd.getOptionValues2("h"));
    }

    @Test
    public void testExtraArgs_test0_decomposed()  {
        assertArrayEquals("Extra args", new String[] {"arg1", "arg2", "arg3"}, cmd.getArgs());
    }

    @Test
    public void testMultipleArgValues_test0_decomposed()  {
        assertTrue("Option e is not set", cmd.hasOption2("e"));
    }

    @Test
    public void testMultipleArgValues_test1_decomposed()  {
        assertTrue("Option e is not set", cmd.hasOption2("e"));
        assertArrayEquals(new String[] {"one", "two"}, cmd.getOptionValues2("e"));
    }

    @Test
    public void testShortArgs_test0_decomposed()  {
        assertTrue("Option a is not set", cmd.hasOption2("a"));
        assertTrue("Option c is not set", cmd.hasOption2("c"));
    }

    @Test
    public void testShortArgs_test1_decomposed()  {
        assertTrue("Option a is not set", cmd.hasOption2("a"));
        assertTrue("Option c is not set", cmd.hasOption2("c"));
        assertNull(cmd.getOptionValues2("a"));
        assertNull(cmd.getOptionValues2("c"));
    }

    @Test
    public void testShortArgsWithValue_test0_decomposed()  {
        assertTrue("Option b is not set", cmd.hasOption2("b"));
    }

    @Test
    public void testShortArgsWithValue_test1_decomposed()  {
        assertTrue("Option b is not set", cmd.hasOption2("b"));
        assertEquals("foo", cmd.getOptionValue4("b"));
    }

    @Test
    public void testShortArgsWithValue_test2_decomposed()  {
        assertTrue("Option b is not set", cmd.hasOption2("b"));
        assertEquals("foo", cmd.getOptionValue4("b"));
        assertEquals(1, cmd.getOptionValues2("b").length);
    }

    @Test
    public void testShortArgsWithValue_test3_decomposed()  {
        assertTrue("Option b is not set", cmd.hasOption2("b"));
        assertEquals("foo", cmd.getOptionValue4("b"));
        assertEquals(1, cmd.getOptionValues2("b").length);
        assertTrue("Option d is not set", cmd.hasOption2("d"));
    }

    @Test
    public void testShortArgsWithValue_test4_decomposed()  {
        assertTrue("Option b is not set", cmd.hasOption2("b"));
        assertEquals("foo", cmd.getOptionValue4("b"));
        assertEquals(1, cmd.getOptionValues2("b").length);
        assertTrue("Option d is not set", cmd.hasOption2("d"));
        assertEquals("bar", cmd.getOptionValue4("d"));
    }

    @Test
    public void testShortArgsWithValue_test5_decomposed()  {
        assertTrue("Option b is not set", cmd.hasOption2("b"));
        assertEquals("foo", cmd.getOptionValue4("b"));
        assertEquals(1, cmd.getOptionValues2("b").length);
        assertTrue("Option d is not set", cmd.hasOption2("d"));
        assertEquals("bar", cmd.getOptionValue4("d"));
        assertEquals(1, cmd.getOptionValues2("d").length);
    }

    @Test
    public void testTwoArgValues_test0_decomposed()  {
        assertTrue("Option g is not set", cmd.hasOption2("g"));
    }

    @Test
    public void testTwoArgValues_test1_decomposed()  {
        assertTrue("Option g is not set", cmd.hasOption2("g"));
        assertArrayEquals(new String[] {"val1", "val2"}, cmd.getOptionValues2("g"));
    }
}