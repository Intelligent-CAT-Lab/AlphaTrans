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
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import org.junit.Test;

@SuppressWarnings("deprecation") // OptionBuilder is marked deprecated
public class OptionBuilderTest {

    @Test
    public void testBaseOptionCharOpt_test0_decomposed()  {
        OptionBuilder.withDescription("option description");
    }

    @Test
    public void testBaseOptionCharOpt_test1_decomposed()  {
        OptionBuilder.withDescription("option description");
        final Option base = OptionBuilder.withDescription("option description").create1('o');
    }

    @Test
    public void testBaseOptionCharOpt_test2_decomposed()  {
        OptionBuilder.withDescription("option description");
        final Option base = OptionBuilder.withDescription("option description").create1('o');
        assertEquals("o", base.getOpt());
    }

    @Test
    public void testBaseOptionCharOpt_test3_decomposed()  {
        OptionBuilder.withDescription("option description");
        final Option base = OptionBuilder.withDescription("option description").create1('o');
        assertEquals("o", base.getOpt());
        assertEquals("option description", base.getDescription());
    }

    @Test
    public void testBaseOptionCharOpt_test4_decomposed()  {
        OptionBuilder.withDescription("option description");
        final Option base = OptionBuilder.withDescription("option description").create1('o');
        assertEquals("o", base.getOpt());
        assertEquals("option description", base.getDescription());
        assertFalse(base.hasArg());
    }

    @Test
    public void testBaseOptionStringOpt_test0_decomposed()  {
        OptionBuilder.withDescription("option description");
    }

    @Test
    public void testBaseOptionStringOpt_test1_decomposed()  {
        OptionBuilder.withDescription("option description");
        final Option base = OptionBuilder.withDescription("option description").create2("o");
    }

    @Test
    public void testBaseOptionStringOpt_test2_decomposed()  {
        OptionBuilder.withDescription("option description");
        final Option base = OptionBuilder.withDescription("option description").create2("o");
        assertEquals("o", base.getOpt());
    }

    @Test
    public void testBaseOptionStringOpt_test3_decomposed()  {
        OptionBuilder.withDescription("option description");
        final Option base = OptionBuilder.withDescription("option description").create2("o");
        assertEquals("o", base.getOpt());
        assertEquals("option description", base.getDescription());
    }

    @Test
    public void testBaseOptionStringOpt_test4_decomposed()  {
        OptionBuilder.withDescription("option description");
        final Option base = OptionBuilder.withDescription("option description").create2("o");
        assertEquals("o", base.getOpt());
        assertEquals("option description", base.getDescription());
        assertFalse(base.hasArg());
    }

    @Test
    public void testBuilderIsResettedAlways_test0_decomposed()  {
        try {
            OptionBuilder.withDescription("JUnit").create1('"');
            fail("IllegalArgumentException expected");
        } catch (final IllegalArgumentException e) {
        }
    }

    @Test
    public void testBuilderIsResettedAlways_test1_decomposed()  {
        try {
            OptionBuilder.withDescription("JUnit").create1('"');
            fail("IllegalArgumentException expected");
        } catch (final IllegalArgumentException e) {
        }
        OptionBuilder.create1('x');
    }

    @Test
    public void testBuilderIsResettedAlways_test2_decomposed()  {
        try {
            OptionBuilder.withDescription("JUnit").create1('"');
            fail("IllegalArgumentException expected");
        } catch (final IllegalArgumentException e) {
        }
        OptionBuilder.create1('x');
        assertNull("we inherited a description", OptionBuilder.create1('x').getDescription());
    }

    @Test
    public void testBuilderIsResettedAlways_test3_decomposed()  {
        try {
            OptionBuilder.withDescription("JUnit").create1('"');
            fail("IllegalArgumentException expected");
        } catch (final IllegalArgumentException e) {
        }
        OptionBuilder.create1('x');
        assertNull("we inherited a description", OptionBuilder.create1('x').getDescription());
        try {
            OptionBuilder.withDescription("JUnit").create0();
            fail("IllegalArgumentException expected");
        } catch (final IllegalArgumentException e) {
        }
    }

    @Test
    public void testBuilderIsResettedAlways_test4_decomposed()  {
        try {
            OptionBuilder.withDescription("JUnit").create1('"');
            fail("IllegalArgumentException expected");
        } catch (final IllegalArgumentException e) {
        }
        OptionBuilder.create1('x');
        assertNull("we inherited a description", OptionBuilder.create1('x').getDescription());
        try {
            OptionBuilder.withDescription("JUnit").create0();
            fail("IllegalArgumentException expected");
        } catch (final IllegalArgumentException e) {
        }
        OptionBuilder.create1('x');
    }

