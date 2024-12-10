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
package org.apache.commons.validator;
import org.junit.Test;

import junit.framework.TestCase;

/**
 * Test <code>Field</code> objects.
 *
 * @version $Revision$
 */
public class FieldTest extends TestCase {

    protected Field field;

    /** FieldTest constructor. */
    public FieldTest(String name) {
        super(name);
    }

    public static FieldTest FieldTest1() {
        return new FieldTest(null);
    }

    /**
     * FieldTest constructor.
     *
     * @param name
     */

    /** Test setup */
    @Override
    public void setUp() {
        field = new Field();
    }

    /** Test clean up */
    @Override
    public void tearDown() {
        field = null;
    }

    /** test Field with no arguments */
    

    /** test Field with only 'default' arguments, no positions specified. */
    

    /** test Field with only 'default' arguments, positions specified. */
    

    /** test Field with only 'default' arguments, position specified for one argument */
    

    /** test Field with only 'default' arguments, some position specified. */
    

    /** test Field with a 'default' argument overriden using 'position' property */
    

    /** test Field with a 'default' argument overriden using 'position' property */
    

    /** test Field with a 'default' argument overriden without positions specified. */
    

    /** test Field with a 'default' argument overriden with some positions specified */
    

    /** Convenience Method - create argument (no name or position specified) */
    private Arg createArg0(String key) {
        Arg arg = new Arg();
        arg.setKey(key);
        return arg;
    }

    /** Convenience Method - create argument (no name, position specified) */
    private Arg createArg1(String key, int position) {
        Arg arg = createArg0(key);
        arg.setPosition(position);
        return arg;
    }

    /** Convenience Method - create argument (name specified, no position) */
    private Arg createArg2(String key, String name) {
        Arg arg = createArg0(key);
        arg.setName(name);
        return arg;
    }

    /** Convenience Method - create argument (name & position specified) */
    private Arg createArg3(String key, String name, int position) {
        Arg arg = createArg2(key, name);
        arg.setPosition(position);
        return arg;
    }

    @Test
    public void testEmptyArgs_test0_decomposed()  {
        assertEquals("Empty Args(1) ", 0, field.getArgs("required").length);
    }

    @Test
    public void testDefaultPositionImplied_test0_decomposed()  {
        createArg0("default-position-0");
    }

