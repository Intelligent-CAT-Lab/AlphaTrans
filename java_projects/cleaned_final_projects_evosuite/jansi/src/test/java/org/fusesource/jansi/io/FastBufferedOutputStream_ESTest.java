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

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.io.PipedOutputStream;

import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.io.MockPrintStream;
import org.junit.Test;
import org.junit.runner.RunWith;

import static org.evosuite.runtime.EvoAssertions.*;
import static org.junit.Assert.*;

@RunWith(EvoRunner.class)
@EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true)
public class FastBufferedOutputStream_ESTest extends FastBufferedOutputStream_ESTest_scaffolding {

    @Test(timeout = 4000)
    public void test00() throws Throwable {
        FastBufferedOutputStream fastBufferedOutputStream0 = new FastBufferedOutputStream((OutputStream) null);
        fastBufferedOutputStream0.count = (-2398);
        // Undeclared exception!
        try {
            fastBufferedOutputStream0.flush();
            fail("Expecting exception: NullPointerException");

        } catch (NullPointerException e) {
            //
            // no message in exception (getMessage() returned null)
            //
            verifyException("org.fusesource.jansi.io.FastBufferedOutputStream", e);
        }
    }

    @Test(timeout = 4000)
    public void test01() throws Throwable {
        FastBufferedOutputStream fastBufferedOutputStream0 = new FastBufferedOutputStream((OutputStream) null);
        byte[] byteArray0 = new byte[1];
        fastBufferedOutputStream0.write0((byte) 0);
        // Undeclared exception!
        try {
            fastBufferedOutputStream0.write1(byteArray0, 1494, 8191);
            fail("Expecting exception: ArrayIndexOutOfBoundsException");

        } catch (ArrayIndexOutOfBoundsException e) {
        }
    }

    @Test(timeout = 4000)
    public void test02() throws Throwable {
        ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream(1484);
        FastBufferedOutputStream fastBufferedOutputStream0 = new FastBufferedOutputStream(byteArrayOutputStream0);
        byte[] byteArray0 = new byte[6];
        fastBufferedOutputStream0.write1(byteArray0, (byte) 0, (byte) 6);
        assertEquals("", byteArrayOutputStream0.toString());
        assertEquals(0, byteArrayOutputStream0.size());
    }

    @Test(timeout = 4000)
    public void test03() throws Throwable {
        byte[] byteArray0 = new byte[14];
        MockPrintStream mockPrintStream0 = new MockPrintStream("lvm *:l{s");
        FastBufferedOutputStream fastBufferedOutputStream0 = new FastBufferedOutputStream(mockPrintStream0);
        fastBufferedOutputStream0.write1(byteArray0, 1495, 8192);
        assertEquals(14, byteArray0.length);
    }

    @Test(timeout = 4000)
    public void test04() throws Throwable {
        ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream(1484);
        FastBufferedOutputStream fastBufferedOutputStream0 = new FastBufferedOutputStream(byteArrayOutputStream0);
        fastBufferedOutputStream0.count = 2277;
        fastBufferedOutputStream0.flush();
        assertEquals(2277, byteArrayOutputStream0.size());
    }

    @Test(timeout = 4000)
    public void test05() throws Throwable {
        PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
        FastBufferedOutputStream fastBufferedOutputStream0 = new FastBufferedOutputStream(pipedOutputStream0);
        byte[] byteArray0 = new byte[0];
        try {
            fastBufferedOutputStream0.write1(byteArray0, 8218, 8218);
            fail("Expecting exception: IOException");

        } catch (IOException e) {
            //
            // Pipe not connected
            //
            verifyException("java.io.PipedOutputStream", e);
        }
    }

    @Test(timeout = 4000)
    public void test06() throws Throwable {
        FastBufferedOutputStream fastBufferedOutputStream0 = new FastBufferedOutputStream((OutputStream) null);
        fastBufferedOutputStream0.count = 8192;
        // Undeclared exception!
        try {
            fastBufferedOutputStream0.write0(8192);
            fail("Expecting exception: NullPointerException");

        } catch (NullPointerException e) {
            //
            // no message in exception (getMessage() returned null)
            //
            verifyException("org.fusesource.jansi.io.FastBufferedOutputStream", e);
        }
    }

    @Test(timeout = 4000)
    public void test07() throws Throwable {
        FastBufferedOutputStream fastBufferedOutputStream0 = new FastBufferedOutputStream((OutputStream) null);
        fastBufferedOutputStream0.count = (-103);
        // Undeclared exception!
        try {
            fastBufferedOutputStream0.write0(2043);
            fail("Expecting exception: ArrayIndexOutOfBoundsException");

        } catch (ArrayIndexOutOfBoundsException e) {
            //
            // Index -103 out of bounds for length 8192
            //
            verifyException("org.fusesource.jansi.io.FastBufferedOutputStream", e);
        }
    }

    @Test(timeout = 4000)
    public void test08() throws Throwable {
        PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
        FastBufferedOutputStream fastBufferedOutputStream0 = new FastBufferedOutputStream(pipedOutputStream0);
        fastBufferedOutputStream0.write0((-4535));
        try {
            fastBufferedOutputStream0.flush();
            fail("Expecting exception: IOException");

        } catch (IOException e) {
            //
            // Pipe not connected
            //
            verifyException("java.io.PipedOutputStream", e);
        }
    }

    @Test(timeout = 4000)
    public void test09() throws Throwable {
        FastBufferedOutputStream fastBufferedOutputStream0 = new FastBufferedOutputStream((OutputStream) null);
        byte[] byteArray0 = new byte[1];
        fastBufferedOutputStream0.write0(3184);
        fastBufferedOutputStream0.write0((byte) 0);
        // Undeclared exception!
        try {
            fastBufferedOutputStream0.write1(byteArray0, (-1), 8191);
            fail("Expecting exception: NullPointerException");

        } catch (NullPointerException e) {
            //
            // no message in exception (getMessage() returned null)
            //
            verifyException("org.fusesource.jansi.io.FastBufferedOutputStream", e);
        }
    }

    @Test(timeout = 4000)
    public void test10() throws Throwable {
        ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream(1495);
        FastBufferedOutputStream fastBufferedOutputStream0 = new FastBufferedOutputStream(byteArrayOutputStream0);
        byte[] byteArray0 = new byte[14];
        // Undeclared exception!
        try {
            fastBufferedOutputStream0.write1(byteArray0, 1495, 8192);
            fail("Expecting exception: IndexOutOfBoundsException");

        } catch (IndexOutOfBoundsException e) {
        }
    }

    @Test(timeout = 4000)
    public void test11() throws Throwable {
        ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
        FastBufferedOutputStream fastBufferedOutputStream0 = new FastBufferedOutputStream(byteArrayOutputStream0);
        fastBufferedOutputStream0.count = (int) (byte) 0;
        fastBufferedOutputStream0.count = 8216;
        // Undeclared exception!
        try {
            fastBufferedOutputStream0.write0(3162);
            fail("Expecting exception: IndexOutOfBoundsException");

        } catch (IndexOutOfBoundsException e) {
        }
    }
}
