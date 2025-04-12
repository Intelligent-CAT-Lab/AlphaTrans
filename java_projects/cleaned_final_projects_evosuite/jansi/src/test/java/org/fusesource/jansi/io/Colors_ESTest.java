/*
 * Copyright (C) 2009-2023 the original author(s).
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.fusesource.jansi.io;

import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.Test;
import org.junit.runner.RunWith;

import static org.evosuite.runtime.EvoAssertions.*;
import static org.junit.Assert.*;

@RunWith(EvoRunner.class)
@EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true)
public class Colors_ESTest extends Colors_ESTest_scaffolding {

    @Test(timeout = 4000)
    public void test0() throws Throwable {
        int int0 = Colors.roundColor0(57, 57);
        assertEquals(21, int0);
    }

    @Test(timeout = 4000)
    public void test1() throws Throwable {
        int int0 = Colors.roundRgbColor((-1), Integer.MAX_VALUE, 1, (-1));
        assertEquals(Integer.MAX_VALUE, int0);
    }

    @Test(timeout = 4000)
    public void test2() throws Throwable {
        int int0 = Colors.roundColor0(1, 0);
        assertEquals(Integer.MAX_VALUE, int0);
    }

    @Test(timeout = 4000)
    public void test3() throws Throwable {
        int int0 = Colors.roundRgbColor(0, (-3159), 86, 1);
        assertEquals(0, int0);
    }

    @Test(timeout = 4000)
    public void test4() throws Throwable {
        int int0 = Colors.roundColor0((-1814), 0);
        assertEquals((-1814), int0);
    }

    @Test(timeout = 4000)
    public void test5() throws Throwable {
        // Undeclared exception!
        try {
            Colors.roundColor0(1391, 0);
            fail("Expecting exception: ArrayIndexOutOfBoundsException");

        } catch (ArrayIndexOutOfBoundsException e) {
            //
            // Index 1391 out of bounds for length 256
            //
            verifyException("org.fusesource.jansi.io.Colors", e);
        }
    }

    @Test(timeout = 4000)
    public void test6() throws Throwable {
        int int0 = Colors.roundColor0(0, Integer.MAX_VALUE);
        assertEquals(0, int0);
    }

    @Test(timeout = 4000)
    public void test7() throws Throwable {
        Colors colors0 = new Colors();
    }

    @Test(timeout = 4000)
    public void test8() throws Throwable {
        // Undeclared exception!
        try {
            Colors.roundRgbColor(751836882, 751836882, 751836882, 751836882);
            fail("Expecting exception: ArrayIndexOutOfBoundsException");

        } catch (ArrayIndexOutOfBoundsException e) {
            //
            // Index 256 out of bounds for length 256
            //
            verifyException("org.fusesource.jansi.io.Colors", e);
        }
    }
}
