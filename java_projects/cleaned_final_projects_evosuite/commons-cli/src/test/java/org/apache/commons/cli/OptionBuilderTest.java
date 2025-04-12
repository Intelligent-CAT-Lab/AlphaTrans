
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
    public void testBaseOptionCharOpt() {
        final Option base = OptionBuilder.withDescription("option description").create1('o');

        assertEquals("o", base.getOpt());
        assertEquals("option description", base.getDescription());
        assertFalse(base.hasArg());
    }

    @Test
    public void testBaseOptionStringOpt() {
        final Option base = OptionBuilder.withDescription("option description").create2("o");

        assertEquals("o", base.getOpt());
        assertEquals("option description", base.getDescription());
        assertFalse(base.hasArg());
    }

    @Test
    public void testBuilderIsResettedAlways() {
        try {
            OptionBuilder.withDescription("JUnit").create1('"');
            fail("IllegalArgumentException expected");
        } catch (final IllegalArgumentException e) {
        }
        assertNull("we inherited a description", OptionBuilder.create1('x').getDescription());

        try {
            OptionBuilder.withDescription("JUnit").create0();
            fail("IllegalArgumentException expected");
        } catch (final IllegalArgumentException e) {
        }
        assertNull("we inherited a description", OptionBuilder.create1('x').getDescription());
    }

    @Test
    public void testCompleteOption() {
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
    public void testCreateIncompleteOption() {
        try {
            OptionBuilder.hasArg0().create0();
            fail("Incomplete option should be rejected");
        } catch (final IllegalArgumentException e) {

            OptionBuilder.create2("opt");
        }
    }

    @Test
    public void testIllegalOptions() {
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
    public void testOptionArgNumbers() {
        final Option opt =
                OptionBuilder.withDescription("option description").hasArgs1(2).create1('o');
        assertEquals(2, opt.getArgs());
    }

    @Test
    public void testSpecialOptChars() throws Exception {
        final Option opt1 = OptionBuilder.withDescription("help options").create1('?');
        assertEquals("?", opt1.getOpt());

        final Option opt2 = OptionBuilder.withDescription("read from stdin").create1('@');
        assertEquals("@", opt2.getOpt());

        try {
            OptionBuilder.create1(' ');
            fail("IllegalArgumentException not caught");
        } catch (final IllegalArgumentException e) {
        }
    }

    @Test
    public void testTwoCompleteOptions() {
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
