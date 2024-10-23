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
package org.apache.commons.validator.util;
import org.junit.Test;

import junit.framework.TestCase;

/**
 * Test the Flags class.
 *
 * @version $Revision$
 */
public class FlagsTest extends TestCase {

    /** Declare some flags for testing. */
    private static final long LONG_FLAG = 1;

    private static final long LONG_FLAG_2 = 2;
    private static final int INT_FLAG = 4;

    /** Constructor for FlagsTest. */
    public FlagsTest(String name) {
        super(name);
    }

    

    

    

    

    

    

    

    

    

    

    /** Test for Object clone() */
    

    /** Test for boolean equals(Object) */
    

    /** Test for String toString() */

    @Test
    public void testHashCode_test0_decomposed()  {
        Flags f = new Flags(1, 45);
    }

    @Test
    public void testHashCode_test1_decomposed()  {
        Flags f = new Flags(1, 45);
        assertEquals(f.hashCode(), 45);
    }

    @Test
    public void testGetFlags_test0_decomposed()  {
        Flags f = new Flags(1, 45);
    }

    @Test
    public void testGetFlags_test1_decomposed()  {
        Flags f = new Flags(1, 45);
        assertEquals(f.getFlags(), 45);
    }

    @Test
    public void testIsOnOff_test0_decomposed()  {
        Flags f = new Flags(0, 0);
    }

    @Test
    public void testIsOnOff_test1_decomposed()  {
        Flags f = new Flags(0, 0);
        f.turnOn(LONG_FLAG);
        f.turnOn(INT_FLAG);
    }

    @Test
    public void testIsOnOff_test2_decomposed()  {
        Flags f = new Flags(0, 0);
        f.turnOn(LONG_FLAG);
        f.turnOn(INT_FLAG);
        assertTrue(f.isOn(LONG_FLAG));
    }

    @Test
    public void testIsOnOff_test3_decomposed()  {
        Flags f = new Flags(0, 0);
        f.turnOn(LONG_FLAG);
        f.turnOn(INT_FLAG);
        assertTrue(f.isOn(LONG_FLAG));
        assertTrue(!f.isOff(LONG_FLAG));
    }

    @Test
    public void testIsOnOff_test4_decomposed()  {
        Flags f = new Flags(0, 0);
        f.turnOn(LONG_FLAG);
        f.turnOn(INT_FLAG);
        assertTrue(f.isOn(LONG_FLAG));
        assertTrue(!f.isOff(LONG_FLAG));
        assertTrue(f.isOn(INT_FLAG));
    }

    @Test
    public void testIsOnOff_test5_decomposed()  {
        Flags f = new Flags(0, 0);
        f.turnOn(LONG_FLAG);
        f.turnOn(INT_FLAG);
        assertTrue(f.isOn(LONG_FLAG));
        assertTrue(!f.isOff(LONG_FLAG));
        assertTrue(f.isOn(INT_FLAG));
        assertTrue(!f.isOff(INT_FLAG));
        assertTrue(f.isOff(LONG_FLAG_2));
    }

    @Test
    public void testTurnOffAll_test0_decomposed()  {
        Flags f = new Flags(1, 98432);
    }

    @Test
    public void testTurnOffAll_test1_decomposed()  {
        Flags f = new Flags(1, 98432);
        f.turnOffAll();
    }

    @Test
    public void testTurnOffAll_test2_decomposed()  {
        Flags f = new Flags(1, 98432);
        f.turnOffAll();
        assertEquals(0, f.getFlags());
    }

    @Test
    public void testClear_test0_decomposed()  {
        Flags f = new Flags(1, 98432);
    }

    @Test
    public void testClear_test1_decomposed()  {
        Flags f = new Flags(1, 98432);
        f.clear();
    }

    @Test
    public void testClear_test2_decomposed()  {
        Flags f = new Flags(1, 98432);
        f.clear();
        assertEquals(0, f.getFlags());
    }

    @Test
    public void testTurnOnAll_test0_decomposed()  {
        Flags f = new Flags(0, 0);
    }

    @Test
    public void testTurnOnAll_test1_decomposed()  {
        Flags f = new Flags(0, 0);
        f.turnOnAll();
    }

    @Test
    public void testTurnOnAll_test2_decomposed()  {
        Flags f = new Flags(0, 0);
        f.turnOnAll();
        assertEquals(~0, f.getFlags());
    }

    @Test
    public void testIsOn_isFalseWhenNotAllFlagsInArgumentAreOn_test0_decomposed()  {
        Flags first = new Flags(1, 1);
    }

    @Test
    public void testIsOn_isFalseWhenNotAllFlagsInArgumentAreOn_test1_decomposed()  {
        Flags first = new Flags(1, 1);
        long firstAndSecond = 3;
        assertFalse(first.isOn(firstAndSecond));
    }

    @Test
    public void testIsOn_isTrueWhenHighOrderBitIsSetAndQueried_test0_decomposed()  {
        Flags allOn = new Flags(1, ~0);
    }

    @Test
    public void testIsOn_isTrueWhenHighOrderBitIsSetAndQueried_test1_decomposed()  {
        Flags allOn = new Flags(1, ~0);
        long highOrderBit = 0x8000000000000000L;
        assertTrue(allOn.isOn(highOrderBit));
    }

    @Test
    public void testToString_test0_decomposed()  {
        Flags f = new Flags(0, 0);
    }

    @Test
    public void testToString_test1_decomposed()  {
        Flags f = new Flags(0, 0);
        String s = f.toString();
    }

    @Test
    public void testToString_test2_decomposed()  {
        Flags f = new Flags(0, 0);
        String s = f.toString();
        assertEquals(64, s.length());
        f.turnOn(INT_FLAG);
    }

    @Test
    public void testToString_test3_decomposed()  {
        Flags f = new Flags(0, 0);
        String s = f.toString();
        assertEquals(64, s.length());
        f.turnOn(INT_FLAG);
        s = f.toString();
    }

    @Test
    public void testToString_test4_decomposed()  {
        Flags f = new Flags(0, 0);
        String s = f.toString();
        assertEquals(64, s.length());
        f.turnOn(INT_FLAG);
        s = f.toString();
        assertEquals(64, s.length());
        assertEquals("0000000000000000000000000000000000000000000000000000000000000100", s);
    }
}