    @Test
    public void testDefaultPositionImplied_test1_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
    }

    @Test
    public void testDefaultPositionImplied_test2_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
    }

    @Test
    public void testDefaultPositionImplied_test3_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
    }

    @Test
    public void testDefaultPositionImplied_test4_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
    }

    @Test
    public void testDefaultPositionImplied_test5_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
    }

    @Test
    public void testDefaultPositionImplied_test6_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testDefaultPositionImplied(1) ", 3, field.getArgs("required").length);
    }

    @Test
    public void testDefaultPositionImplied_test7_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testDefaultPositionImplied(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
    }

    @Test
    public void testDefaultPositionImplied_test8_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testDefaultPositionImplied(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testDefaultPositionImplied(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
    }

    @Test
    public void testDefaultPositionImplied_test9_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testDefaultPositionImplied(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testDefaultPositionImplied(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
    }

    @Test
    public void testDefaultPositionImplied_test10_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testDefaultPositionImplied(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testDefaultPositionImplied(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testDefaultPositionImplied(3) ",
                "default-position-1",
                field.getArg1("required", 1).getKey());
    }

    @Test
    public void testDefaultPositionImplied_test11_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testDefaultPositionImplied(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testDefaultPositionImplied(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testDefaultPositionImplied(3) ",
                "default-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
    }

    @Test
    public void testDefaultPositionImplied_test12_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testDefaultPositionImplied(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testDefaultPositionImplied(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testDefaultPositionImplied(3) ",
                "default-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testDefaultPositionImplied(4) ",
                "default-position-2",
                field.getArg1("required", 2).getKey());
    }

    @Test
    public void testDefaultUsingPositions_test0_decomposed()  {
        createArg1("default-position-1",1);
    }

    @Test
    public void testDefaultUsingPositions_test1_decomposed()  {
        createArg1("default-position-1",1);
        field.addArg(createArg1("default-position-1", 1));
    }

    @Test
    public void testDefaultUsingPositions_test2_decomposed()  {
        createArg1("default-position-1",1);
        field.addArg(createArg1("default-position-1", 1));
        createArg1("default-position-0",0);
    }

    @Test
    public void testDefaultUsingPositions_test3_decomposed()  {
        createArg1("default-position-1",1);
        field.addArg(createArg1("default-position-1", 1));
        createArg1("default-position-0",0);
        field.addArg(createArg1("default-position-0", 0));
    }

    @Test
    public void testDefaultUsingPositions_test4_decomposed()  {
        createArg1("default-position-1",1);
        field.addArg(createArg1("default-position-1", 1));
        createArg1("default-position-0",0);
        field.addArg(createArg1("default-position-0", 0));
        createArg1("default-position-2",2);
    }

    @Test
    public void testDefaultUsingPositions_test5_decomposed()  {
        createArg1("default-position-1",1);
        field.addArg(createArg1("default-position-1", 1));
        createArg1("default-position-0",0);
        field.addArg(createArg1("default-position-0", 0));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
    }

    @Test
    public void testDefaultUsingPositions_test6_decomposed()  {
        createArg1("default-position-1",1);
        field.addArg(createArg1("default-position-1", 1));
        createArg1("default-position-0",0);
        field.addArg(createArg1("default-position-0", 0));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        assertEquals("testDefaultUsingPositions(1) ", 3, field.getArgs("required").length);
    }

    @Test
    public void testDefaultUsingPositions_test7_decomposed()  {
        createArg1("default-position-1",1);
        field.addArg(createArg1("default-position-1", 1));
        createArg1("default-position-0",0);
        field.addArg(createArg1("default-position-0", 0));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        assertEquals("testDefaultUsingPositions(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
    }

    @Test
    public void testDefaultUsingPositions_test8_decomposed()  {
        createArg1("default-position-1",1);
        field.addArg(createArg1("default-position-1", 1));
        createArg1("default-position-0",0);
        field.addArg(createArg1("default-position-0", 0));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        assertEquals("testDefaultUsingPositions(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testDefaultUsingPositions(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
    }

    @Test
    public void testDefaultUsingPositions_test9_decomposed()  {
        createArg1("default-position-1",1);
        field.addArg(createArg1("default-position-1", 1));
        createArg1("default-position-0",0);
        field.addArg(createArg1("default-position-0", 0));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        assertEquals("testDefaultUsingPositions(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testDefaultUsingPositions(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
    }

    @Test
    public void testDefaultUsingPositions_test10_decomposed()  {
        createArg1("default-position-1",1);
        field.addArg(createArg1("default-position-1", 1));
        createArg1("default-position-0",0);
        field.addArg(createArg1("default-position-0", 0));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        assertEquals("testDefaultUsingPositions(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testDefaultUsingPositions(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testDefaultUsingPositions(3) ",
                "default-position-1",
                field.getArg1("required", 1).getKey());
    }

    @Test
    public void testDefaultUsingPositions_test11_decomposed()  {
        createArg1("default-position-1",1);
        field.addArg(createArg1("default-position-1", 1));
        createArg1("default-position-0",0);
        field.addArg(createArg1("default-position-0", 0));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        assertEquals("testDefaultUsingPositions(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testDefaultUsingPositions(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testDefaultUsingPositions(3) ",
                "default-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
    }

    @Test
    public void testDefaultUsingPositions_test12_decomposed()  {
        createArg1("default-position-1",1);
        field.addArg(createArg1("default-position-1", 1));
        createArg1("default-position-0",0);
        field.addArg(createArg1("default-position-0", 0));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        assertEquals("testDefaultUsingPositions(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testDefaultUsingPositions(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testDefaultUsingPositions(3) ",
                "default-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testDefaultUsingPositions(4) ",
                "default-position-2",
                field.getArg1("required", 2).getKey());
    }

    @Test
    public void testDefaultOnePosition_test0_decomposed()  {
        createArg0("default-position-0");
    }

    @Test
    public void testDefaultOnePosition_test1_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
    }

    @Test
    public void testDefaultOnePosition_test2_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
    }

    @Test
    public void testDefaultOnePosition_test3_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
    }

    @Test
    public void testDefaultOnePosition_test4_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        createArg0("default-position-3");
    }

    @Test
    public void testDefaultOnePosition_test5_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        createArg0("default-position-3");
        field.addArg(createArg0("default-position-3"));
    }

    @Test
    public void testDefaultOnePosition_test6_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        createArg0("default-position-3");
        field.addArg(createArg0("default-position-3"));
        assertEquals("testDefaultOnePosition(1) ", 4, field.getArgs("required").length);
    }

    @Test
    public void testDefaultOnePosition_test7_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        createArg0("default-position-3");
        field.addArg(createArg0("default-position-3"));
        assertEquals("testDefaultOnePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
    }

    @Test
    public void testDefaultOnePosition_test8_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        createArg0("default-position-3");
        field.addArg(createArg0("default-position-3"));
        assertEquals("testDefaultOnePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testDefaultOnePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
    }

    @Test
    public void testDefaultOnePosition_test9_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        createArg0("default-position-3");
        field.addArg(createArg0("default-position-3"));
        assertEquals("testDefaultOnePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testDefaultOnePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        assertNull("testDefaultOnePosition(3) ", field.getArg1("required", 1));
        field.getArg1("required",2);
    }

    @Test
    public void testDefaultOnePosition_test10_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        createArg0("default-position-3");
        field.addArg(createArg0("default-position-3"));
        assertEquals("testDefaultOnePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testDefaultOnePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        assertNull("testDefaultOnePosition(3) ", field.getArg1("required", 1));
        field.getArg1("required",2);
        assertEquals(
                "testDefaultOnePosition(4) ",
                "default-position-2",
                field.getArg1("required", 2).getKey());
    }

    @Test
    public void testDefaultOnePosition_test11_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        createArg0("default-position-3");
        field.addArg(createArg0("default-position-3"));
        assertEquals("testDefaultOnePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testDefaultOnePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        assertNull("testDefaultOnePosition(3) ", field.getArg1("required", 1));
        field.getArg1("required",2);
        assertEquals(
                "testDefaultOnePosition(4) ",
                "default-position-2",
                field.getArg1("required", 2).getKey());
        field.getArg1("required",3);
    }

    @Test
    public void testDefaultOnePosition_test12_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        createArg0("default-position-3");
        field.addArg(createArg0("default-position-3"));
        assertEquals("testDefaultOnePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testDefaultOnePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        assertNull("testDefaultOnePosition(3) ", field.getArg1("required", 1));
        field.getArg1("required",2);
        assertEquals(
                "testDefaultOnePosition(4) ",
                "default-position-2",
                field.getArg1("required", 2).getKey());
        field.getArg1("required",3);
        assertEquals(
                "testDefaultOnePosition(5) ",
                "default-position-3",
                field.getArg1("required", 3).getKey());
    }

    @Test
    public void testDefaultSomePositions_test0_decomposed()  {
        createArg0("default-position-0");
    }

    @Test
    public void testDefaultSomePositions_test1_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
    }

    @Test
    public void testDefaultSomePositions_test2_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
    }

    @Test
    public void testDefaultSomePositions_test3_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
    }

    @Test
    public void testDefaultSomePositions_test4_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        createArg0("default-position-3");
    }

    @Test
    public void testDefaultSomePositions_test5_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        createArg0("default-position-3");
        field.addArg(createArg0("default-position-3"));
    }

    @Test
    public void testDefaultSomePositions_test6_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        createArg0("default-position-3");
        field.addArg(createArg0("default-position-3"));
        createArg1("default-position-1",1);
    }

    @Test
    public void testDefaultSomePositions_test7_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        createArg0("default-position-3");
        field.addArg(createArg0("default-position-3"));
        createArg1("default-position-1",1);
        field.addArg(createArg1("default-position-1", 1));
    }

    @Test
    public void testDefaultSomePositions_test8_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        createArg0("default-position-3");
        field.addArg(createArg0("default-position-3"));
        createArg1("default-position-1",1);
        field.addArg(createArg1("default-position-1", 1));
        assertEquals("testDefaultSomePositions(1) ", 4, field.getArgs("required").length);
    }

    @Test
    public void testDefaultSomePositions_test9_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        createArg0("default-position-3");
        field.addArg(createArg0("default-position-3"));
        createArg1("default-position-1",1);
        field.addArg(createArg1("default-position-1", 1));
        assertEquals("testDefaultSomePositions(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
    }

    @Test
    public void testDefaultSomePositions_test10_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        createArg0("default-position-3");
        field.addArg(createArg0("default-position-3"));
        createArg1("default-position-1",1);
        field.addArg(createArg1("default-position-1", 1));
        assertEquals("testDefaultSomePositions(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testDefaultSomePositions(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
    }

    @Test
    public void testDefaultSomePositions_test11_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        createArg0("default-position-3");
        field.addArg(createArg0("default-position-3"));
        createArg1("default-position-1",1);
        field.addArg(createArg1("default-position-1", 1));
        assertEquals("testDefaultSomePositions(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testDefaultSomePositions(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
    }

    @Test
    public void testDefaultSomePositions_test12_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        createArg0("default-position-3");
        field.addArg(createArg0("default-position-3"));
        createArg1("default-position-1",1);
        field.addArg(createArg1("default-position-1", 1));
        assertEquals("testDefaultSomePositions(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testDefaultSomePositions(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testDefaultSomePositions(3) ",
                "default-position-1",
                field.getArg1("required", 1).getKey());
    }

    @Test
    public void testDefaultSomePositions_test13_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        createArg0("default-position-3");
        field.addArg(createArg0("default-position-3"));
        createArg1("default-position-1",1);
        field.addArg(createArg1("default-position-1", 1));
        assertEquals("testDefaultSomePositions(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testDefaultSomePositions(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testDefaultSomePositions(3) ",
                "default-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
    }

    @Test
    public void testDefaultSomePositions_test14_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        createArg0("default-position-3");
        field.addArg(createArg0("default-position-3"));
        createArg1("default-position-1",1);
        field.addArg(createArg1("default-position-1", 1));
        assertEquals("testDefaultSomePositions(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testDefaultSomePositions(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testDefaultSomePositions(3) ",
                "default-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testDefaultSomePositions(4) ",
                "default-position-2",
                field.getArg1("required", 2).getKey());
    }

    @Test
    public void testDefaultSomePositions_test15_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        createArg0("default-position-3");
        field.addArg(createArg0("default-position-3"));
        createArg1("default-position-1",1);
        field.addArg(createArg1("default-position-1", 1));
        assertEquals("testDefaultSomePositions(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testDefaultSomePositions(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testDefaultSomePositions(3) ",
                "default-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testDefaultSomePositions(4) ",
                "default-position-2",
                field.getArg1("required", 2).getKey());
        field.getArg1("required",3);
    }

    @Test
    public void testDefaultSomePositions_test16_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg1("default-position-2",2);
        field.addArg(createArg1("default-position-2", 2));
        createArg0("default-position-3");
        field.addArg(createArg0("default-position-3"));
        createArg1("default-position-1",1);
        field.addArg(createArg1("default-position-1", 1));
        assertEquals("testDefaultSomePositions(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testDefaultSomePositions(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testDefaultSomePositions(3) ",
                "default-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testDefaultSomePositions(4) ",
                "default-position-2",
                field.getArg1("required", 2).getKey());
        field.getArg1("required",3);
        assertEquals(
                "testDefaultSomePositions(5) ",
                "default-position-3",
                field.getArg1("required", 3).getKey());
    }

    @Test
    public void testOverrideUsingPositionA_test0_decomposed()  {
        createArg0("default-position-0");
    }

    @Test
    public void testOverrideUsingPositionA_test1_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
    }

    @Test
    public void testOverrideUsingPositionA_test2_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
    }

    @Test
    public void testOverrideUsingPositionA_test3_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
    }

    @Test
    public void testOverrideUsingPositionA_test4_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
    }

    @Test
    public void testOverrideUsingPositionA_test5_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
    }

    @Test
    public void testOverrideUsingPositionA_test6_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
    }

    @Test
    public void testOverrideUsingPositionA_test7_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
    }

    @Test
    public void testOverrideUsingPositionA_test8_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        assertEquals("testOverrideUsingPositionA(1) ", 3, field.getArgs("required").length);
    }

    @Test
    public void testOverrideUsingPositionA_test9_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        assertEquals("testOverrideUsingPositionA(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",1);
    }

    @Test
    public void testOverrideUsingPositionA_test10_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        assertEquals("testOverrideUsingPositionA(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",1);
        assertEquals(
                "testOverrideUsingPositionA(2) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
    }

    @Test
    public void testOverrideUsingPositionA_test11_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        assertEquals("testOverrideUsingPositionA(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",1);
        assertEquals(
                "testOverrideUsingPositionA(2) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        assertEquals("testOverrideUsingPositionA(3) ", 3, field.getArgs("mask").length);
    }

    @Test
    public void testOverrideUsingPositionA_test12_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        assertEquals("testOverrideUsingPositionA(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",1);
        assertEquals(
                "testOverrideUsingPositionA(2) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        assertEquals("testOverrideUsingPositionA(3) ", 3, field.getArgs("mask").length);
        field.getArg1("mask",1);
    }

    @Test
    public void testOverrideUsingPositionA_test13_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        assertEquals("testOverrideUsingPositionA(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",1);
        assertEquals(
                "testOverrideUsingPositionA(2) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        assertEquals("testOverrideUsingPositionA(3) ", 3, field.getArgs("mask").length);
        field.getArg1("mask",1);
        assertEquals(
                "testOverrideUsingPositionA(4) ",
                "default-position-1",
                field.getArg1("mask", 1).getKey());
    }

    @Test
    public void testOverrideUsingPositionA_test14_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        assertEquals("testOverrideUsingPositionA(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",1);
        assertEquals(
                "testOverrideUsingPositionA(2) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        assertEquals("testOverrideUsingPositionA(3) ", 3, field.getArgs("mask").length);
        field.getArg1("mask",1);
        assertEquals(
                "testOverrideUsingPositionA(4) ",
                "default-position-1",
                field.getArg1("mask", 1).getKey());
        field.getArg0(1);
    }

    @Test
    public void testOverrideUsingPositionA_test15_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        assertEquals("testOverrideUsingPositionA(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",1);
        assertEquals(
                "testOverrideUsingPositionA(2) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        assertEquals("testOverrideUsingPositionA(3) ", 3, field.getArgs("mask").length);
        field.getArg1("mask",1);
        assertEquals(
                "testOverrideUsingPositionA(4) ",
                "default-position-1",
                field.getArg1("mask", 1).getKey());
        field.getArg0(1);
        assertEquals(
                "testOverrideUsingPositionA(5) ", "default-position-1", field.getArg0(1).getKey());
    }

    @Test
    public void testOverrideUsingPositionB_test0_decomposed()  {
        createArg3("required-position-3","required",3);
    }

    @Test
    public void testOverrideUsingPositionB_test1_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
    }

    @Test
    public void testOverrideUsingPositionB_test2_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
    }

    @Test
    public void testOverrideUsingPositionB_test3_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
    }

    @Test
    public void testOverrideUsingPositionB_test4_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg0("default-position-0");
    }

    @Test
    public void testOverrideUsingPositionB_test5_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
    }

    @Test
    public void testOverrideUsingPositionB_test6_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
    }

    @Test
    public void testOverrideUsingPositionB_test7_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
    }

    @Test
    public void testOverrideUsingPositionB_test8_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
    }

    @Test
    public void testOverrideUsingPositionB_test9_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
    }

    @Test
    public void testOverrideUsingPositionB_test10_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testOverrideUsingPositionB(1) ", 4, field.getArgs("required").length);
    }

    @Test
    public void testOverrideUsingPositionB_test11_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testOverrideUsingPositionB(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
    }

    @Test
    public void testOverrideUsingPositionB_test12_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testOverrideUsingPositionB(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideUsingPositionB(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
    }

    @Test
    public void testOverrideUsingPositionB_test13_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testOverrideUsingPositionB(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideUsingPositionB(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
    }

    @Test
    public void testOverrideUsingPositionB_test14_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testOverrideUsingPositionB(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideUsingPositionB(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideUsingPositionB(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
    }

    @Test
    public void testOverrideUsingPositionB_test15_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testOverrideUsingPositionB(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideUsingPositionB(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideUsingPositionB(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
    }

    @Test
    public void testOverrideUsingPositionB_test16_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testOverrideUsingPositionB(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideUsingPositionB(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideUsingPositionB(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideUsingPositionB(4) ",
                "default-position-2",
                field.getArg1("required", 2).getKey());
    }

    @Test
    public void testOverrideUsingPositionB_test17_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testOverrideUsingPositionB(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideUsingPositionB(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideUsingPositionB(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideUsingPositionB(4) ",
                "default-position-2",
                field.getArg1("required", 2).getKey());
        field.getArg1("required",3);
    }

    @Test
    public void testOverrideUsingPositionB_test18_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testOverrideUsingPositionB(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideUsingPositionB(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideUsingPositionB(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideUsingPositionB(4) ",
                "default-position-2",
                field.getArg1("required", 2).getKey());
        field.getArg1("required",3);
        assertEquals(
                "testOverrideUsingPositionB(5) ",
                "required-position-3",
                field.getArg1("required", 3).getKey());
    }

    @Test
    public void testOverrideUsingPositionB_test19_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testOverrideUsingPositionB(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideUsingPositionB(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideUsingPositionB(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideUsingPositionB(4) ",
                "default-position-2",
                field.getArg1("required", 2).getKey());
        field.getArg1("required",3);
        assertEquals(
                "testOverrideUsingPositionB(5) ",
                "required-position-3",
                field.getArg1("required", 3).getKey());
        assertEquals("testOverrideUsingPositionB(6) ", 4, field.getArgs("mask").length);
    }

    @Test
    public void testOverrideUsingPositionB_test20_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testOverrideUsingPositionB(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideUsingPositionB(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideUsingPositionB(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideUsingPositionB(4) ",
                "default-position-2",
                field.getArg1("required", 2).getKey());
        field.getArg1("required",3);
        assertEquals(
                "testOverrideUsingPositionB(5) ",
                "required-position-3",
                field.getArg1("required", 3).getKey());
        assertEquals("testOverrideUsingPositionB(6) ", 4, field.getArgs("mask").length);
        field.getArg1("mask",0);
    }

    @Test
    public void testOverrideUsingPositionB_test21_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testOverrideUsingPositionB(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideUsingPositionB(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideUsingPositionB(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideUsingPositionB(4) ",
                "default-position-2",
                field.getArg1("required", 2).getKey());
        field.getArg1("required",3);
        assertEquals(
                "testOverrideUsingPositionB(5) ",
                "required-position-3",
                field.getArg1("required", 3).getKey());
        assertEquals("testOverrideUsingPositionB(6) ", 4, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverrideUsingPositionB(6) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
    }

    @Test
    public void testOverrideUsingPositionB_test22_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testOverrideUsingPositionB(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideUsingPositionB(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideUsingPositionB(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideUsingPositionB(4) ",
                "default-position-2",
                field.getArg1("required", 2).getKey());
        field.getArg1("required",3);
        assertEquals(
                "testOverrideUsingPositionB(5) ",
                "required-position-3",
                field.getArg1("required", 3).getKey());
        assertEquals("testOverrideUsingPositionB(6) ", 4, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverrideUsingPositionB(6) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
    }

    @Test
    public void testOverrideUsingPositionB_test23_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testOverrideUsingPositionB(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideUsingPositionB(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideUsingPositionB(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideUsingPositionB(4) ",
                "default-position-2",
                field.getArg1("required", 2).getKey());
        field.getArg1("required",3);
        assertEquals(
                "testOverrideUsingPositionB(5) ",
                "required-position-3",
                field.getArg1("required", 3).getKey());
        assertEquals("testOverrideUsingPositionB(6) ", 4, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverrideUsingPositionB(6) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
        assertEquals(
                "testOverrideUsingPositionB(7) ",
                "default-position-1",
                field.getArg1("mask", 1).getKey());
    }

    @Test
    public void testOverrideUsingPositionB_test24_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testOverrideUsingPositionB(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideUsingPositionB(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideUsingPositionB(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideUsingPositionB(4) ",
                "default-position-2",
                field.getArg1("required", 2).getKey());
        field.getArg1("required",3);
        assertEquals(
                "testOverrideUsingPositionB(5) ",
                "required-position-3",
                field.getArg1("required", 3).getKey());
        assertEquals("testOverrideUsingPositionB(6) ", 4, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverrideUsingPositionB(6) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
        assertEquals(
                "testOverrideUsingPositionB(7) ",
                "default-position-1",
                field.getArg1("mask", 1).getKey());
        field.getArg1("mask",2);
    }

    @Test
    public void testOverrideUsingPositionB_test25_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testOverrideUsingPositionB(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideUsingPositionB(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideUsingPositionB(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideUsingPositionB(4) ",
                "default-position-2",
                field.getArg1("required", 2).getKey());
        field.getArg1("required",3);
        assertEquals(
                "testOverrideUsingPositionB(5) ",
                "required-position-3",
                field.getArg1("required", 3).getKey());
        assertEquals("testOverrideUsingPositionB(6) ", 4, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverrideUsingPositionB(6) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
        assertEquals(
                "testOverrideUsingPositionB(7) ",
                "default-position-1",
                field.getArg1("mask", 1).getKey());
        field.getArg1("mask",2);
        assertEquals(
                "testOverrideUsingPositionB(8) ",
                "default-position-2",
                field.getArg1("mask", 2).getKey());
    }

    @Test
    public void testOverrideUsingPositionB_test26_decomposed()  {
        createArg3("required-position-3","required",3);
        field.addArg(createArg3("required-position-3", "required", 3));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        assertEquals("testOverrideUsingPositionB(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideUsingPositionB(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideUsingPositionB(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideUsingPositionB(4) ",
                "default-position-2",
                field.getArg1("required", 2).getKey());
        field.getArg1("required",3);
        assertEquals(
                "testOverrideUsingPositionB(5) ",
                "required-position-3",
                field.getArg1("required", 3).getKey());
        assertEquals("testOverrideUsingPositionB(6) ", 4, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverrideUsingPositionB(6) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
        assertEquals(
                "testOverrideUsingPositionB(7) ",
                "default-position-1",
                field.getArg1("mask", 1).getKey());
        field.getArg1("mask",2);
        assertEquals(
                "testOverrideUsingPositionB(8) ",
                "default-position-2",
                field.getArg1("mask", 2).getKey());
        assertNull("testOverrideUsingPositionB(9) ", field.getArg1("mask", 3));
    }

    @Test
    public void testOverridePositionImplied_test0_decomposed()  {
        createArg0("default-position-0");
    }

    @Test
    public void testOverridePositionImplied_test1_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
    }

    @Test
    public void testOverridePositionImplied_test2_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg2("required-position-1","required");
    }

    @Test
    public void testOverridePositionImplied_test3_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg2("required-position-1","required");
        field.addArg(createArg2("required-position-1", "required"));
    }

    @Test
    public void testOverridePositionImplied_test4_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg2("required-position-1","required");
        field.addArg(createArg2("required-position-1", "required"));
        createArg2("required-position-2","required");
    }

    @Test
    public void testOverridePositionImplied_test5_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg2("required-position-1","required");
        field.addArg(createArg2("required-position-1", "required"));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
    }

    @Test
    public void testOverridePositionImplied_test6_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg2("required-position-1","required");
        field.addArg(createArg2("required-position-1", "required"));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-1","mask");
    }

    @Test
    public void testOverridePositionImplied_test7_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg2("required-position-1","required");
        field.addArg(createArg2("required-position-1", "required"));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-1","mask");
        field.addArg(createArg2("mask-position-1", "mask"));
    }

    @Test
    public void testOverridePositionImplied_test8_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg2("required-position-1","required");
        field.addArg(createArg2("required-position-1", "required"));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-1","mask");
        field.addArg(createArg2("mask-position-1", "mask"));
        assertEquals("testOverridePositionImplied(1) ", 3, field.getArgs("required").length);
    }

    @Test
    public void testOverridePositionImplied_test9_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg2("required-position-1","required");
        field.addArg(createArg2("required-position-1", "required"));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-1","mask");
        field.addArg(createArg2("mask-position-1", "mask"));
        assertEquals("testOverridePositionImplied(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
    }

    @Test
    public void testOverridePositionImplied_test10_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg2("required-position-1","required");
        field.addArg(createArg2("required-position-1", "required"));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-1","mask");
        field.addArg(createArg2("mask-position-1", "mask"));
        assertEquals("testOverridePositionImplied(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverridePositionImplied(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
    }

    @Test
    public void testOverridePositionImplied_test11_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg2("required-position-1","required");
        field.addArg(createArg2("required-position-1", "required"));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-1","mask");
        field.addArg(createArg2("mask-position-1", "mask"));
        assertEquals("testOverridePositionImplied(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverridePositionImplied(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
    }

    @Test
    public void testOverridePositionImplied_test12_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg2("required-position-1","required");
        field.addArg(createArg2("required-position-1", "required"));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-1","mask");
        field.addArg(createArg2("mask-position-1", "mask"));
        assertEquals("testOverridePositionImplied(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverridePositionImplied(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverridePositionImplied(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
    }

    @Test
    public void testOverridePositionImplied_test13_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg2("required-position-1","required");
        field.addArg(createArg2("required-position-1", "required"));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-1","mask");
        field.addArg(createArg2("mask-position-1", "mask"));
        assertEquals("testOverridePositionImplied(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverridePositionImplied(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverridePositionImplied(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
    }

    @Test
    public void testOverridePositionImplied_test14_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg2("required-position-1","required");
        field.addArg(createArg2("required-position-1", "required"));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-1","mask");
        field.addArg(createArg2("mask-position-1", "mask"));
        assertEquals("testOverridePositionImplied(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverridePositionImplied(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverridePositionImplied(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverridePositionImplied(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
    }

    @Test
    public void testOverridePositionImplied_test15_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg2("required-position-1","required");
        field.addArg(createArg2("required-position-1", "required"));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-1","mask");
        field.addArg(createArg2("mask-position-1", "mask"));
        assertEquals("testOverridePositionImplied(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverridePositionImplied(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverridePositionImplied(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverridePositionImplied(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertEquals("testOverridePositionImplied(5) ", 3, field.getArgs("mask").length);
    }

    @Test
    public void testOverridePositionImplied_test16_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg2("required-position-1","required");
        field.addArg(createArg2("required-position-1", "required"));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-1","mask");
        field.addArg(createArg2("mask-position-1", "mask"));
        assertEquals("testOverridePositionImplied(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverridePositionImplied(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverridePositionImplied(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverridePositionImplied(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertEquals("testOverridePositionImplied(5) ", 3, field.getArgs("mask").length);
        field.getArg1("mask",0);
    }

    @Test
    public void testOverridePositionImplied_test17_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg2("required-position-1","required");
        field.addArg(createArg2("required-position-1", "required"));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-1","mask");
        field.addArg(createArg2("mask-position-1", "mask"));
        assertEquals("testOverridePositionImplied(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverridePositionImplied(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverridePositionImplied(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverridePositionImplied(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertEquals("testOverridePositionImplied(5) ", 3, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverridePositionImplied(6) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
    }

    @Test
    public void testOverridePositionImplied_test18_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg2("required-position-1","required");
        field.addArg(createArg2("required-position-1", "required"));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-1","mask");
        field.addArg(createArg2("mask-position-1", "mask"));
        assertEquals("testOverridePositionImplied(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverridePositionImplied(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverridePositionImplied(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverridePositionImplied(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertEquals("testOverridePositionImplied(5) ", 3, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverridePositionImplied(6) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
    }

    @Test
    public void testOverridePositionImplied_test19_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg2("required-position-1","required");
        field.addArg(createArg2("required-position-1", "required"));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-1","mask");
        field.addArg(createArg2("mask-position-1", "mask"));
        assertEquals("testOverridePositionImplied(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverridePositionImplied(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverridePositionImplied(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverridePositionImplied(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertEquals("testOverridePositionImplied(5) ", 3, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverridePositionImplied(6) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
        assertEquals(
                "testOverridePositionImplied(7) ",
                "mask-position-1",
                field.getArg1("mask", 1).getKey());
    }

    @Test
    public void testOverridePositionImplied_test20_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg2("required-position-1","required");
        field.addArg(createArg2("required-position-1", "required"));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-1","mask");
        field.addArg(createArg2("mask-position-1", "mask"));
        assertEquals("testOverridePositionImplied(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverridePositionImplied(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverridePositionImplied(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverridePositionImplied(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertEquals("testOverridePositionImplied(5) ", 3, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverridePositionImplied(6) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
        assertEquals(
                "testOverridePositionImplied(7) ",
                "mask-position-1",
                field.getArg1("mask", 1).getKey());
        assertNull("testOverridePositionImplied(8) ", field.getArg1("mask", 2));
    }

    @Test
    public void testOverridePositionImplied_test21_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg2("required-position-1","required");
        field.addArg(createArg2("required-position-1", "required"));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-1","mask");
        field.addArg(createArg2("mask-position-1", "mask"));
        assertEquals("testOverridePositionImplied(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverridePositionImplied(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverridePositionImplied(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverridePositionImplied(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertEquals("testOverridePositionImplied(5) ", 3, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverridePositionImplied(6) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
        assertEquals(
                "testOverridePositionImplied(7) ",
                "mask-position-1",
                field.getArg1("mask", 1).getKey());
        assertNull("testOverridePositionImplied(8) ", field.getArg1("mask", 2));
        field.getArg0(0);
    }

    @Test
    public void testOverridePositionImplied_test22_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg2("required-position-1","required");
        field.addArg(createArg2("required-position-1", "required"));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-1","mask");
        field.addArg(createArg2("mask-position-1", "mask"));
        assertEquals("testOverridePositionImplied(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverridePositionImplied(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverridePositionImplied(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverridePositionImplied(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertEquals("testOverridePositionImplied(5) ", 3, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverridePositionImplied(6) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
        assertEquals(
                "testOverridePositionImplied(7) ",
                "mask-position-1",
                field.getArg1("mask", 1).getKey());
        assertNull("testOverridePositionImplied(8) ", field.getArg1("mask", 2));
        field.getArg0(0);
        assertEquals(
                "testOverridePositionImplied(9) ", "default-position-0", field.getArg0(0).getKey());
    }

    @Test
    public void testOverridePositionImplied_test23_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg2("required-position-1","required");
        field.addArg(createArg2("required-position-1", "required"));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-1","mask");
        field.addArg(createArg2("mask-position-1", "mask"));
        assertEquals("testOverridePositionImplied(1) ", 3, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverridePositionImplied(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverridePositionImplied(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverridePositionImplied(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertEquals("testOverridePositionImplied(5) ", 3, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverridePositionImplied(6) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
        assertEquals(
                "testOverridePositionImplied(7) ",
                "mask-position-1",
                field.getArg1("mask", 1).getKey());
        assertNull("testOverridePositionImplied(8) ", field.getArg1("mask", 2));
        field.getArg0(0);
        assertEquals(
                "testOverridePositionImplied(9) ", "default-position-0", field.getArg0(0).getKey());
        assertNull("testOverridePositionImplied(10) ", field.getArg0(1));
        assertNull("testOverridePositionImplied(11) ", field.getArg0(2));
    }

    @Test
    public void testOverrideSomePosition_test0_decomposed()  {
        createArg0("default-position-0");
    }

    @Test
    public void testOverrideSomePosition_test1_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
    }

    @Test
    public void testOverrideSomePosition_test2_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
    }

    @Test
    public void testOverrideSomePosition_test3_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
    }

    @Test
    public void testOverrideSomePosition_test4_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
    }

    @Test
    public void testOverrideSomePosition_test5_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
    }

    @Test
    public void testOverrideSomePosition_test6_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
    }

    @Test
    public void testOverrideSomePosition_test7_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
    }

    @Test
    public void testOverrideSomePosition_test8_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
    }

    @Test
    public void testOverrideSomePosition_test9_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
    }

    @Test
    public void testOverrideSomePosition_test10_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
    }

    @Test
    public void testOverrideSomePosition_test11_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
    }

    @Test
    public void testOverrideSomePosition_test12_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
    }

    @Test
    public void testOverrideSomePosition_test13_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
    }

    @Test
    public void testOverrideSomePosition_test14_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideSomePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
    }

    @Test
    public void testOverrideSomePosition_test15_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideSomePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
    }

    @Test
    public void testOverrideSomePosition_test16_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideSomePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideSomePosition(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
    }

    @Test
    public void testOverrideSomePosition_test17_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideSomePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideSomePosition(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
    }

    @Test
    public void testOverrideSomePosition_test18_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideSomePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideSomePosition(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideSomePosition(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
    }

    @Test
    public void testOverrideSomePosition_test19_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideSomePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideSomePosition(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideSomePosition(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertNull("testOverrideSomePosition(5) ", field.getArg1("required", 3));
    }

    @Test
    public void testOverrideSomePosition_test20_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideSomePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideSomePosition(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideSomePosition(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertNull("testOverrideSomePosition(5) ", field.getArg1("required", 3));
        assertEquals("testOverrideSomePosition(6) ", 4, field.getArgs("mask").length);
    }

    @Test
    public void testOverrideSomePosition_test21_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideSomePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideSomePosition(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideSomePosition(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertNull("testOverrideSomePosition(5) ", field.getArg1("required", 3));
        assertEquals("testOverrideSomePosition(6) ", 4, field.getArgs("mask").length);
        field.getArg1("mask",0);
    }

    @Test
    public void testOverrideSomePosition_test22_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideSomePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideSomePosition(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideSomePosition(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertNull("testOverrideSomePosition(5) ", field.getArg1("required", 3));
        assertEquals("testOverrideSomePosition(6) ", 4, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverrideSomePosition(7) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
    }

    @Test
    public void testOverrideSomePosition_test23_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideSomePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideSomePosition(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideSomePosition(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertNull("testOverrideSomePosition(5) ", field.getArg1("required", 3));
        assertEquals("testOverrideSomePosition(6) ", 4, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverrideSomePosition(7) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
    }

    @Test
    public void testOverrideSomePosition_test24_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideSomePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideSomePosition(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideSomePosition(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertNull("testOverrideSomePosition(5) ", field.getArg1("required", 3));
        assertEquals("testOverrideSomePosition(6) ", 4, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverrideSomePosition(7) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
        assertEquals(
                "testOverrideSomePosition(8) ",
                "default-position-1",
                field.getArg1("mask", 1).getKey());
    }

    @Test
    public void testOverrideSomePosition_test25_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideSomePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideSomePosition(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideSomePosition(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertNull("testOverrideSomePosition(5) ", field.getArg1("required", 3));
        assertEquals("testOverrideSomePosition(6) ", 4, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverrideSomePosition(7) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
        assertEquals(
                "testOverrideSomePosition(8) ",
                "default-position-1",
                field.getArg1("mask", 1).getKey());
        field.getArg1("mask",2);
    }

    @Test
    public void testOverrideSomePosition_test26_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideSomePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideSomePosition(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideSomePosition(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertNull("testOverrideSomePosition(5) ", field.getArg1("required", 3));
        assertEquals("testOverrideSomePosition(6) ", 4, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverrideSomePosition(7) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
        assertEquals(
                "testOverrideSomePosition(8) ",
                "default-position-1",
                field.getArg1("mask", 1).getKey());
        field.getArg1("mask",2);
        assertEquals(
                "testOverrideSomePosition(9) ",
                "default-position-2",
                field.getArg1("mask", 2).getKey());
    }

    @Test
    public void testOverrideSomePosition_test27_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideSomePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideSomePosition(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideSomePosition(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertNull("testOverrideSomePosition(5) ", field.getArg1("required", 3));
        assertEquals("testOverrideSomePosition(6) ", 4, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverrideSomePosition(7) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
        assertEquals(
                "testOverrideSomePosition(8) ",
                "default-position-1",
                field.getArg1("mask", 1).getKey());
        field.getArg1("mask",2);
        assertEquals(
                "testOverrideSomePosition(9) ",
                "default-position-2",
                field.getArg1("mask", 2).getKey());
        field.getArg1("mask",3);
    }

    @Test
    public void testOverrideSomePosition_test28_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideSomePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideSomePosition(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideSomePosition(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertNull("testOverrideSomePosition(5) ", field.getArg1("required", 3));
        assertEquals("testOverrideSomePosition(6) ", 4, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverrideSomePosition(7) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
        assertEquals(
                "testOverrideSomePosition(8) ",
                "default-position-1",
                field.getArg1("mask", 1).getKey());
        field.getArg1("mask",2);
        assertEquals(
                "testOverrideSomePosition(9) ",
                "default-position-2",
                field.getArg1("mask", 2).getKey());
        field.getArg1("mask",3);
        assertEquals(
                "testOverrideSomePosition(10) ",
                "mask-position-3",
                field.getArg1("mask", 3).getKey());
    }

    @Test
    public void testOverrideSomePosition_test29_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideSomePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideSomePosition(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideSomePosition(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertNull("testOverrideSomePosition(5) ", field.getArg1("required", 3));
        assertEquals("testOverrideSomePosition(6) ", 4, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverrideSomePosition(7) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
        assertEquals(
                "testOverrideSomePosition(8) ",
                "default-position-1",
                field.getArg1("mask", 1).getKey());
        field.getArg1("mask",2);
        assertEquals(
                "testOverrideSomePosition(9) ",
                "default-position-2",
                field.getArg1("mask", 2).getKey());
        field.getArg1("mask",3);
        assertEquals(
                "testOverrideSomePosition(10) ",
                "mask-position-3",
                field.getArg1("mask", 3).getKey());
        field.getArg0(0);
    }

    @Test
    public void testOverrideSomePosition_test30_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideSomePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideSomePosition(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideSomePosition(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertNull("testOverrideSomePosition(5) ", field.getArg1("required", 3));
        assertEquals("testOverrideSomePosition(6) ", 4, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverrideSomePosition(7) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
        assertEquals(
                "testOverrideSomePosition(8) ",
                "default-position-1",
                field.getArg1("mask", 1).getKey());
        field.getArg1("mask",2);
        assertEquals(
                "testOverrideSomePosition(9) ",
                "default-position-2",
                field.getArg1("mask", 2).getKey());
        field.getArg1("mask",3);
        assertEquals(
                "testOverrideSomePosition(10) ",
                "mask-position-3",
                field.getArg1("mask", 3).getKey());
        field.getArg0(0);
        assertEquals(
                "testOverrideSomePosition(11) ", "default-position-0", field.getArg0(0).getKey());
    }

    @Test
    public void testOverrideSomePosition_test31_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideSomePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideSomePosition(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideSomePosition(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertNull("testOverrideSomePosition(5) ", field.getArg1("required", 3));
        assertEquals("testOverrideSomePosition(6) ", 4, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverrideSomePosition(7) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
        assertEquals(
                "testOverrideSomePosition(8) ",
                "default-position-1",
                field.getArg1("mask", 1).getKey());
        field.getArg1("mask",2);
        assertEquals(
                "testOverrideSomePosition(9) ",
                "default-position-2",
                field.getArg1("mask", 2).getKey());
        field.getArg1("mask",3);
        assertEquals(
                "testOverrideSomePosition(10) ",
                "mask-position-3",
                field.getArg1("mask", 3).getKey());
        field.getArg0(0);
        assertEquals(
                "testOverrideSomePosition(11) ", "default-position-0", field.getArg0(0).getKey());
        field.getArg0(1);
    }

    @Test
    public void testOverrideSomePosition_test32_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideSomePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideSomePosition(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideSomePosition(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertNull("testOverrideSomePosition(5) ", field.getArg1("required", 3));
        assertEquals("testOverrideSomePosition(6) ", 4, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverrideSomePosition(7) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
        assertEquals(
                "testOverrideSomePosition(8) ",
                "default-position-1",
                field.getArg1("mask", 1).getKey());
        field.getArg1("mask",2);
        assertEquals(
                "testOverrideSomePosition(9) ",
                "default-position-2",
                field.getArg1("mask", 2).getKey());
        field.getArg1("mask",3);
        assertEquals(
                "testOverrideSomePosition(10) ",
                "mask-position-3",
                field.getArg1("mask", 3).getKey());
        field.getArg0(0);
        assertEquals(
                "testOverrideSomePosition(11) ", "default-position-0", field.getArg0(0).getKey());
        field.getArg0(1);
        assertEquals(
                "testOverrideSomePosition(12) ", "default-position-1", field.getArg0(1).getKey());
    }

    @Test
    public void testOverrideSomePosition_test33_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideSomePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideSomePosition(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideSomePosition(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertNull("testOverrideSomePosition(5) ", field.getArg1("required", 3));
        assertEquals("testOverrideSomePosition(6) ", 4, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverrideSomePosition(7) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
        assertEquals(
                "testOverrideSomePosition(8) ",
                "default-position-1",
                field.getArg1("mask", 1).getKey());
        field.getArg1("mask",2);
        assertEquals(
                "testOverrideSomePosition(9) ",
                "default-position-2",
                field.getArg1("mask", 2).getKey());
        field.getArg1("mask",3);
        assertEquals(
                "testOverrideSomePosition(10) ",
                "mask-position-3",
                field.getArg1("mask", 3).getKey());
        field.getArg0(0);
        assertEquals(
                "testOverrideSomePosition(11) ", "default-position-0", field.getArg0(0).getKey());
        field.getArg0(1);
        assertEquals(
                "testOverrideSomePosition(12) ", "default-position-1", field.getArg0(1).getKey());
        field.getArg0(2);
    }

    @Test
    public void testOverrideSomePosition_test34_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideSomePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideSomePosition(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideSomePosition(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertNull("testOverrideSomePosition(5) ", field.getArg1("required", 3));
        assertEquals("testOverrideSomePosition(6) ", 4, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverrideSomePosition(7) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
        assertEquals(
                "testOverrideSomePosition(8) ",
                "default-position-1",
                field.getArg1("mask", 1).getKey());
        field.getArg1("mask",2);
        assertEquals(
                "testOverrideSomePosition(9) ",
                "default-position-2",
                field.getArg1("mask", 2).getKey());
        field.getArg1("mask",3);
        assertEquals(
                "testOverrideSomePosition(10) ",
                "mask-position-3",
                field.getArg1("mask", 3).getKey());
        field.getArg0(0);
        assertEquals(
                "testOverrideSomePosition(11) ", "default-position-0", field.getArg0(0).getKey());
        field.getArg0(1);
        assertEquals(
                "testOverrideSomePosition(12) ", "default-position-1", field.getArg0(1).getKey());
        field.getArg0(2);
        assertEquals(
                "testOverrideSomePosition(13) ", "default-position-2", field.getArg0(2).getKey());
    }

    @Test
    public void testOverrideSomePosition_test35_decomposed()  {
        createArg0("default-position-0");
        field.addArg(createArg0("default-position-0"));
        createArg0("default-position-1");
        field.addArg(createArg0("default-position-1"));
        createArg0("default-position-2");
        field.addArg(createArg0("default-position-2"));
        createArg3("required-position-1","required",1);
        field.addArg(createArg3("required-position-1", "required", 1));
        createArg2("required-position-2","required");
        field.addArg(createArg2("required-position-2", "required"));
        createArg2("mask-position-3","mask");
        field.addArg(createArg2("mask-position-3", "mask"));
        assertEquals("testOverrideSomePosition(1) ", 4, field.getArgs("required").length);
        field.getArg1("required",0);
        assertEquals(
                "testOverrideSomePosition(2) ",
                "default-position-0",
                field.getArg1("required", 0).getKey());
        field.getArg1("required",1);
        assertEquals(
                "testOverrideSomePosition(3) ",
                "required-position-1",
                field.getArg1("required", 1).getKey());
        field.getArg1("required",2);
        assertEquals(
                "testOverrideSomePosition(4) ",
                "required-position-2",
                field.getArg1("required", 2).getKey());
        assertNull("testOverrideSomePosition(5) ", field.getArg1("required", 3));
        assertEquals("testOverrideSomePosition(6) ", 4, field.getArgs("mask").length);
        field.getArg1("mask",0);
        assertEquals(
                "testOverrideSomePosition(7) ",
                "default-position-0",
                field.getArg1("mask", 0).getKey());
        field.getArg1("mask",1);
        assertEquals(
                "testOverrideSomePosition(8) ",
                "default-position-1",
                field.getArg1("mask", 1).getKey());
        field.getArg1("mask",2);
        assertEquals(
                "testOverrideSomePosition(9) ",
                "default-position-2",
                field.getArg1("mask", 2).getKey());
        field.getArg1("mask",3);
        assertEquals(
                "testOverrideSomePosition(10) ",
                "mask-position-3",
                field.getArg1("mask", 3).getKey());
        field.getArg0(0);
        assertEquals(
                "testOverrideSomePosition(11) ", "default-position-0", field.getArg0(0).getKey());
        field.getArg0(1);
        assertEquals(
                "testOverrideSomePosition(12) ", "default-position-1", field.getArg0(1).getKey());
        field.getArg0(2);
        assertEquals(
                "testOverrideSomePosition(13) ", "default-position-2", field.getArg0(2).getKey());
        assertNull("testOverrideSomePosition(14) ", field.getArg0(3));
    }
}