    @Test
    public void testBuilderIsResettedAlways_test5_decomposed()  {
        try {
            OptionBuilder.withDescription("JUnit").create1('"');
            fail("IllegalArgumentException expected");
        } catch (final IllegalArgumentException e) {
        }
        OptionBuilder.create1('x');
        assertNull("we inherited a description", OptionBuilder.create1('x').getDescription());
        try {
            OptionBuilder.withDescription("JUnit").create0();
            fail("IllegalArgumentException expected");
        } catch (final IllegalArgumentException e) {
        }
        OptionBuilder.create1('x');
        assertNull("we inherited a description", OptionBuilder.create1('x').getDescription());
    }

    @Test
    public void testCompleteOption_test0_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
    }

    @Test
    public void testCompleteOption_test1_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
    }

    @Test
    public void testCompleteOption_test2_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
    }

    @Test
    public void testCompleteOption_test3_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
    }

    @Test
    public void testCompleteOption_test4_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
    }

    @Test
    public void testCompleteOption_test5_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
    }

    @Test
    public void testCompleteOption_test6_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        final Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
    }

    @Test
    public void testCompleteOption_test7_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        final Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
    }

    @Test
    public void testCompleteOption_test8_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        final Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
        assertEquals("simple option", simple.getLongOpt());
    }

    @Test
    public void testCompleteOption_test9_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        final Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
        assertEquals("simple option", simple.getLongOpt());
        assertEquals("this is a simple option", simple.getDescription());
    }

    @Test
    public void testCompleteOption_test10_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        final Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
        assertEquals("simple option", simple.getLongOpt());
        assertEquals("this is a simple option", simple.getDescription());
        assertEquals(simple.getType(), Float.class);
    }

    @Test
    public void testCompleteOption_test11_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        final Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
        assertEquals("simple option", simple.getLongOpt());
        assertEquals("this is a simple option", simple.getDescription());
        assertEquals(simple.getType(), Float.class);
        assertTrue(simple.hasArg());
    }

    @Test
    public void testCompleteOption_test12_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        final Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
        assertEquals("simple option", simple.getLongOpt());
        assertEquals("this is a simple option", simple.getDescription());
        assertEquals(simple.getType(), Float.class);
        assertTrue(simple.hasArg());
        assertTrue(simple.isRequired());
    }

    @Test
    public void testCompleteOption_test13_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        final Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
        assertEquals("simple option", simple.getLongOpt());
        assertEquals("this is a simple option", simple.getDescription());
        assertEquals(simple.getType(), Float.class);
        assertTrue(simple.hasArg());
        assertTrue(simple.isRequired());
        assertTrue(simple.hasArgs());
    }

    @Test
    public void testCreateIncompleteOption_test0_decomposed()  {
        try {
            OptionBuilder.hasArg0().create0();
            fail("Incomplete option should be rejected");
        } catch (final IllegalArgumentException e) {

            OptionBuilder.create2("opt");
        }
    }

    @Test
    public void testIllegalOptions_test0_decomposed()  {
        try {
            OptionBuilder.withDescription("option description").create1('"');
            fail("IllegalArgumentException not caught");
        } catch (final IllegalArgumentException exp) {
        }
    }

    @Test
    public void testIllegalOptions_test1_decomposed()  {
        try {
            OptionBuilder.withDescription("option description").create1('"');
            fail("IllegalArgumentException not caught");
        } catch (final IllegalArgumentException exp) {
        }
        try {
            OptionBuilder.create2("opt`");
            fail("IllegalArgumentException not caught");
        } catch (final IllegalArgumentException exp) {
        }
        try {
            OptionBuilder.create2("opt");
        } catch (final IllegalArgumentException exp) {
            fail("IllegalArgumentException caught");
        }
    }

    @Test
    public void testOptionArgNumbers_test0_decomposed()  {
        OptionBuilder.withDescription("option description");
    }

    @Test
    public void testOptionArgNumbers_test1_decomposed()  {
        OptionBuilder.withDescription("option description");
        OptionBuilder.withDescription("option description").hasArgs1(2);
    }

    @Test
    public void testOptionArgNumbers_test2_decomposed()  {
        OptionBuilder.withDescription("option description");
        OptionBuilder.withDescription("option description").hasArgs1(2);
        final Option opt =
                OptionBuilder.withDescription("option description").hasArgs1(2).create1('o');
    }

    @Test
    public void testOptionArgNumbers_test3_decomposed()  {
        OptionBuilder.withDescription("option description");
        OptionBuilder.withDescription("option description").hasArgs1(2);
        final Option opt =
                OptionBuilder.withDescription("option description").hasArgs1(2).create1('o');
        assertEquals(2, opt.getArgs());
    }

    @Test
    public void testSpecialOptChars_test0_decomposed() throws Exception {
        OptionBuilder.withDescription("help options");
    }

    @Test
    public void testSpecialOptChars_test1_decomposed() throws Exception {
        OptionBuilder.withDescription("help options");
        final Option opt1 = OptionBuilder.withDescription("help options").create1('?');
    }

    @Test
    public void testSpecialOptChars_test2_decomposed() throws Exception {
        OptionBuilder.withDescription("help options");
        final Option opt1 = OptionBuilder.withDescription("help options").create1('?');
        assertEquals("?", opt1.getOpt());
    }

    @Test
    public void testSpecialOptChars_test3_decomposed() throws Exception {
        OptionBuilder.withDescription("help options");
        final Option opt1 = OptionBuilder.withDescription("help options").create1('?');
        assertEquals("?", opt1.getOpt());
        OptionBuilder.withDescription("read from stdin");
    }

    @Test
    public void testSpecialOptChars_test4_decomposed() throws Exception {
        OptionBuilder.withDescription("help options");
        final Option opt1 = OptionBuilder.withDescription("help options").create1('?');
        assertEquals("?", opt1.getOpt());
        OptionBuilder.withDescription("read from stdin");
        final Option opt2 = OptionBuilder.withDescription("read from stdin").create1('@');
    }

    @Test
    public void testSpecialOptChars_test5_decomposed() throws Exception {
        OptionBuilder.withDescription("help options");
        final Option opt1 = OptionBuilder.withDescription("help options").create1('?');
        assertEquals("?", opt1.getOpt());
        OptionBuilder.withDescription("read from stdin");
        final Option opt2 = OptionBuilder.withDescription("read from stdin").create1('@');
        assertEquals("@", opt2.getOpt());
    }

    @Test
    public void testSpecialOptChars_test6_decomposed() throws Exception {
        OptionBuilder.withDescription("help options");
        final Option opt1 = OptionBuilder.withDescription("help options").create1('?');
        assertEquals("?", opt1.getOpt());
        OptionBuilder.withDescription("read from stdin");
        final Option opt2 = OptionBuilder.withDescription("read from stdin").create1('@');
        assertEquals("@", opt2.getOpt());
        try {
            OptionBuilder.create1(' ');
            fail("IllegalArgumentException not caught");
        } catch (final IllegalArgumentException e) {
        }
    }

    @Test
    public void testTwoCompleteOptions_test0_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
    }

    @Test
    public void testTwoCompleteOptions_test1_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
    }

    @Test
    public void testTwoCompleteOptions_test2_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
    }

    @Test
    public void testTwoCompleteOptions_test3_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
    }

    @Test
    public void testTwoCompleteOptions_test4_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
    }

    @Test
    public void testTwoCompleteOptions_test5_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
    }

    @Test
    public void testTwoCompleteOptions_test6_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
    }

    @Test
    public void testTwoCompleteOptions_test7_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
    }

    @Test
    public void testTwoCompleteOptions_test8_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
        assertEquals("simple option", simple.getLongOpt());
    }

    @Test
    public void testTwoCompleteOptions_test9_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
        assertEquals("simple option", simple.getLongOpt());
        assertEquals("this is a simple option", simple.getDescription());
    }

    @Test
    public void testTwoCompleteOptions_test10_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
        assertEquals("simple option", simple.getLongOpt());
        assertEquals("this is a simple option", simple.getDescription());
        assertEquals(simple.getType(), Float.class);
    }

    @Test
    public void testTwoCompleteOptions_test11_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
        assertEquals("simple option", simple.getLongOpt());
        assertEquals("this is a simple option", simple.getDescription());
        assertEquals(simple.getType(), Float.class);
        assertTrue(simple.hasArg());
    }

    @Test
    public void testTwoCompleteOptions_test12_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
        assertEquals("simple option", simple.getLongOpt());
        assertEquals("this is a simple option", simple.getDescription());
        assertEquals(simple.getType(), Float.class);
        assertTrue(simple.hasArg());
        assertTrue(simple.isRequired());
    }

    @Test
    public void testTwoCompleteOptions_test13_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
        assertEquals("simple option", simple.getLongOpt());
        assertEquals("this is a simple option", simple.getDescription());
        assertEquals(simple.getType(), Float.class);
        assertTrue(simple.hasArg());
        assertTrue(simple.isRequired());
        assertTrue(simple.hasArgs());
    }

    @Test
    public void testTwoCompleteOptions_test14_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
        assertEquals("simple option", simple.getLongOpt());
        assertEquals("this is a simple option", simple.getDescription());
        assertEquals(simple.getType(), Float.class);
        assertTrue(simple.hasArg());
        assertTrue(simple.isRequired());
        assertTrue(simple.hasArgs());
        OptionBuilder.withLongOpt("dimple option");
    }

    @Test
    public void testTwoCompleteOptions_test15_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
        assertEquals("simple option", simple.getLongOpt());
        assertEquals("this is a simple option", simple.getDescription());
        assertEquals(simple.getType(), Float.class);
        assertTrue(simple.hasArg());
        assertTrue(simple.isRequired());
        assertTrue(simple.hasArgs());
        OptionBuilder.withLongOpt("dimple option");
        OptionBuilder.withLongOpt("dimple option").hasArg0();
    }

    @Test
    public void testTwoCompleteOptions_test16_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
        assertEquals("simple option", simple.getLongOpt());
        assertEquals("this is a simple option", simple.getDescription());
        assertEquals(simple.getType(), Float.class);
        assertTrue(simple.hasArg());
        assertTrue(simple.isRequired());
        assertTrue(simple.hasArgs());
        OptionBuilder.withLongOpt("dimple option");
        OptionBuilder.withLongOpt("dimple option").hasArg0();
        OptionBuilder.withLongOpt("dimple option").hasArg0().withDescription("this is a dimple option");
    }

    @Test
    public void testTwoCompleteOptions_test17_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
        assertEquals("simple option", simple.getLongOpt());
        assertEquals("this is a simple option", simple.getDescription());
        assertEquals(simple.getType(), Float.class);
        assertTrue(simple.hasArg());
        assertTrue(simple.isRequired());
        assertTrue(simple.hasArgs());
        OptionBuilder.withLongOpt("dimple option");
        OptionBuilder.withLongOpt("dimple option").hasArg0();
        OptionBuilder.withLongOpt("dimple option").hasArg0().withDescription("this is a dimple option");
        simple =
                OptionBuilder.withLongOpt("dimple option")
                        .hasArg0()
                        .withDescription("this is a dimple option")
                        .create1('d');
    }

    @Test
    public void testTwoCompleteOptions_test18_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
        assertEquals("simple option", simple.getLongOpt());
        assertEquals("this is a simple option", simple.getDescription());
        assertEquals(simple.getType(), Float.class);
        assertTrue(simple.hasArg());
        assertTrue(simple.isRequired());
        assertTrue(simple.hasArgs());
        OptionBuilder.withLongOpt("dimple option");
        OptionBuilder.withLongOpt("dimple option").hasArg0();
        OptionBuilder.withLongOpt("dimple option").hasArg0().withDescription("this is a dimple option");
        simple =
                OptionBuilder.withLongOpt("dimple option")
                        .hasArg0()
                        .withDescription("this is a dimple option")
                        .create1('d');
        assertEquals("d", simple.getOpt());
    }

    @Test
    public void testTwoCompleteOptions_test19_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
        assertEquals("simple option", simple.getLongOpt());
        assertEquals("this is a simple option", simple.getDescription());
        assertEquals(simple.getType(), Float.class);
        assertTrue(simple.hasArg());
        assertTrue(simple.isRequired());
        assertTrue(simple.hasArgs());
        OptionBuilder.withLongOpt("dimple option");
        OptionBuilder.withLongOpt("dimple option").hasArg0();
        OptionBuilder.withLongOpt("dimple option").hasArg0().withDescription("this is a dimple option");
        simple =
                OptionBuilder.withLongOpt("dimple option")
                        .hasArg0()
                        .withDescription("this is a dimple option")
                        .create1('d');
        assertEquals("d", simple.getOpt());
        assertEquals("dimple option", simple.getLongOpt());
    }

    @Test
    public void testTwoCompleteOptions_test20_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
        assertEquals("simple option", simple.getLongOpt());
        assertEquals("this is a simple option", simple.getDescription());
        assertEquals(simple.getType(), Float.class);
        assertTrue(simple.hasArg());
        assertTrue(simple.isRequired());
        assertTrue(simple.hasArgs());
        OptionBuilder.withLongOpt("dimple option");
        OptionBuilder.withLongOpt("dimple option").hasArg0();
        OptionBuilder.withLongOpt("dimple option").hasArg0().withDescription("this is a dimple option");
        simple =
                OptionBuilder.withLongOpt("dimple option")
                        .hasArg0()
                        .withDescription("this is a dimple option")
                        .create1('d');
        assertEquals("d", simple.getOpt());
        assertEquals("dimple option", simple.getLongOpt());
        assertEquals("this is a dimple option", simple.getDescription());
    }

    @Test
    public void testTwoCompleteOptions_test21_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
        assertEquals("simple option", simple.getLongOpt());
        assertEquals("this is a simple option", simple.getDescription());
        assertEquals(simple.getType(), Float.class);
        assertTrue(simple.hasArg());
        assertTrue(simple.isRequired());
        assertTrue(simple.hasArgs());
        OptionBuilder.withLongOpt("dimple option");
        OptionBuilder.withLongOpt("dimple option").hasArg0();
        OptionBuilder.withLongOpt("dimple option").hasArg0().withDescription("this is a dimple option");
        simple =
                OptionBuilder.withLongOpt("dimple option")
                        .hasArg0()
                        .withDescription("this is a dimple option")
                        .create1('d');
        assertEquals("d", simple.getOpt());
        assertEquals("dimple option", simple.getLongOpt());
        assertEquals("this is a dimple option", simple.getDescription());
        assertEquals(String.class, simple.getType());
    }

    @Test
    public void testTwoCompleteOptions_test22_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
        assertEquals("simple option", simple.getLongOpt());
        assertEquals("this is a simple option", simple.getDescription());
        assertEquals(simple.getType(), Float.class);
        assertTrue(simple.hasArg());
        assertTrue(simple.isRequired());
        assertTrue(simple.hasArgs());
        OptionBuilder.withLongOpt("dimple option");
        OptionBuilder.withLongOpt("dimple option").hasArg0();
        OptionBuilder.withLongOpt("dimple option").hasArg0().withDescription("this is a dimple option");
        simple =
                OptionBuilder.withLongOpt("dimple option")
                        .hasArg0()
                        .withDescription("this is a dimple option")
                        .create1('d');
        assertEquals("d", simple.getOpt());
        assertEquals("dimple option", simple.getLongOpt());
        assertEquals("this is a dimple option", simple.getDescription());
        assertEquals(String.class, simple.getType());
        assertTrue(simple.hasArg());
    }

    @Test
    public void testTwoCompleteOptions_test23_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
        assertEquals("simple option", simple.getLongOpt());
        assertEquals("this is a simple option", simple.getDescription());
        assertEquals(simple.getType(), Float.class);
        assertTrue(simple.hasArg());
        assertTrue(simple.isRequired());
        assertTrue(simple.hasArgs());
        OptionBuilder.withLongOpt("dimple option");
        OptionBuilder.withLongOpt("dimple option").hasArg0();
        OptionBuilder.withLongOpt("dimple option").hasArg0().withDescription("this is a dimple option");
        simple =
                OptionBuilder.withLongOpt("dimple option")
                        .hasArg0()
                        .withDescription("this is a dimple option")
                        .create1('d');
        assertEquals("d", simple.getOpt());
        assertEquals("dimple option", simple.getLongOpt());
        assertEquals("this is a dimple option", simple.getDescription());
        assertEquals(String.class, simple.getType());
        assertTrue(simple.hasArg());
        assertFalse(simple.isRequired());
    }

    @Test
    public void testTwoCompleteOptions_test24_decomposed()  {
        OptionBuilder.withLongOpt("simple option");
        OptionBuilder.withLongOpt("simple option").hasArg0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0();
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class);
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0().withType0(Float.class).withDescription("this is a simple option");
        Option simple =
                OptionBuilder.withLongOpt("simple option")
                        .hasArg0()
                        .isRequired0()
                        .hasArgs0()
                        .withType0(Float.class)
                        .withDescription("this is a simple option")
                        .create1('s');
        assertEquals("s", simple.getOpt());
        assertEquals("simple option", simple.getLongOpt());
        assertEquals("this is a simple option", simple.getDescription());
        assertEquals(simple.getType(), Float.class);
        assertTrue(simple.hasArg());
        assertTrue(simple.isRequired());
        assertTrue(simple.hasArgs());
        OptionBuilder.withLongOpt("dimple option");
        OptionBuilder.withLongOpt("dimple option").hasArg0();
        OptionBuilder.withLongOpt("dimple option").hasArg0().withDescription("this is a dimple option");
        simple =
                OptionBuilder.withLongOpt("dimple option")
                        .hasArg0()
                        .withDescription("this is a dimple option")
                        .create1('d');
        assertEquals("d", simple.getOpt());
        assertEquals("dimple option", simple.getLongOpt());
        assertEquals("this is a dimple option", simple.getDescription());
        assertEquals(String.class, simple.getType());
        assertTrue(simple.hasArg());
        assertFalse(simple.isRequired());
        assertFalse(simple.hasArgs());
    }
}